from typing import TYPE_CHECKING

from sphinx.writers.html5 import HTML5Translator

if TYPE_CHECKING:
    from docutils import nodes


def visit_table(self, node: "nodes.table") -> None:
    # Adds a div around the table to allow for horizontal scrolling.
    # Rules for .table-scroller can be found in scss/components/_tables.scss
    self.body.append('<div class="table-scroller">')
    super(HTML5Translator, self).visit_table(node)


def depart_table(self, node: "nodes.table") -> None:
    super(HTML5Translator, self).depart_table(node)
    self.body.append("</div>")
