# -*- coding: utf-8 -*-

import os
from input_file import Input_file

if __name__ == "__main__":
    
    """ 
    Chiede in input il file 
    
    """
    # ottieni i nomi dei file e delle cartelle nella directory
    lista_file = os.listdir('./indata/')
    print(lista_file)
    input_file=Input_file()
    filepath = './indata/'+str(input('Inserisci il nome del file da leggere con formato tiff o json tra uno di quelli elencati:  '))
    leggiFile= input_file.leggi_file(filepath)