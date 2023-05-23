import json # om de json bibliotheek te gebruiken moet je deze eerst importeren.

#we lezen een json bestand in voor ons telefoonboek
#eerst openen we het bestand telefoonboek.json om in te lezen 'r' in variable file
with open('telefoonboek.json','r') as file:
    # het bestand wordt gelezen en met json.load in de variabele telefoonboeg gestopt
    telefoonboek = json.load(file)

# om te beginnen vullen we watwilje
watwilje = 1

# zoalang watwilje geen '0'is blijven we doorgaan dat betekend while
# != betekend is ongelijk aan
while(watwilje != '0'):
    #eerste nieuwe regel voor de duidelijkheid
    print()
    #vraag wat de gebruiker wil doen 1=zoeken anders toevoegen
    watwilje = input('wil je een nummer zoeken(1) of toevoegen(2) of stoppen(0)? ')
    if(watwilje == '1'): # == beteken is gelijk aan
        # vraag de naam van wie je zoekt
        ikzoek = input('wie zoek je dan? ')
        # gebruik de input van de gebruiker als sleutel om te zoeken in het telefoonboek
        # doe dit met een try om de faout van niet gevonden af te vangen
        try:
            telefoonnummer = telefoonboek[ikzoek]
            # als de naam is gevonden blijven we in de try. Wanneer deze niet is gevonden gaan we naar except
            # nummer is gevonden, druk af wat je gevonden hebt
            print('het nummer van ' + ikzoek + ' is ' + telefoonnummer)
        except: # naam is niet in het telefoonboek gevonden daarom komen we in except
            print(ikzoek + 'komt niet voor in het telefoonboek!')
    # check of de beruiker 2 heeft ingegeven    
    elif(watwilje == '2'):
        #vraag de naam
        naam = input('wie wil je toevoegen? ')
        # eerst checken of de naam al in het telefoonboek staat
        #dus probeer de naam te vinden door try te gebruiken
        try:
            #zoek het nummer voor de naam op in het telefoonboek
            nummer = telefoonboek[naam]
            #als die gevonden wordt dan gaan we niet naar exept maar blijven we in de try
            print(naam + ' bestaat al!')
            # vraag of we het nummer moeten overschrijven
            wiljeoverschrijven = input('wil je het nummer van ' + naam + ' overscrijven? j/n')
            if(wiljeoverschrijven == 'j'): #check of het antwoord ja is, bij nee doen we niets
                #vraag het nieuwe nummer
                nummer = input('wat is het nieuwe nummer? ')
                telefoonboek[naam] = nummer
                print('het nummer van ' + naam + ' is overschreven met ' + nummer)
        except: #dus naam is niet gevonden. dat goed want we willen deze toevoegen
            #vraag het nummer
            nummer = input('wat is het nummer? ')
            #sla de nieuwe naam op in het telefoonboek
            telefoonboek[naam] = nummer
            print('het nummer van ' + naam + ' is toegevoegd')
    else:
        #watwilje is geen 1 en geen 2 dus stoppen we
        print('oke dan stoppen we, Doei!')

#bewaar het telefoonboek met de nieuwe naam in het bestand
with open('telefoonboek.json', 'w') as file:
    file.write(json.dumps(telefoonboek))
        
