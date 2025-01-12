#1შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა ორი რიცხვი და დაითვლის (დააბრუნებს) მათ საშუალო არითმეტიკულს. გამოიძახეთ ფუნქცია 3-ჯერ სხვადასხვა რიცხვებისთვის და დაბეჭდეთ შედეგი.

 #2დაწერეთ ფუნქცია, რომელსაც არგუმენტად გადაეცემა ორი რიცხვი და დაითვლის მათ საშუალო არითმეტიკულს და დაბეჭდავს შედეგს (გაითვალისწინეთ რომ დაბეჭდვა უნდა მოხდეს ფუნქციის შიგნით - ფუნქცია არ აბრუნებს მნიშვნელობას). გამოიძახეთ ფუნქცია 3-ჯერ სხვადასხვა რიცხვებისთვის.

#3შექმენით ფუნქცია, რომელიც დაითვლის (დააბრუნებს) არგუმენტად გადაცემული რიცხვის კუბს. გამოიძახეთ ფუნქცია რამდენიმეჯერ და დაბეჭდეთ მიღებული შედეგი.


#1
def avarage(number1, number2):
    return (number1 + number2) / 2
result = avarage(7,9)
print(result)

def avarage(number1, number2):
    return (number1 + number2) / 2
result = avarage(10,12)
print(result)

def avarage(number1, number2):
    return (number1 + number2) / 2
result = avarage(17,27)
print(result)

#2
def avarage():
    result = (18 + 22) / 2
    print(result)
avarage()

def avarage():
    result = (26 + 44) / 2
    print(result)
avarage()

def avarage():
    result = (12 + 14) / 2
    print(result)
avarage()
#3
def square(i):
    return i * i

result = square(4)
print(result)

def square(i):
    return i * i

result = square(6)
print(result)

def square(i):
    return i * i

result = square(12)
print(result)