import string

#Importation de la clé privée de codage
private_key = open('clé privé.key')
private_key = private_key.read()

  
#Récupération du décalage des lettres de la clé privée, exemple: a=1, b=2, etc...

NUM = 31

def positions(str):
    for i in str:
        print((ord(i) & NUM), end =" ")
  
str = private_key
positions(str)

