print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
# using float converts the datatype into floating point.
tip = int(input("What percentage of tip would you like to give? 10, 15, 20: "))
people = int(input("How many people to split the bill? "))

total_tip = (tip/100)*bill
total_bill = bill + total_tip
bill_each = total_bill/people

print("Bill to be paid by each person: $",round(bill_each,2))
# round(x,y) - rounds off 'x' upto 'y' decimal places.
