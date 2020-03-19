# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:29:17 2020

@author: Toshiba
"""

import PySimpleGUI as sg
import time

layout=[[sg.Text('                                 ',background_color="white"),sg.Text('TechClub',text_color="#fafafa", background_color='orange', justification='center', size=(15, 1), font=("Permanent Marker", 14))],
        [sg.Text('         Guess the Number!!',text_color="blue",justification='center',font=("Gotham-Black", 25),background_color="white")         ],
        [sg.Text('',text_color="black",justification='center',font=("Gotham-Black", 15),background_color="white")],
        [sg.Text('      ',background_color="white"),sg.Text('Is Your Number :',text_color="black",justification='center',font=("Gotham-Black", 40),background_color="white",size=(15, 1),key='_MSG_')],
        [sg.Text('                                               ',background_color="white"),sg.Text('50',text_color="black",justification='center',font=("Gotham-Black", 65),background_color="white",key='_NUM_')],
        [sg.Text('                                      ',background_color="white")],
        [sg.Text('         ',background_color="white"),sg.ReadButton('>',size=(5,1),font=("Gotham-Black",25)),sg.Text('      ',background_color="white"),sg.ReadButton('<',size=(5,1),font=("Gotham-Black",25)),sg.Text('      ',background_color="white"),sg.ReadButton('=',size=(5,1),font=("Gotham-Black",25))],
        [sg.Text('                                      ',background_color="white")],
        ]

window = sg.Window('Guess the Number game', default_element_size=(40, 2),background_color="white").Layout(layout)
        
Up_Limit =100
Low_Limit=0
Average=0
Step=0
flag="none"

while True:
    button, values = window.Read(timeout=1)
    
    
    if flag=="none":
        Average=int((Up_Limit+Low_Limit)/2)
        
          
        
        window['_NUM_'].update(Average)
        
        if button=="<":
            Up_Limit=Average
            Step=Step+1
        if button==">":
            Low_Limit=Average
            Step=Step+1
            
        if button=="=":
            window['_MSG_'].update("Yeppie!! Guessed it in " +str(Step+1)+" Steps",font=("Gotham-Black",22))
            window['_NUM_'].update(" ",font=("Gotham-Black",10))
            print("Guessed it correctly!!")
            print("Guessed in " + str(Step+1)+" Steps")
            flag="closed"
            
        if button=='Quit' :
            window.close()
            break
    else:
            time.sleep(5)
            window.close()
            break
            
print("Closing")