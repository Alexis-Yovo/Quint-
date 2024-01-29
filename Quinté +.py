import random

print("Choissisez vos 7 numéros :")
numeros = []
for i in range(7):
   while True:
        numero = int(input("Entrez le numéro {} (entre 1 et 20) : ".format(i+1)))
        if 1 <= numero <= 20:
            numeros.append(numero)
            break
        else:
            print("Veuillez entrer un numéro entre 1 et 20.")
print("Les numéros choisis sont :", numeros)
results = [random.randint(1, 20) for _ in range(7)]
print("Résultats du Quinté : ", results)
