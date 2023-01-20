from encripts import *

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
            return
        else:
            MENU.m_menu()
            return
    def bos_menu():
        print("Wud you code: c); or decode d)?")                            #Option fo change the direction of lether bossing.
        chous = input()                                                     #C) mean the right (as the ABC run); D) mean the oposit direction.
        print("How much will you bos the characters?")
        n_bos = int(input())                                                     #The mesure of the bosing.
        print("Wat text will you encripting?")                              
        text = input()                                                      #It si the text wat wee nead encripting. 
        if chous == "c":
            BOS.code(n_bos, text)
        
            return
        elif chous == "d":  

            return
        else:
            menu()
            return
        


