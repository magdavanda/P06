from . import elements as alchemy_elements
import elements


def healing_potion() -> str:
    return f"Healing potion brewed with '{alchemy_elements.create_earth()}' and '{alchemy_elements.create_air()}'"

def strength_potion() -> str:
    return f"Strength potion brewed with '{elements.create_fire()}' and '{elements.create_water()}'"

print(healing_potion())
print(strength_potion())

print(strength_potion())testetse

