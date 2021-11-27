from django.db import models
from django.utils import timezone

# Create your models here.

class monthly_payment(models.Model):
	id = models.AutoField(primary_key=True)
	principal=models.IntegerField()
	interest=models.DecimalField(max_digits=5,decimal_places=3)
	duration=models.IntegerField()
	payment=models.FloatField(default=0)
	
	def __int__(self):
		return self.principal
class Remaining_Balance(models.Model):
	id = models.AutoField(primary_key=True)
	principal           =models.IntegerField()
	interest            =models.FloatField()
	duration            =models.IntegerField()
	no_of_payments_made =models.IntegerField(default=0)
	amount_due          =models.FloatField()
	
	def __int__(self):
		return (self.principal,self.interest,self.duration)

class Monthly_Expenses(models.Model):
	id = models.AutoField(primary_key=True)
	item      = models.CharField(max_length=20)
	price     = models.FloatField()
	pub_date  = models.DateField(default=timezone.now())
	total     = models.DecimalField(max_digits=6,decimal_places=2,default=0)
	
	def __int__(self):
		return self.item

class Fibonacci_number(models.Model):
	id = models.AutoField(primary_key=True)
	number =models.IntegerField()

class media_store(models.Model):
	id = models.AutoField(primary_key=True)
	title=models.CharField(max_length=20)
	file=models.FileField()

class File_Upload(models.Model):
	id = models.AutoField(primary_key=True)
	Title=models.CharField(max_length=20)
	File=models.FileField()

class Image_Upload(models.Model):
	id = models.AutoField(primary_key=True)
	Name=models.CharField(max_length=20)
	#Image=models.ImageField()

class user_login(models.Model):
	id = models.AutoField(primary_key=True)
	username=models.CharField(max_length=20)
	password=models.CharField(max_length=20)

class Car(models.Model):
	id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=255)
	price=models.DecimalField(max_digits=5,decimal_places=3)
	#image=models.ImageField(upload_to='cars')





