# ==========================================
# LEGENDS OF THE FORGOTTEN REALM
# File: player.py
# Purpose: Player creation and management
# ==========================================
class Player:
    CLASS_STATS = {
        "Warrior": {
            "hp": 180,
            "mana": 40,
            "attack": 25,
            "defense": 18,
            "crit_chance": 5,
            "crit_damage": 1.5
        }, 

         "Mage": {
            "hp": 120,
            "mana": 120,
            "attack": 30,
            "defense": 8,
            "crit_chance": 10,
            "crit_damage": 1.75
        },

        "Archer": {
            "hp": 140,
            "mana": 70,
            "attack": 22,
            "defense": 12,
            "crit_chance": 18,
            "crit_damage": 1.6
        },

        "Assassin": {
            "hp": 110,
            "mana": 60,
            "attack": 32,
            "defense": 7,
            "crit_chance": 25,
            "crit_damage": 1.8
        }
    }
    def __init__(self, name, character_class):

        self.name = name
        self.character_class = character_class

        stats = self.CLASS_STATS[character_class]

        self.level = 1
        self.experience = 0

        self.max_hp = stats["hp"]
        self.hp = self.max_hp

        self.max_mana = stats["mana"]
        self.mana = self.max_mana

        self.attack = stats["attack"]
        self.defense = stats["defense"]

        self.crit_chance = stats["crit_chance"]
        self.crit_damage = stats["crit_damage"]

        self.gold = 100

        self.inventory = []
        self.equipped_weapon = None
        self.equipped_armor = None
        self.potition = []

        self.enemies_defeated = 0
        self.bosses_defeated = 0

    def display_stats(self):
        print("\n" + "=" * 40)
        print("        PLAYER STATISTICS")
        print("=" * 40)
        print(f"Name          : {self.name}")
        print(f"Class         : {self.character_class}")
        print(f"Level         : {self.level}")
        print(f"Experience    : {self.experience}")

        print("-" * 40)

        print(f"Health        : {self.hp}/{self.max_hp}")
        print(f"Mana          : {self.mana}/{self.max_mana}")

        print("-" * 40)

        print(f"Attack        : {self.attack}")
        print(f"Defense       : {self.defense}")
        print(f"Critical      : {self.crit_chance}%")
        print(f"Crit Damage   : {self.crit_damage}x")

        print("-" * 40)

        print(f"Gold          : {self.gold}")
        print(f"Enemies Killed: {self.enemies_defeated}")
        print(f"Bosses Killed : {self.bosses_defeated}")

        print("=" * 40)