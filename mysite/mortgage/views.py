from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate,login
import datetime
# Create your views here.
from .models import monthly_payment,Remaining_Balance,Monthly_Expenses,Image_Upload
from .forms import Monthly_paymentForm, Monthly_payment_raw_Form,Remaining_Balance_Raw_Form,Monthly_Expenses_Raw_Form,Fibonacci_Form,media_form,FileUpload_Form,FileFieldForm,Image_Upload_Form,Login_Form,ContactForm

from  .my_programs.scripts import *


def monthly_payment_func(request,id):
	Loan= get_object_or_404(monthly_payment,pk=id)
	#principal=413788
	principal=Loan.principal
	Rate=get_object_or_404(monthly_payment,pk=id)
	Interest_rate=Rate.interest
	Years=get_object_or_404(monthly_payment,pk=id)
	duration=Years.duration
	if Interest_rate==0:
		monthly_payment1=principal/(duration*12)
	else:
		r=(Interest_rate/100)/12
		n=duration*12
		monthly_payment1=principal*((r*(1+r)**n)/((1+r)**n-1))
	Monthly_due=get_object_or_404(monthly_payment,pk=id)
	Monthly_due.payment=monthly_payment1
	Monthly_due.save()
	return render(request,'mortgage/mortgage_detail.html' ,{'monthly_payment':monthly_payment1})

def remaining_balance_func(request):
	my_form=Remaining_Balance_Raw_Form()
	#print(my_form)
	if request.method=="POST":
		my_form=Remaining_Balance_Raw_Form(request.POST)
		if my_form.is_valid():
			principal=my_form.cleaned_data['principal']
			interest=my_form.cleaned_data['interest']
			duration=my_form.cleaned_data['duration']
			p       =my_form.cleaned_data['no_of_payments_made']
			print(interest)
			#p=12
			if interest==0:
				Remaining_loan_balance=principal*(1-(p/(duration*12)))
				my_form.cleaned_data['amount_due']=Remaining_loan_balance
				Remaining_Balance.objects.create(**my_form.cleaned_data)
			else:
				r=(interest/100)/12
				n=duration*12
				Remaining_loan_balance=principal*((1+r)**n-(1+r)**p)/((1+r)**n-1)
				my_form.cleaned_data['amount_due']=Remaining_loan_balance
				Remaining_Balance.objects.create(**my_form.cleaned_data)
			print(Remaining_loan_balance)
			return render(request,'mortgage/remaining_balance.html',{'Remaining_balance':Remaining_loan_balance})
	
	else:
			print(my_form.errors)

	context={
		'form':my_form
		}
	return render(request,'mortgage/balance.html',context)



#def loan_details_view(request):
	#form=Monthly_paymentForm(request.POST or None)
	#if form.is_valid():
	#	form.save()
	#context={
	#	'form':form
	#	}
	#return render(request,'mortgage/loan_details.html',context)


def loan_details_view(request):
	my_form=Monthly_payment_raw_Form()
	if request.method=="POST":
		my_form=Monthly_payment_raw_Form(request.POST)
		if my_form.is_valid():
			#my_form.save()
			#print(my_form.cleaned_data)
			#monthly_payment.objects.create(**my_form.cleaned_data)
			principal=my_form.cleaned_data['principal']
			interest=my_form.cleaned_data['interest']
			duration=my_form.cleaned_data['duration']
			if interest==0:
				monthly_payment1=principal/(duration*12)
				my_form.cleaned_data['payment']=monthly_payment1
				monthly_payment.objects.create(**my_form.cleaned_data)
			else:
				r=(interest/100)/12
				n=duration*12
				monthly_payment1=principal*((r*(1+r)**n)/((1+r)**n-1))
				my_form.cleaned_data['payment']=monthly_payment1
				monthly_payment.objects.create(**my_form.cleaned_data)
				return render(request,'mortgage/mortgage_detail.html' ,{'monthly_payment':monthly_payment1})
			#print("monthly payment:",monthly_payment1)
			#print(my_form.cleaned_data)
			#my_form.cleaned_data['payment']=monthly_payment1
			#monthly_payment.objects.create(**my_form.cleaned_data)
			
		else:
			print(my_form.errors)

	context={
		'form':my_form
		}
	return render(request,'mortgage/loan_details.html',context)

