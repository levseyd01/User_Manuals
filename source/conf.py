# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys


project = 'User Manuals'
copyright = '2023, Transferonline.'
html_title = 'Transfer Online Documentation'
author = 'D.Levsey'
release = '1'



# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


language = 'en'

latex_elements = {
    'preamble': r'''
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage{adjustbox}
\usepackage{titlesec}
\usepackage{titling}

% Define custom colors
\definecolor{ConfidentialRed}{RGB}{255,0,0} % Adjust RGB values to your liking

% Define graphics path
\graphicspath{{../../source/_static/}}

% Set lengths and styles
\setlength{\headheight}{32.1pt} % Adjusted as per warning
\renewcommand{\headrulewidth}{0pt} % Remove horizontal line from header
\renewcommand{\footrulewidth}{0pt} % Remove horizontal line from footer

% Title format customization for chapters
\titleformat{\chapter}[display]
{\normalfont\huge\bfseries}{\chaptertitlename\ \thechapter}{20pt}{\Huge}
\titlespacing*{\chapter}{0pt}{50pt}{40pt}

% Set up the header and footer
\fancyhf{} % Clear all header and footer fields
\fancyhead[L]{\includegraphics[height=1cm]{solo_light.png}} % Set header image
\fancyfoot[C]{\color{ConfidentialRed}\textbf{Transfer Online Confidential}} % Set center footer

% Custom style for initial pages of chapters using the `plain` style
\fancypagestyle{plain}{
    \fancyhf{} % Clear all header and footer fields for the `plain` style
    \fancyhead[L]{\includegraphics[height=1cm]{solo_light.png}} % Set header image for `plain` style
    \fancyfoot[C]{\color{ConfidentialRed}\textbf{Transfer Online Confidential}} % Set center footer for `plain` style
}

% Adjust box settings (if needed, based on content)
\adjustboxset{max size={\textwidth}{\textheight}}

% Title information
\title{Transfer Agent Issuer Manual}
\author{Author Name}
\date{\today}

% Apply the `fancy` page style as the global page style
\pagestyle{fancy}

% Define the `maketitle` command to create a custom title page
\newcommand{\maketitle}{
    \begin{titlepage}
        \centering
        \vspace*{\fill}
        \includegraphics[width=\textwidth,height=\textheight,keepaspectratio]{solo_cover_page.png}
        \vspace*{\fill}
    \end{titlepage}
    \clearpage
}
''',

    'maketitle': r'''
\begin{titlepage}
\centering
\vspace*{\fill}
\includegraphics[width=\textwidth,height=\textheight,keepaspectratio]{solo_cover_page.png}
\vspace*{\fill}
\end{titlepage}
\clearpage
    ''',
}

autosectionlabel_maxdepth = 5

source_suffix = ['.rst', '.md']
# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'rst2pdf.pdfbuilder',
    'sphinx.ext.todo',
    'sphinx_search.extension',
    'sphinx_prompt',
    'sphinx.builders.linkcheck',
    'sphinx_copybutton',
    'sphinx_togglebutton',
    'sphinx_tippy',
    'myst_parser']

todo_include_todos = True

tippy_rtd_urls = [
    "https://www.sphinx-doc.org/en/master/",
    "https://transferonline.com/"
]

myst_enable_extensions = [
    "attrs_inline",
    "colon_fence"


]


myst_all_links_external = False

intersphinx_mapping = {



    'single-issuer-manual' : (
            'https://transferonline-solo-docsite.readthedocs-hosted.com/projects/transferonline-single-issuer-manual/en/stable/',
             None
    ),

    'ta-issuer-manual' : (
            'https://transferonline-solo-docsite.readthedocs-hosted.com/projects/ta-issuer-manual/en/stable/',
             None
    ),

    'resource-hub': (
        'https://transferonline-resourcehub.readthedocs-hosted.com/en/latest/',
         None
    ),


    'ta-issuer-manual-S2' : (
            'https://transferonline-solo-docsite.readthedocs-hosted.com/projects/transferonline-ta-issuer-s2/en/latest/',
             None
    ),






}

html_theme_options = {
    "repository_url": "https://github.com/levseyd01/User_Manuals",
    "use_source_button": True,
    "use_edit_page_button": True,
    "path_to_docs": "source",
    "repository_branch": "main",
    "use_repository_button": True,
    "use_issues_button": True,
    "collapse_navbar": False,
    "show_navbar_depth": 4,
    "home_page_in_toc": True,
    "use_download_button": True,
    "show_prev_next": False
}

html_logo = "_static/solo_logo_2.png"

html_theme = 'sphinx_book_theme'


exclude_patterns = ['_static',
                    '_build', 'Thumbs.db', '.DS_Store', 'my_custom.css', 'build/images'
                    ]

# -- General configuration ---------------------------------------------------


html_css_files = ["my_custom.css"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


# html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']



suppress_warnings = [
   "undefined",
   "duplicate label"
]



# -- Options for PDF output --------------------------------------------------

# Grouping the document tree into PDF files. List of tuples
# (source start file, target name, title, author, options).
#
# If there is more than one author, separate them with \\.
# For example: r'Guido van Rossum\\Fred L. Drake, Jr., editor'
#
# The options element is a dictionary that lets you override
# this config per-document. For example:
#
# ('index', 'MyProject', 'My Project', 'Author Name', {'pdf_compressed': True})
#
# would mean that specific document would be compressed
# regardless of the global 'pdf_compressed' setting.



# A comma-separated list of custom stylesheets. Example:
#pdf_stylesheets = ['sphinx', 'a4']

# A list of folders to search for stylesheets. Example:
#pdf_style_path = ['.', '_styles']

# Create a compressed PDF
# Use True/False or 1/0
# Example: compressed=True
# pdf_compressed = False

# A colon-separated list of folders to search for fonts. Example:
# pdf_font_path = ['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']

# Language to be used for hyphenation support
# pdf_language = "en_US"

# Mode for literal blocks wider than the frame. Can be
# overflow, shrink or truncate
# pdf_fit_mode = "shrink"

# Section level that forces a break page.
# For example: 1 means top-level sections start in a new page
# 0 means disabled
pdf_break_level = 2

# When a section starts in a new page, force it to be 'even', 'odd',
# or just use 'any'
# pdf_breakside = 'any'

# Insert footnotes where they are defined instead of
# at the end.
# pdf_inline_footnotes = True

# verbosity level. 0 1 or 2
# pdf_verbosity = 0

# If false, no index is generated.
pdf_use_index = True

# If false, no modindex is generated.
# pdf_use_modindex = True

# If false, no coverpage is generated.
pdf_use_coverpage = True

# Name of the cover page template to use
# pdf_cover_template = 'sphinxcover.tmpl'

# Documents to append as an appendix to all manuals.
# pdf_appendices = []

# Enable experimental feature to split table cells. Use it
# if you get "DelayedTable too big" errors
# pdf_splittables = False

# Set the default DPI for images
# pdf_default_dpi = 72

# Enable rst2pdf extension modules
# pdf_extensions = []

# Page template name for "regular" pages
# pdf_page_template = 'cutePage'

# Show Table Of Contents at the beginning?
pdf_use_toc = True

# How many levels deep should the table of contents be?
# pdf_toc_depth = 9999

# Add section number to section references
pdf_use_numbered_links = False

# Background images fitting mode
pdf_fit_background_mode = 'scale'

# Repeat table header on tables that cross a page boundary?
pdf_repeat_table_rows = True

# Enable smart quotes (1, 2 or 3) or disable by setting to 0
pdf_smartquotes = 1

html_context= {
 "default_mode": "light",
}
