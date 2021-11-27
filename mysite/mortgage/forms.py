from django import forms

from .models import monthly_payment,media_store,File_Upload,user_login

class Monthly_paymentForm(forms.ModelForm):
	class Meta:
		model=monthly_payment
		fields=[
			'principal',
			'interest',
			'duration',
			'payment'
 			]
			

class Monthly_payment_raw_Form(forms.Form):
	principal             =forms.IntegerField()
	interest              =forms.FloatField()
	duration              =forms.IntegerField()
	

class Remaining_Balance_Raw_Form(forms.Form):
	principal             =forms.IntegerField()
	interest              =forms.FloatField()
	duration              =forms.IntegerField()
	no_of_payments_made   =forms.IntegerField()

class Monthly_Expenses_Raw_Form(forms.Form):
	item  =forms.CharField()
	price =forms.FloatField()
	pub_date  =forms.DateField()

class Fibonacci_Form(forms.Form):
	number=forms.IntegerField()

class media_form(forms.ModelForm):
	class Meta:
		model=media_store
		fields=[
			'title',
			'file'
			]
		
class FileUpload_Form(forms.ModelForm):
	class Meta:
		model=File_Upload
		fields=[
			'Title',
			 'File'
			]

class FileFieldForm(forms.Form):
	file_field=forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))

class Image_Upload_Form(forms.Form):
		Name=forms.CharField(max_length=20)
		Image=forms.ImageField()
class Login_Form(forms.ModelForm):
		username=forms.CharField(max_length=20)
		password=forms.CharField(label='Password',widget=forms.PasswordInput )
		
		class Meta:
			model=user_login
			fields=('username','password')
class ContactForm(forms.Form):
	name=forms.CharField(max_length=20)
	message=forms.CharField(widget=forms.Textarea)
	
	def send_email(self):
		pass


	
	

