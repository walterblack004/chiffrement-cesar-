from collections import Counter

# Fonction pour chiffrer le texte avec un décalage donné
def chiffrer(texte, decalage):
    """
    Chiffre un texte en utilisant le chiffrement de César.
    :param texte: Le texte à chiffrer.
    :param decalage: Le décalage à appliquer.
    :return: Le texte chiffré.
    """
    resultat = ""
    for lettre in texte:
        if lettre.isalpha():
            base = ord('A') if lettre.isupper() else ord('a')
            resultat += chr((ord(lettre) - base + decalage) % 26 + base)
        else:
            resultat += lettre
    return resultat

# Fonction pour déchiffrer le texte en utilisant le décalage inverse
def dechiffrer(texte, decalage):
    """
    Déchiffre un texte en utilisant le chiffrement de César
    :param texte: Le texte à déchiffrer.
    :param decalage: Le décalage à appliquer.
    :return: Le texte déchiffré.
    """
    return chiffrer(texte, -decalage)

# Fonction pour compter les occurrences des lettres dans un texte
def compter_occurrences(texte):
    """
    Compte les occurences de chaque lettre dans un texte.
    :param texte: Le texte à analyser.
    :return: Une liste de tuples contenant les lettres et les occurences
    """
    occurrences = Counter(lettre.lower() for lettre in texte if lettre.isalpha())
    occurrences_triees = sorted(occurrences.items(), key=lambda x: x[1], reverse=True)
    print("\n=== OCCURRENCES DES LETTRES ===")
    for lettre, count in occurrences_triees:
        print(f"{lettre} : {count}")
    print("===============================")
    return occurrences_triees

# Fonction pour déchiffrer un texte de manière interactive
def dechiffrer_interactif(texte_chiffre):
    """
    Déchiffre un texte de manière interactive.
    :param texte_chiffre: Le texte à déchiffrer.
    :return: Le texte déchiffré.
    """
    remplacements = {}
    print("\n=== DÉCHIFFREMENT ===")
    print("Texte chiffré initial :")
    print(texte_chiffre)

    while True:
        choix = input("Voulez-vous remplacer une lettre ? (O/N) : ").strip().upper()
        if choix == 'N':
            break
        elif choix == 'O':
            lettre_chiffree = input("Lettre chiffrée : ").strip().lower()
            lettre_remplacement = input(f"Remplacer par : ").strip().lower()
            if len(lettre_chiffree) == 1 and len(lettre_remplacement) == 1:
                remplacements[lettre_chiffree] = lettre_remplacement
            texte_chiffre = texte_chiffre.translate(str.maketrans(remplacements))
            print("Texte mis à jour :")
            print(texte_chiffre)
        else:
            print("Entrée invalide.")
    return texte_chiffre

# Fonction principale
def main():
    while True:
        print("\n=============================")
        print("         MENU PRINCIPAL      ")
        print("=============================")
        print("1. Chiffrer un texte")
        print("2. Déchiffrer un texte (avec décalage connu)")
        print("3. Compter les occurrences des lettres")
        print("4. Effectuer un déchiffrement manuel")
        print("5. Quitter")
        print("=============================")
        choix = input("Choisissez une option (1-5) : ").strip()
        if choix == '1':
            texte = input("Entrez le texte à chiffrer : ").strip()
            decalage = int(input("Entrez le décalage : "))
            print("Texte chiffré :", chiffrer(texte, decalage))
        elif choix == '2':
            texte = input("Entrez le texte à déchiffrer : ").strip()
            decalage = int(input("Entrez le décalage : "))
            print("Texte déchiffré :", dechiffrer(texte, decalage))
        elif choix == '3':
            texte = input("Entrez le texte pour analyser les occurrences : ").strip()
            compter_occurrences(texte)
        elif choix == '4':
            texte_chiffre = input("Entrez le texte chiffré : ").strip()
            dechiffrer_interactif(texte_chiffre)
        elif choix == '5':
            print("Merci d'avoir utilisé le programme.")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
