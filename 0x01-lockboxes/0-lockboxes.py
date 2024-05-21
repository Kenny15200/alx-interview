#!/usr/bin/python3
"""
This module provides a function to determine whether all the locked boxes in a list can be opened.
The boxes are numbered sequentially from 0 to n-1, and each box contains keys that can open other boxes.
The goal is to figure out if all boxes can eventually be opened starting from box 0.
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened starting from the first box.
    
    This function uses a breadth-first search (BFS) approach to explore the boxes.
    It begins with the first box (index 0) and uses a queue to manage the boxes
    that need to be checked. As keys are found, they are used to open new boxes
    and add them to the queue for further exploration.

    Args:
        boxes (list of lists): A list where each element is a list of integers representing keys
                               to other boxes. The index of the list represents the box number.

    Returns:
        bool: True if all boxes can be opened, False otherwise.

    Example:
        boxes = [[1], [2], [3], [4], []]
        canUnlockAll(boxes) -> True

        boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
        canUnlockAll(boxes) -> True

        boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
        canUnlockAll(boxes) -> False
    """
    from collections import deque

    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    queue = deque([0])

    while queue:
        current = queue.popleft()
        for key in boxes[current]:
            if key < n and not opened[key]:
                opened[key] = True
                queue.append(key)

    return all(opened)

