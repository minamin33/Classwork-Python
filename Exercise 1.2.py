hours = (int(input("Enter Hours:")))
rate = (float(input("Enter Rate:")))
try :
    if hours <= 40:
        pay = hours * rate
    else:
        pay = ((hours - 40) * (1.5 * rate))+ (40 * rate)
    print(("Pay = "),pay)
except:
    print('Error, please enter numeric input' )

