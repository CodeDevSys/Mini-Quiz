# Mini-Quiz mit 5 Fragen
def quiz():
    fragen = [
        ("Wie heißt die Hauptstadt von Deutschland?", "berlin"),
        ("Wie viele Kontinente gibt es?", "7"),
        ("Was ist 5 + 3?", "8"),
        ("Welche Farbe hat die Sonne?", "gelb"),
        ("Wie heißt das größte Tier der Welt?", "blauwal")
    ]
    
    punkte = 0
    print("Willkommen zum Mini-Quiz! 🌟\n")

    for frage, antwort in fragen:
        user = input(frage + " ").lower()
        if user == antwort:
            print("✅ Richtig!\n")
            punkte += 1
        else:
            print("❌ Falsch! Die richtige Antwort war:", antwort, "\n")

    print(f"Du hast {punkte} von {len(fragen)} Punkten erreicht!")

quiz()
