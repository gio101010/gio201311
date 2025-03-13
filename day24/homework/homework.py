#დავალება: ეცადეთ შექმნათ კალკულატორი პითონში
num1 = int(input("sheiyvane pirveli ricxvi: "))
num2 = int(input("sheiyvane meore ricxvi: "))
operator = input("sheiyvane romelime aqedan --> + | - | * | /: ")

if operator == "+":
     print(num1 + num2)
elif operator == "-":
     print(num1 - num2)
elif operator == "*":
     print(num1 * num2)
else:
     print(num1 / num2)

 #დავალება: მომხარებელს შემოატანინეთ სახელი, შემდეგ ეგ სახელი ჩასვით ლისტში და შემდეგ დაპრინტე მომხმარებლის შემოტანილი სახელი, გაითვალისწინეთ რომ არ უნდა იყოს 1 სახელი ლისტში, რამოდენიმე სახელი ჩაწერეთ, ხოლო დაუპრინტეთ ის სახელი რომელიც მომხმარებელი შეიყვანს

name = input("chawere sheni saxeli:")
names_list = ["vano", "luka", "nika"]
names_list.append(name)