#1
def can_divided(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        if num1 % num2 == 0:
            return True
        else:
            return False
    except ZeroDivisionError:
        return "cannot devide by zero" 
    except ValueError:
        return "the numbers are not input correct"
        
num1 = input("input the first number: ")
num2 = input("input the second number: ")
print(can_divided(num1, num2))

#2
word = input("input a word please: ")
try:
    print(word[5])
except IndexError:
    print("the word does not have enough letters")

#3
#???