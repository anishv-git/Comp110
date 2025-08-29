"""Linked List."""

from __future__ import annotations

import builtins

__author__ = "730773852"


class Node:
    """Mutating and creating the Node object."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Constructor for the Node Object."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Magic method for the Node Object."""
        rest: str = "TODO"

        if self.next is None:
            rest = "None"
        else:
            rest = self.next.__str__()
        return f"{self.value} -> {rest}"


def value_at(head: Node | None, index: int) -> int:
    """Finds value at certain index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.value
    else:
        return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Finds max value."""
    if head is None:
        raise ValueError("Cannot call max_recursive with None")
    if head.next is None:
        return head.value
    return builtins.max(head.value, max(head.next))


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns the scale."""
    if head is None:
        return None
    else:
        return Node(head.value * factor, scale(head.next, factor))


def linkify(items: list[int]) -> Node | None:
    """Links all items."""
    if not items:
        return None
    else:
        return Node(items[0], linkify(items[1:]))
