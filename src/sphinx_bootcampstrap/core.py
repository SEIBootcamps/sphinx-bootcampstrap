from typing import TYPE_CHECKING

from os import path
from pathlib import Path

from sphinx.util.osutil import copyfile, ensuredir
from sphinx.util import logging

if TYPE_CHECKING:
    from sphinx.application import Sphinx


module_dir = Path(path.abspath(path.dirname(__file__)))
assets_dir = (module_dir / "assets").resolve()

local_css_files = [
    ("bootcampstrap.css", {}),
    ("bootcampstrap.css.map", {}),
]
ext_css_files = []  # empty for now, but added in case we need to add later

local_js_files = []  # empty for now, but added in case we need to add later
ext_js_files = [
    (
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js",
        {
            "loading_method": "defer",
            "integrity": "sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL",
            "crossorigin": "anonymous",
        },
    ),
]

logger = logging.getLogger(__name__)


def setup(app: "Sphinx") -> None:
    # Selectively enable for certain builders.
    # Pass constant ALL to apply to all builders?
    # Empty will disable.
    app.add_config_value("bs_builders", ["html"], "html")
    # override Bootcampstrap CSS + JS
    app.add_config_value("bs_css_files", local_css_files + ext_css_files, "html")
    app.add_config_value("bs_js_files", local_js_files + ext_js_files, "html")

    app.connect("builder-inited", add_static_files)


def add_static_files(app: "Sphinx") -> None:
    # Only add static files to enabled builders.
    if app.builder.name in app.config.bs_builders:
        # Register CSS and JS files with builder and copy to build output
        _add_bs_assets(app)
        app.connect("build-finished", _copy_bs_assets)


def _add_bs_assets(app: "Sphinx") -> None:
    """Register CSS and JS files with Sphinx app."""

    # People typically want to load Bootstrap *before* any other stylesheets,
    # so we're inentionally deviating from convention here and setting priority=100.
    for f, opts in app.config.bs_css_files:
        app.add_css_file(f, priority=100, **opts)

    for f, opts in app.config.bs_js_files:
        app.add_js_file(f, priority=100, **opts)


def _copy_bs_assets(app: "Sphinx", _: Exception) -> None:
    """Copy CSS and JS files into output directory."""

    staticdir = (Path(app.builder.outdir) / "_static").resolve()
    for f in [file for file, *_ in app.config.bs_css_files + app.config.bs_js_files]:
        try:
            source = assets_dir / f
            dest = staticdir / Path(f).name
            ensuredir(str(dest.parent))
            copyfile(str(source), str(dest))
        except FileNotFoundError:
            logger.warning(
                f"Unable to copy {f} into output folder. If this is an external file, you can ignore this warning",
                color="yellow",
            )
