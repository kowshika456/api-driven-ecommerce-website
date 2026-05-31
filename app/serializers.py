from rest_framework.serializers import ModelSerializer
from .models import Product

class DataSerializers(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'