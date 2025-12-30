from django.urls import path
from .views import update_my_profile, admin_update_profile, profile_details,get_all_profiles

urlpatterns = [
    path("my-profile/", profile_details, name="my-profile"),     
    path("update-profile/", update_my_profile, name="update-profile"), 
    path("update-profile-admin/<int:user_id>/", admin_update_profile, name="update-profile-admin"), 
    path("all-profiles/", get_all_profiles, name="all-profiles"), 
]
