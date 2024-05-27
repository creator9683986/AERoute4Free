from django.core.management.base import BaseCommand
from django.db import connection
from myapp.models import ListOfRules, NameOfMedicaments

class Command(BaseCommand):
    help = 'Reset indexes in the database and start from 1'

    def handle(self, *args, **kwargs):
        NameOfMedicaments.objects.all().delete()
        ListOfRules.objects.all().delete()
        sequence_sql_name_of_medicaments = f"ALTER SEQUENCE {NameOfMedicaments._meta.db_table}_id_seq RESTART WITH 1"
        with connection.cursor() as cursor:
            cursor.execute(sequence_sql_name_of_medicaments)
        self.stdout.write(self.style.SUCCESS('Successfully reset indexes and started from 1'))



# команда для сброса бд python manage.py reset_db_indexes