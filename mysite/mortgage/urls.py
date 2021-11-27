from django.urls import path
from .import views
from django.views.generic import TemplateView

app_name='mortgage'
urlpatterns=[
	path('',views.loan_details_view,name='loan_details_view'),
	path('balance_func/',views.remaining_balance_func,name='balance_func'),
	path('<int:id>/',views.monthly_payment_func,name='monthly_payment_func'),
	path('monthly_expenses/',views.expenses_func,name='monthly_expenses'),
	path('monthly_payment_func3/',views.monthly_payment_func3,name='monthly_payment_func3'),
	path('Yearly_Mortgage_Balance/',views.Yearly_Mortagage_Balance,name='Yearly_Mortgage_Balance'),
	path('fibonacci_number/',views.fibonacci_number,name='Fibonacci_Number'),
	path('media_func/',views.media_func,name='media_func'),
	path('file_store/',views.file_store,name='file_store'),
	path('post/',views.FileFieldView.post,name='post'),
	path('image_func/',views.image_func,name='image_func'),
	path('login/',views.user_login,name='login'),
	path('file_response/',views.file_response,name='file_response'),
	path('contact/',TemplateView.as_view(template_name="mortgage/contact.html")),
	]
