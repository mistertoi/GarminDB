import os
import shutil

# z scripts
# geht zu: p03_GarminDB\scripts
# python garmindb_cli.py --activities --download --import --analyze --latest

# Dateien werden dann nach
# C:\\Users\\thors\\HealthData\\FitFiles\\Activities
# downgeloadet.
# Von dort die NEUEN Dateien nach "Z:\Dokumente\Sport\Garmin\GarminDB\HealthData\FitFiles\Activities"
# KOPIEREN!!
# Jetzt können die Aktivitäten in GoldenCheetah importiert werden, um z.B eine Heatmap zu erzeugen.

print("Kopiervorgang startet...")
print()

# Quell- und Zielverzeichnisse definieren
source_directory = r"C:\Users\thors\HealthData\FitFiles\Activities"
fit_destination_directory = r"Z:\Dokumente\Sport\Garmin\GarminDB\HealthData\FitFiles\Activities"
json_destination_directory = r"Z:\Dokumente\Sport\Garmin\GarminDB\HealthData\FitFiles\Activities\json"

# Sicherstellen, dass Zielverzeichnisse existieren, falls nicht, erstellen
os.makedirs(fit_destination_directory, exist_ok=True)
os.makedirs(json_destination_directory, exist_ok=True)

# Liste aller Dateien im Quellverzeichnis
files = os.listdir(source_directory)

# Variablen für Erfolgs- und Misserfolgszähler initialisieren
success_count = 0
failure_count = 0


# Durch alle Dateien iterieren und entsprechend kopieren
for file in files:
    # Überprüfen, ob es sich um eine .fit-Datei handelt
    if file.endswith(".fit"):
        # Ziel-Pfad für .fit-Dateien
        fit_destination_path = os.path.join(fit_destination_directory, file)
        # Falls die Datei noch nicht im Zielverzeichnis existiert, kopieren
        if not os.path.exists(fit_destination_path):
            try:
                shutil.copy2(os.path.join(source_directory, file), fit_destination_path)
                success_count += 1
                print(f"Die Datei '{file}' wurde erfolgreich ins Zielverzeichnis kopiert.")
            except Exception as e:
                failure_count += 1
                print(f"Fehler beim Kopieren der Datei '{file}': {e}")
        else:
            print(f"Die Datei '{file}' existiert bereits im Zielverzeichnis.")
    # Überprüfen, ob es sich um eine .json-Datei handelt
    elif file.endswith(".json"):
        # Ziel-Pfad für .json-Dateien
        json_destination_path = os.path.join(json_destination_directory, file)
        # Falls die Datei noch nicht im Zielverzeichnis existiert, kopieren
        if not os.path.exists(json_destination_path):
            try:
                shutil.copy2(os.path.join(source_directory, file), json_destination_path)
                success_count += 1
                print(f"Die Datei '{file}' wurde erfolgreich ins Zielverzeichnis kopiert.")
            except Exception as e:
                failure_count += 1
                print(f"Fehler beim Kopieren der Datei '{file}': {e}")
        else:
            print(f"Die Datei '{file}' existiert bereits im Zielverzeichnis.")

# Ausgabe der Zusammenfassung
print(f"\nZusammenfassung:")
print(f"Erfolgreich kopierte Dateien: {success_count}")
print(f"Nicht kopierte Dateien (Fehler): {failure_count}")
