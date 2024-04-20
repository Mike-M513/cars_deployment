from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import AppUser, UserProfile
from django.core.serializers import serialize
import json

# Create your views here.
class AllAppUsers(APIView):
    def get(self, request):
        app_users = AppUser.objects.order_by('account_id')
        serialized_app_users = serialize("json", app_users)
        json_app_users = json.loads(serialized_app_users)
        return Response(json_app_users)

class PostAppUser(APIView):
    def post(self, request):
        new_app_user = AppUser.objects.create(**request.data)
        new_app_user.save()
        new_app_user.full_clean()
        new_app_user = json.loads(serialize('json', [new_app_user]))
        return Response(new_app_user)

class AppUserCRUD(APIView):
    def get_app_user(self, id):
        return AppUser.objects.get(account_id=id)
    
    def get(self, request, id):
        app_user = self.get_app_user(id)
        serialized_app_user = serialize("json", [app_user])
        json_app_user = json.loads(serialized_app_user)[0]
        return Response(json_app_user)
    
    def put(self, request, id):
        app_user = self.get_app_user(id)
        if 'email' in request.data:
            app_user.update_email(request.data['email'])
        if 'password' in request.data:
            app_user.update_password(request.data['password'])
        app_user.full_clean()
        app_user.save()
        app_user = json.loads(serialize('json', [app_user]))
        return Response(app_user)
    
    def delete(self, request, id):
        app_user = self.get_app_user(id)
        account_id = app_user.account_id
        app_user.delete()
        return Response(f"Account ID {account_id} has been deleted")

class AllUserProfiles(APIView):
    def get(self, request):
        user_profiles = UserProfile.objects.order_by('profile_id')
        serialized_user_profiles = serialize("json", user_profiles)
        json_user_profiles = json.loads(serialized_user_profiles)
        return Response(json_user_profiles)

class PostUserProfile(APIView):
    def post(self, request):
        requested_app_user_id = request.data.get('account_id')
        app_user = AppUser.objects.get(account_id=requested_app_user_id)
        user_profile_data = request.data.copy()
        user_profile_data['account_id'] = app_user  
        new_user_profile = UserProfile.objects.create(**user_profile_data)
        new_user_profile.save()
        new_user_profile.full_clean()
        new_user_profile = json.loads(serialize('json', [new_user_profile]))
        return Response(new_user_profile) 

class UserProfileCRUD(APIView):
    def get_user_profile(self, id):
        return UserProfile.objects.get(profile_id=id)
    
    def get(self, request, id):
        user_profile = self.get_user_profile(id)
        serialized_user_profile = serialize("json", [user_profile])
        json_user_profile = json.loads(serialized_user_profile)[0]
        return Response(json_user_profile)
    
    def put(self, request, id):
        user_profile = self.get_user_profile(id)

        # assumption that entire address will change; if anything stays the same maybe we can make sure front-end side still sends it
        user_profile.update_address(request.data['street_name'],
                                    request.data['street_number'],
                                    request.data['zip_code'],
                                    request.data['city'])
        user_profile.full_clean()
        user_profile.save()
        user_profile = json.loads(serialize('json', [user_profile]))
        return Response(user_profile)

    def delete(self, request, id):
        user_profile = self.get_user_profile(id)
        user_profile_id = user_profile.profile_id
        user_profile.delete()
        return Response(f"User Profile ID {user_profile_id} has been deleted.")

