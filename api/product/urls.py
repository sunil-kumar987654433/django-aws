
from django.urls import path
from api.product import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register("product", views.ProductViewSet, basename='product')


urlpatterns = [
    
]+router.urls

