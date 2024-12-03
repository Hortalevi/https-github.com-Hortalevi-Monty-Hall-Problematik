#Monty-Hall-Problematik-Gui
 #Author: Levi Horta
 #Version: 1.5
 #License: MIT
 #@copyright 2024 Levi Horta
 #Quellen; Chatgpt was used for debugging and the GUI-Manual. 
import random
import tkinter as tk
from tkinter import messagebox

# Global variables for the images
door_image = None
door_opened_image = None
car_image = None
goat_image = None

# Function to simulate a single round of the Monty Hall game
def play_round(switch_player, manual_choice=None):
    doors = [0, 0, 1]  # 0 for goat, 1 for car
    random.shuffle(doors)

    # Player makes a choice (manual or random)
    if manual_choice is not None:
        player_choice = manual_choice - 1
    else:
        player_choice = random.randint(0, 2)

    # Monty reveals a door with a goat
    monty_choice = next(i for i in range(3) if i != player_choice and doors[i] == 0)

    # If the player chooses to switch, change their choice
    if switch_player:
        player_choice = next(i for i in range(3) if i != player_choice and i != monty_choice)

    # Return True if the player's final choice is the car
    return doors[player_choice] == 1

def main_menu_gui(menu_window):
    for widget in menu_window.winfo_children():
        widget.destroy()

    # Function to start the simulation
    def start_simulation():
        try:
            rounds = int(rounds_entry.get())  # Get the number of rounds from input
            simulate_monty_hall_gui(rounds)
        except ValueError:
            messagebox.showerror("Ungültige Eingabe“, “Bitte geben Sie eine gültige Anzahl von Runden ein.")

    # Function to start the game
    def start_game():
        play_game_gui(menu_window)

    # Create buttons and input fields for the main menu
    play_button = tk.Button(menu_window, text="Spiel spielen", width=20, height=2, command=start_game)
    play_button.grid(row=0, column=0, padx=20, pady=20)

    simulation_label = tk.Label(menu_window, text="Geben Sie die Anzahl der Runden für die Simulation ein:")
    simulation_label.grid(row=1, columnspan=2)

    rounds_entry = tk.Entry(menu_window, width=5)
    rounds_entry.grid(row=2, column=0)

    simulation_button = tk.Button(menu_window, text="Simulation starten", width=20, height=2, command=start_simulation)
    simulation_button.grid(row=2, column=1, padx=20)

