class MENU:

    num = 0

    def menu():
        print("Wich tipes of encryption wud you use?")
        print(" a)  x character svap")
        print(" x)  quit")
        print("")
        print("Tipe the lether of the choused Funkcion!")
        #chous = input()
        if input() == "a":
            print("Wud you code: c); or decode d)?")
            chous = input()
            if chous == "c":
                print("how mani caracter wud you bos the text?")
                # hear shud be macke a funktion     bos = input()
          
                return
            elif chous == "d":  

                return
            else:
                menu()
                return
            return
        elif input == "x":
            return
        else:
            menu()
            return
        print(chous)

menu = MENU
menu.menu()
