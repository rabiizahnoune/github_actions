import pandas as pd
import sys

# Charger les données
df = pd.read_csv("sales_data.csv")

# Validation 1 : Vérifier les quantités négatives
negative_quantities = df[df["quantity"] < 0]
if not negative_quantities.empty:
    print("Erreur : Quantités négatives détectées !")
    print(negative_quantities)
    with open("validation_errors.txt", "w") as f:
        f.write("Quantités négatives détectées :\n")
        f.write(negative_quantities.to_string())
    sys.exit(1)  # Échoue pour bloquer le workflow

# Validation 2 : Vérifier les valeurs manquantes
missing_values = df[df["quantity"].isna()]
if not missing_values.empty:
    print("Erreur : Valeurs manquantes détectées !")
    print(missing_values)
    with open("validation_errors.txt", "a") as f:
        f.write("\nValeurs manquantes détectées :\n")
        f.write(missing_values.to_string())
    sys.exit(1)

# Si tout est OK
print("Validation réussie : toutes les données sont correctes !")
with open("validation_success.txt", "w") as f:
    f.write("Données valides, prêtes à être utilisées.")