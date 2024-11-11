import random

class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.health = 100
        self.inventory = []
        self.stats = self.set_stats(character_class)
        self.level = 1
        self.xp = 0
        self.max_health = 100  # Max health for leveling up
        self.mana = 10  # For magic abilities like Fireball or Warrior's Charge
        self.companion = None  # The companion starts as None

    def set_stats(self, character_class):
        if character_class == "Warrior":
            return {"Strength": 15, "Agility": 5, "Magic": 2, "Defense": 6}  # Increased strength and defense
        elif character_class == "Mage":
            return {"Strength": 2, "Agility": 5, "Magic": 10, "Defense": 1}
        elif character_class == "Rogue":
            return {"Strength": 5, "Agility": 10, "Magic": 2, "Defense": 3}

    def attack(self):
        damage = random.randint(1, self.stats["Strength"])
        # Add chance for a critical hit
        if random.random() < 0.1:  # 10% chance for a critical hit
            damage *= 2
            print("Critical Hit!")
        return damage

    def defend(self):
        return random.randint(1, self.stats["Agility"])

    def use_item(self, item):
        if item in self.inventory:
            if item == "Health Potion":
                self.health += 20
                self.inventory.remove(item)
                print(f"{self.name} used a Health Potion. Health is now {self.health}.")
            elif item == "Magic Wand":
                self.stats["Magic"] += 5
                self.inventory.remove(item)
                print(f"{self.name} used the Magic Wand. Magic power increased!")
        else:
            print("Item not in inventory.")

    def level_up(self):
        self.level += 1
        self.stats["Strength"] += 2
        self.stats["Agility"] += 2
        self.stats["Magic"] += 1
        self.max_health += 20
        self.health = self.max_health
        print(f"{self.name} leveled up! They are now level {self.level}.")

    def add_xp(self, xp):
        self.xp += xp
        print(f"{self.name} gained {xp} XP! Total XP: {self.xp}")
        if self.xp >= self.level * 50:  # Level up threshold: 50 XP per level
            self.xp = 0  # Reset XP for next level
            self.level_up()

    def warrior_charge(self, enemy):
        """Warrior's powerful charge attack."""
        if self.mana >= 5:  # Charge costs 5 mana
            self.mana -= 5
            charge_damage = random.randint(10, self.stats["Strength"] * 2)
            enemy.health -= charge_damage
            print(f"{self.name} used Warrior's Charge! Dealt {charge_damage} damage to {enemy.name}.")
        else:
            print("Not enough mana for Warrior's Charge!")

    def add_companion(self, companion):
        """Adds a companion to the player."""
        self.companion = companion
        print(f"{self.name} has gained a companion, {self.companion.name}!")

    def heal(self):
        """Heals the player with the companion's ability."""
        if self.companion:
            healing_amount = self.companion.heal()
            self.health += healing_amount
            self.health = min(self.health, self.max_health)  # Prevent health from going over max
            print(f"{self.companion.name} healed {self.name} for {healing_amount} health!")

class Companion:
    def __init__(self, name):
        self.name = name
        self.health = 50  # A companion has their own health
        self.healing_power = 15  # How much the companion can heal each time
        self.heal_count = 3  # The number of times the companion can heal

    def heal(self):
        if self.heal_count > 0:
            self.heal_count -= 1
            print(f"{self.name} heals you for {self.healing_power} health.")
            return self.healing_power
        else:
            print(f"{self.name} is out of healing power!")
            return 0  # No healing left

    def attack(self):
        """Companion can also attack if needed (optional)."""
        damage = random.randint(1, 5)  # Companions aren't as strong as the player
        return damage

class Enemy:
    def __init__(self, name, health, strength, xp_reward):
        self.name = name
        self.health = health
        self.strength = strength
        self.xp_reward = xp_reward

    def attack(self):
        return random.randint(1, self.strength)

    def drop_loot(self):
        return random.choice(["Gold", "Health Potion", "Magic Wand", "Sword"])

