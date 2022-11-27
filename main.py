import string
from collections import Counter
import replace

#Importation de la clé privée de codage
private_key = open('clé privé.key')
private_key = private_key.read()
print(private_key)

#Définition de la longueur de la clé privée pour calculer ensuite combien avons-nous besoin de la copier

def count_letters(key_length):
    return len(key_length) - key_length.count(' ')

key_length = private_key
key_count = int(count_letters(key_length))

#Demande du message à chiffrer avec la clé privée
message_a_chiffrer = input("Écrivez le message à chiffrer: ")

#Récupération du décalage des lettres de la clé privée, exemple: a=1, b=2, etc...

NUM = 31

def positions(str):
    for i in str:
          
        # Performing AND operation
        # with number 31
        print((ord(i) & NUM), end ="")
  
str = private_key
key_number = positions(str)
fichier = open("test.txt", "r")
print(fichier)

#Récupération du nombre de lettres à chiffrer dans le message pour définir le nombre de fois que nous avons besoin de la clé de chiffrement privée
# (+) Division du nombre de caractère par la longueur de la clé de chiffrement privée
#On ajoute 1 pour éviter 9/2 = 1 fois la clé au lieu de 2

def count_letters(msg):
    return len(msg) - msg.count(' ')

msg = message_a_chiffrer
key_repeat = int(count_letters(msg) / key_count) + 1

#Définition de la liste de décalage à éxécuter (pour chaque lettre) en fonction de la clé privée, ex: 123451234512345

#key_chain = positions(str) * 3
#print(key_chain)

#Création d'une liste avec le décalage à effectuer pour la lettre 1, 2, 3, etc... (selon la longueur nécessaire définis précedemment)

