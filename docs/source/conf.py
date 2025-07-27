import sys
from pathlib import Path


# -- Path setup ------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src" / "witcherLib"))


# -- Project information -----------------------------------------------------

project = 'WitcherLib'
copyright = '%Y, 22skowron'
author = '22skowron'
release = '0.0.1'


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    # 'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []


# -- sphinx.ext.napoleon configuration ---------------------------------------

napoleon_google_docstring = True
napoleon_numpy_docstring = False


# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']
# html_show_sphinx = False
html_show_sourcelink = False

# Alabaster theme specific configuration
html_theme_options = {
    "description": "Fictional Python library inspired by The Witcher universe.",
    "github_user": "22skowron",
    "github_repo": "WitcherLib",
    "github_type": "star",
    "fixed_sidebar": True,
}


# -- Autodoc settings ------------------------------------------------------

# autoclass_content = 'class'  # include class-level docstring only (not __init__)