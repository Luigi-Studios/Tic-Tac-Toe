# Tic Tac Toe in der Konsole

# TODO: Wenn fertig, check_for_wins als eine Funktion versuchen, umzuprogrammieren
# TODO: Wenn fertig, Befehle wie "Quit" "New Game" "Skip" "Stats" einbauen
# TODO: Wenn fertig, wins mit Primzahlen und Produkten probieren
# TODO: CLEANUP

""" Bibliotheken """

# random für Gegenspieler
import random

""" Variablen """

# die Nummern von 1 bis 9 sind die Positionen auf dem Spiel-Feld, die
# leeren Strings, ob Spieler 1 oder Spieler 2 dort platziert hat
spots = {"1": " ", "2": " ", "3": " ",
         "4": " ", "5": " ", "6": " ",
         "7": " ", "8": " ", "9": " "}

made_another_valid_input = False

""" Funktionen """


# Starttext am Anfang eines neuen Spiels
def say_hello():
    # Willkommens-Text
    print("Herzlich Willkommen bei Tac Tac Toe!")
    print("Befehle: ")
    print("        - Quit für Beenden des Spiels")
    print("        - Skip für das Überspringen des Spielzuges")
    print("        - Stats für die aktuellen Informationen\n")
    print("Spielprinzip: das Ziel ist es, drei in einer Reihe zu platzieren, z.B.:")
    show_game({"1": " ", "2": "x", "3": " ",
               "4": " ", "5": "x", "6": " ",
               "7": " ", "8": "x", "9": " "})
    print("Zum Spielen gebe eine von diesen Positionen ein:")
    show_game({"1": "1", "2": "2", "3": "3",
               "4": "4", "5": "5", "6": "6",
               "7": "7", "8": "8", "9": "9"})
    print("\nLos geht's!\n")


""" hier braucht man current_spots, da man am Beginn eines Spieles ein Beispiel-Spots zeigen möchte,
 d.h. man muss die spots bearbeiten können """


# zeigt das aktuelle Spiel an
def show_game(current_spots: dict):
    print(f" {current_spots['1']} | {current_spots['2']} | {current_spots['3']}")
    print("---+---+---")
    print(f" {current_spots['4']} | {current_spots['5']} | {current_spots['6']}")
    print("---+---+---")
    print(f" {current_spots['7']} | {current_spots['8']} | {current_spots['9']}")


# shows the current stats
def show_stats():
    spieler_spots = [int(player_spot) for player_spot in spots if spots[player_spot] == "x"]
    computer_spots = [int(computer_spot) for computer_spot in spots if spots[computer_spot] == "o"]
    print("+---| Spiel-Stats |---+ ")
    print(f" ○ Spieler-Spots: {spieler_spots} ➜ Züge: {len(spieler_spots)}")
    print(f" ○ Computer-Spots: {computer_spots} ➜ Züge: {len(computer_spots)}\n")

    # returns true, so the control loop it not executed
    return True


# Gegenspieler
def Computer():
    # die Liste aus Positionen, die der Computer zu Verfügung hat
    verfuegbare_Positionen = []

    for current_spot in spots:
        if check_spot(int(current_spot)):
            verfuegbare_Positionen.append(int(current_spot))

    zufaellige_Position = random.choice(verfuegbare_Positionen)
    # schauen, ob die zufällige Position schon frei ist
    if check_spot(zufaellige_Position):
        return zufaellige_Position
    else:
        pass


# lets you skip your play move
def skip_play_move():
    print("Möchtest du deinen Spielzug wirklich überspringen? [j]a oder [n]ein")
    eingabe = input("Eingabe: ")
    if eingabe == "j" or eingabe == "n":
        if eingabe == "j":
            print("Spielzug wurde übersprungen")
            change_state(Computer(), 2)
            show_game(spots)
            return True
        if eingabe == "n":

            print("Spielzug wird nicht übersprungen")
            show_game(spots)
            return False
    else:
        while eingabe != "j" or eingabe != "n":
            print("Falsche Eingabe! Gebe entweder [j]a oder [n]ein ein!")
            eingabe = input("Eingabe: ")
            if eingabe == "j" or eingabe == "n":
                if eingabe == "j":
                    print("Spielzug wurde übersprungen")
                    change_state(Computer(), 2)
                    show_game(spots)
                    return True
                if eingabe == "n":
                    print("Spielzug wird nicht übersprungen")
                    show_game(spots)
                    return False


# ändert ein Spot, z.B. wenn der Spieler platziert
def change_state(selected_pos_int: int, spieler: int):
    if spieler == 1:
        spots[str(selected_pos_int)] = "x"
    else:
        spots[str(selected_pos_int)] = "o"


# checken, ob ein Spot schon belegt ist
def check_spot(current_spot: int):
    # wenn der Spot noch nicht besetzt ist, also " ", dann True, sonst ist er ja besetzt also False
    if spots[str(current_spot)] == " ":
        return True
    else:
        return False


