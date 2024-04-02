from .models import Burger
from rest_framework import viewsets, permissions
from .serializers import BurgerSerializer


class BurgerViewSet(viewsets.ModelViewSet):
    #Everything in the burger object (which is everything = everything)
    queryset=Burger.objects.all()
    #specifies the which serializer to use. In this case, we will be using the file: BurgerSerializer to do the serialization and deserialization
    serializer_class=BurgerSerializer
    # unrestricted access to the api
    permission_classes=[permissions.AllowAny]