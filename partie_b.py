import random


# Étape 1 : Génération du nombre secret
    nombre_secret = random.randint(borne_min, borne_max)
    print(f"\n--- Devine le nombre entre {borne_min} et {borne_max} ---")
    print(f"Vous avez {max_essais} essais maximum !")


    # Boucle des essais
    for essai in range(1, max_essais + 1):
        # Saisie sécurisée
        while True:
            try:
                saisie = int(input(f"\nEssai {essai}/{max_essais} - Votre proposition : "))
                break
            except ValueError:
                print("⚠️ Veuillez entrer un nombre entier valide !")
                #mesage d'erreur
                