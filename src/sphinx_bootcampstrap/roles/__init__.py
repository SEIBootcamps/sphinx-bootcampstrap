"""sphinx_bootcampstrap.roles"""

from typing import TYPE_CHECKING

from docutils import nodes
from bootcamps_sphinxutils.roleutils import get_role_function

from .constants import COLOR_ROLES

if TYPE_CHECKING:
    from sphinx.application import Sphinx


def setup(app: "Sphinx") -> None:
    for role_name in COLOR_ROLES:
        app.add_role(
            role_name,
            get_role_function(
                nodes.inline, opts_fn=lambda: {"classes": COLOR_ROLES[role_name]}
            ),
        )
