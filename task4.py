import math

class Hexagon:
    def __init__(self, cnic_last_digit):
        self.side_length = cnic_last_digit
        self.angle = 120

    def calcArea(self):
        return 1.5 * math.sqrt(3) * self.side_length ** 2

    def calcPeri(self):
        return 6 * self.side_length

    def calcAngleSum(self):
        return 360  # Sum of all angles in a hexagon is always 360 degrees

    def display(self):
        print(f"Hexagon - Area: {self.calcArea():.2f}, Perimeter: {self.calcPeri()}, Sum of Angles: {self.calcAngleSum()} degrees")


class Square:
    def __init__(self, cnic_last_digit):
        self.side_length = cnic_last_digit + 1

    def calc_area_square(self):
        return self.side_length ** 2

    def calc_peri_square(self):
        return 4 * self.side_length

    def display_square(self):
        print(f"Square - Area: {self.calc_area_square()}, Perimeter: {self.calc_peri_square()}")


def main():
    cnic = input("Enter your CNIC: ")
    cnic_last_digit = int(cnic[-1])

    hexagon = Hexagon(cnic_last_digit)
    square = Square(cnic_last_digit)
   

    while True:
        print("Enter 1 to calculate area,perimeter,and sum of angles of hexagon")
        print("Enter 2 to calculate area and perimeter of square")
        print("press any other key to exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            hexagon.display()
        elif choice == '2':
            square.display_square()
        else:
            print("Program terminated.")
            break

if __name__ == "__main__":
    main()
