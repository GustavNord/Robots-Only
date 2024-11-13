import os
import time
import random

def clear_screen():
    """Clears the terminal screen when the player inputs something."""
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Mac/Linux/Unix

def type_effect(text, delay=0.05):
    """Simulates a typing effect, printing text letter by letter."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)  # Delay between each character
    print()  # Newline after the text is fully printed

bandit_art = "\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣶⣤⣀⣀⣤⣶⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⣾⣷⣶⣶⣶⣦⣤⠀⢤⣤⣈⣉⠙⠛⠛⠋⣉⣁⣤⡤⠀⣤⣴⣶⣶⣶⣾⣷⠀\n⠀⠈⠻⢿⣿⣿⣿⣿⣶⣤⣄⣉⣉⣉⣛⣛⣉⣉⣉⣠⣤⣶⣿⣿⣿⣿⡿⠟⠁⠀\n⠀⠀⠀⠀⠀⠉⠙⠛⠛⠿⠿⠿⢿⣿⣿⣿⣿⡿⠿⠿⠿⠛⠛⠋⠉⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⠦⠄⢀⣠⡀⠠⣄⡀⠠⠴⣾⡿⠀⠀⠀⠀⠀⣀⡀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠺⣷⣄⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣙⣛⣻⣿⣿⣿⡿⠃⠐⠿⠿⣾⣿⣷⡄⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
ghost_art = "⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣦⠀\n⠀⠀⠀⠀⣰⣿⡟⢻⣿⡟⢻⣧\n⠀⠀⠀⣰⣿⣿⣇⣸⣿⣇⣸⣿\n⠀⠀⣴⣿⣿⣿⣿⠟⢻⣿⣿⣿\n⣠⣾⣿⣿⣿⣿⣿⣤⣼⣿⣿⠇\n⢿⡿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠀\n⠀⠀⠈⠿⠿⠋⠙⢿⣿⡿⠁⠀\n"

#⠀ ⠀⠀⠀⠀⢀⣴⣿⣿⣿⣦⠀
# ⠀⠀⠀⠀⣰⣿⡟⢻⣿⡟⢻⣧
# ⠀⠀⠀⣰⣿⣿⣇⣸⣿⣇⣸⣿
# ⠀⠀⣴⣿⣿⣿⣿⠟⢻⣿⣿⣿
# ⣠⣾⣿⣿⣿⣿⣿⣤⣼⣿⣿⠇
# ⢿⡿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠀
# ⠀⠀⠈⠿⠿⠋⠙⢿⣿⡿⠁⠀


class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.health = 100
        self.stats = self.set_stats(character_class)
        self.level = 1
        self.xp = 0
        self.max_health = 100  # Max health for leveling up
        self.mana = 100  # For magic abilities like Fireball or Warrior's Charge

    def set_stats(self, character_class):
        if character_class == "Warrior":
            return {"Strength": 20, "Agility": 5, "Magic": 10, "Defense": 6}  # Increased strength and defense
        elif character_class == "Mage":
            return {"Strength": 2, "Agility": 5, "Magic": 10, "Defense": 1}
        elif character_class == "Rogue":
            return {"Strength": 5, "Agility": 10, "Magic": 2, "Defense": 3}

    def attack(self):
        damage = random.randint(1, self.stats["Strength"])
        if random.random() < 0.5:  # 50% chance for a critical hit
            damage *= 2
        return damage

    def defend(self):
        return random.randint(1, self.stats["Agility"])

    def level_up(self):
        self.level += 1
        self.stats["Strength"] += 2
        self.stats["Agility"] += 2
        self.stats["Magic"] += 1
        self.max_health += 20
        self.health = self.max_health
        type_effect(f"\n{self.name} leveled up! They are now level {self.level}.")
        time.sleep(2)  # Pause for 2 seconds after leveling up

    def add_xp(self, xp):
        self.xp += xp
        type_effect(f"\n{self.name} gained {xp} XP! Total XP: {self.xp}")
        time.sleep(1)  # Pause for 1 second after XP gain
        if self.xp >= 30 + (self.level - 1) * 30:  # Level up threshold: 30 XP per level, increases as level increases
            self.xp = 0  # Reset XP for next level
            self.level_up()

    def warrior_charge(self, enemy):
        """Warrior's powerful charge attack."""
        if self.mana >= 5:  # Charge costs 5 mana
            self.mana -= 5
            charge_damage = random.randint(10, self.stats["Strength"] * 2)
            enemy.health -= charge_damage
            type_effect(f"{self.name} used Warrior's Charge! Dealt {charge_damage} damage to {enemy.name}.")
        else:
            type_effect("Not enough mana for Warrior's Charge!")
        time.sleep(1)  # Pause for 1 second after charge

    def health_bar(self):
        """Returns health as a bar using hashtags."""
        max_health = self.max_health
        num_hashes = int(self.health / max_health * 10)  # Calculate relative to max health
        health_display = "#" * num_hashes  # Create a string of hashes
        return f"[{health_display:<10}] {self.health}/{max_health} HP"  # Return health bar with full/max health

