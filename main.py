import string
from collections import Counter

#Importation de la clé privée de codage
private_key = open('clé privé.key')
private_key = private_key.read()

#Définition de la longueur de la clé privée pour calculer ensuite combien avons-nous besoin de la copier

def count_letters(key_length):
    return len(key_length) - key_length.count(' ')

key_length = private_key
key_count = int(count_letters(key_length))
print(key_count)

#Demande du message à chiffrer avec la clé privée
message_a_chiffrer = input("Écrivez le message à chiffrer: ")

#Récupération du décalage des lettres de la clé privée, exemple: a=1, b=2, etc...

NUM = 31

def positions(str):
    for i in str:
        print((ord(i) & NUM), end =" ")
  
str = private_key

#Récupération du nombre de lettres à chiffrer dans le message pour définir le nombre de fois que nous avons besoin de la clé de chiffrement privée
# (+) Division du nombre de caractère par la longueur de la clé de chiffrement privée

def count_letters(msg):
    return len(msg) - msg.count(' ')

msg = message_a_chiffrer
key_count = int(count_letters(msg) / key_count) + 1 #On ajoute 1 pour éviter 9/2 = 1 fois la clé au lieu de 2

#Création d'une liste avec le décalage à effectuer pour la lettre 1, 2, 3, etc... (selon la longueur nécessaire définis précedemment)



#Définition du décalage à éxécuter (pour chaque lettre) en fonction de la clé privée

def decalage(str):
    for i in str:
        print((ord(i) & NUM), end =" ")
  
str = private_key
decalage(str)

print(int(decalage(str)) * key_count)