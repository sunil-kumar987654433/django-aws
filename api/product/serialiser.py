from product.models import Product
from rest_framework import serializers
from django.utils import timezone
from zoneinfo import ZoneInfo

class ProductSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    is_deleted = serializers.ReadOnlyField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()


    def get_created_at(self, instance):
        return timezone.localtime(instance.created_at)
    def get_updated_at(self, instance):
        return timezone.localtime(instance.updated_at)
    class Meta:
        model = Product
        fields = '__all__'

        
