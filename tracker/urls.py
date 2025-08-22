from django.urls import path
from .views import (
    group_blackout_schedule, 
    group_locations, 
    list_regions, 
    search_by_region, 
    search_by_location, 
    search_affected_areas,
    list_locations
)

urlpatterns = [
    # Original endpoints
    path('api/group/<str:group_id>/blackout-schedule/', group_blackout_schedule, name='group_blackout_schedule'),
    path('api/group/<str:group_id>/locations/', group_locations, name='group_locations'),
    
    # New search endpoints
    path('api/regions/', list_regions, name='list_regions'),
    path('api/region/<str:region>/locations/', search_by_region, name='search_by_region'),
    path('api/location/<str:location>/schedule/', search_by_location, name='search_by_location'),
    path('api/search/', search_affected_areas, name='search_affected_areas'),
    path('api/locations/', list_locations, name='list_locations'),
]