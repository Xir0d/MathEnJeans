import string
from collections import Counter
from tkinter import *
from tkinter.messagebox import showinfo


#Importation de la clé privée de codage
private_key = open('clé privé.key')
private_key = private_key.read()

#Définition de la longueur de la clé privée pour calculer ensuite combien avons-nous besoin de la copier

def count_letters(key_length):
    return len(key_length) - key_length.count(' ')

key_length = private_key
key_count = int(count_letters(key_length))

#Demande du message à chiffrer avec la clé privée
message_a_chiffrer = input("Écrivez le message à chiffrer: ")

#Récupération du nombre de lettres à chiffrer dans le message pour définir le nombre de fois que nous avons besoin de la clé de chiffrement privée
# (+) Division du nombre de caractère par la longueur de la clé de chiffrement privée
#On ajoute 1 pour éviter 9/2 = 1 fois la clé au lieu de 2


def count_letters(msg):
    return len(msg) - msg.count(' ')

msg = message_a_chiffrer
key_repeat = int(count_letters(msg) / key_count) + 1
message_length = int(count_letters(msg))

#Définition de la liste de décalage à éxécuter (pour chaque lettre) en fonction de la clé privée, ex: abcabcabcabcabcabc

key_chain = private_key * key_repeat

#Convertion de la liste de décalage (en lettres) vers une liste de décalage en chiffres ex: 123123123123123

NUM = 31

#def positions(str):
    #for i in str:
        #print((ord(i) & NUM), end ="")
        #test = 1
        #return test


#str = key_chain
# position str n'est rien il renvoie a none

#Envoi de la liste de décalage en chiffre dans un fichier txt et remplacement des a par 1, b par 2, etc ...
key_chain = key_chain.replace('A', '1\n')
key_chain = key_chain.replace('B', '2\n')
key_chain = key_chain.replace('C', '3\n')
key_chain = key_chain.replace('D', '4\n')
key_chain = key_chain.replace('E', '5\n')
key_chain = key_chain.replace('F', '6\n')
key_chain = key_chain.replace('G', '7\n')
key_chain = key_chain.replace('H', '8\n')
key_chain = key_chain.replace('I', '9\n')
key_chain = key_chain.replace('J', '10\n')
key_chain = key_chain.replace('K', '11\n')
key_chain = key_chain.replace('L', '12\n')
key_chain = key_chain.replace('M', '13\n')
key_chain = key_chain.replace('N', '14\n')
key_chain = key_chain.replace('O', '15\n')
key_chain = key_chain.replace('P', '16\n')
key_chain = key_chain.replace('Q', '17\n')
key_chain = key_chain.replace('R', '18\n')
key_chain = key_chain.replace('S', '19\n')
key_chain = key_chain.replace('T', '20\n')
key_chain = key_chain.replace('U', '21\n')
key_chain = key_chain.replace('V', '22\n')
key_chain = key_chain.replace('W', '23\n')
key_chain = key_chain.replace('X', '24\n')
key_chain = key_chain.replace('Y', '25\n')
key_chain = key_chain.replace('Z', '26\n')
key_chain_export = open('keychain.txt', 'w')
key_chain_export = key_chain_export.write(key_chain)

#Décalage des lettres selon la liste établie précedemment
message_chiffre = 0
file = open('keychain.txt')
lines = file.readlines()
while message_chiffre >= message_length:
    for line in lines:
        print(line.strips())
        print('test') #Voir si il est possible de faire des choses dans une boucle et si non comment en extraire les informatinoscomme des variables

#Fermeture du fichier
file.close()
#Message final chiffre
message_chiffre = 1
#Envoie du résultat (message chiffré) dans une infoBox
message_chiffre = showinfo('Message chiffré avec succès:', message_chiffre)

#SOLUTION: Au lieu d'utiliser une fonction, directement remplacer les a par 1 et b par 2, etc...
#OBJECTIF: FAIRE SORTIR LA VARIABLE LIGNE 42 DE LA FONCTION POUR POUVOIR L'UTILISER en utilisant return

#PLAN C: remplacer la clé directement en chiffre/avoir une clé prédéfinis
#PLAN B: utiliser le code d'aikoo


