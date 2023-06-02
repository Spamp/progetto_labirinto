# PROGETTO_LABIRINTO

Il programma implementato riceve in ingresso un file contenente le caratteristiche del labirinto, una lista di partenze e una lista di destinazioni, e fornisce in output il path del percorso di costo minimo fra i punti specificati, insieme al costo totale associato al percorso.

## Descrizione dell'input

Il programma riceve in ingresso dei file che contengono le caratteristiche del labirinto da analizzare. 
Il file può essere fornito nei seguenti formati: .json, .tiff, .png, .jpg. 

Il file in formato .json è un dizionario con le seguenti chiavi:

- "larghezza": un numero che indica il numero di posizioni lungo la dimensione orizzontale;
- "altezza": un numero che indica il numero di posizioni lungo la dimensione verticale;
- "pareti": una lista di segmenti, ogni segmento costituito da un dizionario con chiavi:
- "orientamento": "H" per orizzontale, "V" per verticale;
- "posizione": un coppia di indici che indicano una posizione "iniziale" (per convenzione il segmento si estende in orizzontale da  sinistra verso destra e in verticale dall'alto verso il basso);
- "lunghezza": un numero che indica il numero di posizioni occupate dal segmento;
- "iniziali": una lista di coppie di indici che indicano ciascuno una posizione di partenza;
- "finale": una coppia di indici che indica la posizione di arrivo;
- "costi": una lista di posizioni con costo, che sono triple costituite da una coppia di indici che indicano una posizione e un valore intero da 1 a 15 che indica il costo.

Il file fornito come immagine è un file in formato .tiff, .jpg, .png che corrisponde a una matrice rettangolare un cui i pixel neri corrispondono a posizioni occupate da pareti che non possono essere attraversate, e tutti gli altri pixel corrispondono a posizioni che possono essere attraversate per raggiungere il punto di arrivo.

I pixel bianchi sono posizioni che non assegnano punti, i pixel grigi indicano caselle che assegnano costi, i pixel verdi indicano le posizioni di partenza, il pixel rosso indica la posizione di arrivo.

I livelli di grigio possibili sono:

- 16 che assegna un costo pari a 1
- 32 che assegna un costo pari a 2
- 48 che assegna un costo pari a 3
- 64 che assegna un costo pari a 4
- 80 che assegna un costo pari a 5
- 96 che assegna un costo pari a 6
- 112 che assegna un costo pari a 7
- 128 che assegna un costo pari a 8
- 144 che assegna un costo pari a 9
- 160 che assegna un costo pari a 10
- 176 che assegna un costo pari a 11
- 192 che assegna un costo pari a 12
- 208 che assegna un costo pari a 13
- 124 che assegna un costo pari a 14
- 240 che assegna un costo pari a 15

### Esempio di input

Una volta avviato il codice, il file di input può essere fornito come segue:

![image](https://github.com/Spamp/progetto_labirinto/assets/118067217/32349e8b-3d91-40df-9bf1-6926602547a9)


## Elaborazione

Il programma acquisisce il layout di un labirinto costituito da una matrice di posizioni, una o più posizioni di partenza e una posizione di arrivo. Il labirinto viene trasformato in una matrice le cui celle contengono i costi riportati nel file, oppure valori NaN quando si ha una parete. 
La matrice viene allora convertita in un grafo indiretto pesato, che viene esplorato a partire dai nodi di partenza specificati.

## Output

Il programma risolve il labirinto, calcolando per ogni punto di partenza il percorso minimo che permette di raggiungere il punto di arrivo con il minor costo possibile. Il costo viene calcolato come la somma dei pesi degli archi incontrati e la lunghezza del cammino stesso. Se non esiste alcun percorso possibile, il programma restituisce un cammino vuoto. 
Inoltre, il programma calcola tutti i cammini possibili fra i punti di partenza e arrivo specificati, con i rispettivi costi associati.

Il risultato del labirinto per la ricerca dei cammini minimi viene fornito con un'immagine che restituisce un percorso colorato fra partenza e destinazione, e con un file json che riporta le caratteristiche del percorso trovato. 

### Esempio di output:

Eseguendo il programma per il file di input "30-20_marked.json" si ottengono i risultati seguenti:

- 30-20_marked_0.jpg: 

![image](https://github.com/Spamp/progetto_labirinto/assets/118067217/768e37a4-edcd-42e8-b6b9-aea4d98b571d)

Il file .json associato alla soluzione è:

![image](https://github.com/Spamp/progetto_labirinto/assets/118067217/0103cfbb-1a72-474e-a3be-966e4ba9403c)

- 30-20_marked_1.jpg:

![image](https://github.com/Spamp/progetto_labirinto/assets/118067217/3c306f36-3e75-41f0-a98e-ed105478f615)

Il file .json associato alla soluzione è: 

![image](https://github.com/Spamp/progetto_labirinto/assets/118067217/6ec64848-e67a-4090-87a4-c22f1a1e5005)

# Dockerfile

Docker è un ambiente che consente l'esecuzione di container basato sull'impiego di immagini. Un'immagine è un file non modificabile che contiene tutte le informazioni per l'esecuzione di un'applicazione (quindi codice sorgente, librerie, dipendenze, e così via). Il container è un'immagine in esecuzione, quindi si modifica ed evolve nel tempo. 

Un Dockerfile è un documento di testo che contiene i comandi necessari per creare un'immagine Docker. Nel nostro caso, i comandi specificati nel Dockerfile  si occupano di sviluppare l'ambiente virtuale python, scaricare i pacchetti specificati nel file requirements.txt e copiare tutti i file presenti nella directory Labirinto. 

## Istruzioni per l'esecuzione del Docker

Per creare un'immagine Docker bisogna assicurarsi di utilizzare il prompt dei comandi nella cartella contenente il Dockerfile, il file requirements.txt e il file del programma. A questo punto, si digita il seguente comando: 

![image](https://github.com/Spamp/progetto_labirinto/assets/118067217/67399ec8-72f2-47ff-ac14-c877e20dae7c)

In questo caso "clanto" è il nome utente del creatore dell'immagine, "maze" è il nome dell'immagine, e 1 si riferisce alla versione. 

In seguito, eseguiamo il container "labirinto", specificando il percorso della cartella dei dati di input (indata) da cui prendere i dati in ingresso, e il percorso della cartella di output dove restituire i risultati (output). 

![image](https://github.com/Spamp/progetto_labirinto/assets/118067217/25af8bbb-afe1-4775-8bba-6eb4e844a832)

- I flag -a stdin e -a stdout connettono lo stdin e lo stdout del container con quello dell'host.
- Il flag -it attiva la modalità interattiva del container: in questo modo l'utente può interagire con la shell del container.
- I flag -v C:\progetto_labirinto\Labirinto\indata e -v C:\progetto_labirinto\Labirinto\output rappresentano il path del computer per raggiungere le cartelle "indata" e "output" alle quali è collegato il container.
- I flag /usr/src/app/indata e /usr/src/app/output rappresentano il path delle cartelle virtuali del container. 
- Il flag --name labirinto, indica il container creato di nome "labirinto", mentre "clanto/maze:1" è l'immagine creata in precedenza, con il rispettivo nome utente. 

In seguito a questo comando, viene restituita la richiesta di input del programma, nel quale il file di input viene inserito come segue:

![image](https://github.com/Spamp/progetto_labirinto/assets/118067217/a93d4079-f197-4e5d-861a-74fa402789ba)

Successivamente, si può continuare ad eseguire il programma all'interno dello stesso container labirinto digitando il comando sottostante, in seguito al quale viene restituita nuovamente la richiesta di input.  

![image](https://github.com/Spamp/progetto_labirinto/assets/118067217/e35d689d-a167-480f-9645-fa2bb147d035)

Per visualizzare l'output, si utilizzano i seguenti comandi:

![image](https://github.com/Spamp/progetto_labirinto/assets/118067217/80c9f97f-5143-47f5-969e-5ad8013efb7c)

![image](https://github.com/Spamp/progetto_labirinto/assets/118067217/7fd968c4-74e9-4e90-829c-71b9d4225366)

Il primo comando avvia il container "labirinto", mentre il secondo apre una shell interattiva all'interno del container. In questo modo, attraverso la shell, si può interagire direttamente con l'ambiente all'interno del container Docker, e quindi accedere ai file. 


