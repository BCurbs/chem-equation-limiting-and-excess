# Ben Curby and Brandon Roller, April 21 2021
# Main file
from Compound import Compound
from Equation import Equation, EquationError
from Solution import Solution, SolutionError 
if __name__ == "__main__":
    while True:
        choice = int(input("For inputing a compound press 1. \nFor imputing an equation press 2.\nFor inputing a solution press 3. \nTo exit, press 4\n"))
        if choice==1:
            equation = input("What is the equation of the compound?\n")
            compound = Compound(equation)
            choice = int(input("Your options are:\n1:Get molar mass\n"))
            if choice==1:
                print("The molar mass is: "+str(compound.get_molar_mass()))
            
        elif choice==2:
            equation = input("\nPlease type in a balanced equation.\nExample of format: CaCl+NaCO3+H2O-->NaCl+CaCO3\n").replace(" ", "").replace("=", "-->")
            # Everything after entering an equation goes in the try block.
            # This assumes errors are the users fault which they may not be. 
            try:
                my_equation = Equation(equation)
                print("Reactants: "+str(my_equation.reactants))
                print("Products: " + str(my_equation.products))
                reactants_masses = {}
                for r in my_equation.reactants:
                    reactants_masses[str(r)] = float(input("How much, in grams, is the input mass of " + str(r) + "?" + "\n"))
                my_equation.solve(reactants_masses)
                #print("The limiting compound is: ")
                #print("    " + my_equation.equation)
                print("The outputs of the equation are:")
                for com in my_equation.products:
                    print("    The output of " + com.formula + " is " + str(my_equation.smallest*com.percent)+" grams.")
                print("The excess reactants are:")
                for com in my_equation.reactants:
                    excess = reactants_masses[str(com.formula)]-(my_equation.smallest*com.percent)
                    if excess == 0:
                        print("    There is no excess of " + str(com.formula) + "(So its the limiting reactant)")
                    else:
                        print("    The excess of " + str(com.formula) + " is " + str(excess))
            except EquationError:
                print("Error: Invalid equation syntax.")
                print("I mean its still an error but its prolly just cuz we screwed up programing it")
        elif choice==3:
            solutionstr = input("\nPlease type in a balanced equation.\nExample of format: CaCl+NaCO3+H2O-->NaCl+CaCO3\n").replace(" ", "").replace("=", "-->")
            solution = Solution(solutionstr)
            reactants_volume = {}
            reactants_molarity = {}
            for compound in solution.reactants:
                reactants_volume[str(compound)] = float(input("How much, in ml, is the input volume of " + str(compound) + "?" + "\n"))
                reactants_molarity[str(compound)] = float(input("How much, in ml, is the input volume of " + str(compound) + "?" + "\n"))
        elif choice==4:
            break;
        
