#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of lists): A list of lists representing locked boxes. Each box may contain keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    # Check if boxes list is empty
    if not boxes:
        return False

    # Set to keep track of visited boxes
    visited = set()

    # Queue for BFS traversal
    queue = [0]

    # Start BFS traversal
    while queue:
        current_box = queue.pop(0)
        visited.add(current_box)

        # Check keys in the current box
        for key in boxes[current_box]:
            if key not in visited and key < len(boxes):
                queue.append(key)

    # If all boxes are visited, return True
    return len(visited) == len(boxes)

