import difflib
import re
import string
from myapp.models import SearchSettings

def my_dist(str1, str2):
    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1
    matrix = [[0 for _ in range(len_str2)] for _ in range(len_str1)]
    for i in range(len_str1):
        matrix[i][0] = i
    for j in range(len_str2):
        matrix[0][j] = j
    for i in range(1, len_str1):
        for j in range(1, len_str2):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + cost
            )
    return matrix[len_str1 - 1][len_str2 - 1]

def levenshtein_search(user_text, medicament_names):
    try:
        search_settings = SearchSettings.objects.first()
        if not search_settings:
            raise ValueError("SearchSettings instance is not configured in the database.")
        allowed_error_percentage = search_settings.allowed_error_percentage / 100
    except Exception as e:
        print(f"Error fetching search settings: {e}")
        allowed_error_percentage = 0.5

    user_text_lower = user_text.lower()
    translator = str.maketrans('', '', string.punctuation.replace('-', ''))
    user_text_lower = user_text_lower.translate(translator)
    user_text_lower = user_text_lower.replace('«', '').replace('»', '')
    user_text_words = user_text_lower.split()

    found_names = set()
    for name in medicament_names:
        name_lower = name.lower()
        for word in user_text_words:
            comp = my_dist(name_lower, word)
            if comp <= int(len(name_lower) * allowed_error_percentage):
                found_names.add(name)
                break

    return found_names
