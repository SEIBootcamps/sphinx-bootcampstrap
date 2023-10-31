"""sphinx_bootcampstrap.icons"""

from typing import TYPE_CHECKING

from pathlib import Path
from os import path

from .constants import BS_ICONS, BS_ICONS_PREFIX, BS_ICONS_FILENAME

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.config import Config


module_dir = Path(path.abspath(path.dirname(__file__)))
icons_file = (module_dir / ".." / "assets" / BS_ICONS_FILENAME).resolve()


def setup(app: "Sphinx") -> None:
    app.connect("config-inited", add_icon_substitutions)
    app.connect("html-page-context", add_icons_to_template_context)


def add_icon_substitutions(_, config: "Config") -> None:
    """Add icon substitutions to the Sphinx config."""

    substitutions = "\n\n".join(
        [_build_substitution(icon_code) for icon_code in BS_ICONS]
    )

    # Concat existing config.rst_prolog value so user's config overrides ours.
    config.rst_prolog = substitutions + "\n" + (config.rst_prolog or "")


def add_icons_to_template_context(_, __, ___, context: dict, ____) -> None:
    """Add SVG for icons to template context.

    This allows you to render the SVGs with `{{ bs_icons|safe }}`.

    Icons are rendered with the `<use>` element, so browser needs to load SVG
    *before* any `<use>` elements appear. Therefore, you should render this
    right after the `<body>` tag to guarantee all icons appear properly.
    """

    with open(icons_file) as f:
        icons = f.read()

    context["bs_icons"] = icons


def _build_substitution(icon_code) -> str:
    """Return markup for RST text substitution for rendering SVG of Bootstrap icon.

    Used to create substitutions for all names in BS_ICONS.

    This implementation relies on rendering markup from `add_icons_to_template_context`
    in HTML template.
    """

    return f"""\
.. |{BS_ICONS_PREFIX}{icon_code}| raw:: html

   <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi" viewBox="0 0 16 16">
     <use href="#{icon_code}"></use>
   </svg>
"""
