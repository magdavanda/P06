
def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    from alchemy.grimoire.dark_spellbook import dark_spell_record

    spell_name: str = "Dark magic"
    ingredients: str = "Bats and frogs"
    result: str = dark_spell_record(spell_name, ingredients)

    print(
            f"Testing record dark spell:"
            f" {result}"
            )


if __name__ == "__main__":
    main()

# try:
#     print("=== Kaboom 1 ===")
#     print("Access to alchemy/grimoire/dark_spellbook.py directly")
#     print("Test import now - THIS WILL RAISE AN EXCEPTION")
#     import alchemy.grimoire.dark_spellbook
#     spell_name: str = "Dark magic"
#     ingredients: str = "Bats and frogs"
#     result: str = alchemy.grimoire.dark_spellbook.dark_spell_record(
#             spell_name, ingredients)
#     print(
#             f"Testing record dark spell: "
#             f"{result}"
#             )
# except ImportError:
#     print("ImportError - circular import!")
