from rest_framework import generics
from .models import Car
from .serializers import CarSerializer


class CarList(generics.ListAPIView):
    """ Car list view """

    serializer_class = CarSerializer
    queryset = Car.objects.all()
