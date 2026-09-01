import alchemy.grimoire

print("=== Kaboom 0 ===")
print("Using grimoire module directly")
spell_name: str = "Fantasy"
ingredients: str = "Earth, wind and fire"
print(
        f"Testing record light spell:"
        f" {alchemy.grimoire.light_spell_record(spell_name, ingredients)}"
    )
