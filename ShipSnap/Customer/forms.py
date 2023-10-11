from django import forms
# from django.contrib import 
from Account.models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=["Goodscategory","weight","kilo_meter"]
        widgets={
            "Goodscategory":forms.Select(attrs={"class":"form-control"}),
            "weight":forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter weight"}),
            "kilo_meter":forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter distance in kilometer"})

            
         }
        
    # weight = forms.IntegerField(label="Product Weight")

class ShipForm(forms.ModelForm):
    class Meta:
        model=ShipModel
        fields=["fr_name","fr_phone","fr_landmark","fr_district","fr_addrss","to_name","to_phone","to_landmark","to_district","to_addrss"]

        widgets={
                "fr_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter name"}),
                "fr_phone":forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter Phone number"}),
                "fr_district":forms.Select(attrs={"class":"form-control"}),
                "fr_landmark":forms.TextInput(attrs={"class":"form-control","placeholder":"Landmark "}),
                "fr_addrss":forms.TextInput(attrs={"class":"form-control","placeholder":"Address"}),
            
                "to_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter name"}),
                "to_phone":forms.NumberInput(attrs={"placeholder":"Enter Phone number"}),
                "to_district":forms.Select(attrs={"class":"form-control"}),
                
                "to_landmark":forms.TextInput(attrs={"class":"form-control","placeholder":"Landmark"}),
                "to_addrss":forms.TextInput(attrs={"class":"form-control","placeholder":"Address"})
                
            }
            