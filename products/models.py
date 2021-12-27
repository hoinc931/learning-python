from django.db import models
from home.models import categories

# Create your models here.

class products(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(null=False, max_length=200)
    category_id = models.ForeignKey(categories, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images", null=False, default=None)

    def __str__(self):
        return f"{self.product_id},{self.name},{self.description},{self.image}"
