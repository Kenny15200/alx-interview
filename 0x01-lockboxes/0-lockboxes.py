#!/usr/bin/python3

def can_unlock_all(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of lists): A list of lists representing locked boxes.
            Each box may contain keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    visited = set()
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        visited.add(current_box)

        for key in boxes[current_box]:
            if key not in visited and key < len(boxes):
                queue.append(key)
                visited.add(key)  # Add the key to visited to avoid revisiting

    return len(visited) == len(boxes)

