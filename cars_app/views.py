from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import status
from .models import Car, CarModel
from django.core.serializers import serialize
from .serializers import CarSerializer
import json

# Create your views here.
class AllCarModels(APIView):
    def get(self, request):
        car_models = CarModel.objects.order_by('car_model_id')
        serialized_car_models = serialize("json", car_models)
        json_car_models = json.loads(serialized_car_models)
        return Response(json_car_models)
    
class PostCarModel(APIView):
    def post(self, request):
        new_car_model = CarModel.objects.create(**request.data)
        new_car_model.save()
        new_car_model.full_clean()
        new_car_model = json.loads(serialize('json', [new_car_model]))
        return Response(new_car_model)

class CarModelCRUD(APIView):
    def get_car_model(self, id):
        return CarModel.objects.get(car_model_id=id)
    
    def get(self, request, id):
        car_model = self.get_car_model(id)
        serialized_car_model = serialize("json", [car_model])
        json_car_model = json.loads(serialized_car_model)[0]
        return Response(json_car_model)
    
    def put(self, request, id):
        car_model = self.get_car_model(id)
        if 'make' in request.data:
            car_model.update_car_make(request.data['make'])
        if 'model' in request.data:
            car_model.update_car_model(request.data['model'])
        car_model.full_clean()
        car_model.save()
        car_model = json.loads(serialize('json', [car_model]))
        return Response(car_model)
    
    def delete(self, request, id):
        car_model = self.get_car_model(id)
        car_model_id = car_model.car_model_id
        car_model.delete()
        return Response(f"Car Model ID {car_model_id} has been deleted")
    
class AllCars(APIView):
    def get(self, request):
        cars = Car.objects.order_by('car_id')
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
        # serialized_cars = serialize("json", cars)
        # json_cars = json.loads(serialized_cars)
        # return Response(json_cars)

    
class PostCar(APIView):
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # requested_car_model_id = request.data.get('car_model_id')
        # car_model = CarModel.objects.get(car_model_id=requested_car_model_id)
        # car_data = request.data.copy()
        # car_data['car_model_id'] = car_model  
        # new_car = Car.objects.create(**car_data)
        # new_car.save()
        # new_car.full_clean()
        # new_car = json.loads(serialize('json', [new_car]))
        # return Response(new_car)

class CarCRUD(APIView):
    def get_car(self, id):
        return Car.objects.get(car_id=id)
    
    def get(self, request, id):
        car = self.get_car(id)
        serialized_car = serialize("json", [car])
        json_car = json.loads(serialized_car)[0]
        return Response(json_car)
    
    def put(self, request, id):
        car = self.get_car(id)
        if 'owners' in request.data:
            car.increase_number_of_owners(request.data['owners'])
        if 'mileage' in request.data:
            car.increase_mileage(request.data['mileage'])
        car.full_clean()
        car.save()
        car = json.loads(serialize('json', [car]))
        return Response(car)
    
    def delete(self, request, id):
        car = self.get_car(id)
        car_id = car.car_id
        car.delete()
        return Response(f"Car ID {car_id} has been deleted")
    