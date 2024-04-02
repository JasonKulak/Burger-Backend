from .models import Burger
from rest_framework import serializers

# serializing and deserializing data (and data is the data from the table) to json
class BurgerSerializer(serializers.HyperlinkedModelSerializer):
    # for configuring the burgerserializer above
    class Meta:
            #model to serialize
            model=Burger
            #fields to show
            # fields=('id', 'nameOfBurger', 'ingredients')
            fields='__all__'