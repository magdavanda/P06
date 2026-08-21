

def main():
    print("=== Kaboom 1 ===")
    print("Using grimoire module directly")
    spell_name: str = "Fantasy"
    ingredients: str = "Eart, wind and fire"
    print(
            f"Testing record light spell:"
            f" {light_spell_record(spell_name, ingredients)}"
            )


if __name__ == "__main__":
    main()
