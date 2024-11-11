import random

class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.health = 100
        self.inventory = []
        self.stats = self.set_stats(character_class)

    def set_stats(self, character_class):
        if character_class == "Warrior":
            return {"Strength": 10, "Agility": 5, "Magic": 2}
        elif character_class == "Mage":
            return {"Strength": 2, "Agility": 5, "Magic": 10}
        elif character_class == "Rogue":
            return {"Strength": 5, "Agility": 10, "Magic": 2}

    def attack(self):
        return random.randint(1, self.stats["Strength"])

    def defend(self):
        return random.randint(1, self.stats["Agility"])

    def use_item(self, item):
        if item in self.inventory:
            if item == "Health Potion":
                self.health += 20
                self.inventory.remove(item)
                print(f"{self.name} used a Health Potion. Health is now {self.health}.")
        else:
            print("Item not in inventory.")

class Enemy:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self):
        return random.randint(1, self.strength)

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
            else:
                print("That's not a valid command.")

            if enemy.health > 0:
                enemy_damage = enemy.attack()
                self.player.health -= enemy_damage
                print(f"{enemy.name} dealt {enemy_damage} damage to you. Your health is now {self.player.health}.")

        if self.player.health <= 0:
            print("You have been defeated!")
        else:
            print(f"You defeated {enemy.name}!")

    def explore_area(self):
        if self.current_area == "Haunted Forest":
            enemy = Enemy("Ghost", 30, 5)
            self.combat(enemy)
            self.player.inventory.append("Health Potion")
            print("You found a Health Potion!")
            self.current_area = "Enchanted Castle"
        elif self.current_area == "Enchanted Castle":
            print("You explore the castle and find a magical artifact!")
            self.player.inventory.append("Magic Wand")
            self.current_area = "Bandit's Lair"
        elif self.current_area == "Bandit's Lair":
            enemy = Enemy("Bandit", 40, 7)
            self.combat(enemy)
            print("You have completed your quest!")

    def start_game(self):
        print("Welcome to Quest for the Lost Relic!")
        self.create_character()
        while self.player.health > 0:
            print(f"You are in the {self.current_area}.")
            self.explore_area()
            if self.current_area == "Bandit's Lair":
                break

# Main execution
if __name__ == "__main__":
    game = Game()
    game.start_game()