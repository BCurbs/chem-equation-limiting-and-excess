# Ben Curby and  Brandon Roller, April 21 2021
# Main file

from Equation import Equation, EquationError, Compound


if __name__ == "__main__":
    
    equation = input("\nPlease type in a compound\n").replace(" ", "").replace("=", "-->")
    # Everything after entering an equation goes in the try block.
    mass = float(input("how much of that compound do you have\n"))
    
    try:
        compound = Compound(equation)
        molarmass=mass/compound.get_molar_mass()
        print(compound.get_molar_mass())
        liters = float(input("How many liters of water\n"))
        print("The molarity is:" + str(molarmass/liters))
    except EquationError:
        print("Error: Invalid equation syntax.")
        print("I mean its still an error but its prolly just cuz we screwed up programing it")