def expenses_func(request):
	my_form=Monthly_Expenses_Raw_Form
	if request.method=="POST":
		my_form=Monthly_Expenses_Raw_Form(request.POST)
		if my_form.is_valid():
			#Item  =my_form.cleaned_data['item']
			#Price =my_form.cleanded_data['price']
			print(my_form.cleaned_data)
			output_dict={}
			Monthly_Expenses.objects.create(**my_form.cleaned_data)
			items_list=Monthly_Expenses.objects.all().filter(pub_date__gte=timezone.now()-datetime.timedelta(days=timezone.now().day))
			Total=0
			#print(items_list)
			item_list=list(items_list)
			for data in range(0,len(item_list)):
				queryset=item_list[data]
				#print("Queryset",queryset)
				Total=Total+queryset.price
				output_dict.setdefault(queryset.item,0)
				output_dict[queryset.item]=output_dict[queryset.item]+queryset.price
			print("Total",Total)
			Monthly_Expenses.objects.total=Total
			output_dict['Total']=Total
			
			return render(request,'mortgage/monthly_expenses.html',{'Total_monthly_expenses':output_dict})
		else:
			print(my_form.errors)
	context={
		'form':my_form
		}
	return render(request,'mortgage/monthly_expenses_detail.html',context)


				
			

def monthly_payment_func2(principal,interest,duration):
	if interest==0:
		monthly_payment1=principal/(duration*12)
	else:
		r=(interest/100)/12
		n=duration*12
		monthly_payment1=principal*((r*(1+r)**n)/((1+r)**n-1))
	#Monthly_due=get_object_or_404(monthly_payment,pk=id)
	#Monthly_due.payment=monthly_payment1
	#Monthly_due.save()
	return render(request,'mortgage/mortgage_detail.html' ,{'monthly_payment':monthly_payment1})

def monthly_payment_func3(request):
	my_form=Monthly_payment_raw_Form()
	print(my_form)
	queryset=monthly_payment.objects.all()
	print("{0:^10s}|{1:^10s}|{2:^10s}|{3:^10s}".format("prncipal","interest","duration","payment"))
	print("queryset length:",len(queryset))
	count=0
	output_list=[]
	for item in range(0,len(queryset)):
		count=count+1
		new_list=[]
		x="{0:10d}|{1:10f}|{2:10d}|{3:10f}".format(queryset[item].principal,queryset[item].interest,queryset[item].duration,queryset[item].payment)
		new_list.append(queryset[item].principal)
		new_list.append(queryset[item].interest)
		new_list.append(queryset[item].duration)
		new_list.append(queryset[item].payment)
		output_list.append(new_list)
		print(x)
	print("Output list length :" ,len(output_list))
	return render(request,'mortgage/output_detail.html',{'output':output_list})
	print(count)

def Yearly_Mortagage_Balance(request):
	my_form=Monthly_payment_raw_Form()
	if request.method=="POST":
		my_form=Monthly_payment_raw_Form(request.POST)
		if my_form.is_valid():
			Principal     = my_form.cleaned_data['principal']
			Interest_rate = my_form.cleaned_data['interest']
			duration      = my_form.cleaned_data['duration']
			Total_payment=0
			output_list=[]
			for x in range(1,duration+1):
				BALANCE=rb_func(Principal,Interest_rate,duration)
				PAYMENT=0
				PAYMENT=mp_func(Principal,Interest_rate,duration)
				yearly_payment=12*PAYMENT
				Total_payment=Total_payment+yearly_payment
				#print("Monthly Payment",PAYMENT)
				new_list=[]
				#print(" YEAR:",x," BALANCE: ",BALANCE,"TOTAL PAYMENTS:",Total_payment)
				print(" YEAR{0:5}  BALANCE  {1:10.3f}   TOTAL PAYMENTS  {2:.3f}".format(x,BALANCE,Total_payment))
				Principal=BALANCE
				duration=duration-1
				new_list.append(x)
				new_list.append(round(BALANCE,3))
				new_list.append(round(Total_payment,3))
				output_list.append(new_list)
				x=x+1
			return render(request,'mortgage/yearly_balance_details.html',{'output_list':output_list,'PAYMENT':PAYMENT},)
				
		else:
			print(my_form.errors)
	context={
		'form':my_form
		}
	return render(request,'mortgage/yearly_balance.html',context)


def fibonacci_number(request):
	print(request.user)
	my_form=Fibonacci_Form()
	if request.method=='POST':
		my_form=Fibonacci_Form(request.POST)
		if my_form.is_valid():
			n=my_form.cleaned_data['number']
			output_list=[]
			for k in range(0,n+1):
				if k==0:
					output_list.append(0)
				elif k==1:
					output_list.append(1)
				else:
					output_list.append(output_list[k-2]+output_list[k-1])
				print(output_list)
			return render(request,'mortgage/fibonacci_number.html',{'Fibonacci_number':output_list,'number':n})
		else:
			print(my_form.errors)
	context={'form':my_form}
	return render(request,'mortgage/fibonacci.html',context)
	


