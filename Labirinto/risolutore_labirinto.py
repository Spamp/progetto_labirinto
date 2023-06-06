# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:47:28 2023

"""
import os
from input_file import Input_file
from labirinto import Labirinto
from output_file import Output_file
import threading
import time


def calcolatore():
    
    """
    Funzione che richiama i metodi implementati per risolvere il labirinto. 
    
    Questa funzione chiede inizialmente in input il file da analizzare, e richiama il metodo leggi_file dalla classe Input_file, per poter
    leggere il file a seconda del formato (.json o .tiff)
    
    Successivamente, dopo aver creato un'istanza della classe labirinto, in seguito alla quale il labirinto viene trasformato in un grafo,
    vengono calcolati i cammini minimi per connettere i nodi di partenza e di destinazione. I cammini minimi sono quelli che minimizzano
    il peso associato al cammino, che viene calcolato come la somma della lunghezza del path trovato e i pesi degli archi incontrati
    lungo il percorso. 
    
    Dopo aver trovato i cammini più brevi, vengono calcolati anche tutti i cammini possibili per connettere i nodi richiesti attraverso il metodo
    "trova_tutti_i_cammini". Essendo un calcolo molto oneroso da svolgere, viene avviato un thread che assegna al metodo di ricerca un tempo massimo
    di esecuzione. In particolare, viene assegnato un tempo massimo di 25 secondi per svolgere l'operazione, in seguito al quale vengono restituiti
    tutti i cammini trovati. 
    Nel caso in cui i 25 secondi stabiliti non fossero sufficienti per calcolare tutti i cammini, e quindi il thread rimanesse attivo più a lungo,
    arriviamo alla conclusione che il metodo ha trovato troppi percorsi da calcolare, che possiamo assumere di numero infinito, motivo per il quale
    il thread si blocca.
    
    In seguito alla conclusione del thread, viene richiamato il metodo "get_attributo", che ci restituisce tutti i cammini trovati con il loro peso
    associato. Questo metodo è necessario per poter accedere alle due variabili, essendo degli attributi della classe Labirinto. 
    
    Infine, viene creata un'istanza della classe di output, in seguito alla quale viene richiamato il metodo per restituire l'immagine di output
    dei percorsi trovati nel labirinto, e quello per creare un file json che specifica le caratteristiche dei percorsi trovati (nodo di partenza, 
    nodo di destinazione, costo totale del percorso, path del percorso). 


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
    
    # Calcolo tutti i cammini possibili fra partenza e destinazione: 
        
    #Richiamo un metodo che crea un thread che scorre la funzione trova_tutti_i_cammini   
    thread = threading.Thread(target=maze.trova_tutti_i_cammini)
    
    #avvio il thread appena creato
    thread.start()
    
    #blocco il codice principale per 5 secondi per dare il tempo al thread di calcolare tutti i cammini
    time.sleep(5)
    
    # quando termina il blocco, controllo se il thread per cercare tutti i cammini è attivo (non è ancora termato)
    if thread.is_alive():
        
        #se è ancora attivo, gli lascio altri 20 secondi per trovare tutti i cammini
        thread.join(timeout=20)
        
        # se dopo 20 secondi (25 totali) non si è ancora concluso, potrei avere cammini infiniti, quindi blocco il thread
        print("il thread ha trovato solo i cammini minimi, ma non altre soluzioni")
    else:
        #se il thread non è più attivo, quindi si è concluso prima dei 25 secondi autonomamnete, vuol dire che ha trovato tutti 
        #i cammini e si chiude restituendo un messaggio
        thread.join()
        print('il thread si è concluso con successo: ha trovato tutti i cammini possibili')
        
    # richiamo il metodo che mi restituisce gli attributi della classe labirinto "cammini_semplici" e # "pesi_cammini_semplici". 
    cammini_semplici=maze.cammini_semplici
    pesi_cammini_semplici=maze.pesi_cammini_semplici

    
    #creo un'istanza della classe Output_file
    outfile= Output_file(nome_labirinto)
    
    # restituisco i percorsi trovati
    outfile.crea_immagini_output(labirinto, partenze, destinazioni, shortest_path)
    # creo un file json con le caratteristiche dei cammini minimi trovati
    outfile.crea_file_json(shortest_path,weight,'tutti i cammini minimi')
    # creo un file json con le caratteristiche di tutti i cammini possibili trovati
    outfile.crea_file_json(cammini_semplici,pesi_cammini_semplici,'tutti i cammini semplici')
    
    
