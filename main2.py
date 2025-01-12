#1. შეიყვანეთ ნებისმიერი რიცხვი და დაბეჭდეთ ამ რიცხვის პირველი ციფრი.

#2. შეიყვანეთ ნებისმიერი რიცხვი. იპოვეთ ამ რიცხვის ციფრთა რაოდენობა და დაბეჭდეთ. (len ფუნქციის გარეშე)

#3. დაბეჭდეთ 5-ის ჯერადი რიცხვები 20-დან 125-ის ჩათვლით.

#4. დაბეჭდეთ 8-ის ჯერადი რიცხვები 200-დან 25-ის ჩათვლით კლებადობით.

#5. კონსოლიდან მომხარებელმა უნდა შეიყვანოს ნებისმიერი რიცხვი. დაადგინეთ არის თუ არა შეტანილი რიცხვი პალინდრომი.
     
     
#1
number = int(input("input number: "))
while number > 10:
    number = number // 10
print(number)     
     
#2
amount = 0
    
number = int(input("input number: "))
while number > 0:
    number //= 10
    amount += 1
print(amount)
    
#3
x = 20
 
for x in range (20, 126):
if x % 5 == 0
print(x)
    
#4
x = 200
while x > 25:
    if x % 8 == 0:
        print(x)
    x -= 1    

#5
reverse = 0
point = 0

number = int(input("input the number: "))
number1 = number
while number > 0:
    point = number % 10
    reverse = reverse * 10 + point
    number //= 10
if reverse == number1:
    print("it is palindrome")
else:
    print("it is not palindrome")