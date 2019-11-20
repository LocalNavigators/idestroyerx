from django.db import models
#from django_pandas.managers import DataFrameManager

# Create your models hre.
class FilesInventory(models.Model):
    #File1=models.CharField(max_length=3000, blank=True) 
	File1=models.FileField(upload_to='', blank=True)
	#product_name=models.TextField()
	objects = models.Manager()
	#pdobjects = DataFrameManager()  # Pandas-Enabled Manager 
'''class Product(models.Model):
  	product_name=models.TextField()
    objects = models.Manager()
    pdobjects = DataFrameManager()  # Pandas-Enabled Manager '''