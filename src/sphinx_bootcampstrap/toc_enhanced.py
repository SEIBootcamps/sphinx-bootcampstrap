"""sphinx_seibootcamps.bs.toctree

Sets 'toc' key in template context to Bootstrap-style nav.
"""

from typing import TYPE_CHECKING, Type

from docutils import nodes
from docutils.nodes import Element
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.environment.adapters.toctree import TocTree
from sphinx.writers.html5 import HTML5Translator

if TYPE_CHECKING:
    from sphinx.application import Sphinx


class BootstrapTocBuilder(StandaloneHTMLBuilder):
    @property
    def default_translator_class(self) -> Type["BootstrapTocTranslator"]:
        return BootstrapTocTranslator


class BootstrapTocTranslator(HTML5Translator):
    def visit_bullet_list(self, node: Element) -> None:
        self.body.append(
            self.starttag(node, "nav", **{"class": " ".join(node["classes"])})
        )

    def depart_bullet_list(self, node: Element) -> None:
        self.body.append("</nav>\n")

    def visit_list_item(self, node: Element) -> None:
        """Don't render <li> tags."""

        return

    def depart_list_item(self, node: Element) -> None:
        return

    def visit_reference(self, node: Element) -> None:
        atts = {"class": "reference"}
        if node.get("internal") or "refuri" not in node:
            atts["class"] += " internal"
        else:
            atts["class"] += " external"
        if "refuri" in node:
            atts["href"] = node["refuri"] or "#"
            if self.settings.cloak_email_addresses and atts["href"].startswith(
                "mailto:"
            ):
                atts["href"] = self.cloak_mailto(atts["href"])
                self.in_mailto = True
        else:
            assert (
                "refid" in node
            ), 'References must have "refuri" or "refid" attribute.'
            atts["href"] = "#" + node["refid"]
        if not isinstance(node.parent, nodes.TextElement):
            assert len(node) == 1 and isinstance(node[0], nodes.image)  # NoQA: PT018
            atts["class"] += " image-reference"
        if "reftitle" in node:
            atts["title"] = node["reftitle"]
        if "target" in node:
            atts["target"] = node["target"]

        atts["class"] += " nav-link"

        self.body.append(self.starttag(node, "a", "", **atts))

        if node.get("secnumber"):
            self.body.append(
                ("%s" + self.secnumber_suffix) % ".".join(map(str, node["secnumber"]))
            )


def add_toc_to_context(app, pagename, templatename, context, doctree) -> None:
    toctree = TocTree(app.env).get_toc_for(pagename, app.builder)

    for ul in toctree.findall(nodes.bullet_list):
        ul["classes"] += [f"toctree-l{_get_list_level(ul) + 1}", "nav", "nav-toc"]

    builder = BootstrapTocBuilder(app, app.env)
    builder.init()
    f = builder.render_partial(toctree)["fragment"]
    context["toc"] = f


def _get_list_level(n: nodes.Node) -> int:
    """Return the number of parent bullet_list nodes."""

    count = 0
    curr = n
    while curr.parent:
        if getattr(curr.parent, "tagname") == "bullet_list":
            count += 1
        curr = curr.parent

    return count


def setup(app: "Sphinx") -> None:
    app.connect("html-page-context", add_toc_to_context)
