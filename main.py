
# ==========================================
# LEGENDS OF THE FORGOTTEN REALM
# File: main.py
# Purpose: Main menu and character creation
# ==========================================

from player import Player


def display_title():

    print("=" * 50)
    print("       LEGENDS OF THE FORGOTTEN REALM")
    print("=" * 50)

    print("The kingdom of Eldoria awaits its hero!")
    print()


# Character creation
def create_character():

    print("\n========== CHARACTER CREATION ==========")

    # Get player name
    while True:

        name = input("\nEnter your character name: ").strip()

        if name:
            break

        print("Name cannot be empty. Try again.")

    # Display available classes
    print("\nChoose Your Class")

    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Assassin")

    classes = {
        "1": "Warrior",
        "2": "Mage",
        "3": "Archer",
        "4": "Assassin"
    }

    # Get valid class selection
    while True:

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice in classes:
            character_class = classes[choice]
            break

        print("Invalid choice! Please select between 1 and 4.")

    # Create Player object
    player = Player(name, character_class)

    print("\nCharacter created successfully!")
    print(f"Welcome to Eldoria, {player.name}!")

    # Display player statistics
    player.display_stats()

    return player


# Main application
def main():

    display_title()

    while True:

        print("\n========== MAIN MENU ==========")

        print("1. New Game")
        print("2. Continue")
        print("3. Instructions")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            player = create_character()

            print("\nYour adventure is about to begin!")

        elif choice == "2":

            print("\nSave/load functionality is coming soon!")

        elif choice == "3":

            print("\n========== INSTRUCTIONS ==========")

            print("1. Create your character.")
            print("2. Choose your character class.")
            print("3. Fight enemies and collect rewards.")
            print("4. Level up and defeat powerful bosses.")
            print("5. Defeat the Ancient Demon King.")

        elif choice == "4":

            print("\nThank you for playing!")
            print("See you again, hero of Eldoria!")

            break

        else:

            print("\nInvalid option! Please choose 1-4.")


# Application entry point
if __name__ == "__main__":
    main()
