from typing import TYPE_CHECKING

from docutils import nodes
from docutils.parsers.rst.directives.body import Container

if TYPE_CHECKING:
    from typing import List


class Compare(Container):
    def run(self) -> "List[nodes.Node]":
        node, *rest = super().run()
        node["classes"] += ["compare"]
        return [node] + rest
