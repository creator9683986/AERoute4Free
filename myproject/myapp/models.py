from django.db import models


class SearchSettings(models.Model):
    allowed_error_percentage = models.FloatField(default=50.0)

    def __str__(self):
        return f"SearchSettings: {self.allowed_error_percentage}%"

class ListOfRules(models.Model):
    obligation = models.TextField()
    comment = models.TextField()
    ae_source_countries = models.TextField()
    receiver = models.TextField()
    format = models.TextField()
    other_procedures = models.TextField()
    type_of_event = models.TextField()
    valid_start_date = models.DateField()
    valid_end_date = models.DateField()
    deadline_to_submit = models.TextField()
    link_from_names = models.BigIntegerField(primary_key=True)

class NameOfMedicaments(models.Model):
    name = models.TextField()
    link_to_rule = models.ForeignKey(ListOfRules, on_delete=models.CASCADE)

