#!/usr/bin/python3
""" Method that determines if all the boxes can be opened """


def canUnlockAll(boxes):
    """ logic for determining whether all the boxes can be unlocked """
    total_boxes = len(boxes)
    opened = [False] * total_boxes
    opened[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < total_boxes and not opened[key]:
                opened[key] = True
                stack.append(key)

    return all(opened)