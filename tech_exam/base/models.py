from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    
    def __str__(self) -> str:
        return self.name
    
    
class Order(models.Model):
    stock_ref = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    @property
    def price(self):
        return self.quantity * self.stock_ref.price
    