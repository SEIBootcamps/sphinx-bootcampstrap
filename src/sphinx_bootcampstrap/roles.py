"""sphinx_seibootcamps.bs.roles

These roles depend on Bootstrap. Don't put generic roles here.
"""

from typing import TYPE_CHECKING

from docutils import nodes

from ..roles.utils import get_role_function

if TYPE_CHECKING:
    from sphinx.application import Sphinx

COLOR_ROLES = {
    "blue": ["text-blue"],
    "blue-light": ["text-blue-light"],
    "blue-dark": ["text-blue-dark"],
    "indigo": ["text-indigo"],
    "indigo-light": ["text-indigo-light"],
    "indigo-dark": ["text-indigo-dark"],
    "purple": ["text-purple"],
    "purple-light": ["text-purple-light"],
    "purple-dark": ["text-purple-dark"],
    "pink": ["text-pink"],
    "pink-light": ["text-pink-light"],
    "pink-dark": ["text-pink-dark"],
    "red": ["text-red"],
    "red-light": ["text-red-light"],
    "red-dark": ["text-red-dark"],
    "orange": ["text-orange"],
    "orange-light": ["text-orange-light"],
    "orange-dark": ["text-orange-dark"],
    "yellow": ["text-yellow"],
    "yellow-light": ["text-yellow-light"],
    "yellow-dark": ["text-yellow-dark"],
    "green": ["text-green"],
    "green-light": ["text-green-light"],
    "green-dark": ["text-green-dark"],
    "teal": ["text-teal"],
    "teal-light": ["text-teal-light"],
    "teal-dark": ["text-teal-dark"],
    "cyan": ["text-cyan"],
    "cyan-light": ["text-cyan-light"],
    "cyan-dark": ["text-cyan-dark"],
    "body": ["text-body"],
    "black": ["text-black"],
    "black50": ["text-black-50"],
    "white": ["text-white"],
    "white50": ["text-white-50"],
    "secondary": ["text-body-secondary"],
    "tertiary": ["text-body-tertiary"],
}


def add_color_roles(app: "Sphinx") -> None:
    for role_name in COLOR_ROLES:
        app.add_role(
            role_name,
            get_role_function(
                nodes.inline, opts_fn=lambda: {"classes": COLOR_ROLES[role_name]}
            ),
        )
