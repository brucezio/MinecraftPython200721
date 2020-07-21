# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:13:42 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
u=input("請輸入名字:")
while True:
    m=input("輸入訊息:")

    mc.postToChat("["+u+"]"+m)
