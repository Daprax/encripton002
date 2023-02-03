import numpy
import sys
from menus import *
from encripts import *


menu = MENU
m_m_v = 1
while m_m_v != 0:
    m_m_v = menu.m_menu()                               #main_menu_value
    if  m_m_v == "bos":
        menu.bos_menu()
    elif m_m_v == "scytale":
        menu.scytale_menu()
print("Thank you for ur using!")
