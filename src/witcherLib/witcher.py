"""witcher.py

A fictional Python library for interacting with the Witcher universe.
Provides tools to summon Witchers, brew potions, and hunt monsters.
"""

import random


class PotionBrewingError(Exception):
    """Raised when a potion cannot be brewed due to missing ingredients."""
    pass


class MonsterNotFoundError(Exception):
    """Raised when a requested monster is not found in the bestiary."""
    pass


def summon_witcher(name: str) -> str:
    """Summon a Witcher by name.

    Args:
        name (str): The name of the Witcher to summon.

    Returns:
        str: A confirmation message.

    Example:
        >>> summon_witcher("Geralt")
        'Witcher Geralt has been summoned!'
    """
    return f"Witcher {name} has been summoned!"


def brew_potion(potion_name: str, ingredients: list[str]) -> str:
    """Brew a potion using given ingredients.

    Args:
        potion_name (str): Name of the potion to brew.
        ingredients (list of str): List of ingredients to use.

    Returns:
        str: Success message with potion name.

    Raises:
        PotionBrewingError: If required ingredients are missing.

    Example:
        >>> brew_potion("Swallow", ["celandine", "drowner brain"])
        'Potion Swallow brewed successfully!'
    """
    required = {"Swallow": ["celandine", "drowner brain"],
                "Thunderbolt": ["ghoul blood", "crow's eye"]}

    if potion_name not in required or not all(i in ingredients for i in required[potion_name]):
        raise PotionBrewingError(f"Missing ingredients for {potion_name}.")
    return f"Potion {potion_name} brewed successfully!"


def hunt_monster(monster: str) -> str:
    """Hunt a monster by name.

    Args:
        monster (str): Name of the monster.

    Returns:
        str: Result of the hunt.

    Raises:
        MonsterNotFoundError: If the monster is unknown.

    Example:
        >>> hunt_monster("griffin")
        'The griffin has been hunted successfully!'
    """
    known_monsters = ["griffin", "leshen", "wraith", "nekker"]
    if monster not in known_monsters:
        raise MonsterNotFoundError(f"Unknown monster: {monster}")
    return f"The {monster} has been hunted successfully!"


def get_random_witcher() -> str:
    """Retrieve a random Witcher from the School of the Wolf.

    Returns:
        str: Name of the Witcher.

    Example:
        >>> get_random_witcher()
        'Lambert'
    """
    return random.choice(["Geralt", "Vesemir", "Eskel", "Lambert"])
