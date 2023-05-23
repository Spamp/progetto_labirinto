# -*- coding: utf-8 -*-

from input_file import Input_file

if __name__ == "__main__":
    
    """ 
    Chiede in input il file 
    
    """
    input_file=Input_file()
    filepath = './indata/'+str(input('Inserisci il nome del file da leggere  '))
    leggiFile= input_file.leggi_file_json(filepath)