class Game:
    def __init__(self):
        self.player = None
        self.current_area = "Haunted Forest"

    def create_character(self):
        name = input("Enter your character's name: ")
        print("Choose a class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Rogue")
        class_choice = input("Enter the number of your choice: ")
        
        if class_choice == "1":
            character_class = "Warrior"
        elif class_choice == "2":
            character_class = "Mage"
        elif class_choice == "3":
            character_class = "Rogue"
        else:
            print("Invalid choice, defaulting to Warrior.")
            character_class = "Warrior"

        self.player = Character(name, character_class)
        print(f"{self.player.name} the {self.player.character_class} has been created!")

    def combat(self, enemy):
        print(f"A wild {enemy.name} appears!")
        while self.player.health > 0 and enemy.health > 0:
            print("Choose an action:")
            print("1. Attack")
            print("2. Defend")
            print("3. Use Item")
            if self.player.character_class == "Mage" and self.player.stats["Magic"] >= 5:
                print("4. Cast Fireball")
            if self.player.character_class == "Warrior" and self.player.mana >= 5:
                print("5. Warrior's Charge")
            if self.player.companion:
                print("6. Heal with Companion")

            action = input("Enter the number of your choice: ")

            if action == "1":
                damage = self.player.attack()
                enemy.health -= damage
                print(f"You dealt {damage} damage to {enemy.name}.")
            elif action == "2":
                defense = self.player.defend()
                print(f"You defended with {defense} agility.")
            elif action == "3":
                item = input("Which item do you want to use? ")
                self.player.use_item(item)
            elif action == "4" and self.player.character_class == "Mage" and self.player.stats["Magic"] >= 5:
                self.cast_fireball(enemy)
            elif action == "5" and self.player.character_class == "Warrior" and self.player.mana >= 5:
                self.player.warrior_charge(enemy)
            elif action == "6" and self.player.companion:
                self.player.heal()
            else:
                print("That's not a valid command.")

            if enemy.health > 0:
                enemy_damage = enemy.attack()
                # Consider defense value for reducing incoming damage
                defense = self.player.defend()
                total_damage = max(0, enemy_damage - defense)
                self.player.health -= total_damage
                print(f"{enemy.name} dealt {total_damage} damage to you. Your health is now {self.player.health}.")
            else:
                print(f"{enemy.name} has been defeated!")
                self.player.add_xp(enemy.xp_reward)
                loot = enemy.drop_loot()
                print(f"You found a {loot}!")

        if self.player.health <= 0:
            print("You have been defeated!")
        else:
            print(f"You defeated {enemy.name}!")

    def cast_fireball(self, enemy):
        """Mage specific attack."""
        print("Casting Fireball...")
        if random.random() < 0.8:  # 80% chance to hit
            damage = random.randint(10, self.player.stats["Magic"])
            enemy.health -= damage
            print(f"Fireball hit! You dealt {damage} fire damage to {enemy.name}.")
        else:
            print("The Fireball missed!")

    def explore_area(self):
        if self.current_area == "Haunted Forest":
            print("You venture deeper into the Haunted Forest...")
            # Additional events in the Haunted Forest after Ghost battle
            enemy = Enemy("Ghost", 30, 5, 20)
            self.combat(enemy)
            self.player.inventory.append("Health Potion")
            print("You found a Health Potion!")
            companion = Companion("Luna the Healer")  # Example companion
            self.player.add_companion(companion)
            self.current_area = "Haunted House"
        elif self.current_area == "Haunted House":
            print("You enter the Haunted House. It's eerily quiet...")
            # Add an enemy encounter or event in the haunted house
            enemy = Enemy("Haunted Spirit", 40, 7, 30)
            self.combat(enemy)
            print("You found a Magic Wand in the Haunted House!")
            self.current_area = "Enchanted Castle"
        elif self.current_area == "Enchanted Castle":
            print("You explore the castle and find a magical artifact!")
            self.player.inventory.append("Magic Wand")
            self.current_area = "Bandit's Lair"
        elif self.current_area == "Bandit's Lair":
            enemy = Enemy("Bandit", 40, 7, 30)
            self.combat(enemy)
            print("You have completed your quest!")

    def start_game(self):
        print("Welcome to Quest for the Lost Relic!")
        self.create_character()
        while self.player.health > 0:
            print(f"You are in the {self.current_area}.")
            self.explore_area()
            if self.current_area == "Bandit's Lair":
                break  # End the game after the final area
