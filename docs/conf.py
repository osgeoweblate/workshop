# -*- coding: utf-8 -*-
#
# Workshop - FOSS4G routing with pgRouting tools
# sphinx-quickstart on Sat Jul  3 21:23:22 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

################## bootstrap
# At the top.
import sphinx_bootstrap_theme

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.autosectionlabel',
    ]
autosectionlabel_prefix_document = True


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Workshop @WORKSHOP_AREA@'
copyright = u'@COPYRIGHT@'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '@PGR_WORKSHOP_VERSION@'
# The full version, including alpha/beta/rc tags.
release = '@PGR_WORKSHOP_RELEASE@'

#OSGeoLive Version
osgeolive_version = '@OSGeoLive_VERSION@'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
locale_dirs = ['../../locale']
gettext_compact = False
gettext_auto_build = True

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_patterns = ['_build', 'latex.rst']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
#html_theme = 'default'
#html_theme = 'workshop-theme'
#html_theme_path = ['.'] # make sphinx search for themes in current dir

################## bootstrap
# Activate the theme.
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
  'navbar_site_name': "Chapters",
  'globaltoc_depth': 2,
  'navbar_fixed_top': "true",
  'bootstrap_version': "3",
}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "@PGR_HTML_TITLE@"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "@PGR_HTML_SHORT_TITLE@"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "@PGR_WORKSHOP_SOURCE_DIR@/docs/_static/images/pgrouting.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "@PGR_WORKSHOP_SOURCE_DIR@/docs/_static/images/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['@PGR_WORKSHOP_SOURCE_DIR@/docs/_static']

def setup(app):
    app.add_css_file("custom.css")

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False
html_copy_source = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'pgRoutingWorkshop'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
  'papersize'     : 'a4paper',
  'pointsize'     : '10pt'
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('latex', 'pgRoutingWorkshop.tex', u'Workshop - FOSS4G routing with pgRouting',
   u'Daniel Kastl, Vicky Vergara', 'manual', False),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
latex_use_modindex = False

# New in version 1.0
latex_show_pagerefs = False
latex_domain_indices = False

# Linkcheck configuration, see http://sphinx.pocoo.org/latest/config.html#options-for-the-linkcheck-builder

linkcheck_ignore = [
        r'http://localhost:\d+/',  r'http://localhost:\d+', r'http://localhost/', r'http://127.0.0.1:\d+/',
        r'https://localhost:\d+/',  r'https://localhost:\d+', r'https://localhost/', r'https://127.0.0.1:\d+/',

        # TODO remove when openlayers page is found
        'https://openlayers.org/en/master/examples/preload.html',
        ]
linkcheck_anchors = False


# -- Custom Options --------------------------------------------------

# Enable ToDo extension
todo_include_todos = True

html_show_sphinx = False

images_config = dict(
  backend='LightBox2',
  default_image_width='200px'
)

rst_epilog="""
.. |pgrouting-web| replace:: `pgRouting <https://pgrouting.org/>`__
.. |pgrouting-ver| replace:: 2.6
.. |osm-web| replace:: `OpenStreetMap <https://www.openstreetmap.org>`__
.. |postgis-web| replace:: `PostGIS <https://postgis.net>`__
.. |osm2pgrouting-web| replace:: https://pgrouting.org/docs/tools/osm2pgrouting.html
.. |osm2pgrouting-wiki| replace:: https://github.com/pgRouting/osm2pgrouting/wiki/Documentation-for-osm2pgrouting-v2.2
.. |osm2pgrouting-ver| replace:: 2.3
.. |georepublic| replace:: `GeoRepublic <https://georepublic.info/>`__
.. |paragon| replace:: `Paragon Corporation <https://www.paragoncorporation.com/>`__
.. |osgeo| replace:: `OSGeo <https://www.osgeo.org/>`__
.. |id_1| replace:: ``@ID_1@``
.. |id_2| replace:: ``@ID_2@``
.. |id_3| replace:: ``@ID_3@``
.. |id_4| replace:: ``@ID_4@``
.. |id_5| replace:: ``@ID_5@``
.. |osmid_1| replace:: ``@OSMID_1@``
.. |osmid_2| replace:: ``@OSMID_2@``
.. |osmid_3| replace:: ``@OSMID_3@``
.. |osmid_4| replace:: ``@OSMID_4@``
.. |osmid_5| replace:: ``@OSMID_5@``
.. |place_1| replace:: @PLACE_1@
.. |place_2| replace:: @PLACE_2@
.. |place_3| replace:: @PLACE_3@
.. |place_4| replace:: @PLACE_4@
.. |place_5| replace:: @PLACE_5@
"""
