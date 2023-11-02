"""sphinx_bootcampstrap

Adding this extension will load all features. To selectively load features, use one of:
- sphinx_bootcampstrap.core (REQUIRED)
- sphinx_bootcampstrap.icons
- sphinx_bootcampstrap.roles
- sphinx_bootcampstrap.toc_enhanced
- sphinx_bootcampstrap.betternodes
"""

import importlib.metadata
from typing import TYPE_CHECKING

from . import core, roles, icons, toc_enhanced, betternodes, components

if TYPE_CHECKING:
    from sphinx.application import Sphinx

__name__ = "sphinx-bootcampstrap"
__version__ = importlib.metadata.version(__name__)


def setup(app: "Sphinx") -> None:
    core.setup(app)
    roles.setup(app)
    icons.setup(app)
    components.setup(app)
    toc_enhanced.setup(app)
    betternodes.setup(app)
