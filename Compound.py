debug = False
import re
from Element import Element
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
