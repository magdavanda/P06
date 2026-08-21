from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients: list[str] = light_spell_allowed_ingredients()
    ingredients = ingredients.lower()
    for item in allowed_ingredients:
        if item in ingredients:
            return ("VALID")
    return ("INVALID")
