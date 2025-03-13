  #1- კალკულატორი

def simplecalculator(num1, num2, operation):
    if operation == "დამატება":
        return num1 + num2
    elif operation == "გამოკლება":
        return num1 - num2
    elif operation == "გამრავლება":
        return num1 * num2
    elif operation == "გაყოფა":
        if num2 == 0:
            return "ნულზე გაყოფა შეუძლებელია"
        else:
            return num1 / num2
    else:
        return "Bruh"

result1 = simplecalculator(10, 5, "დამატება")
print(result1) 

result2 = simplecalculator(10, 5, "გამოკლება")
print(result2)  

result3 = simplecalculator(10, 5, "გამრავლება")
print(result3)  

result4 = simplecalculator(10, 5, "გაყოფა")
print(result4)  

result5 = simplecalculator(10, 0, "გაყოფა")
print(result5)





# მართკუთხედის ფართობი

def calculate_area(length, width):
    area = length * width
    return area


length = 10
width = 5
print(calculate_area(length, width))




# მაქსიმალური რიცხვის პოვნა
def findmax(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

num1 = 7
num2 = 12
print(findmax(num1, num2))


#ლუწია თუ კენტია
def კენტი_ლუწი():
    number = int(input("შემოიყვანე რიცხვი: "))
    if number % 2 == 0:
        print("ლუწია")
    else:
        print("კენტია")

კენტი_ლუწი()
         