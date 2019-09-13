from django.db import models

# Create your models here.
class Product(models.Model):
    title =  models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen",upload_to="products")
    price= models.DecimalField(max_digits=10, decimal_places=2)



    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de modificación")
    
    
    # para poder traducirla bien... añadir el verbose_name en plural o google lo traducirá por defecto
    
    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering =  ["-created"]
    def __str__(self):
        return str(self.title) + " - " + str(self.price)+ " €."
