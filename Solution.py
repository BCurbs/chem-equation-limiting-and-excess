# Ben Curby and Brandon Roller, April 21 2021

# File containing resource classes
# A solution is made up of Compounds which is made up of Elements
# File includes a custom exception used for flagging errors with the inputted equation
# Periodic table of molar masses
import re
from Compound import Compound


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
                self.smallest = sidemass
                smallestcompound = compound.formula
        self.limitingReactant=smallestcompound
        
    def get_proportion(self):
        self.reactantsmass = 0
        self.productsmass = 0
        for x in self.products:
            self.productsmass += x.get_molar_mass()
        for x in self.reactants:
            self.reactantsmass += x.get_molar_mass()
        for x in self.products:
            x.percent = x.get_molar_mass()/self.productsmass
        for x in self.reactants:
            x.percent = x.get_molar_mass()/self.reactantsmass
            
    
