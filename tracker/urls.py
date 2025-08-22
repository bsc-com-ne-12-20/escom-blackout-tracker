from django.urls import path
from .views import group_blackout_schedule, group_locations

urlpatterns = [
    path('api/group/<str:group_id>/blackout-schedule/', group_blackout_schedule),
    path('api/group/<str:group_id>/locations/', group_locations),
]