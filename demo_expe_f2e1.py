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

nensayos=120  #40 ensayos x 3 valvulas 120
repes=40
valvulas=3
valv_l=['a','b','c']#nombres valvulas


def block_randomizer( inici, final):
    
    secr=[0 for i in range(nensayos//4)] #array 1d almacena secuencia random presentacion
    secex = [] #array 2d para almacenar trials
    aux=[0 for i in range(nensayos//4)]
    secexr = [0 for i in range(nensayos//4)]

    ## Genera serie aleatoria para presentación
    for x in range(nensayos//4):     
        cont=0
        while (cont < 1 ):
            num1= random.randint(inici, final); # 0 , nensayos//4 -1
            if aux[num1] < 1:
                aux[num1]=1
                secr[x]=num1
                cont+=1
    
    #genera serie experimental 
    for x in range(len(valv_l)):
        for r in range(repes//4): #repeticiones             
            secex.append(valv_l[x])
            
    #aleatoriza serie experimental
    for x in range(nensayos//4):
        secexr[x]=secex[secr[x]]
        
    return secexr

secexr1 = block_randomizer(0, nensayos//4 -1)
secexr2 = block_randomizer(0, nensayos//4 -1)
secexr3 = block_randomizer(0, nensayos//4 -1)
secexr4 = block_randomizer(0, nensayos//4 -1)

secexr = secexr1 +secexr2 + secexr3 + secexr4   



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
        
seq_animals = seq_generator(repes + repes //2)
seq_animals = fix_seq(seq_animals)

#=====================SEQ PRESENTACIÓ IMATGES OBJECTES=========================

seq_obj = seq_generator(repes + repes //2)
seq_obj = fix_seq(seq_obj)


#========================== Crea Log File =====================================  

sujeto=input("Introduce Id sujeto: ")
fecha=time.strftime("_%d_%m_%y_")
hora=time.strftime("%H_%M") 
fileName = sujeto + fecha+hora 
dataFile = open(fileName+'.csv', 'w')  
dataFile.write('triger_type,time,trial,olor,Imatge,Resposta\n') #Quan faci servir el pupil labs faré servir t-pupil en comtpes del modul time
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
    'image_fin' : pyglet.resource.image('imatges_manel_finals/others/img_fin.jpg'),
    'image_pausa' : pyglet.resource.image('imatges_manel_finals/others/pausa.jpg')
    }

#============================= INTERRUPTORS ===================================  

      


inici_exp = -1
contador_seq = 0 
contador_ani = 0 
contador_obj = 0 
contador_neutre = 0 
contador_pausa = 0
accepta_resposta = 0
dt2 = 0
int_olor_log = False #interruptor per enviar dades al logfile
int_img_log = False #interruptor per enviar dades al logfile

#==============================================================================
#==========================EVENTS PYGLET=======================================  
#==============================================================================

def update(dt):
    global dt2
    dt2=dt2+dt

@window.event
def on_draw():
    window.clear()
    global inici_exp, dt2, accepta_resposta, Nimage, int_olor_log, int_img_log
    
    if inici_exp == -1:
        dict_imatges['image_inst'].blit((window.width/2)-width/2, (window.height/2)-height/2, width
                   =800, height=800)
    elif inici_exp == 0:
        dict_imatges['image_ini'].blit((window.width/2)-width/2, (window.height/2)-height/2, width
                   =800, height=800)
    elif inici_exp == 2:
        dict_imatges['image_fin'].blit((window.width/2)-width/2, (window.height/2)-height/2, width
                   =800, height=800)
    elif contador_pausa == 10:
        dict_imatges['image_pausa'].blit((window.width/2)-width/2, (window.height/2)-height/2, width
                   =800, height=800)
    elif inici_exp == 1:
        if dt2 < 4:
            dict_imatges['image_fix'].blit((window.width/2)-width/2, (window.height/2)-height/2, width
                   =800, height=800)    
        if dt2 > 4 and dt2 < 8 and int_olor_log == False:
            dataFile = open(fileName+'.csv', 'a')  
            dataFile.write('Triger_Olor,'+str(time.time())+', '+str(contador_seq)+', '+str(secexr[contador_seq])+'\n')#guarda datos ensayo
            dataFile.close()
            int_olor_log = True
        if dt2 > 4 and dt2 < 8 and int_olor_log == True:
            if secexr[contador_seq] == 'a':
                dict_imatges['image_pos'].blit((window.width/2)-width/2, (window.height/2)-height/2, width
                   =800, height=800)     
            elif secexr[contador_seq] == 'b':
                dict_imatges['image_neut'].blit((window.width/2)-width/2, (window.height/2)-height/2, width
                   =800, height=800)   
            elif secexr[contador_seq]== 'c':
                dict_imatges['image_neg'].blit((window.width/2)-width/2, (window.height/2)-height/2, width
                   =800, height=800)
                
        elif dt2 > 8 and dt2 < 10:
            if secexr[contador_seq] == 'a':
                if int_img_log == False:
                    Nimage= 'imatges_manel_finals/objectes/OB'+str(seq_obj[contador_obj])+'_720.jpg'
                    dataFile = open(fileName+'.csv', 'a')  
                    dataFile.write('Triger_Img,'+str(time.time())+', '+str(contador_seq)+', '+str(secexr[contador_seq])+', '+Nimage+'\n')#guarda datos ensayo
                    dataFile.close()
                    int_img_log = True
                if int_img_log == True:
                    image = pyglet.resource.image(Nimage)
                    image.blit((window.width/2)-width/2, (window.height/2)-height/2, width
                               =800, height=800)
                             
            elif secexr[contador_seq] == 'b':
                if contador_neutre % 2 == 0:
                    if int_img_log == False:
                        Nimage= 'imatges_manel_finals/objectes/OB'+str(seq_obj[contador_obj])+'_720.jpg'
                        dataFile = open(fileName+'.csv', 'a')  
                        dataFile.write('Triger_Img,'+str(time.time())+', '+str(contador_seq)+', '+str(secexr[contador_seq])+', '+Nimage+'\n')#guarda datos ensayo
                        dataFile.close()
                        int_img_log = True
                    if int_img_log == True:
                        image = pyglet.resource.image(Nimage)
                        image.blit((window.width/2)-width/2, (window.height/2)-height/2, width
                                   =800, height=800)
                             
                else:
                    if int_img_log == False:
                        Nimage= 'imatges_manel_finals/animals/AN'+str(seq_obj[contador_ani])+'_720.jpg'
                        dataFile = open(fileName+'.csv', 'a')  
                        dataFile.write('Triger_Img,'+str(time.time())+', '+str(contador_seq)+', '+str(secexr[contador_seq])+', '+Nimage+'\n')#guarda datos ensayo
                        dataFile.close()
                        int_img_log = True
                    if int_img_log == True:
                        image = pyglet.resource.image(Nimage)
                        image.blit((window.width/2)-width/2, (window.height/2)-height/2, width
                           =800, height=800)
                
            elif secexr[contador_seq]== 'c':
                if int_img_log == False:
                    Nimage= 'imatges_manel_finals/animals/AN'+str(seq_obj[contador_ani])+'_720.jpg'
                    dataFile = open(fileName+'.csv', 'a')  
                    dataFile.write('Triger_Img,'+str(time.time())+', '+str(contador_seq)+', '+str(secexr[contador_seq])+', '+Nimage+'\n')#guarda datos ensayo
                    dataFile.close()
                    int_img_log = True
                if int_img_log == True:
                    image = pyglet.resource.image(Nimage)
                    image.blit((window.width/2)-width/2, (window.height/2)-height/2, width
                       =800, height=800)

        elif  dt2 > 10:       
            dict_imatges['image_valora'].blit((window.width/2)-width/2, (window.height/2)-height/2, width
                   =800, height=800)
            accepta_resposta = 1
            

     
def press_button(resp):
    global inici_exp, dt2, contador_seq,contador_obj,contador_ani,accepta_resposta,secexr,Nimage,int_olor_log,int_img_log,contador_neutre,contador_pausa 
    
    dataFile = open(fileName+'.csv', 'a')  
    dataFile.write('resposta,'+str(time.time())+', '+str(contador_seq)+', '+str(secexr[contador_seq]) +', '+Nimage+', '+str(resp)+'\n')#guarda datos ensayo
    dataFile.close()
    
    if secexr[contador_seq] == 'a':
                 contador_obj +=1
    elif secexr[contador_seq] == 'b':
        if contador_neutre % 2 == 0:
            contador_obj +=1
        else:
            contador_ani +=1 
        contador_neutre +=1
    elif secexr[contador_seq] == 'c':
        contador_ani +=1   
    if contador_seq < len(secexr)-1:
        contador_seq +=1
        accepta_resposta = 0
        int_olor_log = False
        int_img_log = False
        contador_pausa +=1
        dt2 = 0  
    else:
       inici_exp = 2



@window.event
def on_key_press(symbol, modifiers):
    global inici_exp, dt2, contador_seq,contador_obj,contador_ani,accepta_resposta,contador_pausa
    if symbol == key.SPACE and inici_exp == -1:
        inici_exp = 0
    elif symbol == key.SPACE and inici_exp == 0:
        inici_exp = 1
        dt2 = 0
    elif accepta_resposta == 1:
        if symbol == key._1:
            press_button(1)   
        if symbol == key._2:
            press_button(2)    
        if symbol == key._3:
            press_button(3) 
        if symbol == key._4:
            press_button(4)
        if symbol == key._5:
            press_button(5)
        if symbol == key._6:
            press_button(6)
        if symbol == key._7:
            press_button(7)
    elif symbol == key.C and contador_pausa == 10:
        contador_pausa = 0
        dt2 = 0
            
pyglet.clock.schedule_interval(update, 1/60.0)            
pyglet.app.run()



