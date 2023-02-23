print("Welcome to the tip calculator")
print("-----------------------------")
total_bill=float(input("What is the total bill? $"))
tip_precentage=int(input("What precentage tip would you like to give? 10, 12 or 15? %"))
people=int(input("How many people to split the bill? "))
total_tip_amount=(total_bill*tip_precentage)/100
final_bill=total_bill+total_tip_amount
amount_per_person=final_bill/people
final_amount=round(amount_per_person,2)
final_amount="{:.2f}".format(amount_per_person)
print(f"Each person should pay: ${final_amount}")
print("-----------------------------")
print("Thank you for using the tip calculator")