import csv
from django.core.management.base import BaseCommand
from tracker.models import LoadSheddingGroup, GroupLocation

class Command(BaseCommand):
    help = 'Import groups and locations from CSV file'

    def handle(self, *args, **kwargs):
        # Clear existing data
        GroupLocation.objects.all().delete()
        LoadSheddingGroup.objects.all().delete()
        
        groups_created = set()
        locations_count = 0
        
        with open('load_shedding_groups.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                group_id = row['Group']
                region = row['Region']
                location = row['Location']
                affected_areas = row['Affected Areas']
                
                # Create group if it doesn't exist
                if group_id not in groups_created:
                    LoadSheddingGroup.objects.get_or_create(group_id=group_id)
                    groups_created.add(group_id)
                    
                # Create location
                group = LoadSheddingGroup.objects.get(group_id=group_id)
                GroupLocation.objects.create(
                    group=group,
                    region=region,
                    location=location,
                    affected_areas=affected_areas
                )
                locations_count += 1
                
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully imported {len(groups_created)} groups and {locations_count} locations.'
            )
        )
