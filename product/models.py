from django.db import models
import uuid
from account.models import User

class Product(models.Model):
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    produt_name = models.CharField(max_length=100)
    product_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    product_discount = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    product_image = models.ImageField(upload_to="upload/product/")
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<Product (id: {self.id}), (user: {self.user.email}), (produt_name: {self.produt_name})>'


    

