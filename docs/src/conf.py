#!/usr/bin/python3

import time
import os
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive
from docutils.nodes import emphasis, strong, literal
from docutils.parsers.rst.roles import set_classes
from sphinx.writers.latex import LaTeXTranslator

from docutils import nodes

DIR = os.path.dirname(__file__)

extensions = [
    'sphinx.ext.graphviz',
    'sphinx.ext.imgmath',
    'sphinxcontrib.plantuml',
]
templates_path = ['_templates']
source_suffix = '.rst'

master_doc = 'index'
project = 'EWAN ISP'
copyright = (u'EveryWAN 2019-%s, ' % time.strftime('%Y'))
version = '1.0'
language = 'es_ES'[:2]
exclude_patterns = []
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------
try:
    from better import better_theme_path
except ImportError:
    html_theme = 'default'
else:
    html_theme = 'better'
    html_theme_path = [better_theme_path]
html_theme_options = {
    # 'showrelbarbottom': False,
    'inlinecss': """
        header#pageheader, footer#pagefooter, div.related, div.document {
            max-width: 75rem;
        }
        dt {
            font-weight: bold;
            color: darkgreen;
        }
        .rst_xmenu {
            font-weight: bold;
            color: darkred;
        }
        .rst_xgui {
            background-color: #FFFBE2;
            padding: 2px 4px;
            color: #000000;
        }
        img {
            padding-bottom: 12px;
        }
        """,
    'cssfiles': [
        'https://maxcdn.bootstrapcdn.com/font-awesome/'
        '4.6.3/css/font-awesome.min.css'
    ],
    'linktotheme': False,
}
html_title = project
html_short_title = project
html_logo = '_static/logo.png'
html_favicon = '_static/favicon.ico'
html_static_path = ['_static']
html_sidebars = {
    '**': ['globaltoc.html', 'pdf_download.html'],
}
htmlhelp_basename = 'adoc'
# -- Options for LaTeX output -----------------------------------------------
xpreamb = r'\usepackage[default,osfigures,scale=1]{opensans} '
xpreamb += r'\raggedbottom'
xpreamb += r'\usepackage{fontawesome}'
latex_elements = {
    'papersize': 'a4paper,openany',
    # 'pointsize': '10pt',
    'preamble': xpreamb,
    'babel': r'\usepackage[spanish]{babel}',
}
tex_document_name = 'ewan-isp.tex'
latex_documents = [
    (master_doc, tex_document_name, project,
     copyright, 'manual'),
]
latex_logo = '_static/logo.png'

# -- Options for manual page output ------------------------------------------
man_pages = [
    (master_doc, 'ewan-isp-1.0-es', project,
     [copyright], 1)
]
# man_show_urls = False
# -- Options for Texinfo output ---------------------------------------------
texinfo_documents = [
    (master_doc, 'ewan-isp-1.0-es', project, copyright,
     'Odoo-%s' % version, 'EWAN ISP Documentation.', 'EWAN ISP'),
]

# ----------------------------------------------------------------------------
# EXTENSIONS
# ----------------------------------------------------------------------------


def align(argument):
    """Conversion function for the "align" option."""
    return directives.choice(argument, ('left', 'center', 'right'))


class IframeVideo(Directive):
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'height': directives.nonnegative_int,
        'width': directives.nonnegative_int,
        'align': align,
    }
    default_width = 500
    default_height = 281

    def run(self):
        self.options['video_id'] = directives.uri(self.arguments[0])
        if not self.options.get('width'):
            self.options['width'] = self.default_width
        if not self.options.get('height'):
            self.options['height'] = self.default_height
        if not self.options.get('align'):
            self.options['align'] = 'left'
        return [nodes.raw('', self.html % self.options, format='html')]


class Youtube(IframeVideo):
    html = '<iframe src="https://www.youtube.com/embed/%(video_id)s" \
    width="%(width)u" height="%(height)u" frameborder="0" \
    webkitAllowFullScreen mozallowfullscreen allowfullscreen \
    class="align-%(align)s"></iframe>'


class Vimeo(IframeVideo):
    html = '<iframe src="https://player.vimeo.com/video/%(video_id)s" \
    width="%(width)u" height="%(height)u" frameborder="0" \
    webkitAllowFullScreen mozallowfullscreen allowFullScreen \
    class="align-%(align)s"></iframe>'


def fa_global(key=''):
    def xfa(role, rawtext, text, lineno, inliner, options={}, content=[]):
        options.update({'classes': []})
        options['classes'].append('fa')
        if key:
            options['classes'].append('fa-%s' % key)
        else:
            for x in text.split(","):
                options['classes'].append('fa-%s' % x)
        set_classes(options)
        node = emphasis(**options)
        return [node], []
    return xfa


def xmenu(role, rawtext, text, lineno, inliner, options={}, content=[]):
    options.update({'classes': []})
    options['classes'].append('rst_xmenu')
    submenus = text.split('/')
    s = u' » '.join(submenus)
    set_classes(options)
    node = strong(text=s, **options)
    return [node], []


def xgui(role, rawtext, text, lineno, inliner, options={}, content=[]):
    options.update({'classes': []})
    options['classes'].append('rst_xgui')
    set_classes(options)
    node = literal(text=text, **options)
    return [node], []


class MyLaTexTranslator(LaTeXTranslator):

    def visit_emphasis(self, node):
        # type: (nodes.Element) -> None
        def snake_to_camel(word):
            return ''.join(x.capitalize() or '-' for x in word.split('-'))

        if 'fa' in node.attributes.get('classes', []):
            classes = node.attributes.get('classes', [])
            icon = snake_to_camel(classes[1])
            icon = icon[0].lower() + icon[1:]
            self.body.append(r'\{}'.format(icon))
        else:
            self.body.append(r'\sphinxstyleemphasis{')

    def depart_emphasis(self, node):
        # type: (nodes.Element) -> None
        if 'fa' not in node.attributes.get('classes', []):
            self.body.append('}')


def setup(app):
    app.add_role('xfa', fa_global())
    app.add_role('xmenu', xmenu)
    app.add_role('gui', xgui)
    app.set_translator('latex', MyLaTexTranslator, override=True)
    directives.register_directive('youtube', Youtube)
    directives.register_directive('vimeo', Vimeo)
