#1. შექმენით 10 ელემენტიანი სია, რომლის ელემენტებია ნებისმიერი შემთხვევითი მთელი
#რიცხვები 25-დან 110-მდე. დაბეჭდეთ სია და იპოვეთ მინიმალური ელემენტი.

#2. დაწერეთ ფუნქცია, რომელსაც არგუმენტად გადაეცემა 2 სია. ფუნქცია აბრუნებს
#მნიშვნელობა True-ს თუ სიებს აქვთ ერთი მაინც საერთო ელემენტი. წინააღმდეგ
#შემთხვევაში აბრუნებს False მნიშვნელობას.

#1
import random
numbers = []
for _ in range(10):
    numbers.append(random.randrange(25, 100))
print(numbers)
print(min(numbers))

#2
#???
        