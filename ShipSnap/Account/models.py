from django.db import models
from django.contrib.auth.models import User


# Create your models here.
d1={'Electronics':45,'Fashion':25,'Books':15,'Accessories':40,'Home Appliances':60,'Food packets':20}
class Product(models.Model):
    ch=(
        ('Electronics','Electronics'),
        ('Fasion','Fasion'),
        ('Accessories','Accessories'),
        ('Books','Books'),
        ('Home Appliances','Home Appliances'),
        ('Food packets','Food packets')
    )
    Goodscategory=models.CharField(max_length=200,choices=ch,default='Accessories')
    weight=models.FloatField(verbose_name="Product Weight")
    kilo_meter=models.IntegerField(verbose_name="Distance in Kilometer")
    price=models.FloatField(null=True)

class ShipModel(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    fr_name=models.CharField(max_length=30,verbose_name="Your Name")
    fr_phone=models.IntegerField(verbose_name="phone number")
    fr_landmark=models.CharField(max_length=30 , verbose_name="Your landmark")
    opt = (
        ('choose district','choose district'),
        ('kasarkode','kasarkode'),
        ('kannur','kannur'),
        ('kozhikode','kozhikode'),
        ('malappuram','malappuram'),
        ('wayanad','wayanad'),
        ('palakkad','palakkad'),
        ('idukki','idukki'),
        ('thrissur','thrissur'),
        ('eranakulam','eranakulam'),
        ('alappuzha','alappuzha'),
        ('pathanamthitta','pathanamthitta'),
        ('kollam','kollam'),
        ('kottayam','kottayam'),
        ('thiruvananthapuram','thiruvananthapuram')

    )
    fr_district = models.CharField(max_length=100,choices=opt,default='choose district',verbose_name="Your District")
   
    fr_addrss=models.TextField(max_length=300,verbose_name="Your Address")

    to_name=models.CharField(max_length=30,verbose_name="Reciepient name")
    to_phone=models.IntegerField(verbose_name="Reciepient phone")
    to_landmark=models.CharField(max_length=30,verbose_name="Reciepient Landmark")
   
    to_district = models.CharField(max_length=100,choices=opt,default='choose district',verbose_name="Reciepient District")
   
    to_addrss=models.TextField(max_length=300,verbose_name="Reciepient Address")


class save(models.Model):
    ship=models.ForeignKey(ShipModel,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
     


class order(models.Model):
    ship=models.ForeignKey(ShipModel,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ('Confirmed','Confirmed'),
        ('Shipped','Shipped'),
        ('Order cancelled','Order cancelled'),
        
        
    )
    Status=models.CharField(max_length=200,choices=options,default='Confirmed')



