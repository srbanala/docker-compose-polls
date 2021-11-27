# To calculate monthly payments

def mp_func(Principal,Interest_rate,duration):
    if Interest_rate==0:
        monthly_payment=Principal/(duration*12)
    else:
        r=(Interest_rate/100)/12
        n=duration*12
        monthly_payment=Principal*((r*(1+r)**n)/((1+r)**n-1))
    return monthly_payment

#This program calculates remaining balance.

p=12
def rb_func(Principal,Interest_rate,duration):
    if Interest_rate==0:
        Remaining_loan_balance=Principal*(1-(p/(duration*12)))
        
    else:
        r=(Interest_rate/100)/12
        n=duration*12
        Remaining_loan_balance=Principal*((1+r)**n-(1+r)**p)/((1+r)**n-1)
    return Remaining_loan_balance
#print (remaining_balance_func(Principal,Interest_rate,duration))

#This program display balances yearwise
#print(" Loan amount :",int(Principal),"Interest rate (percent) :",float(Interest_rate))
#print(" Duration (YEARS) : ",duration ," Monthly Payment :",int(monthly_payment_func(Principal,Interest_rate,duration)))
#Total_payment=0
#Principal=remaining_balance_func(Principal)
#Interest_rate=remaining_balance_func(Principal)
#duration=remaining_balance_func(duration)

                                
#for x in range(1,duration+1):
#   BALANCE=remaining_balance_func(Principal,Interest_rate,duration)
#    PAYMENT=0
#    PAYMENT=monthly_payment_func(Principal,Interest_rate,duration)
#    yearly_payment=12*PAYMENT
#    Total_payment=Total_payment+yearly_payment
   # print(" YEAR:",x," BALANCE: ",BALANCE,"TOTAL PAYMENTS:",Total_payment)
#    print(" YEAR{0:5}  BALANCE  {1:10.3f}   TOTAL PAYMENTS  {2:.3f}".format(x,BALANCE,Total_payment))
#    Principal=BALANCE
#    duration=duration-1
#    x=x+1














