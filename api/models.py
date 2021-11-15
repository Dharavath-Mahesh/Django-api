from django.db import models

# Create your models here.
class Cart(models.Model):
    product_name = models.CharField(max_length =20)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()


    def __str__(self):
        return self.product_name

class CartImage(models.Model):
    img_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    products = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name= 'results')
    

    def __str__(self):
        return self.img_name