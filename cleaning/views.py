from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cleaning.models import Point, Truck, User
from cleaning.serializers import PointSerializer, TruckSerializer, UserSerializer


def confirm_email(request, key):
    email_confirmation = EmailConfirmationHMAC.from_key(key)
    if email_confirmation:
        email_confirmation.confirm(request)
    return HttpResponseRedirect(reverse_lazy('api'))


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
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WorkerUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
