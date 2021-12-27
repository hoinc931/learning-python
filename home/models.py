from django.db import models

# Create your models here.

class categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=50)

    def __str__(self):
        return f"{self.category_id},{self.name}"