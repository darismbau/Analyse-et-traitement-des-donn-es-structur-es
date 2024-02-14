from Voiture import *

mycar1 = Voiture(m1="BMW",m2="BTY-1998/3",p=10,c="Rouge" )
mycar2 = Voiture( m1="Bently" , m2="BTY-1998/3" , c="Doré",p=25)
mycar3 = Voiture(m1="Bently" , m2="BTY-1998/3" , c="Doré",p=25)
mycar4 = Voiture(m1="Bently" , m2="BTY-1998/3" , p=25, c=123)

#print("Marque :", mycar1.marque)
#print("Modèle :", mycar1.modele)
#print("Puissance_fiscale :", mycar1.puissance_fiscale)
#print("Couleur :", mycar1.couleur)

#"print("Marque :", mycar4.marque)
#print("Modèle :", mycar4.modele)
#print("Puissance_fiscale :", mycar4.puissance_fiscale)
#print("Couleur :", mycar4.couleur)

print(mycar1)
print("Marque :", mycar1.get_marque())

