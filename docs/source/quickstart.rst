Quickstart
==========

Welcome to WitcherLib! This quickstart will show you how to install and use the library in just a few minutes.

Prerequisites
-------------

- Python 3.8 or higher
- A working internet connection
- (Optional) A virtual environment

Installation
------------

Install WitcherLib via pip (from TestPyPI):

.. code-block:: console

   $ pip install --index-url https://test.pypi.org/simple/ --no-deps witcherLib

For more detailed installation instructions and troubleshooting tips, see the :doc:`installation` page.

Basic Usage
-----------

After installing WitcherLib, you can immediately start using its functions to summon Witchers, brew potions, and hunt monsters.

Summoning a Witcher
^^^^^^^^^^^^^^^^^^^

Use the :py:func:`summon_witcher()` function to call upon a Witcher by name:

.. code-block:: python

   from witcher import summon_witcher

   message = summon_witcher("Geralt")
   print(message)
   # Output: Witcher Geralt has been summoned!

Getting a Random Witcher
^^^^^^^^^^^^^^^^^^^^^^^^

Retrieve a random Witcher from the School of the Wolf using :py:func:`get_random_witcher()`:

.. code-block:: python

   from witcher import get_random_witcher

   name = get_random_witcher()
   print(f"You summoned: {name}")

Brewing Potions
^^^^^^^^^^^^^^^

Brew known potions by providing the correct ingredients using :py:func:`brew_potion()`.
If any required ingredient is missing, a :py:exc:`PotionBrewingError` is raised:

.. code-block:: python

   from witcher import brew_potion, PotionBrewingError

   try:
       result = brew_potion("Swallow", ["celandine", "drowner brain"])
       print(result)
   except PotionBrewingError as e:
       print(f"Error: {e}")

Hunting Monsters
^^^^^^^^^^^^^^^^

To hunt a monster, use the :py:func:`hunt_monster()` function.
If the monster is unknown, a :py:exc:`MonsterNotFoundError` is raised:

.. code-block:: python

   from witcher import hunt_monster, MonsterNotFoundError

   try:
       result = hunt_monster("griffin")
       print(result)
   except MonsterNotFoundError as e:
       print(f"Error: {e}")

Where to Go Next
----------------

- Learn more about available functions and classes in the :doc:`api`
- Explore the :doc:`advanced_usage` guide for deeper integrations
- Read about the :doc:`witcher_universe` to immerse yourself in the Witcher lore

