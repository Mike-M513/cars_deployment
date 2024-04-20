from rest_framework import serializers
from .models import Car, CarModel


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('make', 'model')

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('car_model_id', 'number_of_owners', 'registration_number', 'manufacture_year', 'number_of_doors', 'mileage')

    # def create(self, validated_data):
    #     model_data = validated_data.pop('car_model_id')
    #     car = Car.objects.create(**validated_data)
    #     for model_datum in model_data:
    #         model = CarModel.objects.create(**model_datum)
    #         car.car_model_id.add(model)
    #     return car