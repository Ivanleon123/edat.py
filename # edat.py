# edat.py

def comprova_edat(edat):
    if edat > 18:
        return "Ets major d'edat."
    elif edat < 18:
        return "No ets major d'edat."
    else:
        return "Tens exactament 18 anys."
    from edat import comprova_edat

# Llegeix l'edat de l'usuari
try:
    edat = int(input("Introdueix la teva edat: "))
    # Crida la funció i imprimeix el resultat
    resultat = comprova_edat(edat)
    print(resultat)
except ValueError:
    print("Si us plau, introdueix un número vàlid.")
    