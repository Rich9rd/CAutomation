from rest_framework import serializers

from cleaning.models import Point, Truck, User

class PointSerializer(serializers.ModelSerializer):
    lng = serializers.RegexField(regex = '^-?[0-9]{3}\.[0-9]+$')
    lat = serializers.RegexField(regex = '^-?[0-9]{3}\.[0-9]+$')

    class Meta:
        model = Point
        fields = '__all__'
        read_only = ('lng', 'lat', 'capacity')


class TruckSerializer(serializers.ModelSerializer):
    points = PointSerializer(many=True)

    class Meta:
        model = Truck
        fields = '__all__'
        read_only = ('registrationMark',)


class UserSerializer(serializers.ModelSerializer):
    truck = TruckSerializer()

    class Meta:
        model = User
        fields = ('id', 'truck', 'password', 'email', 'username')        