class Enemy:
    def __init__(self, name, xp_reward):
        self.name = name
        self.health = 20  # All enemies now have 20 health
        self.strength = 5
        self.xp_reward = xp_reward

    def attack(self):
        return random.randint(1, self.strength)

    def health_bar(self):
        """Returns health as a bar using hashtags for the enemy."""
        num_hashes = self.health // 10  # Calculate how many hashes should be displayed
        health_display = "#" * num_hashes  # Create a string of hashes
        return f"[{health_display:<10}] {self.health} HP"  # Return health bar with health value

class Game:
    def __init__(self):
        self.player = None
        self.current_area = "Haunted Forest"
        self.enemy_count = 0  # Track how many enemies the player has defeated
        self.waited_once = False  # Track if the player has waited once
        self.waited_twice = False  # Track if the player has waited twice

    def create_character(self):
        type_effect("\nPlease enter your character's name.")
        name = input("Character name: ")
        type_effect("\nChoose a class:\n1. Warrior\n2. Mage\n3. Rogue")
        class_choice = input("Enter the number of your choice: ")
        
        if class_choice == "1":
            character_class = "Warrior"
        elif class_choice == "2":
            character_class = "Mage"
        elif class_choice == "3":
            character_class = "Rogue"
        else:
            type_effect("\nInvalid choice, defaulting to Warrior.")
            character_class = "Warrior"

        self.player = Character(name, character_class)
        clear_screen()  # Clear screen after character creation
        type_effect(f"\n{self.player.name} the {self.player.character_class} has been created!\n")
        time.sleep(2)  # Pause for 2 seconds after character creation

    def combat(self, enemy):
        
        time.sleep(1)  # Pause after enemy appears
        clear_screen() 
        if enemy.name == "Bandit":
            type_effect("\nThe Bandit appears in front of you!")
            time.sleep(1)  # Pause for a bit before printing the ASCII art
            print(bandit_art)  # Print the ASCII art of the Bandit
            time.sleep(2)  # Pause for 2 seconds to allow the art to be displayed
        else:
            type_effect("\nThe Ghost appears in front of you!")
            time.sleep(1)  # Pause for a bit before printing the ASCII art
            print(ghost_art)  # Print the ASCII art of the Bandit
            time.sleep(2)  # Pause for 2 seconds to allow the art to be displayed

        while self.player.health > 0 and enemy.health > 0:
            clear_screen()  # Clear screen after each player action
            # Display health bars immediately without word-by-word typing effect
            print(f"\n{self.player.name:<20}{self.player.health_bar()}{' ' * 10}{enemy.name:<20}{enemy.health_bar()}")
            time.sleep(1)  # Pause before showing the action options

            type_effect("\nChoose an action:")
            type_effect("1. Attack")
            type_effect("2. Defend")
            if self.player.character_class == "Mage" and self.player.stats["Magic"] >= 5:
                type_effect("4. Cast Fireball")
            if self.player.character_class == "Warrior" and self.player.mana >= 5:
                type_effect("5. Warrior's Charge")

            action = input("Choose your action (1-5): ")
            clear_screen()  # Clear screen after player action input

            if action == "1":
                damage = self.player.attack()
                enemy.health -= damage
                type_effect(f"\n{self.player.name} attacked {enemy.name} for {damage} damage.")
                time.sleep(1)  # Pause after attack
            elif action == "2":
                defense = self.player.defend()
                type_effect(f"\n{self.player.name} defended, reducing damage by {defense}.")
                time.sleep(1)  # Pause after defense
            
            elif action == "4" and self.player.character_class == "Mage" and self.player.stats["Magic"] >= 5:
                # Mage-specific action
                self.player.stats["Magic"] -= 5
                type_effect(f"\n{self.player.name} cast Fireball!")
                time.sleep(1)  # Pause after fireball
            elif action == "5" and self.player.character_class == "Warrior" and self.player.mana >= 5:
                # Warrior-specific action
                self.player.warrior_charge(enemy)
            else:
                type_effect("\nInvalid action, try again.")
                time.sleep(1)  # Pause after invalid action
                continue

            if enemy.health > 0:
                # Enemy attacks
                damage = enemy.attack()
                self.player.health -= damage
                type_effect(f"\n{enemy.name} attacks {self.player.name} for {damage} damage.")
                time.sleep(1)  # Pause after enemy attack

            if self.player.health <= 0:
                type_effect("\nYou have been defeated!")
                break
            elif enemy.health <= 0:
                type_effect(f"\n{enemy.name} has been defeated!")
                self.player.add_xp(enemy.xp_reward)
                time.sleep(1)  # Pause after enemy defeat

    def crossroads(self):
        """Crossroads event that occurs after two enemies are defeated."""
        clear_screen()
        type_effect("\nAfter defeating both enemies, you come across two doors.")
        time.sleep(1)
        clear_screen()
        type_effect("There are two doors ahead of you.")
        type_effect("1. Enter the left door.")
        type_effect("2. Enter the right door.")
        type_effect("3. Wait for 5 seconds\n")
        
        choice = input("Choose your action (1, 2, or 3): ")
        
        if choice == "1":
            type_effect("\nYou enter the left door and find freedom!")
            time.sleep(1)  # Pause after freedom
            self.enemy_count = 0  # Reset enemy count for next level
        elif choice == "2":
            type_effect("\nYou enter the door to the right and fall into a trap!")
            time.sleep(1)  # Pause before death message
            type_effect("\nLevel Failed! You died!")
            self.player.health = 0  # Player dies
        elif choice == "3":
            if self.waited_once:  # If they've already waited once
                type_effect("\nA clock from the wall jumps out and hits you on the head!")
                time.sleep(1)  # Pause before death message
                type_effect("\nLevel Failed! You died!")
                self.player.health = 0  # Player dies
            else:
                type_effect("\nYou decide to wait for a moment... The house suddenly rumbles and shakes.")
                time.sleep(5)  # Wait for 5 seconds
                type_effect("\nYou can choose again.")
                self.waited_once = True  # Mark the player as having waited once
                self.crossroads()  # Retry the door selection after the wait
        else:
            type_effect("\nInvalid choice. Please choose 1, 2, or 3.")
            self.crossroads()  # Recursively ask for a valid input

    def start_game(self):
        clear_screen()  # Clear the screen at the start of the game
        type_effect("╔══════════════════════════════════════╗\n  Welcome to Quest for the Lost Relic!\n╚══════════════════════════════════════╝")
        time.sleep(1)  # Pause after intro
        self.create_character()
        type_effect("\nThe adventure begins...")
        time.sleep(1)  # Pause after adventure start

        # Haunted Forest
        type_effect("\nYou are in the Haunted Forest.")
        self.combat(Enemy("Bandit", 20))  # First enemy in the forest

        # Haunted House
        type_effect("\nYou enter the Haunted House.")
        self.combat(Enemy("Ghost", 20))  # Second enemy in the house

        # Crossroads
        self.crossroads()  # After defeating both enemies, crossroads appear

# Start the game
if __name__ == "__main__":
    game = Game()
    game.start_game()