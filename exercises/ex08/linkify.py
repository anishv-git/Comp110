"""EX08 - linkify List Util."""

from linked_list import Node

__author__ = "730773852"


def linkify(items: list[int]) -> Node | None:
    """Links all items."""
    if not items:
        return None
    else:
        return Node(items[0], linkify(items[1:]))
