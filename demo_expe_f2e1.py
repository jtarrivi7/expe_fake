# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:52:44 2020

@author: Joan
"""

#==========================CARREGO LLIBRERIES==================================
import pyglet
from pyglet.window import key
import random
import csv
from itertools import zip_longest

import os
import time

os.chdir('D:/Escritorio/phd/experiments/codi_expe')
#==============================================================================
#===================GENERO SEQÜENCIA EXPERIMENTAL==============================
#==============================================================================


#=================CODI JOAN==============================
# num_trials = 10
# chunk = num_trials//5 #per a que el codi funcioni el num d'expes ha de ser multiple de 5
# seq_expe = []
# resp_suje = []

# for x in range(num_trials):
#     seq_expe.append(0)
#     resp_suje.append(0)
# for i in range(num_trials):
#     if i < chunk:
#         seq_expe[i]= 1 
#     elif i < chunk *2:
#         seq_expe[i]= 2
#     elif i < chunk *3:
#         seq_expe[i]= 3
#     elif i < chunk *4:
#         seq_expe[i]= 4
#     elif i < chunk *5:
#         seq_expe[i]= 5

# random.shuffle(seq_expe)  


#=================CODI MANEL==============================
nensayos=10  #40 ensayos x 3 valvulas 120
repes=2
valvulas=5
valv_l=['a','b','c','d','e'] #nombres valvulas


SECR=[0 for i in range(nensayos)] #array 1d almacena secuencia random presentacion
SECEX = [[] * 3 for i in range(nensayos)] #array 2d para almacenar trials
SECEXR = [[] * 3 for i in range(nensayos)] #array 2d para almacenar serie aleatoria
aux1=[0 for i in range(nensayos)]

## Genera serie aleatoria para presentación
for x in range(nensayos):     
    cont=0
    while (cont < 1 ):
        num1= random.randint(0, nensayos-1);
        if aux1[num1] < 1:
            aux1[num1]=1
            SECR[x]=num1
            cont+=1
cont=0
#genera serie experimental ([direc][veloc][durac])*10 repes
for x in range(len(valv_l)):
    for r in range(repes): #repeticiones             
        SECEX[cont].append(valv_l[x])
        cont+=1
#aleatoriza serie experimental
for x in range(nensayos):
    SECEXR[x]=SECEX[SECR[x]]   

contae=-1
#===================GENERO WINDOW I CARREGO IMATGES============================
window = pyglet.window.Window(720, 700)

dict_imatges ={
    'image_inst': pyglet.resource.image('inst.jpg'),
    'image_ini' : pyglet.resource.image('img_ini.jpg'),
    'image_fin' : pyglet.resource.image('img_fin.jpg'),
    'image_void' : pyglet.resource.image('void.jpg'),
    'image_valora' : pyglet.resource.image('valora.jpg'),
    'valvula1' : pyglet.resource.image('sakuragi.jpg'),
    'valvula2' : pyglet.resource.image('greatshark.png'),
    'valvula3' : pyglet.resource.image('olfactometre.jpg'),
    'valvula4' : pyglet.resource.image('image4.png') 
    }

   
#==========================EVENTS PYGLET=======================================        
imatge_presentada = 0
contador = 0
contador2 = 0
sujeto=input("Introduce Id sujeto: ")
fecha=time.strftime("%d_%m_%y_")
hora=time.strftime("%H%M") 
fileName = sujeto + fecha+hora 
dataFile = open(fileName+'.csv', 'w')  
dataFile.write('trial, est, resp\n')
dataFile.close()
@window.event
def on_draw():
    window.clear()
    global contae
    if imatge_presentada == 0:
        dict_imatges['image_inst'].blit(0, 0)
   
    elif imatge_presentada == 1:
        dict_imatges['image_ini'].blit(0, 0)
    elif imatge_presentada == 2:
       dict_imatges['image_void'] .blit(0, 0)
        
#imatge expe
    elif  imatge_presentada == 3 and contae < nensayos-1:
        contae += 1
        if SECEXR[contae][0] == 'a':
            dict_imatges['valvula1'] .blit(0, 0)
        elif SECEXR[contae][0]  == 'b':
             dict_imatges['valvula2'].blit(0, 0)
        elif SECEXR[contae][0]  == 'c':
           dict_imatges['valvula3'].blit(0, 0)
        elif SECEXR[contae][0]  == 'd':
            dict_imatges['valvula4'].blit(0, 0)
        elif SECEXR[contae][0]  == 'e':
            print('CLAC CLAC, el soroll de la valvula està passant')
    elif imatge_presentada == 3 and contae == nensayos-1:
        dict_imatges['image_fin'].blit(0, 0)   
        
    elif  imatge_presentada == 4:
       dict_imatges['image_valora'].blit(0, 0)
                
@window.event
def on_key_press(symbol, modifiers):
        global imatge_presentada
        global contador2, tecla
        if symbol == key.SPACE and imatge_presentada == 0:
                imatge_presentada = 1
        elif symbol == key.SPACE and imatge_presentada == 1:
            imatge_presentada = 2 
        elif symbol == key.SPACE and imatge_presentada == 2:
            imatge_presentada = 3
        elif symbol == key.SPACE and imatge_presentada == 3:
            imatge_presentada = 4  
        elif imatge_presentada == 4:
            if symbol == key.NUM_1:
                #resp_suje[contador2] = 1
                tecla = 1
                dataFile = open(fileName+'.csv', 'a')  
                dataFile.write(str(contae)+', '+str(SECEXR[contae])+', '+str(tecla)+', '+'\n')#guarda datos ensayo
                dataFile.close()
                imatge_presentada = 2
            elif symbol == key.NUM_2:
                 #resp_suje[contador2] = 2
                 tecla = 2
                 dataFile = open(fileName+'.csv', 'a')  
                 dataFile.write(str(contae)+', '+str(SECEXR[contae])+', '+str(tecla)+', '+'\n')#guarda datos ensayo
                 dataFile.close()
                 imatge_presentada = 2
            elif symbol == key.NUM_3:  
                  #resp_suje[contador2] = 3
                tecla = 3
                dataFile = open(fileName+'.csv', 'a')  
                dataFile.write(str(contae)+', '+str(SECEXR[contae])+', '+str(tecla)+', '+'\n')#guarda datos ensayo
                dataFile.close()
                imatge_presentada = 2
            # contador2 +=1
            # d = [seq_expe, resp_suje]
            # export_data = zip_longest(*d, fillvalue = '')
            # with open('resultats.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
            #     wr = csv.writer(myfile)
            #     wr.writerow(("seq_expe", "resp_suje"))
            #     wr.writerows(export_data)
            #     myfile.close()
            
pyglet.app.run()





    
    
