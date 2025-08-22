from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
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

@api_view(['GET'])
def list_regions(request):
    """Get all unique regions"""
    regions = GroupLocation.objects.values_list('region', flat=True).distinct().order_by('region')
    return Response({'regions': list(regions)})

@api_view(['GET'])
def search_by_region(request, region):
    """Get all locations in a specific region"""
    locations = GroupLocation.objects.filter(region__icontains=region).order_by('location')
    serializer = GroupLocationSerializer(locations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def search_by_location(request, location):
    """Get group info and schedule for a specific location"""
    try:
        group_location = GroupLocation.objects.get(location__iexact=location)
        group = group_location.group
        
        # Get location info
        location_serializer = GroupLocationSerializer(group_location)
        
        # Get schedules for this group
        schedules = BlackoutSchedule.objects.filter(group=group)
        schedule_serializer = BlackoutScheduleSerializer(schedules, many=True)
        
        return Response({
            'location_info': location_serializer.data,
            'schedules': schedule_serializer.data
        })
    except GroupLocation.DoesNotExist:
        return Response({'error': 'Location not found'}, status=404)

@api_view(['GET'])
def search_affected_areas(request):
    """Search affected areas by text query"""
    query = request.GET.get('q', '').strip()
    
    if not query:
        return Response({'error': 'Query parameter "q" is required'}, status=400)
    
    # Search in affected_areas field
    locations = GroupLocation.objects.filter(
        Q(affected_areas__icontains=query) | 
        Q(location__icontains=query)
    ).order_by('group__group_id', 'location')
    
    results = []
    for location in locations:
        # Get schedules for this group
        schedules = BlackoutSchedule.objects.filter(group=location.group)
        schedule_serializer = BlackoutScheduleSerializer(schedules, many=True)
        
        results.append({
            'group_id': location.group.group_id,
            'region': location.region,
            'location': location.location,
            'affected_areas': location.affected_areas,
            'schedules': schedule_serializer.data
        })
    
    return Response({
        'query': query,
        'results': results,
        'count': len(results)
    })

@api_view(['GET'])
def list_locations(request):
    """Get all locations with their groups"""
    locations = GroupLocation.objects.select_related('group').order_by('region', 'location')
    serializer = GroupLocationSerializer(locations, many=True)
    return Response(serializer.data)