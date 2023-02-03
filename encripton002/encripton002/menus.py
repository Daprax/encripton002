from encripts import *
from youser_secure import *

class MENU:

    num = 0

    def m_menu():
        print("Wich tipes of encryption wud you use?")
        print(" a)  x character bos")
        print(" b)  Scytale")
        print(" x)  quit")
        print("")
        print("Tipe the lether of the choused Funkcion!")
        chous = input()
        if chous == "a":
            return "bos"
        elif chous == "b":
            return "scytale"
        elif chous == "x":
            return 0                                                        #onli the '0' break the main while
        else:
            return 1

    def bos_menu():
        print("Would you code: c); or decode d)?")                            #Option fo change the direction of lether bossing.
        chous = input()                                                     #C) mean the right (as the ABC run); D) mean the oposit direction.
        if chous != "c" and chous != "d":
            if chous == "x":
                return 1
            else:
                return MENU.bos_menu()
        else:
            print("How much will you bos the characters?")
            n_bos = int(bee_num(input()))                                       #The mesure of the bosing.
            print("What text will you encripting?")
            if MENU.num == 0:
                print("The program encrypt onli the lether of the Englis abc!")
                ++MENU.num
            text = input()                                                      #It si the text wat wee nead encripting. 
            if chous == "c":
                BOS.code(n_bos, text)
                return
            elif chous == "d":  
                BOS.d_code(n_bos, text)
                return

    def scytale_menu():
        print("Would you code: c); or decode d)?")                          #Option fo change the direction of lether bossing.
        chous = input()                                                     #C) mean encripting; D) mean the oposit direction.
        if chous != "c" and chous != "d":
            if chous == "x":
                return 1
            else:
                return MENU.bos_menu()
        print("what size cilinfer would you youse?\nGive a number!")
        size = int(bee_num(input()))                                       #The mesure of the bosing.
        print("What text will you encripting?")                              
        text = input()                                                      #It si the text wat wee nead encripting. 
        if chous == "c":
            SCYTALE.code(size, text)
            return
        elif chous == "d":  
            SCYTALE.d_code(size, text)
            return
        elif chous == "x":
            return 1
        else:
            return MENU.bos_menu()

        


