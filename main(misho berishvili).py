#1დაწერეთ პროგრამა, სადაც იუზერს კონსოლიდან შეყავს 5 რიცხვი და იპოვეთ ჩაშენებული ფუნქციების გამოყენებით უდიდესი და უმცირესი
#2შეაიმპორტეთ მათემატიკის მოდული და იპოვეთ ფესვი მომხარების მიერ შემოყვანილი რიცხვიდან. (თუ რიცხვი უარყოფითია დაბეჭდეთ რომ უარყოფითი რიცხვიდან ფესვი არ არსებობს)
#3დააგენერირეთ 100 რიცხვი 70 დან 150-ის ინტერვალში და დაბეჭდეთ. გამოიყენეთ random მოდული


#1
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))
number4 = float(input("Enter the fourth number: "))
number5 = float(input("Enter the fifth number: "))
largest = max(number1, number2, number3, number4, number5)
smallest = min(number1, number2, number3, number4, number5)
print("Largest number:", largest)
print("Smallest number:", smallest)

#2
number_sqrt = int(input("input number: "))
import math
if number_sqrt > 0:
    squareroot = math.sqrt(number_sqrt)
    print("the square root of number: ",squareroot)
else:
    print("cant get sqrt from negative numbers")
#3
#???