# überprüft, ob bei dem Spiel jemand gewonnen hat
def check_for_wins():
    # Liste aller möglichen wins für den Spieler
    collection_of_wins = {"1": [1, 2, 3],
                          "2": [4, 5, 6],
                          "3": [7, 8, 9],
                          "4": [1, 5, 9],
                          "5": [3, 5, 7],
                          "6": [9, 5, 1],
                          "7": [7, 5, 3],
                          "8": [1, 4, 7],
                          "9": [2, 5, 8],
                          "10": [3, 6, 9]}

    spieler_spots = []
    computer_spots = []
    spieler_check = []
    computer_check = []

    # die Liste von allen Spieler-Spots, also die ein 'x' sind
    # die Liste von allen Computer-Spots, also die ein 'o' sind

    for current_spot in spots:
        if spots[current_spot] == "x":
            spieler_spots.append(int(current_spot))
        elif spots[current_spot] == "o":
            computer_spots.append(int(current_spot))

    # geht durch das Dict 'collection_of_wins' durch
    for win in collection_of_wins:
        # geht durch alle Zahlen durch, die vom Spieler gesetzt worden
        for number in spieler_spots:
            """ wenn die Zahl in 'spots' sich auch im gerade ausgewähltem Wins befindet, 
            dann wird diese Zahl zu der Liste 'spieler_check' hinzugefügt """
            if number in collection_of_wins[win]:
                spieler_check.append(number)

        """ nachdem es durch den gesamten Win, also z.B. [4, 5, 6]  durchgelaufen ist und es mit den Spieler-Positionen 
        überprüft hat, wird es mit dem Win verglichen"""

        """ Erkärung: angenommen, man hat die Spieler-Positionen [1, 2, 3, 5, 7], dann wird es jedes einzelne als erstes
            mit dem Win 1, also [1, 2, 3] vergleichen. In dem Fall sind alle Zahlen von Spieler-Positionen auch im Win
            [1, 2, 3] enthalten. Jedes mal, wenn eine Zahl in Spieler-Positionen und im Win enthalten ist, wird es zur 
            Liste 'spieler_check' hinzugefügt. Danach wird 'spieler_check' mit dem Win verglichen. Wenn es mit dem Win 
            übereinstimmt, dann hat der Spieler gewonnen, wenn nicht, dann (noch) nicht."""

        """ Wenn 'spieler_check' nicht mit dem Win übereinstimmt, dann wird 'spieler_check' wieder geleert und dieser 
            Vorgang wiederholt sich, bis die Spieler-Spots mit allen Wins verglichen wurden"""

        if spieler_check == collection_of_wins[win]:
            return "Spieler"

        else:
            spieler_check.clear()

    # das gleiche jetzt für Computer

    # geht durch das Dict 'collection_of_wins' durch
    for win in collection_of_wins:
        # geht durch alle Zahlen durch, die vom Spieler gesetzt worden
        for number in computer_spots:
            """ wenn die Zahl in 'spots' sich auch im gerade ausgewähltem Wins befindet, 
            dann wird diese Zahl zu der Liste 'spieler_check' hinzugefügt """
            if number in collection_of_wins[win]:
                computer_check.append(number)

        """ nachdem es durch den gesamten Win, also z.B. [4, 5, 6]  durchgelaufen ist und es mit den Spieler-Positionen 
        überprüft hat, wird es mit dem Win verglichen"""

        """ Erkärung: angenommen, man hat die Spieler-Positionen [1, 2, 3, 5, 7], dann wird es jedes einzelne als erstes
            mit dem Win 1, also [1, 2, 3] vergleichen. In dem Fall sind alle Zahlen von Spieler-Positionen auch im Win
            [1, 2, 3] enthalten. Jedes mal, wenn eine Zahl in Spieler-Positionen und im Win enthalten ist, wird es zur 
            Liste 'spieler_check' hinzugefügt. Danach wird 'spieler_check' mit dem Win verglichen. Wenn es mit dem Win 
            übereinstimmt, dann hat der Spieler gewonnen, wenn nicht, dann (noch) nicht."""

        """ Wenn 'spieler_check' nicht mit dem Win übereinstimmt, dann wird 'spieler_check' wieder geleert und dieser 
            Vorgang wiederholt sich, bis die Spieler-Spots mit allen Wins verglichen wurden"""

        if computer_check == collection_of_wins[win]:
            return "Computer"

        else:
            computer_check.clear()


# untersucht das aktuelle Spiel auf ein Unentschieden
def istUntenschieden():
    available_spots_left = []

    for spot in spots:
        if spots[spot] == " ":
            available_spots_left.append(spot)

    if len(available_spots_left) == 0:
        return True
    else:
        return False


