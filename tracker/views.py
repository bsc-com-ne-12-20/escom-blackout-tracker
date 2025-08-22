from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import LoadSheddingGroup, BlackoutSchedule, GroupLocation
from .serializers import BlackoutScheduleSerializer, GroupLocationSerializer

@api_view(['GET'])
def group_blackout_schedule(request, group_id):
    try:
        group = LoadSheddingGroup.objects.get(group_id=group_id)
    except LoadSheddingGroup.DoesNotExist:
        return Response({'error': 'Group not found'}, status=404)
    
    schedules = BlackoutSchedule.objects.filter(group=group)
    serializer = BlackoutScheduleSerializer(schedules, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def group_locations(request, group_id):
    """Get all locations for a specific group"""
    try:
        group = LoadSheddingGroup.objects.get(group_id=group_id)
    except LoadSheddingGroup.DoesNotExist:
        return Response({'error': 'Group not found'}, status=404)
    
    locations = GroupLocation.objects.filter(group=group)
    serializer = GroupLocationSerializer(locations, many=True)
    return Response(serializer.data)