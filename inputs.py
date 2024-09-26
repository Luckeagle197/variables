name = input("What is your name?")
age = int(input("How old are you?"))
height = float(input("What is your height?"))

def checkIfTall(heightValue):
    if heightValue > 1.5:
        print("You are tall.")

print("Your name is", name, "You are", age, "years old", "I am", height, "metres tall")
checkIfTall(height)