# creates the a new game
def new_game():
    # asking the player if he/she really wants to continue
    print("Beim Erstellen eines neuen Spieles werden alle aktuellen Daten\nwie Positionen gelöscht und das Spiel "
          "startet von neu.\nMöchtest du fortfahren? j[a] oder n[ein]\n")

    eingabe = input("Eingabe: ")
    if eingabe == "j" or eingabe == "n":
        if eingabe == "j":
            print("Neues Spiel wird erstellt")
            return True
        if eingabe == "n":
            print("Vorgang wird abgebrochen")
            return False
    else:
        while eingabe != "j" or eingabe != "n":
            print("Falsche Eingabe! Gebe entweder [j]a oder [n]ein ein!")
            eingabe = input("Eingabe: ")
            if eingabe == "j" or eingabe == "n":
                if eingabe == "j":
                    print("Neues Spiel wird erstellt")
                    return True
                if eingabe == "n":
                    print("Vorgang wird abgebrochen")
                    return False


""" Game Loop """

# Willkommenstext am Start
say_hello()

# Schleifenkontrolle
active = True
# the game loop
while active:

    """ User Inputs """

    user_input = input("Position: ")

    # Als erstes schauen wir, ob die Eingabe "Quit" ist
    if user_input == "Quit":
        quit()
    elif user_input == "Skip":
        made_another_valid_input = skip_play_move()
    elif user_input == "Stats":
        made_another_valid_input = show_stats()
    elif user_input == "New Game":
        made_another_valid_input = new_game()
    else:
        pass

    # als nächstes schauem wir, ob es ein integer ist

    """ kurze Erklärung, warum wir ein try-except brauchen: user_input = input("Position: ") ist immer ein String,
        also macht es keinen Sinn, wenn wir überprüfen, ob es ein String oder doch ein Integer ist. In dem try-Block 
        versuchen wir, die Eingabe in einen Integer zu konvertieren "5" → 5. Wenn das nicht funktioniert, weil es
        kein Integer ist, dann geben wir eine Fehlermeldung aus, und fordern den Spieler solange zu auf, eine Eingabe
        zu machen, bis es ein Integer ist oder bis man die Eingabe zu einem Integer konvertieren kann. """

    """ jetzt checken wir, ob die Eingabe zwischen 1 und 9 ist. Wenn das nicht der Fall ist, fordern wir den User
           wie immer dazu auf, solange eine Eingabe zu machen, bis die zwischen 1 und 9 ist. """

    if not made_another_valid_input:
        try:

            """ User Input verarbeiten """

            convert_user_input = int(user_input)
            # ist die Eingabe zwischen 1 und 9?

            if convert_user_input < 1 or convert_user_input > 9:
                # leider nicht
                print("Falsche Eingabe! Gebe bitte eine Zahl zwischen 1 und 9 ein!")
                # solange wiederholen, bis Eingabe korrekt ist
                while convert_user_input < 1 or convert_user_input > 9:
                    check_user_input = input("Position: ")
                    # versuchen, es in einen Integer zu konvertieren
                    if check_user_input == "Quit":
                        # wenn die Eingabe "Quit" ist, dann beenden wir das Spiel
                        quit()
                    try:
                        convert_user_input = int(check_user_input)
                        # ist die Eingabe zwischen 1 und 9?
                        if convert_user_input < 1 or convert_user_input > 9:
                            # Falsche Eingabe
                            print("Falsche Eingabe! Gebe bitte eine Zahl zwischen 1 und 9 ein!")
                        else:
                            # Es ist zwischen 1 und 9!
                            # wenn es alle Tests erfolgreich durchlaufen hat, dann kann es weiter gehen!
                            made_another_valid_input = False
                            break
                    except ValueError:
                        # Error Handling
                        print("Falsche Eingabe! Gebe bitte eine Zahl zwischen 1 und 9 ein!")

            """ Spielverarbeitung """

            # Spot wird überprüft, ob er noch frei ist

            if check_spot(convert_user_input):
                # Spot ist frei
                change_state(convert_user_input, 1)

                if check_for_wins() == "Spieler":
                    show_game(spots)
                    print("Spieler hat gewonnen!")
                    quit()

                elif check_for_wins() == "Computer":
                    show_game(spots)
                    print("Computer hat gewonnen!")
                    quit()

                elif istUntenschieden():
                    show_game(spots)
                    print("Unentschieden!")
                    quit()

                else:
                    change_state(Computer(), 2)
                    show_game(spots)
            else:
                # Spot ist nicht frei
                print("Spot schon besetzt, bitte einen Anderen wählen!")
                show_game(spots)

            """ Gewinn-Analyse """

            if check_for_wins() == "Spieler":
                print("Spieler hat gewonnen!")
                quit()
            if check_for_wins() == "Computer":
                print("Computer hat gewonnen!")
                quit()

        except ValueError:
            # Error Handling
            print("Falsche Eingabe! Gebe bitte eine Zahl zwischen 1 und 9 ein!")
