# Ben Curby and Brandon Roller, April 21 2021

# File containing resource classes
# An Equation is made up of Compounds which is made up of Elements
# File includes a custom exception used for flagging errors with the inputted equation
debug = False
# Periodic table of molar masses
import re

from Compound import Compound
table = {
  "He":	4.002602,
  "Li":	6.941,
  "Be":	9.012182,
  "Ne":	20.1797,
  "Na":	22.989768,
  "Mg":	24.3050,
  "Al":	26.981539,
  "Si":	28.0855,
  "Cl":	35.4527,
  "Ar":	39.948,
  "K":	39.0983,
  "Ca":	40.078,
  "Sc":	44.955910,
  "Ti":	47.88,
  "V":	50.9415,
  "Cr":	51.9961,
  "Mn":	54.93805,
  "Fe":	55.847,
  "Co":	58.93320,
  "Ni":	58.6934,
  "Cu":	63.546,
  "Zn":	65.39,
  "Ga":	69.723,
  "Ge":	72.61,
  "As":	74.92159,
  "Se":	78.96,
  "Br":	79.904,
  "Kr":	83.80,
  "Rb":	85.4678,
  "Sr":	87.62,
  "Y":	88.90585,
  "Zr":	91.224,
  "Nb":	92.90638,
  "Mo":	95.94,
  "Tc":	98,
  "Ru":	101.07,
  "Rh":	102.90550,
  "Pd":	106.42,
  "Ag":	107.8682,
  "Cd":	112.411,
  "In":	114.82,
  "Sn":	118.710,
  "Sb":	121.757,
  "Te":	127.60,
  "Xe":	131.29,
  "Cs":	132.90543,
  "Ba":	137.327,
  "La":	138.9055,
  "Ce":	140.115,
  "Pr":	140.90765,
  "Nd":	144.24,
  "Pm":	145,
  "Sm":	150.36,
  "Eu":	151.965,
  "Gd":	157.25,
  "Tb":	158.92534,
  "Dy":	162.50,
  "Ho":	164.93032,
  "Er":	167.26,
  "Tm":	168.93421,
  "Yb":	173.04,
  "Lu":	174.967,
  "Hf":	178.49,
  "Ta":	180.9479,
  "W":	183.85,
  "Re":	186.207,
  "Os":	190.2,
  "Ir":	192.22,
  "Pt":	195.08,
  "Au":	196.96654,
  "Hg":	200.59,
  "Tl":	204.3833,
  "Pb":	207.2,
  "Bi":	208.98037,
  "Po":	209,
  "At":	210,
  "Rn":	222,
  "Fr":	223,
  "Ra":	226.0254,
  "Ac":	227,
  "Th":	232.0381,
  "Pa":	213.0359,
  "U":	238.0289,
  "Np":	237.0482,
  "Pu":	244,
  "Am":	243,
  "Cm":	247,
  "Bk":	247,
  "Cf":	251,
  "Es":	252,
  "Fm":	257,
  "Md":	258,
  "No":	259,
  "Lr":	260,
  "Rf":	261,
  "Db":	262,
  "Sg":	263,
  "Bh":	262,
  "Hs":	265,
  "Mt":	266,
  "N": 14.00674,
  "B": 10.811,
  "C": 12.011,
  "O": 15.9994,
  "F": 18.9984032,
  "I": 126.90447,
  "S": 32.066,
  "P": 30.973762,
  "H":	1.00794,
}

class SolutionError(Exception):
    pass

# Element class
class Element:
    def __init__(self, symbol):
        self.symbol = symbol

    def __repr__(self):
        return self.symbol

    def __str__(self):
        return self.__repr__()

    def get_molar_mass(self):
        return table[self.symbol]


# Compound class
class Compound:
    def __init__(self, formula):
        self.formula = formula
        self.elements = []
        self.percent = 0
        # TODO: manipulate the formula string to fill a list of Elements.
        #done
        
        
        if re.findall('[0-9]', self.formula[0]):
            #splits the equation up by capitol letters
            if re.findall('[0-9]', self.formula[1]):
                repeat = int(self.formula[0:1])
                self.formula = self.formula[2:]
            else:
                repeat = int(self.formula[0])
                self.formula = self.formula[1:]
        else:
            repeat = 1
        
        if self.formula.find("(")!=-1:#this code looks for parentheses and gets the multiplier after and the elements in them and repeats it. 
            cord1 = self.formula.index('(')
            cord2 = self.formula.index(')')
            parems = self.formula[int(cord1):int(cord2)+1]
            multiplier = self.formula[self.formula.index(")")+1]
            print(parems)
            print(multiplier)
            self.formula = self.formula[0:int(cord1)]+self.formula[int(cord2)+2:len(self.formula)]
            for x in range(0,int(multiplier)):
                self.formula+=parems[1:len(parems)-1]
        a = re.findall('[A-Z][^A-Z]*', self.formula)
        
        for b in a:#for each element look through and add them the number of times of the number after them. 

            if debug:
                print(repeat)
            for x in range(0, repeat):
                if debug:
                    print(re.findall('\d+', b))
                q = (re.findall('\d+', b))
                if not q:
                    q.append(1)
                    if debug:
                        print(q)
                for o in range(0, int(q[0])):
                    
                    self.elements.append(Element(re.sub(r'[0-9]+', '', b)))
        

    def __repr__(self):
        return self.formula

    def __str__(self):
        return self.__repr__()

    def get_molar_mass(self):
        sum = 0
        for e in self.elements:
            sum += e.get_molar_mass()
        return sum


# Equation class
class Solution:
    def __init__(self, string: str):
        self.equation = string
        self.reactants = []
        self.products = []
        try:
            split_string: list = self.equation.split("-->")
            for r in split_string[0].split("+"):
                self.reactants.append(Compound(r))
            for p in split_string[1].split("+"):
                self.products.append(Compound(p))
        except Exception:
            raise EquationError
        self.get_proportion()
    def __repr__(self):
        return self.equation

    def __str__(self):
        return self.__repr__()
    
    def solve(self, dictionary):
        self.dictionary = dictionary
        sidemass = 0
        smallest = 10000000000000000000000#in programing never do this. I just picked an arbitrarily large number. 
        for compound in self.reactants:
            sidemass = dictionary[str(compound.formula)] / compound.percent
            if sidemass<smallest:
                smallest = sidemass
                smallestcompound = compound.formula
        print("The limiting compound is: ")
        print("    " + smallestcompound)
        print("The outputs of the equation are:")
        for com in self.products:
            print("    The output of " + com.formula + " is " + str(smallest*com.percent)+" grams.")
        print("The excess reactants are:")
        for com in self.reactants:
            excess = dictionary[str(com.formula)]-(smallest*com.percent)
            if excess == 0:
                print("    There is no excess of " + str(com.formula) + "(So its the limiting reactant)")
            else:
                print("    The excess of " + str(com.formula) + " is " + str(excess))
    def get_proportion(self):
        self.reactantsmass = 0
        self.productsmass = 0
        for x in self.products:
            self.productsmass += x.get_molar_mass()
        for x in self.reactants:
            self.reactantsmass += x.get_molar_mass()
            if debug:
                print(reactantsmass)
        for x in self.products:
            x.percent = x.get_molar_mass()/self.productsmass
        for x in self.reactants:
            x.percent = x.get_molar_mass()/self.reactantsmass
            if debug:
                print(str(x.get_molar_mass()) + '/' + str(self.reactantsmass) + '=' + str(x.percent))
                print(x.percent)
    
