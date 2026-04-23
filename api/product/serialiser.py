from product.models import Product
from rest_framework import serializers

class ProductSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    is_deleted = serializers.ReadOnlyField()
    class Meta:
        model = Product
        fields = '__all__'

        
