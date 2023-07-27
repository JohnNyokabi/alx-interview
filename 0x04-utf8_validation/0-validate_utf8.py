#!/usr/bin/python3
"""
method that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    function that determines if the provided data is a valid unicode
    """
    def get_byte_count(byte):
        """
        determines the byte count
        """
        if byte & 0x80 == 0:
            return 1
        elif byte & 0xE0 == 0xC0:
            return 2
        elif byte & 0xF0 == 0xE0:
            return 3
        elif byte & 0xF8 == 0xF0:
            return 4
        return -1

    def is_valid_sequence(start, data, length):
        """
        Check if the subsequent bytes match the pattern 10xxxxxx
        """
        for i in range(start + 1, start + length):
            if i >= len(data) or data[i] & 0xC0 != 0x80:
                return False
        return True

    i = 0
    while i < len(data):
        byte_count = get_byte_count(data[i])
        if byte_count == -1:
            return False

        if not is_valid_sequence(i, data, byte_count):
            return False

        i += byte_count

    return True
