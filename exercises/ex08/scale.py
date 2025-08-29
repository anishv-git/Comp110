"""EX08 -  Scale List Util."""

from linked_list import Node

__author__ = "730773852"


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns the scale."""
    if head is None:
        return None
    else:
        return Node(head.value * factor, scale(head.next, factor))
