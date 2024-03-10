# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PR Pilot'
copyright = '2024, Marco Lamina'
author = 'Marco Lamina'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_material'
html_static_path = ['_static']
html_theme_options = {
    'base_url': 'https://pr-pilot.ai',
    'repo_url': 'https://github.com/PR-Pilot-AI/pr-pilot-public',
    'repo_name': 'PR Pilot',
    'html_minify': True,
    'css_minify': True,
    'nav_title': 'PR Pilot',
    'logo_icon': '&#xe869',
    'globaltoc_depth': 2,
    "master_doc": False,
    "nav_links": [],
    "heroes": {
        "index": "Your AI collaborator for Github issues and PRs",
    },
}
html_sidebars = {
    "**": ["globaltoc.html"]
}