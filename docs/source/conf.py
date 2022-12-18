# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Lumache'
copyright = '2022, Graziella'
author = 'Graziella'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.duration', 'sphinx.ext.doctest', 'sphinx.ext.autodoc', 'sphinx.ext.autosummary', 'furo']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_logo = "https://ocdn.eu/pulscms-transforms/1/p8nk9kqTURBXy80NThmZDJiNzY1NjNiMWRmODZmNGJhMGI0OTljZWY4ZS5qcGVnk5UDAwDNAwfNAbSTBc0DFM0BvJMJpmZiNDIwNAbeAAGhMAU/onet-wprowadza-nowe-logo-i-haslo-wiem-z-onet.webp"
html_theme_options = {"announcement": "<strong>Important <font color='red'>NEWS</font></strong>TESTOWE OSTRZEŻENIE"}



# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
import pathlib
import sys
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())
