# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:47:28 2023

"""
import os
from input_file import Input_file
from Labirinto import Labirinto

class Risolutore_labirinto:
    """
    Classe che risolve il labirinto
    
    """
    def calcolatore():
        """
        Metodo che richiama i metodi implementati per risolvere il labirinto

        Returns
        -------
        None.

        """
        # ottieni i nomi dei file e delle cartelle nella directory
        lista_file = os.listdir('./indata/')
        print(lista_file)
        
        #Chiedo il file di input e richiamo la funzione di lettura
        input_file=Input_file()
        filepath = './indata/'+str(input('Inserisci il nome del file da leggere con formato tiff o json tra uno di quelli elencati:  '))
        array=input_file.leggi_file_json(filepath)
        
        #maze=Labirinto()
        #labirinto, partenze, destinazioni = maze.crea_labirinto_json(array)
        return filepath, array