# -*- coding: utf-8 -*-

from __future__ import unicode_literals

# -- PROJECT Variables ----------------------------------------------------
settings_project_name = "Manuale Open City"
settings_copyright_copyleft = 'Opencontent'
settings_editor_name = 'Opencontent'
settings_doc_version = 'version: latest'
settings_doc_release = 'version: latest'
settings_basename = 'manuale-opencity'
settings_file_name = 'manuale-opencity'

import sys, os


from recommonmark.transform import AutoStructify
from recommonmark.parser import CommonMarkParser

# -- RTD configuration ------------------------------------------------

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# This is used for linking and such so we link to the thing we're building
rtd_version = os.environ.get('READTHEDOCS_VERSION', 'latest')
if rtd_version not in ['stable', 'latest']:
    rtd_version = 'stable'

rtd_project = os.environ.get('READTHEDOCS_PROJECT', '')

sys.path.append(os.path.abspath(os.pardir))

__version__ = '1.0'

# -- General configuration -----------------------------------------------------

source_suffix = '.rst'
master_doc = 'index'
project = 'Verso OntoPiA - Classi di contenuto'
copyright = '[licenza CC - BY OpenContent - SA]'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = settings_doc_version
# The full version, including alpha/beta/rc tags.
release = settings_doc_release

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'it'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['.DS_Store', 'README', 'README.md', '.venv*']


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- AutoStructify --------------------------------------------------------
def setup(app):
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents',
        'enable_eval_rst': True,
        'enable_auto_doc_ref': True
    }, True)
    app.add_transform(AutoStructify)


extlinks = {}

# -- Options for HTML output ---------------------------------------------------

html_theme = 'default'

html_static_path = ['static']

def setup(app):
    # overrides for wide tables in RTD theme
    app.add_stylesheet('theme_overrides.css') # path relative to static

    
"""
  You might want to uncomment the “latex_documents = []” if you use CKJ characters in your document.
  Because the pdflatex raises exception when generate Latex documents with CKJ characters.
"""

# Output file base name for HTML help builder.
htmlhelp_basename = settings_basename + 'doc'

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', settings_file_name, settings_project_name,
     [settings_editor_name], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', settings_file_name, settings_project_name,
   settings_copyright_copyleft, settings_project_name, settings_project_name,
   'Miscellaneous'),
]

numfig = True