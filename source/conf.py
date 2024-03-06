# Sphinx configuration file

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'PR Pilot Documentation'
author = 'PR Pilot Team'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

html_theme = 'alabaster'
