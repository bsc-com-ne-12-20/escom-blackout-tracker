import csv
from django.core.management.base import BaseCommand
from tracker.models import Groups_and_Area

class Command(BaseCommand):
    help = 'Import groups and areas from CSV file'

    def handle(self, *args, **kwargs):
        with open('load_shedding_groups.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for row in reader:
                group_id = row['Group']
                region = row['Region']
                location = row['Location']
                affected_areas = row['Affected Areas']
                obj, created = Groups_and_Area.objects.get_or_create(
                    Group_ID=group_id,
                    Region=region,
                    Location=location,
                    defaults={'Affected_Areas': affected_areas}
                )
                if not created:
                    obj.Affected_Areas = affected_areas
                    obj.save()
                count += 1
            self.stdout.write(self.style.SUCCESS(f'Imported {count} records.'))