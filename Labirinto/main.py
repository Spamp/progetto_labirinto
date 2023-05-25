# -*- coding: utf-8 -*-


from Risolutore_labirinto import Risolutore_labirinto


if __name__ == "__main__":
    
    """ 
    Richiama la classe Risolutore_labirinto per risolvere il percorso
    
    """
    risolutore=Risolutore_labirinto
    (labirinto, partenze, destinazioni, grafo, cammini_minimi, weight) = risolutore.calcolatore()