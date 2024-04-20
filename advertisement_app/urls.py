from django.urls import path
from .views import AllAdvertisements, SelectedAdvertisement, PostAdvertisement

urlpatterns = [
    path('all_advertisements', AllAdvertisements.as_view(), name='all_advertisements'),
    path('<int:id>/', SelectedAdvertisement.as_view(), name='selected_advertisement'),
    path('new_advertisement', PostAdvertisement.as_view(), name= 'new_advertisement')
]