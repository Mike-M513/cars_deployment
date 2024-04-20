from rest_framework.views import APIView, Response
from .models import Advertisement
from cars_app.models import Car
from user_app.models import AppUser
from django.core.serializers import serialize
import json

# Create your views here.

# Get All Advertisements
# Post Advertisement
# Get Specific Advertisement
# Put (update) Specific Advertisement
# Delete Specific Advertisement


class AllAdvertisements(APIView):
    def get(self, request):
        ads = Advertisement.objects.order_by('advertisement_id')
        serialized_ads = serialize('json', ads)
        json_ads = json.loads(serialized_ads)
        return Response(json_ads)
         
    
class SelectedAdvertisement(APIView):
    
    def get_ad(self, id):
        return Advertisement.objects.get(advertisement_id= id)
    
    def get(self, request, id):
        ad =self.get_ad(id)
        serialized_ad = serialize('json', [ad])
        json_ad = json.loads(serialized_ad)
        return Response(json_ad)
    
    def delete(self, request, id):
        ad = self.get_ad(id)
        ad_id = Advertisement.advertisement_id
        ad.delete()
        return Response(f'{ad_id} has been deleted.')


    def put(self, request, id):
        ad = self.get_ad(id)
        if 'advertisement_date' in request.data:
            ad.ChangeDate(request.data['advertisement_date'])
        ad.full_clean()
        ad.save()
        ad = json.loads(serialize('json', [ad]))
        return Response(ad)

class PostAdvertisement(APIView):
    
    def post(self, request):
        request_seller_account_id = request.data.get('seller_account_id')
        request_car_id = request.data.get('car_id')
        
        car_id_data = Car.objects.get(car_model_id= request_car_id)
        seller_account_id_data = AppUser.objects.get(seller_account_id= request_seller_account_id)
        
        account_data = request.data.copy()
        account_data['seller_account_id'] = seller_account_id_data
        account_data['car_id'] = car_id_data
        
        new_ad = Advertisement.objects.create(**account_data)
        new_ad.save()
        new_ad.full_clean()
        
        new_ad = json.loads(serialize('json', [new_ad]))
        return Response(new_ad)