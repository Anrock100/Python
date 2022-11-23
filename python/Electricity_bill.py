def intitaldisplay():
    display='''                     Sunway Int' Billing system             
                      Maitidevi,Kathmandu        Date:10th November
________*________*_________*__________*__________*________*________'''
    print(display)

def inputInformation():
    CustomerName=input("Enter the customer name:")
    CustomerAddress=input("Enter the customer address:")
    CustomerUnit=int(input("Enter the total unit consume:"))
    return CustomerName,CustomerAddress,CustomerUnit


def CalculationUnit(ConsumedUnit):

    if(ConsumedUnit<=20):
        rate=ConsumedUnit*4
        discount=0
        
        
    elif(20>=ConsumedUnit<=50):
        rate=20*4+(ConsumedUnit-20)*7.5
      
        
        
    elif(ConsumedUnit>=50 and ConsumedUnit<=150):
        rate=(ConsumedUnit-50)*9.5+30*7.5+20*4
        discount=(ConsumedUnit-50)*9.5*5/100
        AfterDiscoutAmt=rate-discount
        
        
    elif(ConsumedUnit>=150 and ConsumedUnit<=250):
        rate=(ConsumedUnit-150)*11.5+100*9.5+30*7.5+20*4
        discount=(ConsumedUnit-150)*11.5*10/100
        Totaldiscount=discount+100*9.5*5/100
        AfterDiscoutAmt=rate-Totaldiscount
        
        
    elif(ConsumedUnit>=250):
        rate=(ConsumedUnit-250)*13.5+100*11.5+100*9.5+30*7.5+20*4
        discount=(ConsumedUnit-250)*13.5*15/100
        Totaldiscount=discount+100*11.5*10/100
        AfterDiscoutAmt=rate-Totaldiscount
      
        
        

    return rate,discount,Totaldiscount,AfterDiscoutAmt


intitaldisplay()
CustomerName,CustomerAddress,CustomerUnit =inputInformation()
rate, discount, Totaldiscount, AfterDiscoutAmt= CalculationUnit(CustomerUnit)
intitaldisplay()

def displayInformation(CustomerName,CustomerAddress, rate,  Totaldiscount,ConsumedUnit):
    print(f'''Customer Name :{CustomerName} \t  "CustomerAddress :{CustomerAddress} \t"  
        "Customer Consumed Unit :{ConsumedUnit}
        Total amount to pay :{rate}
        "Total Discount :{Totaldiscount} ''')


displayInformation(CustomerName,CustomerAddress,rate,Totaldiscount,CustomerUnit)
        
        

