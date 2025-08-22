from rest_framework import serializers
from .models import BlackoutSchedule, GroupLocation

class BlackoutScheduleSerializer(serializers.ModelSerializer):
    group_id = serializers.CharField(source='group.group_id', read_only=True)
    
    class Meta:
        model = BlackoutSchedule
        fields = ['group_id', 'date', 'start_time', 'end_time']

class GroupLocationSerializer(serializers.ModelSerializer):
    group_id = serializers.CharField(source='group.group_id', read_only=True)
    
    class Meta:
        model = GroupLocation
        fields = ['group_id', 'region', 'location', 'affected_areas']