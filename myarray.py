
#  index   0 1 2 3 4 5  6  7  8 ....
# myarray = [5,6,7,8,9,10,11,12,13,14,15]
# print(myarray[7])

# start = 5
# stop = 30
# step = 2                         # 0  1  2 3  4  5  6  7
# myarray = range(start,stop,step) # 5, 7, 9,11,13,15,17,19..... 30
# print(myarray[7])

#TREINTJE is een ARRAY en werkt met een index. Dat is de positie van de wagon in de trein.
#        volgorde is hier heel belangrijk
treintje = [
    'schapen','koeien', 'kippen'
    ]

print(treintje[2])

#TELEFOONBOEK is een HASH of DICTIONARY en werkt met een sleutel. Volgorde is onbelangrijk
#        de sleutel is altijd uniek
telefoonboek = {
    'joop':'181419',
    'els':'192833',
    'greet': '202020',
    'fred': '12',
    'olaf':'883773883737',
    'maarten': '838737673676'
 }

# iets toevoegen aan de dictinoary
telefoonboek['michiel'] = '0634210168'
telefoonboek['olaf'] = '0654324424'

#iets verwijderen uit de dictionary
del telefoonboek['greet']

#vraag de gebruiker om een naam
ikzoek=input('wie zoek je? ')
telefoonnummer = telefoonboek[ikzoek]

#toon de naam met telefoonnummer
print('het nummer van ' + ikzoek + ' is ' + telefoonnummer)
