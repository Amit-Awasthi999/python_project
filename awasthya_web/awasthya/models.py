from django.db import models

# Create your models here.
PRODUCT_TYPES = (
        ('men','MEN'),
        ('women','WOMEN'),
        ('kids','KIDS'),
        ('other','OTHER'),

)
CATOGARY_TYPES = (
        ('t-shirt','T-shirt'),
        ('shirt','shirt'),
        ('Trouser','Trouser'),
        ('jeans','Jeans'),
        ('tops','Tops'),
        ('leggings','Leggings'),
        ('sarees','Sarees'),
        ('kurta','Kurta'),
        ('mask','Mask'),
    

)
class product(models.Model):
    app_label = 'awasthya'
    name = models.CharField(max_length = 100)
    img =models.ImageField( upload_to='pics')
    desc = models.TextField() 
    price = models.IntegerField()
    offer = models.BooleanField(default = False)
    offer_value = models.CharField(max_length = 2)
    product_catogary = models.CharField(max_length=15, default='men' , choices = PRODUCT_TYPES)
    catogary_type = models.CharField(max_length=15, default='t-shirt' , choices = CATOGARY_TYPES)

