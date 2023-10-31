"""sphinx_bootcampstrap"""

import importlib.metadata
from typing import TYPE_CHECKING

from os import path
from pathlib import Path
from docutils import nodes
from sphinx.util.osutil import copyfile, ensuredir

from . import icons, roles, toctree
from .betternodes import depart_table, visit_table

if TYPE_CHECKING:
    from sphinx.application import Sphinx

__name__ = "sphinx-bootcampstrap"
__version__ = importlib.metadata.version(__name__)

module_dir = Path(path.abspath(path.dirname(__file__)))
assets_dir = module_dir / "assets"

css_files = [
    ("bootcampstrap.css", {}),
    ("bootcampstrap.css.map", {}),
]

js_files = [
    (
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js",
        {
            "loading_method": "defer",
            "integrity": "sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL",
            "crossorigin": "anonymous",
        },
    ),
]


def add_bs_assets(app: "Sphinx") -> None:
    for f, opts in css_files:
        app.add_css_file(f, **opts)

    for f, opts in js_files:
        app.add_js_file(f, **opts)


def is_external_file(file: str) -> bool:
    return file.startswith("http") or file.startswith("://")


def copy_bs_assets(app: "Sphinx", exc: Exception) -> None:
    staticdir = (Path(app.builder.outdir) / "_static").resolve()
    local_assets = css_files + js_files
    for f in [file for file, *_ in local_assets if not is_external_file(file)]:
        source = assets_dir / f
        dest = staticdir / Path(f).name
        ensuredir(str(dest.parent))
        copyfile(str(source), str(dest))


def setup(app: "Sphinx") -> None:
    add_bs_assets(app)
    app.connect("build-finished", copy_bs_assets)

    roles.add_color_roles(app)
    icons.setup(app)

    app.connect("html-page-context", toctree.add_toc_to_context)
    app.add_node(nodes.table, html=(visit_table, depart_table), override=True)