# Function to play the Monty Hall game in the GUI
def play_game_gui(menu_window):
    # Display the Monty Hall game interface.
    
    for widget in menu_window.winfo_children():
        widget.destroy()

    doors = [0, 0, 1]  # 0 for goat, 1 for car
    random.shuffle(doors)

    player_choice = None
    monty_choice = None

    # Function to handle when a door is clicked
    def on_door_click(door_number):
        nonlocal player_choice, monty_choice
        player_choice = door_number - 1

        # Disable all doors and highlight the player's choice
        for i in range(3):
            buttons[i].config(state="disabled")
        buttons[player_choice].config(bg="orange", image=door_image, compound="center")

        # Monty opens a door with a goat
        monty_choice = next(i for i in range(3) if i != player_choice and doors[i] == 0)
        buttons[monty_choice].config(bg="red", image=door_opened_image, compound="center")

        # Update the instructions and enable switch/stay buttons
        result_label.config(text=f"Monty öffnet Tür {monty_choice + 1} und enthüllt eine Ziege!")
        switch_button.config(state="normal")
        stay_button.config(state="normal")

    # Function to handle the "Switch Door" option
    def on_switch():
        nonlocal player_choice
        player_choice = next(i for i in range(3) if i != player_choice and i != monty_choice)
        result()

    # Function to handle the "Stay with Door" option
    def on_stay():
        result()

    # Function to display the result
    def result():
        nonlocal player_choice

        # Find the winning door
        winning_door = doors.index(1)

        # Highlight the winning door with green (only the car door)
        buttons[winning_door].config(bg="green", image=door_opened_image, compound="center")  # Highlight the winning door

        # Check if the player wins
        if player_choice == winning_door:
            result_label.config(text="Herzlichen Glückwunsch! Sie haben das Auto gewonnen!")
            result_image.config(image=car_image)
        else:
            result_label.config(text="Entschuldigung! Du hast eine Ziege gewonnen!")
            result_image.config(image=goat_image)

        # Disable all buttons after the result
        switch_button.config(state="disabled")
        stay_button.config(state="disabled")

        # Show return button
        return_button.grid(row=3, column=1)

    # Function to return to the main menu
    def return_to_menu():
        main_menu_gui(menu_window)

    # Create door buttons
    buttons = []
    for i in range(3):
        button = tk.Button(menu_window, text=f"Tür {i + 1}", width=133, height=200, command=lambda i=i: on_door_click(i + 1), compound="center")
        button.grid(row=0, column=i)
        button.config(image=door_image)  # Set the initial image for the door button
        buttons.append(button)

    # Create labels and action buttons
    result_label = tk.Label(menu_window, text="Wähle eine Tür, um das Spiel zu beginnen!", font=("Arial", 14))
    result_label.grid(row=1, columnspan=3)

    result_image = tk.Label(menu_window)
    result_image.grid(row=2, columnspan=3)

    switch_button = tk.Button(menu_window, text="Tür wechseln", width=20, height=2, state="disabled", command=on_switch)
    switch_button.grid(row=2, column=0)

    stay_button = tk.Button(menu_window, text="Tür behalten", width=20, height=2, state="disabled", command=on_stay)
    stay_button.grid(row=2, column=2)

    return_button = tk.Button(menu_window, text="Zurück zum Menü", width=20, height=2, command=return_to_menu)
    return_button.grid(row=3, column=1)
    return_button.grid_remove()

    # Add a legend explaining the colors used in the game
    legend_label = tk.Label(menu_window, text="Legend:", font=("Arial", 12, "bold"))
    legend_label.grid(row=4, column=0, columnspan=3, pady=10)

    legend_info = tk.Label(menu_window, text="Orange: Deine gewählte Tür\nRot: Monty öffnet Tür (Ziege)\nGrün: Die letzte Tür, die gewählt wurde",
                           font=("Arial", 10), justify="left")
    legend_info.grid(row=5, column=0, columnspan=3, pady=5)

# Function to simulate multiple rounds of the Monty Hall game
def simulate_monty_hall_gui(rounds):
    wins_without_switch = 0
    wins_with_switch = 0

    for _ in range(rounds):
        if play_round(switch_player=False):
            wins_without_switch += 1
        if play_round(switch_player=True):
            wins_with_switch += 1

    percentage_without_switch = (wins_without_switch / rounds) * 100
    percentage_with_switch = (wins_with_switch / rounds) * 100

    # Show results in a popup
    messagebox.showinfo(
        "Ergebnisse der Simulation",
        f"Ergebnisse nach {rounds} Runden:\n"
        f"Prozentsatz der Siege ohne Wechsel: {percentage_without_switch:.2f}%\n"
        f"Prozentualer Anteil der Siege mit Wechsel: {percentage_with_switch:.2f}%"
    )

# Initialize the main application window
menu_window = tk.Tk()
menu_window.title("Monty Hall Spiel")

# Load the door images globally before creating the GUI
try:
    door_image = tk.PhotoImage(file="door.png")  # Ensure this file exists and is correct
    door_opened_image = tk.PhotoImage(file="door_opened.png")  # Same for this image
    car_image = tk.PhotoImage(file="car.png")  # Load car image
    goat_image = tk.PhotoImage(file="goat.png")  # Load goat image
except Exception as e:
    messagebox.showerror("Image Load Error", f"Error loading image files: {e}")
    menu_window.quit()

# Start the main menu
main_menu_gui(menu_window)

menu_window.mainloop()








