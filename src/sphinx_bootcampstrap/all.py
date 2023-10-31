"""sphinx_bootcampstrap.all

Add this to extensions list in `conf.py` to load all features.
"""
from typing import TYPE_CHECKING

from . import roles

if TYPE_CHECKING:
    from sphinx.application import Sphinx


def setup(app: "Sphinx") -> None:
    roles.setup(app)
