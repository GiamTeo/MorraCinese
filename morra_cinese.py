import random # importazione libreria random 

def controllo_vittoria(vittorie_pc, vittorie_utente): # funzione per il controllo della vittoria finale
    print(partite) # stampo a schermo i risultati di ogni partita
    if vittorie_utente == 3: # controllo se l'utente è arrivato a 3 vittorie
            print("Complimenti, hai vinto il match!\n")
    elif vittorie_pc == 3: # controllo se il PC è arrivato a 3 vittorie
            print("PC ha vinto il match!\n")

def controllo_mossa(mossa_utente): # funzione per il controllo delle mosse inserite dall'utente
    while mossa_utente not in mosse: # controllo se la mossa inserita c'è nella lista delle mosse possibili
        print("Mossa non valida. Riprova.")
        mossa_utente = input("Scegli la tua mossa (s - c - f): ") # reinserimento della mossa

mosse = ["s", "c", "f"] # inizializzazione della lista delle mosse
partite = [] # inizializzazione lista dei risultati delle partite giocate
pareggio = 0 # inizializzazione delle variabili per il controllo della vittoria finale
vittorie_pc = 0
vittorie_utente = 0
salva_mosse = [] # salva le mosse dell'utente
i = 0 # counter delle partite

print("Benvenuto nel gioco: SASSO - CARTA - FORBICE\n")
print("Per fare SASSO inserire: s,\nPer fare CARTA inserire: c,\nPer fare FORBICE inserire: f\n ")

while i < 3: # l'utente deve giocare 3 partite

    while vittorie_pc != 3 and vittorie_utente != 3: # finchè nessuno dei 2 giocatori arriva a 3, il programma gira

        mossa_utente = input("Scegli la tua mossa (s - c - f): ") # inserimento mossa utente
        controllo_mossa(mossa_utente) # richiamo funzione controllo mossa dell'utente

        mossa_pc = random.choice(mosse) # scelta randomica della mossa del PC
        print("La mossa del computer è: ", mossa_pc)

        salva_mosse.append(mossa_utente) # aggiungo le mosse dell'utente alla lista delle mosse salvate

        if (mossa_utente == mossa_pc): # controllo se le mosse inserite sono uguali
            print("Pareggio") # se sono uguali, il round finisce in parità
            partite.append("Pareggio") # aggiungo pareggio alla lista dei risultati delle partite
        elif (mossa_utente == "s" and mossa_pc == "f") or (mossa_utente == "f" and mossa_pc == "c") or (mossa_utente == "c" and mossa_pc == "s"): # controllo delle mosse per vedere se l'utente ha vinto
            print("Hai vinto!") # utente ha vinto
            vittorie_utente += 1 # aggiorno l'indice delle vittorie dell'utente
            partite.append("Utente") # aggiungo la vittoria dell'utente alla lista dei risultati delle partite
        else: # se tutte le mosse di prima non avvengono, la vittoria del round è del PC
            print("PC ha vinto!") # PC ha vinto
            vittorie_pc += 1 # aggiorno l'indice delle vittorie del PC
            partite.append("PC") # aggiungo la vittoria del PC alla lista dei risultati delle partite

        controllo_vittoria(vittorie_pc, vittorie_utente) # funzione per il controllo della vittoria finale
    i += 1 # aggiorno il counter delle partite
    vittorie_pc = 0 # imposto le variabili delle vittorie a 0
    vittorie_utente = 0


# MODALITA PC-INTELLIGENTE

index_s = 0 # inizializzazioni indici per vedere le giocate dell'utente
index_c = 0
index_f = 0

print("Adesso il computer ha un'intelligenza e conosce le tue mosse preferite...")
print("Prova a fare una partita contro il PC-INTELLIGENTE\n")
print(salva_mosse) # stampo le mosse fatte nella partita precedente dall'utente

index_s = salva_mosse.count("s") # indice è uguale al count di quella mossa
index_c = salva_mosse.count("c")
index_f = salva_mosse.count("f")

print("Sasso: " + str(index_s) + " Carta: " + str(index_c) + " Forbice: " + str(index_f)) # stampo le count delle mosse fatte dall'utente

print("Adesso il PC-INTELLIGENTE ti sfiderà nuovamente...") # inizio nuova partita

partite = [] # inizializzazione lista dei risultati delle partite giocate
pareggio = 0 # inizializzazione le variabili per il controllo della vittoria finale
vittorie_pc = 0
vittorie_utente = 0

while vittorie_pc != 3 and vittorie_utente != 3: # finchè nessuno dei 2 giocatori arriva a 3, il programma gira

    mossa_utente = input("Scegli la tua mossa (s - c - f): ") # inserimento mossa utente
    controllo_mossa(mossa_utente) # richiamo funzione controllo mossa dell'utente
    
    if(index_s > index_c) and (index_s > index_f): # controllo se l'utente ha giocato più volte sasso 
        if(mossa_utente == "s"): # se anche in questo round ha giocato sasso
            print("Ho capito che ti piace giocare sasso...")
            mossa_pc = "c" # computer capisce quale mossa fare
        else:
            print("Non conosco le tue mosse...")
            mossa_pc = random.choice(mosse) # scelta randomica della mossa del PC
    elif(index_c > index_s) and (index_c > index_f): # controllo se l'utente ha giocato più volte carta
        if(mossa_utente == "c"):
            print("Ho capito che ti piace giocare carta...")
            mossa_pc = "f" # computer capisce quale mossa fare
        else:
            print("Non conosco le tue mosse...")
            mossa_pc = random.choice(mosse) # scelta randomica della mossa del PC
    elif(index_f > index_s) and (index_f > index_c): # controllo se l'utente ha giocato più volte forbice
        if(mossa_utente == "f"):
            print("Ho capito che ti piace giocare forbice...")
            mossa_pc = "s" # computer capisce quale mossa fare
        else:
            print("Non conosco le tue mosse...")
            mossa_pc = random.choice(mosse) # scelta randomica della mossa del PC
    else:
        print("Non conosco le tue mosse...") # se non ci sono giocate maggiori di altre, il computer sceglie randomicamente la mossa
        mossa_pc = random.choice(mosse) # scelta randomica della mossa del PC

    print("La mossa del computer è: ", mossa_pc) # stampa della mossa del PC

    if (mossa_utente == mossa_pc): # controllo se le mosse inserite sono uguali
        print("Pareggio") # se sono uguali, il round finisce in parità
        partite.append("Pareggio") # aggiungo pareggio alla lista dei risultati delle partite
    elif (mossa_utente == "s" and mossa_pc == "f") or (mossa_utente == "f" and mossa_pc == "c") or (mossa_utente == "c" and mossa_pc == "s"): # controllo delle mosse per vedere se l'utente ha vinto
        print("Hai vinto!") # utente ha vinto 
        vittorie_utente += 1 # aggiorno l'indice delle vittorie dell'utente
        partite.append("Utente") # aggiungo la vittoria dell'utente alla lista dei risultati delle partite
    else: # se tutte le mosse di prima non avvengono, la vittoria del round è del PC
        print("PC ha vinto!") # PC ha vinto
        vittorie_pc += 1 # aggiorno l'indice delle vittorie del PC
        partite.append("PC") # aggiungo la vittoria del PC alla lista dei risultati delle partite

    controllo_vittoria(vittorie_pc, vittorie_utente) # funzione per il controllo della vittoria finale