from .elements import create_air, create_earth
from elements import create_fire, create_water


def healing_potion() -> str:
    return (
            f"Healing potion brewed with "
            f"'{create_earth()}' "
            f"and '{create_air()}'"
            )


def strength_potion() -> str:
    return (
            f"Strength potion brewed with "
            f"'{create_fire()}' "
            f"and '{create_water()}'"
            )


def main() -> None:
    print(healing_potion())
    print(strength_potion())


if __name__ == "__main__":
    main()
