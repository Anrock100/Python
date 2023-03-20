# Description: This program is used to calculate the discount and net amount of the customer
# Function to display heading
def initialDisplay():
    a="""Sunway College BhatBhateni"""
    b="""Kathmandu,Nepal"""
    c="""date: 2077/01/01"""
    print(a)
    print(b)
    print(c)
    print("=============================================")

#fuction for input and information
def initialInformation(): 
    n=int(input("Enter the number of customers: "))
    #first for loop for different customers
    for i in range(n):
        #input for details
        name=input(f"Enter the name of customer [{i+1}]: ")
        address=input(f"Enter the address of customer {i+1}: ")
        email=input(f"Enter the email of customer {i+1}: ")
        itemno=int(input(f"Enter the number of items of customer : "))
        for j in range(itemno):
            totalPrice=0
            itemname=input(f"Enter the name of item {j+1}: ")
            itemprice=int(input(f"Enter the price of item {j+1}: "))
            itemqty=int(input(f"Enter the quantity of item {j+1}: "))
            totalPrice=totalPrice+itemprice*itemqty

        #callig functions
        netAmount,discount=calculation(totalPrice)
        #forbiling purpose 
        initialDisplay()
        displayInformation(name,address,email,totalPrice,discount,netAmount)


#function for calculation of discount and Net amount
def calculation(totalPrice):
    discount=0
    if totalPrice<=5000:
        discount = totalPrice*0.05
    elif totalPrice<=7000:
        discount=(5000*0.05)+(totalPrice-5000)*0.08
    elif totalPrice<=10000:
        discount=(5000*0.05)+(2000*0.08)+(totalPrice-7000)*0.10
    else:
        discount=(5000*0.05)+(2000*0.08)+(3000*0.10)+(totalPrice-10000)*0.15
    # net amount after discount
    netAmount=totalPrice-discount
    return netAmount,discount

#function for displaying information by printing them
def displayInformation(name,address,email,totalPrice,discount,netAmount):
    print(f"Customer Name: {name}")
    print(f"Customer Address: {address}")
    print(f"Customer Email: {email}")
    print(f"Total Price: {totalPrice}")
    print(f"Discount: {discount}")
    print(f"Net Amount: {netAmount}")


#funrion call
initialDisplay()
initialInformation()