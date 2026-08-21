try:
    import alchemy.grimoire
except ImportError:
        print("hallo")
        


def main():
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    spell_name: str = "Dark magic"
    ingredients: str = "Bats and frogs"

    print(
            f"Testing record dark spell:"
            f" {alchemy.grimoire.dark_spell_record(spell_name, ingredients)}"
            )


if __name__ == "__main__":
    main()
