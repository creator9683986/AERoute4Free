from django.contrib import admin
from .models import ListOfRules, NameOfMedicaments, SearchSettings


admin.site.register(ListOfRules)
admin.site.register(NameOfMedicaments)
admin.site.register(SearchSettings)
