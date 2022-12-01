from rest_framework import generics, permissions
from .models import Car
from .serializers import CarSerializer


class CarList(generics.ListCreateAPIView):
    """ 
    List car posts and create post for logged in users.
    Perform_create method ties a post to the logged in user.
    """

    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Car.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
