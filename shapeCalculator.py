import math

def calculate_area_of_circle():
    while True:
        try:
            radius = float(input("Enter the radius of the circle: "))
            if radius < 0:
                print("Please enter a positive number")
                continue
            area = math.pi * radius ** 2
            print(f"The area of the circle is {area:.2f}")
            break
        except ValueError:
            print("Please enter a valid number")
            
def calculate_area_of_triangle():
    while True:
        try:
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            if base < 0 or height < 0:
                print("Please enter a positive number")
                continue
            area = 0.5 * base * height
            print(f"The area of the triangle is {area:.2f}")
            break
        except ValueError:
            print("Please enter a valid number")
            
def main():
    print("Welcome to the shape calculator!")
    
    while True:
        option = input("Enter 1 to calculate the area of a circle, 2 to calculate the area of a triangle, or 3 to exit: ")
        
        if option == "1":
            calculate_area_of_circle()
        elif option == "2":
            calculate_area_of_triangle()
        elif option == "3":
            print("Thank you for using the shape calculator!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()