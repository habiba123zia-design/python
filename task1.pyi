print(" welcome to our website")
The_amount=int(input("enter the amount you want to pay:"))
discount=0
if The_amount<100:
    discount=0
    print(f" your discount is {discount}%")
    print(f" your total amount to pay is {The_amount - (The_amount * discount / 100)}")
elif   500>=The_amount>=100:
    discount=10
    print(f" your discount is {discount}%")
    print(f" your total amount to pay is {The_amount - (The_amount * discount / 100)}")
elif The_amount>500:
    discount=20
    print(f" your discount is {discount}%")
    print(f" your total amount to pay is {The_amount - (The_amount * discount / 100)}")