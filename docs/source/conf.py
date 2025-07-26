import sys
from pathlib import Path


# -- Path setup ------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'WitcherLib'
copyright = '2025, 22skowron'
author = '22skowron'
release = '0.0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    # 'sphinx.ext.viewcode',
    # 'sphinx.ext.autosummary',
]

# autosummary_generate = True
napoleon_google_docstring = True
napoleon_numpy_docstring = False

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'furo'
html_static_path = ['_static']


# -- Autodoc settings ------------------------------------------------------

# autoclass_content = 'class'  # include class-level docstring only (not __init__)