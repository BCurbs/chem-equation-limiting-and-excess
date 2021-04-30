# Ben Curby and  Brandon Roller, April 21 2021
# Main file

from Equation import Equation, EquationError, Compound


if __name__ == "__main__":
    
    equation = input("\nPlease type in a compound\n").replace(" ", "").replace("=", "-->")
    # Everything after entering an equation goes in the try block.
    try:
        my_equation = Compound(equation)
        print(my_equation.get_molar_mass())
    except EquationError:
        print("Error: Invalid equation syntax.")
        print("I mean its still an error but its prolly just cuz we screwed up programing it")
