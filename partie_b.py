import random


# Étape 1 : Génération du nombre secret
    nombre_secret = random.randint(borne_min, borne_max)
    print(f"\n--- Devine le nombre entre {borne_min} et {borne_max} ---")
    print(f"Vous avez {max_essais} essais maximum !")