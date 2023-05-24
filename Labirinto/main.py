# -*- coding: utf-8 -*-


from Risolutore_labirinto import Risolutore_labirinto


if __name__ == "__main__":
    
    """ 
    Chiede in input il file 
    
    """
    risolutore=Risolutore_labirinto
    filepath, img_array, labirinto, partenze, destinazioni = risolutore.calcolatore()