# PROGETTO_LABIRINTO

Il programma implementato riceve in ingresso un file contenente le caratteristiche del labirinto, una lista di partenze e una lista di destinazioni, e fornisce in output il path del percorso di costo minimo fra i punti specificati, insieme al costo totale associato al percorso.

## DESCRIZIONE DELL'INPUT

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

16 che assegna un costo pari a 1
32 che assegna un costo pari a 2
48 che assegna un costo pari a 3
64 che assegna un costo pari a 4
80 che assegna un costo pari a 5
96 che assegna un costo pari a 6
112 che assegna un costo pari a 7
128 che assegna un costo pari a 8
144 che assegna un costo pari a 9
160 che assegna un costo pari a 10
176 che assegna un costo pari a 11
192 che assegna un costo pari a 12
208 che assegna un costo pari a 13
124 che assegna un costo pari a 14
240 che assegna un costo pari a 15

## INPUT

Il file di input può essere fornito come segue:

![image](https://github.com/Spamp/progetto_labirinto/assets/118067217/cd90ac22-7f42-4b4e-8dce-e6c273c9ca38)

## ELABORAZIONE

Il programma acquisisce il layout di un labirinto costituito da una matrice di posizioni, una o più posizioni di partenza e una posizione di arrivo. Il labirinto viene trasformato in una matrice le cui celle contengono i costi riportati nel file, oppure valori NaN quando si ha una parete. 
La matrice viene allora convertita in un grafo indiretto pesato, che viene esplorato a partire dai nodi di partenza specificati.

## OUTPUT

Il programma risolve il labirinto, calcolando per ogni punto di partenza il percorso minimo che permette di raggiungere il punto di arrivo con il minor costo possibile. Il costo viene calcolato come la somma dei pesi degli archi incontrati e la lunghezza del cammino stesso. Se non esiste alcun percorso possibile, il programma restituisce un cammino vuoto. 
Inoltre, il programma calcola tutti i cammini possibili fra i punti di partenza e arrivo specificati, con i rispettivi costi associati.

Il risultato del labirinto viene fornito con un'immagine che restituisce un percorso colorato fra partenza e destinazione. 

### ESEMPIO DI OUTPUT:


