import csv
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_date
from phones.models import Phone

class Command(BaseCommand):
    help = 'Import phones from a CSV file'

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:

                release_date = parse_date(row['release_date'])

                lte_exists = row['lte_exists'].lower() in ['true', '1', 't', 'y', 'yes']

                Phone.objects.create(
                    name=row['name'],
                    price=row['price'],
                    image=row['image'],
                    release_date=release_date,
                    lte_exists=lte_exists,

                )
                self.stdout.write(self.style.SUCCESS(f"Successfully imported phone '{row['name']}'"))

