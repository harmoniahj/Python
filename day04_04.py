# Input (사용자 입력)
# 기본타입 (str)

name = input("Enter Your Name : ")
grade = input("Enter Your Grade : ")
company = input("Enter Your Company : ")

print('name :', name, ',', 'grade: ', grade, ',', 'company :', company) # name : DB , grade:  2 , company : Good

number = input("Enter Number : ")
name = input("Enter Your Name : ")

print('type of number :', type(number), 'type of name :', type(name)) # type of number : <class 'str'> type of name : <class 'str'>

# 계산
number = int(input("Write Number : "))
number2 = int(input("Write Number2 : "))

total = number + number2

print('type of number :', type(number), 'type of number2 :', type(number2)) # type of number : <class 'int'> type of number2 : <class 'int'>
print('total :', total) # total : 30

float_number = float(input("Write Number : "))
float_number2 = float(input("Write Number2 : "))

total = float_number + float_number2

print('type of number :', type(float_number), 'type of number2 :', type(float_number2)) # type of number : <class 'float'> type of number2 : <class 'float'>
print('total :', total) # total : 5.83

print("FirstName : {0}, LastName : {1}".format(input("Enter first name : "), input("Enter second name : "))) # FirstName : Kim, LastName : Nice Name