# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:52:44 2020

@author: Joan
"""

#==========================CARREGO LLIBRERIES==================================
import pyglet
from pyglet.window import key
from pyglet.gl import gl  #funciones OpenGL
import random
import os
import time

os.chdir('D:/Escritorio/phd/codi_experiments/expe_fake_pyglet') #directori on tenim el projecte.Les imatges estaran en subdirectoris.

#==============================================================================
#===================GENERO SEQÜENCIES EXPERIMENTALS============================
#==============================================================================

#==========================SEQ PRESENTACIÓ OLORS===============================

nensayos=6  #40 ensayos x 3 valvulas 120
repes=2
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
#genera serie experimental 
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
    return seq
        
seq_animals = seq_generator(repes)
seq_animals = fix_seq(seq_animals)

#=====================SEQ PRESENTACIÓ IMATGES OBJECTES=========================

seq_obj = seq_generator(repes)
seq_obj = fix_seq(seq_obj)


#========================== Crea Log File =====================================  

sujeto=input("Introduce Id sujeto: ")
fecha=time.strftime("_%d_%m_%y_")
hora=time.strftime("%H_%M") 
fileName = sujeto + fecha+hora 
dataFile = open(fileName+'.csv', 'w')  
dataFile.write('trial,temps,olor,Imatge,Resposta\n')
dataFile.close()


#==============================================================================
#===================GENERO WINDOW I CARREGO IMATGES============================
#==============================================================================
#Parametres per la window
background_color = (.5, .5, .5, 1)
width= 800
height= 800


window = pyglet.window.Window(1920, 1080)

# define color de fondo

gl.glClearColor(*background_color)


dict_imatges ={
    'image_ini' : pyglet.resource.image('imatges_manel_finals/others/img_ini.jpg'), 
    'image_inst': pyglet.resource.image('imatges_manel_finals/others/inst.jpg'),
    'image_fix': pyglet.resource.image('imatges_manel_finals/others/p_fijac.jpg'),
    'image_valora' : pyglet.resource.image('imatges_manel_finals/others/valora_7.jpg'),
    'image_pos' : pyglet.resource.image('imatges_manel_finals/others/positiu.jpg'),
    'image_neut' : pyglet.resource.image('imatges_manel_finals/others/neutre.jpg'),
    'image_neg' : pyglet.resource.image('imatges_manel_finals/others/negatiu.jpg'),
    'image_blink' : pyglet.resource.image('imatges_manel_finals/others/blink.jpg'),
    'image_fin' : pyglet.resource.image('imatges_manel_finals/others/img_fin.jpg')
    }

#=============================== Flags ========================================  

      


inici_exp = -1
contador_seq = 0 
contador_ani = 0 
contador_obj = 0 
accepta_resposta = 0
dt2 = 0



#==============================================================================
#==========================EVENTS PYGLET=======================================  
#==============================================================================

def update(dt):
    global dt2
    dt2=dt2+dt

@window.event
def on_draw():
    window.clear()
    global inici_exp, dt2, accepta_resposta
    
    if inici_exp == -1:
        dict_imatges['image_inst'].blit((window.width/2)-width/2, (window.height/2)-height/2, width
                   =800, height=800)
    elif inici_exp == 0:
        dict_imatges['image_ini'].blit((window.width/2)-width/2, (window.height/2)-height/2, width
                   =800, height=800)
    elif inici_exp == 2:
        dict_imatges['image_fin'].blit((window.width/2)-width/2, (window.height/2)-height/2, width
                   =800, height=800)
    elif inici_exp == 1:
        if dt2 < 4:
            dict_imatges['image_fix'].blit((window.width/2)-width/2, (window.height/2)-height/2, width
                   =800, height=800)       
        elif dt2 > 4 and dt2 < 8:
            if secexr[contador_seq][0] == 'a':
                dict_imatges['image_pos'].blit((window.width/2)-width/2, (window.height/2)-height/2, width
                   =800, height=800)     
            elif secexr[contador_seq][0] == 'b':
                dict_imatges['image_neut'].blit((window.width/2)-width/2, (window.height/2)-height/2, width
                   =800, height=800)   
            elif secexr[contador_seq][0]== 'c':
                dict_imatges['image_neg'].blit((window.width/2)-width/2, (window.height/2)-height/2, width
                   =800, height=800)
                
        elif dt2 > 8 and dt2 < 10:
            if secexr[contador_seq][0] == 'a':
                Nimage= 'imatges_manel_finals/objectes/OB'+str(seq_obj[contador_obj])+'_720.jpg'
                image = pyglet.resource.image(Nimage)
                image.blit((window.width/2)-width/2, (window.height/2)-height/2, width
                   =800, height=800)
                             
            elif secexr[contador_seq][0] == 'b':
                dict_imatges['image_fix'].blit((window.width/2)-width/2, (window.height/2)-height/2, width
                   =800, height=800)
                
            elif secexr[contador_seq][0]== 'c':
                Nimage= 'imatges_manel_finals/animals/AN'+str(seq_obj[contador_ani])+'_720.jpg'
                image = pyglet.resource.image(Nimage)
                image.blit((window.width/2)-width/2, (window.height/2)-height/2, width
                   =800, height=800)

        elif  dt2 > 10:       
            dict_imatges['image_valora'].blit((window.width/2)-width/2, (window.height/2)-height/2, width
                   =800, height=800)
            accepta_resposta = 1
            
def press_button():
    global inici_exp, dt2, contador_seq,contador_obj,contador_ani,accepta_resposta,secexr
    if secexr[contador_seq][0] == 'a':
                 contador_obj +=1
    elif secexr[contador_seq][0] == 'c':
        contador_ani +=1   
    if contador_seq < len(secexr)-1:
        contador_seq +=1
        accepta_resposta = 0
        dt2 = 0  
    else:
       inici_exp = 2
     

@window.event
def on_key_press(symbol, modifiers):
    global inici_exp, dt2, contador_seq,contador_obj,contador_ani,accepta_resposta
    if symbol == key.SPACE and inici_exp == -1:
        inici_exp = 0
    elif symbol == key.SPACE and inici_exp == 0:
        inici_exp = 1
        dt2 = 0
    elif accepta_resposta == 1:
        if symbol == key._1:
            press_button()   
        if symbol == key._2:
            press_button()    
        if symbol == key._3:
            press_button() 
        if symbol == key._4:
            press_button()
        if symbol == key._5:
            press_button()
        if symbol == key._6:
            press_button()
        if symbol == key._7:
            press_button()
            
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
    
