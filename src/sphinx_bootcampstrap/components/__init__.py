from typing import TYPE_CHECKING

from .compare import Compare
from .console import Console, cmd_role

if TYPE_CHECKING:
    from sphinx.application import Sphinx


def setup(app: "Sphinx") -> None:
    app.add_directive("compare", Compare)
    app.add_directive("console", Console)
    app.add_role("cmd", cmd_role)
