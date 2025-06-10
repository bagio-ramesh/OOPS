cash = int(input("Enter Your Cash For Purchase: "))
DISCOUNT_PER = 10
if cash > 2999:
    discount = round(cash * DISCOUNT_PER / 100)
    pay_amount = cash - discount
    print(f"Congrats You got {DISCOUNT_PER}% discount on this product:({discount}off)\nand You have to pay ({pay_amount})rupees only.")
else:
    print(f"There is no discount\nYou can purchase without {DISCOUNT_PER}% discount! ")

