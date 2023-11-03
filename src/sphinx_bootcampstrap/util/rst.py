from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Callable, List, Optional, Tuple
    from docutils.nodes import Node, system_message


def get_role_function(node: "Callable", opts_fn: "Optional[Callable]") -> "Callable":
    """Generate role function."""

    options = opts_fn() if opts_fn else {}

    def role_function(
        _, rt: str, t: str, *__, **___
    ) -> "Tuple[List[Node], List[system_message]]":
        # return [nodes.inline(rt, t, classes=_span_roles[role_name])], []
        return [node(rt, t, **options)], []

    return role_function
