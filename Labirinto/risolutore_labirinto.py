# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:47:28 2023

"""
import os
from input_file import Input_file
from labirinto import Labirinto
from output_file import Output_file


def calcolatore():
    
    """
    Metodo che richiama i metodi implementati per risolvere il labirinto

    Returns
    -------
    labirinto: array 
    partenze: list
    destinazioni: list
    grafo: graph
    shortest_path: list of tuple
    weight: list

    """
    # ottieni i nomi dei file e delle cartelle nella directory
    lista_file = os.listdir('./indata/')
    print(lista_file)
    nomefile=str(input('Inserisci il nome del file da leggere con formato tiff o json tra uno di quelli elencati:  '))
    nomelist=nomefile.split('.')
    nome_labirinto=nomelist[0]
    #Chiedo il file di input e richiamo la funzione di lettura
    filepath = './indata/'+nomefile
    input_file=Input_file(filepath)
    (labirinto, partenze, destinazioni)=input_file.leggi_file()
    # creo un'istanza della classe Labirinto
    maze = Labirinto(labirinto, partenze, destinazioni)
    # calcolo il cammino minimo e il peso ad esso associato
    shortest_path, weight= maze.cammino_minimo()
    outfile= Output_file(nome_labirinto)
    outfile.crea_immagini_output(labirinto, partenze, destinazioni, shortest_path)
    dataframe, peso_archi =maze.trova_tutti_i_cammini()
    
    return (labirinto, partenze, destinazioni, shortest_path, weight, dataframe, peso_archi)
