from typing import TYPE_CHECKING

from docutils import nodes
from docutils.parsers.rst.directives.body import ParsedLiteral

if TYPE_CHECKING:
    from typing import List, Tuple


class Console(ParsedLiteral):
    def run(self) -> "List[nodes.Node]":
        node, *rest = super().run()
        node["classes"] += ["console"]
        return [node] + rest


def cmd_role(
    _, rt: str, t: str, *__, **___
) -> "Tuple[List[nodes.Node], List[nodes.system_message]]":
    """Used to distinguish user input from program output.

    Example::

       .. console::

          \$ :cmd:`echo hello`
          hello
    """

    return [nodes.inline(rt, t, classes=["cmd"])], []
