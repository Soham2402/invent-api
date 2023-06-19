from django.db import models
import uuid

class Item(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4,unique=True)
    name = models.CharField(max_length = 40)
    discription = models.TextField(null=True,blank=True)
    pricd = models.IntegerField(blank=False,null=False)
    quantity = models.IntegerField(blank=False,null=False)
    in_stock = models.BooleanField(default=True)


    def __str__(self):
        return self.name
