from encripts import *
from youser_secure import *

class MENU:

    num = 0

    def m_menu():
        print("Wich tipes of encryption wud you use?")
        print(" a)  x character bos")
        print(" x)  quit")
        print("")
        print("Tipe the lether of the choused Funkcion!")
        chous = input()
        if chous == "a":
            return "bos"
        elif chous == "x":
            return 0                                                        #onli the '0' break the main while
        else:
            #MENU.m_menu()
            return 1
    def bos_menu():
        print("Would you code: c); or decode d)?")                            #Option fo change the direction of lether bossing.
        chous = input()                                                     #C) mean the right (as the ABC run); D) mean the oposit direction.
        print("How much will you bos the characters?")
        n_bos = int(bee_num(input()))                                       #The mesure of the bosing.
        print("What text will you encripting?")                              
        text = input()                                                      #It si the text wat wee nead encripting. 
        if chous == "c":
            BOS.code(n_bos, text)
            return
        elif chous == "d":  
            BOS.d_code(n_bos, text)
            return
        else:
            MENU.m_menu()
            return
        