##############

def fibonacci_number_1(request):
	form=Login_Form()
	if request.method=='POST':
		user=authenticate(username=request.POST['username'],password=request.POST['password'])
		if user.username is not None:
			print(request.user)
			my_form=Fibonacci_Form()
			if request.method=='POST':
				my_form=Fibonacci_Form(request.POST)
				if my_form.is_valid():
					n=my_form.cleaned_data['number']
					output_list=[]
					for k in range(0,n+1):
						if k==0:
							output_list.append(0)
						elif k==1:
							output_list.append(1)
						else:
							output_list.append(output_list[k-2]+output_list[k-1])
						print(output_list)
					return render(request,'mortgage/fibonacci_number.html',{'Fibonacci_number':output_list,'number':n})
				else:
					print(my_form.errors)
			context={'form':my_form}
			return render(request,'mortgage/fibonacci.html',context)
	return render(request,'mortgage/login.html',{'form':form})

########################
def handle_uploaded_file(f):
	with open('C:\\Users\\anred\\Downloads\\new_file.txt','wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

def media_func(request):
	my_form=media_form()
	if request.method=='POST':
		my_form=media_form(request.POST,request.FILES)
		if my_form.is_valid():
			handle_uploaded_file(request.FILES['file'])
			name=my_form.cleaned_data['title']
			return render(request,'mortgage/media.html',{'Name':'Uloaded sucessfully'})
		else:
			print(my_form.errors)
	context={'form':my_form}
	return render(request,'mortgage/media_initial.html',context)

def file_store(request):
	my_form=FileUpload_Form()
	if request.method=='POST':
		my_form=FileUpload_Form(request.POST,request.FILES)
		if my_form.is_valid():
			
			my_form.save(request.FILES['File'])
			Title=my_form.cleaned_data['Title']
			print("Title is ",Title)
			return render(request,'mortgage/file_upload.html',{'Title':Title,})
		else:
			print(my_form.errors)
	my_form=FileUpload_Form()
	return render(request,'mortgage/file_store.html',{'form':my_form})

from django.views.generic.edit import FormView

class FileFieldView(FormView):
	form_class=FileFieldForm
	template_name='mortgage/files_upload.html'
	
	def post(self,request,*args,**kwargs):
		from_class=self.get_form_class()
		form=self.get_form(form_class)
		files=request.FILES.getllist('files_field')
		if form.is_valid():
			count=0
			for f in files:
				count=count+1
				print("Number of files",count)
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

		

def image_func(request):
	my_form=Image_Upload_Form()
	if request.method=='POST':
		my_form=Image_Upload_Form(request.POST,request.FILES)
		if my_form.is_valid():
			name=my_form.cleaned_data['Name']
			#image=my_form.cleaned_data[request.FILES['Image']]
			print("Name is ",name)
			Image_Upload.objects.create(**my_form.cleaned_data)
			queryset=Image_Upload.objects.all()
			queryset_list=list(queryset)
			item=queryset_list[0].Image
			print("Item ",item)
			#return render(request,'mortgage/media.html',{'Name':name,'Image':request.FILES['Image']})
			return render(request,'mortgage/media.html',{'Name':name,'Image':item})
		else:
			print(my_form.errors)
	context={'form':my_form}
	return render(request,'mortgage/media_initial.html',context)

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def user_login(request):
	my_form=Login_Form()
	if request.method=='POST':
		my_form=Login_Form()
		user=authenticate(username=request.POST['username'],password=request.POST['password'])
		if user is not None:
			m=User.objects.get(username=request.POST['username'])
			print(request.POST['password'])
			print(m.password)
			print(m)
			if m.username==request.POST['username'] and  m.password==user.password:
				request.session['member_id']=m.id
				return HttpResponseRedirect('http://127.0.0.1:8000/mortagage/file_store/')
		else:
			return HttpResponse("Your username and password didn't match.")
	return render(request,'mortgage/login.html',{'form':my_form})

		


def file_response(request):
	#response=HttpResponse(my_data,content_type='application/vnd.ms-excel')
	response=HttpResponse('page upload',content_type='application/vnd.ms-excel')
	response['Content-Disposition']='attachment; filename="Example.xlsx"'	
	return response

	
from django.views.generic.edit import FormView

class ContactView(FormView):
	template_name='contact.html'
	form_clas=ContactForm
	success_url='/thanks/'

	def form_valid(self,form):
		form.send_email()
		return super().form_valid(form)







		



		

		

	