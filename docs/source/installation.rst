Installation and Usage
======================

.. _installation:

Installation
------------

To use WitcherLib, first install it using pip (once it's published):

.. code-block:: console

   (.venv) $ pip install witcherlib

You can also install it locally from source:

.. code-block:: console

   (.venv) $ pip install -e .

Usage
-----

After installation, you can import the library and use its functions.

Summoning Witchers
------------------

Use the :py:func:`witcher.summon_witcher` function to summon a Witcher by name:

.. autofunction:: witcher.summon_witcher

Brewing Potions
---------------

Use :py:func:`witcher.brew_potion` to brew potions like Swallow or Thunderbolt.
This function checks for the required ingredients:

.. autofunction:: witcher.brew_potion

If required ingredients are missing, it raises:

.. autoexception:: witcher.PotionBrewingError

Monster Hunting
---------------

Use :py:func:`witcher.hunt_monster` to simulate a monster hunt:

.. autofunction:: witcher.hunt_monster

If the monster is unknown:

.. autoexception:: witcher.MonsterNotFoundError

Random Witcher
--------------

To summon a random Witcher from the School of the Wolf:

.. autofunction:: witcher.get_random_witcher
