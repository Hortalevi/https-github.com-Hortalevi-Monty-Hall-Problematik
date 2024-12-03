#Monty-Hall-Problematik
 #Author: Levi Horta
 #Version: 1.5
 #License: MIT
 #@copyright 2024 Levi Horta
 #Quellen; Chatgpt was used for debugging and the Cheat-Sheet. 
import random

# Function for a single round of the Monty Hall problem
def play_round(switch_player, manual_choice=None, verbose=True):
    doors = [0, 0, 1]  
    random.shuffle(doors)  # Randomize the car's position

    # Player selects a door
    if manual_choice is not None:
        player_choice = manual_choice - 1  # Convert to 0-based index
        if verbose:
            print(f"Der Spieler wählt Tür {player_choice + 1}.")
    else:
        player_choice = random.randint(0, 2)  # Random choice
        if verbose:
            print(f"Der Spieler wählt Tür {player_choice + 1}.")

    # Monty reveals a door with a goat
    monty_choice = next(i for i in range(3) if i != player_choice and doors[i] == 0)
    if verbose:
        print(f"Monty öffnet die Tür {monty_choice + 1} und bringt eine Ziege raus !")

    # Player decides whether to switch
    if switch_player:
        player_choice = next(i for i in range(3) if i != player_choice and i != monty_choice)
        if verbose:
            print(f"Der Spieler wechselt zu Tür {player_choice + 1}.")

    # Check if the player wins
    won = doors[player_choice] == 1
    if verbose:
        if won:
            print("Herzlichen Glückwunsch! Der Spieler gewinnt das Auto!")
        else:
            print("Diesmal nur eine Ziege. Mehr Glück beim nächsten Mal!")
    return won

# Function to simulate the Monty Hall problem
def simulate_monty_hall(rounds):
    wins_without_switch = 0
    wins_with_switch = 0

    for _ in range(rounds):
        if play_round(switch_player=False, verbose=False):  # Player keeps initial choice
            wins_without_switch += 1
        if play_round(switch_player=True, verbose=False):  # Player switches choice
            wins_with_switch += 1

    print(f"\nErgebnisse nach {rounds} Runden:")
    print(f"Gewinnt ohne zu wechseln: {wins_without_switch} ({(wins_without_switch / rounds) * 100:.2f}%)")
    print(f"Gewinnt mit dem Wechsel: {wins_with_switch} ({(wins_with_switch / rounds) * 100:.2f}%)")

# Function for a single interactive game
def play_game():
    doors = [0, 0, 1]
    random.shuffle(doors)

    try:
        player_choice = int(input("Wählen Sie eine Tür (1, 2 oder 3): ")) - 1
        if player_choice not in [0, 1, 2]:
            print("Ungültige Eingabe. Bitte wählen Sie eine Tür zwischen 1 und 3.")
            return
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
        return

    monty_choice = next(i for i in range(3) if i != player_choice and doors[i] == 0)
    print(f"Monty öffnet die Tür {monty_choice + 1} und bringt eine Ziege raus !")

    # Using match-case to handle the switch decision
    match input("Möchten Sie die Tür wechseln (ja/nein)? ").strip().lower():
        case "ja":
            player_choice = next(i for i in range(3) if i != player_choice and i != monty_choice)
        case "nein":
            new_func()
        case _:
            print("Ungültige Eingabe. Bitte wählen Sie 'ja' oder 'nein'.")
            return

    if doors[player_choice] == 1:
        print("Herzlichen Glückwunsch! Der Spieler gewinnt das Auto!")
    else:
        print("Diesmal nur eine Ziege. Mehr Glück beim nächsten Mal")

def new_func():
    pass

# Main menu for the game using match-case
def main_menu():
    print("Willkommen beim Monty-Hall-Spiel!")
    print("1: Simulation ausführen")
    print("2: Spiel spielen")

    match input("Bitte wählen Sie eine Option (1 oder 2): ").strip():
        case "1":
            try:
                rounds = int(input("Wie viele Runden möchten Sie simulieren? "))
                simulate_monty_hall(rounds)
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl für die Runden ein.")
        case "2":
            play_game()
        case _:
            print("Ungültige Auswahl. Bitte wählen Sie 1 oder 2.")

# Start the program
main_menu()




















   

