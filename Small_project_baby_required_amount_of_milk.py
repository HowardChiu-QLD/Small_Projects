'''
Small project of baby's estimate feed per feed.
Key fact:
Newborn baby requires 180 ml of top-up milk per kg of weight.
The amount of milk is calculated as 4-hours of feeding.
'''
print("This is a small program calculating my twin daughter's feeding amount of milk.")
name = input("What is baby's name?")
weight = int(input("Please type in baby's weight in grams."))

def Cal_milk_requirement (weight,name):
    requirement = ((weight/1000) * 180)/6
    return print(f"{name} needs {requirement} ml per feed.")

Cal_milk_requirement(weight, name)