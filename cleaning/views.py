from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cleaning.models import Point, Truck, Worker
from cleaning.serializers import PointSerializer, TruckSerializer, WorkerSerializer

class PointListView(generics.ListAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer

class PointUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer

class TruckListView(generics.ListAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer

class TruckUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer

class WorkerListView(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class WorkerUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
