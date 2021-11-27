from django.contrib import admin

# Register your models here.
from .models import monthly_payment,Remaining_Balance,Monthly_Expenses

class monthly_paymentAdmin(admin.ModelAdmin):
	list_display=('principal','interest','duration','payment')

class Remaining_BalanceAdmin(admin.ModelAdmin):
	list_display=('principal','interest','duration')

class Monthly_ExpensesAdmin(admin.ModelAdmin):
	list_display=('item','price','total','pub_date')


admin.site.register(monthly_payment,monthly_paymentAdmin)
admin.site.register(Remaining_Balance,Remaining_BalanceAdmin)
admin.site.register(Monthly_Expenses,Monthly_ExpensesAdmin)

