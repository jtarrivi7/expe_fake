# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:52:44 2020

@author: Joan
"""

#==========================CARREGO LLIBRERIES==================================
import pyglet
from pyglet.window import key
import random
import os
import time

os.chdir('D:/Escritorio/phd/codi_experiments/expe_fake_pyglet') #directori on tenim el projecte.Les imatges estaran en subdirectoris.

#==============================================================================
#===================GENERO SEQÜENCIES EXPERIMENTALS============================
#==============================================================================

#==========================SEQ PRESENTACIÓ OLORS===============================

nensayos=12  #40 ensayos x 3 valvulas 120
repes=4
valvulas=3
valv_l=['a','b','c']#nombres valvulas


secr=[0 for i in range(nensayos)] #array 1d almacena secuencia random presentacion
secex = [[] * 3 for i in range(nensayos)] #array 2d para almacenar trials
secexr = [[] * 3 for i in range(nensayos)] #array 2d para almacenar serie aleatoria
aux1=[0 for i in range(nensayos)]

## Genera serie aleatoria para presentación
for x in range(nensayos):     
    cont=0
    while (cont < 1 ):
        num1= random.randint(0, nensayos-1);
        if aux1[num1] < 1:
            aux1[num1]=1
            secr[x]=num1
            cont+=1
cont=0
#genera serie experimental ([direc][veloc][durac])*10 repes
for x in range(len(valv_l)):
    for r in range(repes): #repeticiones             
        secex[cont].append(valv_l[x])
        cont+=1
#aleatoriza serie experimental
for x in range(nensayos):
    secexr[x]=secex[secr[x]]   



#=====================SEQ PRESENTACIÓ IMATGES ANIMALS==========================

#funció per generar sequencies experimentals

def seq_generator(nensayos):

    SECEX=[]
    aux1=[]

    for x in range(nensayos):
        SECEX.append(0)
        aux1.append(0)
    
    for x in range(nensayos):
        cont=0
        while (cont < 1 ):
            num1= random.randint(0, nensayos-1);
            if aux1[num1] < 1:
                aux1[num1]=1
                SECEX[x]=num1
                cont=cont+1
    return SECEX

def fix_seq(seq):
    for i in range(len(seq)):
        seq[i] += 1
        
seq_animals = seq_generator(repes)
seq_animals = fix_seq(seq_animals)

#=====================SEQ PRESENTACIÓ IMATGES OBJECTES=========================

seq_obj = seq_generator(repes)
seq_obj = fix_seq(seq_obj)




#==============================================================================
#===================GENERO WINDOW I CARREGO IMATGES============================
#==============================================================================
window = pyglet.window.Window(720, 700)

dict_imatges ={
    'image_ini' : pyglet.resource.image('imatges_manel_finals/others/img_ini.jpg'), 
    'image_inst': pyglet.resource.image('imatges_manel_finals/others/inst.jpg'),
    'image_fix': pyglet.resource.image('imatges_manel_finals/others/p_fijac.jpg'),
    'image_valora' : pyglet.resource.image('imatges_manel_finals/others/valora.jpg'),
    'image_void' : pyglet.resource.image('imatges_manel_finals/others/void.jpg'),
    'image_blink' : pyglet.resource.image('imatges_manel_finals/others/blink.jpg'),
    'image_fin' : pyglet.resource.image('imatges_manel_finals/others/img_fin.jpg')
    }

#=============================== Flags ========================================  

      


inici_exp = -1
final_exp = 0 
contador_seq = 0 
dt2 = 0

#========================== Crea Log File =====================================  

# sujeto=input("Introduce Id sujeto: ")
# fecha=time.strftime("%d_%m_%y_")
# hora=time.strftime("%H%M") 
# fileName = sujeto + fecha+hora 
# dataFile = open(fileName+'.csv', 'w')  
# dataFile.write('trial, est, resp\n')
# dataFile.close()


#==============================================================================
#==========================EVENTS PYGLET=======================================  
#==============================================================================

def update(dt):
    global dt2
    dt2=dt2+dt

@window.event
def on_draw():
    window.clear()
    global inici_exp, dt2
    
    if inici_exp == -1:
        dict_imatges['image_inst'].blit(0, 0)
    elif inici_exp == 0:
        dict_imatges['image_ini'].blit(0, 0)
    elif inici_exp == 1:
        if dt2 < 4:
            dict_imatges['image_fix'].blit(0, 0)         
        elif dt2 >= 4:
            dict_imatges['image_void'].blit(0, 0)      
            
        
    # elif inici_exp == 1 and contador_seq <= nensayos-1:
    #      if dt2 <= 5:   
    #         if secexr[contador_seq][0] == 1:
    #             dict_imatges['estímul1'].blit(0, 0)
    #         elif secexr[contador_seq][0]  == 2:
    #             dict_imatges['estímul2'].blit(0, 0)
    #      else:
    #         contador_seq +=1
    #         dt2 = 0
    # else:
    #     dict_imatges['image_fin'].blit(0, 0)

@window.event
def on_key_press(symbol, modifiers):
    global inici_exp, dt2
    if symbol == key.SPACE and inici_exp == -1:
        inici_exp = 0
    elif symbol == key.SPACE and inici_exp == 0:
        inici_exp = 1
        dt2 = 0


pyglet.clock.schedule_interval(update, 1/60.0)            
pyglet.app.run()



#==============================================================================
#=========================== CODI ANTIC =======================================  
#==============================================================================

# @window.event
# def on_draw():
#     window.clear()
#     global contae
    
#     if imatge_presentada == 0:
#         dict_imatges['image_inst'].blit(0, 0)
#     elif imatge_presentada == 1:
#         dict_imatges['image_ini'].blit(0, 0)
#     elif imatge_presentada == 2:
#        dict_imatges['image_fix'] .blit(0, 0)
        
# #imatge expe
#     elif  imatge_presentada == 3 and contae < nensayos-1:
#         contae += 1
#         if SECEXR[contae][0] == 'a':
#             dict_imatges['valvula1'] .blit(0, 0)
#         elif SECEXR[contae][0]  == 'b':
#              dict_imatges['valvula2'].blit(0, 0)
#         elif SECEXR[contae][0]  == 'c':
#            dict_imatges['valvula3'].blit(0, 0)
#         elif SECEXR[contae][0]  == 'd':
#             dict_imatges['valvula4'].blit(0, 0)
#         elif SECEXR[contae][0]  == 'e':
#             print('CLAC CLAC, el soroll de la valvula està passant')
#     elif imatge_presentada == 3 and contae == nensayos-1:
#         dict_imatges['image_fin'].blit(0, 0)   
        
#     elif  imatge_presentada == 4:
#        dict_imatges['image_valora'].blit(0, 0)
                
# @window.event
# def on_key_press(symbol, modifiers):
#         global imatge_presentada
#         global contador2, tecla
#         if symbol == key.SPACE and imatge_presentada == 0:
#                 imatge_presentada = 1
#         elif symbol == key.SPACE and imatge_presentada == 1:
#             imatge_presentada = 2 
#         elif symbol == key.SPACE and imatge_presentada == 2:
#             imatge_presentada = 3
#         elif symbol == key.SPACE and imatge_presentada == 3:
#             imatge_presentada = 4  
#         elif imatge_presentada == 4:
#             if symbol == key.NUM_1:
#                 #resp_suje[contador2] = 1
#                 tecla = 1
#                 dataFile = open(fileName+'.csv', 'a')  
#                 dataFile.write(str(contae)+', '+str(SECEXR[contae])+', '+str(tecla)+', '+'\n')#guarda datos ensayo
#                 dataFile.close()
#                 imatge_presentada = 2
#             elif symbol == key.NUM_2:
#                  #resp_suje[contador2] = 2
#                  tecla = 2
#                  dataFile = open(fileName+'.csv', 'a')  
#                  dataFile.write(str(contae)+', '+str(SECEXR[contae])+', '+str(tecla)+', '+'\n')#guarda datos ensayo
#                  dataFile.close()
#                  imatge_presentada = 2
#             elif symbol == key.NUM_3:  
#                   #resp_suje[contador2] = 3
#                 tecla = 3
#                 dataFile = open(fileName+'.csv', 'a')  
#                 dataFile.write(str(contae)+', '+str(SECEXR[contae])+', '+str(tecla)+', '+'\n')#guarda datos ensayo
#                 dataFile.close()
#                 imatge_presentada = 2
#             # contador2 +=1
#             # d = [seq_expe, resp_suje]
#             # export_data = zip_longest(*d, fillvalue = '')
#             # with open('resultats.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
#             #     wr = csv.writer(myfile)
#             #     wr.writerow(("seq_expe", "resp_suje"))
#             #     wr.writerows(export_data)
#             #     myfile.close()
            
# pyglet.app.run()   
    
