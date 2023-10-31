"""sphinx_bootcampstrap.icons"""

from typing import TYPE_CHECKING

from pathlib import Path
from os import path

from .constants import BS_ICONS

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.config import Config


module_dir = Path(path.abspath(path.dirname(__file__)))
icons_file = module_dir / "assets" / "bootstrap-icons.svg"


def setup(app: "Sphinx") -> None:
    app.connect("config-inited", add_icon_substitutions)
    app.connect("html-page-context", add_icons_to_context)


def add_icon_substitutions(app: "Sphinx", config: "Config") -> None:
    """Add icon substitutions to the Sphinx config."""

    config.rst_prolog = (
        _build_bs_icons_substitutions() + "\n" + (config.rst_prolog or "")
    )


def add_icons_to_context(app: "Sphinx", _, __, context: dict, ___) -> None:
    with open(icons_file) as f:
        icons = f.read()

    context["bs_icons"] = icons


def _build_substitution(icon_code) -> str:
    return f"""\
.. |bi-{icon_code}| raw:: html

   <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi" viewBox="0 0 16 16">
     <use href="#{icon_code}"></use>
   </svg>
"""


def _build_bs_icons_substitutions() -> str:
    return "\n\n".join([_build_substitution(icon_code) for icon_code in BS_ICONS])
