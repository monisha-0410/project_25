from django.db import models

# Create your models here.
class Country(models.Model):
    Country_id=models.IntegerField(primary_key=True)
    Country_Name=models.CharField(max_length=100)
    population=models.IntegerField()
    def __str__(self):
        return self.Country_Name

class Capital(models.Model):
    Capital_Id=models.IntegerField(primary_key=True)
    Country_id=models.OneToOneField(Country,on_delete=models.CASCADE)
    capital_name=models.CharField(max_length=100)

    def __str__(self):
        return self.capital_name