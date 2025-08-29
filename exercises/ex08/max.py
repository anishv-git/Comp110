"""EX08 - max List Util."""

from linked_list import Node

import builtins

__author__ = "730773852"


def max(head: Node | None) -> int:
    """Finds max value."""
    if head is None:
        raise ValueError("Cannot call max_recursive with None")
    if head.next is None:
        return head.value
    return builtins.max(head.value, max(head.next))
