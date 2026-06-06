import math

while True:
    print("==================")
    print("Area Calculator 📐")
    print("==================")
    print("1) Triangle")
    print("2) Rectangle")
    print("3) Square")
    print("4) Circle")
    print("5) Quit")

    shape = input("Which shape: ")

    if shape == "1":
        base = float(input("Base: "))
        height = float(input("Height: "))
        area = (height * base) / 2
        print("The area is", area)

    elif shape == "2":
        length = float(input("Length: "))
        width = float(input("Width: "))
        area = length * width
        print("The area is", area)

    elif shape == "3":
        side = float(input("Side: "))
        area = side ** 2
        print("The area is", area)

    elif shape == "4":
        radius = float(input("Radius: "))
        area = math.pi * radius ** 2
        print("The area is", area)

    elif shape == "5":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice, please pick 1-5.")
