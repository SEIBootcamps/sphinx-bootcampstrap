# FIXME: this shit needs to move to sphinx-handouts

from typing import TYPE_CHECKING

from sphinx.writers.html5 import HTML5Translator
from docutils import nodes

if TYPE_CHECKING:
    from sphinx.application import Sphinx


def visit_table(self, node: "nodes.table") -> None:
    # Adds a div around the table to allow for horizontal scrolling.
    # Rules for .table-scroller can be found in scss/components/_tables.scss
    self.body.append('<div class="table-scroller">')
    super(HTML5Translator, self).visit_table(node)


def depart_table(self, node: "nodes.table") -> None:
    super(HTML5Translator, self).depart_table(node)
    self.body.append("</div>")


def setup(app: "Sphinx") -> None:
    app.add_node(nodes.table, html=(visit_table, depart_table), override=True)
