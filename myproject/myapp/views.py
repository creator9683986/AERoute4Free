from django.shortcuts import render
from .models import NameOfMedicaments
from .utils import levenshtein_search


def search_medicaments(request):
    if request.method == "POST":
        user_text = request.POST['user_text']
        print("User text:", user_text)

        medicament_names = NameOfMedicaments.objects.values_list('name', flat=True)
        print("Medicament names:", list(medicament_names))

        found_names = levenshtein_search(user_text, medicament_names)
        print("Found names:", found_names)

        medicaments_data = NameOfMedicaments.objects.filter(name__in=found_names).select_related('link_to_rule')
        print("Medicaments data:", list(medicaments_data))

        return render(request, 'results.html', {'medicaments_data': medicaments_data})

    return render(request, 'search.html')



