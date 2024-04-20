from django.urls import path
from .views import AllCarModels, PostCarModel, CarModelCRUD, AllCars, PostCar, CarCRUD

urlpatterns = [
    path('all_car_models', AllCarModels.as_view(), name='all_car_models'),
    path('all_cars', AllCars.as_view(), name='all_cars'),
    path('post_car_model', PostCarModel.as_view(), name='post_car_model'),
    path('car_model_crud/<int:id>/', CarModelCRUD.as_view(), name='car_model_crud'),
    path('post_car', PostCar.as_view(), name='post_car'),
    path('car_crud/<int:id>/', CarCRUD.as_view(), name='car_crud'),
]