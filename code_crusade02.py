# # 
a = 1000
b = 5

print("Addition of a and b is:", a + b)
print("Subtraction of a and b is:", a - b)
print("Multiplication of a and b is:", a * b)
print("Division of a and b is:", a / b)
print("Modulus of a and b is:", a % b)
print("power of a and b is:", a ** b)

print
a = 5 
b = 5
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
#input by user
customer_name = input("Enter your name: ")
item_price = float(input("Enter the item price: "))
Quantity = int(input("Enter the quantity: "))
Discount = float(input("Enter the discount percentage: "))


Total_price = Quantity * item_price

Discount_amount = Discount / 100 * Total_price

Final_price = Total_price - Discount_amount

#print


print("Customer Name:", type(customer_name))
print("Item Price:", type(item_price))
print("Quantity:", type(Quantity))
print("Discount:", type(Discount))
print("Total Price:", type(Total_price))
print("Discount Amount:", type(Discount_amount))
print("Final Price:", type(Final_price))

print("final_Bill:", Final_price)

#Create variables for Name, Age, Height, and Student Status. Print each value along with its data type.
name = "John Doe"
age = 25
height = 5.9
Student_Status = True

print("Name:", name, "Type:", type(name))
print("Age:", age, "Type:", type(age))
print("Height:", height, "Type:", type(height))
print("Student Status:", Student_Status, "Type:", type(Student_Status))

#Take two numbers as input and print their sum, difference, product, and quotient.

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

print("Sum:", float(num1) + float(num2))
print("Difference:", float(num1) - float(num2))
print("Product:", float(num1) * float(num2))
print("Quotient:", float(num1) / float(num2)) 
   
# Create a python program that calculates a player's final gaming score.

# Take the following input:

player_name = input("Enter the player's name: ")
number_of_matches = int(input("Enter the number of matches played: "))
Points_scored_per_match = int(input("Enter the points scored per match: "))
bonus_points = int(input("Enter the bonus points: "))
#calculate_total_points = number_of_matches * Points_scored_per_match
#final_score = calculate_total_points + bonus_points
#check = final_score > 100
#displayed_the_data_type = type(final_score),type(player_name),type(number_of_matches)
print("Player Name:", player_name)
print("Number of Matches Played:", number_of_matches)
print("Points Scored per Match:", Points_scored_per_match)
print("Bonus Points:", bonus_points)

#Change the CELCIUS to FAHRENHEIT and vice versa. Take the temperature value as input from the user and display the converted temperature.
celsius = float(input("Enter temperature in Celsius: "))

farenheit = (celsius * 9/5) + 32    
kelvin = celsius + 273.15
celsius+=5


print("Temperature in Fahrenheit:", farenheit)
print("Temperature in Kelvin:", kelvin)         
print("Temperature in Fahreneit >= 100:", farenheit >= 100)
print("Temperature in Celsius after adding 5:", celsius)

# pratice questions of day 2 code crusade

name: str = input("Enter your name: ")
age: int = int(input("Enter your age: "))
height: float = float(input("Enter your height in meters: "))
student_status: bool = input("Are you a student? (yes/no): ") == "yes"
print(type(name), type(age), type(height), type(student_status))

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if(a>b):
   print("True")
else:
    print("False")

x = 44
print(type(x))
y = (float(x))
print(type(y))
z = (str(x))
print(type(z))

#Make a calculator that takes two numbers and an operator (+, -, *, /) as input and performs the corresponding operation. Display the result.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("1. Addition (+)", num1 + num2)
print("2. Subtraction (-)", num1 - num2)
print("3. Multiplication (*)", num1 * num2)
print("4. Division (/)", num1 / num2)

a = 10
b = 20
c = 30
d = ((a + b)*c/(a-b))
print(d)
 
English = int(input("Enter your English marks: "))
Pps = int(input("Enter your Pps marks: "))
Maths = int(input("Enter your maths marks: "))
Chemistry = int(input("Enter your chemistry marks: "))
total_marks = (Pps + Maths + Chemistry)
print("Total Marks:", total_marks)
print("Average Marks:", total_marks / 3)
print("Percentage:", (total_marks / 300) * 100)
percentage = (total_marks / 300) * 100
if percentage >= 75:
    print("Grade: B") 
  
a = 10
b = 20
c = 30
print((a+b)**2/(c+1)-a*b)
