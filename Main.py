# Ben Curby and  Brandon Roller, April 21 2021
# Main file

from Equation import Equation, EquationError


if __name__ == "__main__":
    equation = input("\nPlease type in a balanced equation.\nExample of format: CaCl+NaCO3+H2O-->NaCl+CaCO3\n").replace(" ", "").replace("=", "-->")
    # Everything after entering an equation goes in the try block.
    try:
        my_equation = Equation(equation)
        print("Reactants: "+str(my_equation.reactants))
        print("Products: " + str(my_equation.products))
        reactants_masses = {}
        for r in my_equation.reactants:
            reactants_masses[str(r)] = float(input("How much, in grams, is the input mass of " + str(r) + "?" + "\n"))
        my_equation.solve(reactants_masses)
    except EquationError:
        print("Error: Invalid equation syntax.")
        print("I mean its still an error but its prolly just cuz we screwed up programing it")
