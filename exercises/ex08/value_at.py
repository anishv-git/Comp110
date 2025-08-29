"""EX08 - value_at List Util."""

from linked_list import Node

__author__ = "730773852"


def value_at(head: Node | None, index: int) -> int:
    """Finds value at certain index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.value
    else:
        return value_at(head.next, index - 1)
