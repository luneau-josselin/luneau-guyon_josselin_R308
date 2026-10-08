


def ajouter_etudiant(d: dict, nom: str, note: float) -> None:
# Ajoute ou met à jour un étudiant dans le dictionnaire
    try:
        d[nom.strip()] = float(note)
    except (ValueError, TypeError):
        print(f"Erreur : La note '{note}' pour '{nom}' n'est pas valide.")
#mesage d'erreur

def moyenne_classe(d: dict) -> float:
    #Calcule la moyenne de la classe
    if not d:
        return 0.0
    return sum(d.values()) / len(d)

def meilleur_etudiant(d: dict) -> tuple[str, float] | None:
#Renvoie (nom, note) du meilleur étudiant
    if not d:
        return None
    cle_max = max(d, key=d.get)
    return (cle_max, d[cle_max])

def sauvegarder_notes(d: dict, fichier: str) -> None:
#Sauvegarde le dictionnaire dans un fichier texte
    try:
        with open(fichier, "w", encoding="utf-8") as f:
            for nom, note in d.items():
                f.write(f"{nom}: {note}\n")
        print(f"Notes sauvegardées dans '{fichier}'.")
    except IOError as e:
        print(f"Erreur lors de la sauvegarde : {e}")

def recharger_notes(fichier: str) -> dict:
#Recharge le dictionnaire depuis un fichier texte.
    d = {}
    if not os.path.exists(fichier):
        return d
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            for ligne in f:
                ligne = ligne.strip()
                if ":" in ligne:
                    nom, note_str = ligne.split(":", 1)
                    try:
                        d[nom.strip()] = float(note_str.strip())
                    except ValueError:
                        continue
    except IOError as e:
        print(f"Erreur de lecture : {e}")
    return d


if __name__ == "__main__":
    etudiants = {}

    print("=== SAISIE DES ÉTUDIANTS ET DE LEURS NOTES ===")
    
    while True:
        nom = input("\nEntrez le nom de l'étudiant (ou appuyez sur Entrée pour terminer) : ").strip()
        
        # Condition de sortie : si l'utilisateur entre une chaîne vide
        if not nom:
            break
            
        # Saisie sécurisée de la note
        while True:
            try:
                note_input = input(f"Entrez la note pour {nom} (ex: 14.5) : ")
                note = float(note_input)
                break
            except ValueError:
                print("Note invalide ! Veuillez saisir un nombre (ex: 12 ou 15.5).")

        # Ajout au dictionnaire
        ajouter_etudiant(etudiants, nom, note)

    # Affichage des résultats
    print("\n" + "="*40)
    print("RÉSUMÉ DE LA CLASSE :")
    print(f"Dictionnaire complet : {etudiants}")
    
    if etudiants:
        print(f"Moyenne de la classe : {moyenne_classe(etudiants):.2f}")
        nom_meilleur, note_meilleur = meilleur_etudiant(etudiants)
        print(f"Meilleur étudiant : {nom_meilleur} avec {note_meilleur}/20")
        
        # Sauvegarde
        sauvegarder_notes(etudiants, "notes.txt")
    else:
        print("Aucun étudiant n'a été saisi.")