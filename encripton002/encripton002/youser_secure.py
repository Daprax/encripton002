
def bee_num(imp):                                       #imp: imput
    if imp.isnumeric() == True:
        return imp
    else:
        while imp.isnumeric() != True:
            print("Pleas give a number!")
            imp = input()
        return imp
