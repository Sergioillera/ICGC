# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:53:24 2017

@author: Usuario
"""
import os 

params=[]#{} conexion a la bd

currentpath=os.path.dirname(__file__)
currentpath=currentpath+'\\'
archivo=open(currentpath+'config.txt','r')
for row in archivo:
    params.append( row.replace('\n','').split('=')[1])
archivo.close()
params[3]=int(params[3])

filezone=[]# lista de archivos posibles para cargar

archivo=open(currentpath+'spi_zone.txt','r')
for row in archivo:
    filezone.append( row.replace('\n',''))
archivo.close()

'''
params[0]="QPSQL"
params[1]='localhost' #host postgre
params[2]='gis_psi' #bd name
params[3]=5432 #port
params[4]='postgres' #user name
params[5]='1941987' #password
'''
