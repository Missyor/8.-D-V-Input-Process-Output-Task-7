##Ask the user for the principal
principal = input("Enter principal amount: ")
principal = float(principal)
##Ask the user for the interest rate
rate = input("What is the interest rate? ")
rate = float(rate)
##Ask the user for the ength of time
time = input("What is the time in years? ")
time = float(time)
##Simple interest formula - how much interest I will pay
amount = principal * rate * time
##Display the answer
print(amount)







#How can we improve our code?
###############################################

##Ask the user for the principal
principal = input("Enter principal amount: ")
principal = float(principal)
print("\n")

##Ask the user for the interest rate
rate = input("What is the interest rate? ")
rate = float(rate)
print("\n")

##Ask the user for the ength of time
time = input("What is the time in years? ")
time = float(time)
print("\n")

##Simple interest formula - how much interest I will pay
amount = principal * rate * time

##Display the answer
print("The interest is €",amount)
print("\n")

##Can we write some code to find the new total amount that I owe
total = principal + amount
print("You will owe €",total, "over", time, "years")
print("\n")
##Can we improve this by working out how much they would owe per year?
perYear = float(total/time)
print("That is €", round(perYear, 2), "per year")

##WHat happens if you chane float to int?

##Copy and paste the above code below and change the float command for the interest variable to int. What happens?
##Write down the type of error and comment it out.
print("hello", total)