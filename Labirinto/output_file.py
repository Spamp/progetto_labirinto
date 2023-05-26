# -*- coding: utf-8 -*-
"""
Created on Fri May 26 18:04:49 2023

"""

class Output_file:
    """
    classe che implementa metodi di per la creazione dei file di output
    """
    def __init__(self, nomefile):
        """
        Costruttore della classe Output_file
        
        parameters
        ----------
        nomefile= string
        
        Returns
        -------
        None.
        
        """
        self.percorso_cartella='./output'
        self.nomefile=nomefile
        self.percorso_file=self.percorso_cartella+'/'+self.nomefile
        
