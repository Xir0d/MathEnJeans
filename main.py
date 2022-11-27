import string
from collections import Counter
import replace

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


#Définition de la liste de décalage à éxécuter (pour chaque lettre) en fonction de la clé privée, ex: abcabcabcabcabcabc

key_chain = private_key * key_repeat

#Convertion de la liste de décalage (en lettres) vers une liste de décalage en chiffres ex: 123123123123123

NUM = 31
  
def positions(str):
    for i in str:
        print((ord(i) & NUM), end ="")
        test = 1
        return test

  
str = key_chain
# position str n'est rien il renvoie a none

#Envoi de la liste de décalage en chiffre dans un fichier txt

print(test)

#SOLUTION: Au lieu d'utiliser une fonction, directement remplacer les a par 1 et b par 2, etc...
#OBJECTIF: FAIRE SORTIR LA VARIABLE LIGNE 42 DE LA FONCTION POUR POUVOIR L'UTILISER en utilisant return

#PLAN B: utiliser le code d'aikoo
#PLAN C: remplacer la clé directement en chiffre/avoir une clé prédéfinis

