from . import elements as alchemy_elements
import elements


def healing_potion() -> str:
    return (
            f"Healing potion brewed with "
            f"'{alchemy_elements.create_earth()}' "
            f"and '{alchemy_elements.create_air()}'"
            )


def strength_potion() -> str:
    return (
            f"Strength potion brewed with "
            f"'{elements.create_fire()}' "
            f"and '{elements.create_water()}'"
            )


print(healing_potion())
print(strength_potion())
