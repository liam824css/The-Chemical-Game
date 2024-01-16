#-*- coding: utf-8 -*-
#######################################################################
#                                                                     #
#                                                                     #
# Developer : Liam824css License : Mozilla Public License Version 2.0 #
#                                                                     #
# This will be a open-source project later. ( Wait! )                 #
#                                                                     #
# File : main.py                                                      #
#                                                                     #
# Github : https://github.com/Liam824css/The-Chemical-Game            #
#                                                                     #
# Date : 2024 January 17th                                            #
#                                                                     #
# Version : 1.0.0                                                     #
#                                                                     #
# Description : The game of chemistry. Our team simulated some chemic #
# al mixtures and chemical reaction. Also it has Chemicals Market.    #
# You can transact mixtures, materials and Laboratory Equipment.      #
#                                                                     #
#######################################################################

import socket
import requests
import pyxel

screen_width = 960 # 1920/2
screen_height = 540 # 1080/2

class Main:
    def __init__(self):
        pyxel.init(screen_width,screen_height)
        self.x = 0
        pyxel.run(self.update, self.draw)
    
    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)

if __name__ == "__main__":
    Main()