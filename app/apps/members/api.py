from rest_framework.generics import ListAPIView
from .models import Car
from .serializers import CarSerializer


class CarApiView(ListAPIView):
    queryset = Car.objects
    serializer_class = CarSerializer
