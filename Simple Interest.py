print("Welcome to your simple interest calaculator")

principal = int(input("Enter the principal amount: "))
interest = int(input("Enter the interest rate: "))
time = int(input("Enter the time in years: "))

print("Your return will be: ", principal*time*interest)