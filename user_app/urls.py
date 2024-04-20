from django.urls import path
from .views import AllAppUsers, PostAppUser, AppUserCRUD, AllUserProfiles, PostUserProfile, UserProfileCRUD

urlpatterns = [
    path('all_app_users', AllAppUsers.as_view(), name='all_app_users'),
    path('post_app_user', PostAppUser.as_view(), name='post_app_user'),
    path('app_user_crud/<int:id>/', AppUserCRUD.as_view(), name='app_user_crud'),
    path('all_user_profiles', AllUserProfiles.as_view(), name='all_user_profiles'),
    path('post_user_profile', PostUserProfile.as_view(), name='post_user_profile'),
    path('user_profile_crud/<int:id>/', UserProfileCRUD.as_view(), name='user_profile_crud'),
]