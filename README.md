# chem-equation-limiting-and-excess

## Please do not assume this code is working

This should be able to get the limiting and excess reactants from a properly formated chemical equation. 

If anyone finds this and uses it let me know. If you find issues please report them. If you want to fix them yourself make a pull request and I will take a look. 
## Coming soon: Solution.py and molarity/solution reactions

### How it works:

It basically takes a formula, splits it up at the --> and + signs, and then creates instances of the compound object with each part. That object parses it into a list of elements. 

### Known limitations:

It can't handle a coeficient of more than 2 digits. Used to be 1 but I fixed added another. 

This code is hacked together and shouldn't be trusted. 

I belive it can only handle a multiplier of 1 digit on parentheses. 
