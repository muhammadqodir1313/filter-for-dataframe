# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A4HYTCXk_ClEknJViqcG-skwmFFSu4Sb
"""

import pandas as pd
baza={
    "FI":[ "Abdullajonov Muhammadqodir", "Inomov Abdulhamid","Aliyeva Ra'no","ISMOILOV SULTONBEK", "ABDURASULOVA MAVLUDAXON","MUSAYEVA NAVRO‘ZAXON ","QOSIMOVA MUXTASARXON","MAHSUDJONOVA MAVLUDAXON", "XAZRATKULOV SANJAR ","JO‘RAYEV SHAXZODBEK " ],
    "Yoshi":["9", "13","11","12","10","14", "8","16","15","11" ],
    "Jinsi":["o'g'il bola", "o'gil bola", "qiz bola","o'gil bola","qiz bola","qiz bola","qiz bola","qiz bola","o'gil bola","o'gil bola"],
    "Ta'lim maskani":["66-maktab", "63-maktab", "59-maktab","21-maktab","2-maktab","1-maktab","11-maktab","71-maktab","73-maktab","26-maktab"],
    "Manzili":["O'zbekiston tumani", "Quva tumani", "Marg'ilon shahar","O'zbekiston tumani", "Quva tumani", "Marg'ilon shahar","O'zbekiston tumani", "Quva tumani", "Marg'ilon shahar","Furqat tumani"]
}
mb=pd.DataFrame(baza)
print(mb)

filtr=mb[(mb['Manzili']=='Quva tumani') & (mb["Jinsi"]=="o'gil bola")]
print(filtr)