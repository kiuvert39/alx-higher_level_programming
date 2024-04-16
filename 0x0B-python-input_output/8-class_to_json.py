##!/usr/bin/python3
def class_to_json(obj):
    """
    Serialize an object to a dictionary with simple data structures for JSON serialization.

    Args:
    obj: An instance of a class with serializable attributes.

    Returns:
    dict: A dictionary representing the serialized object.
    """
    serialized = {}
    # Iterate through all attributes of the object
    for attr, value in vars(obj).items():
        # Check if the value is serializable
        if isinstance(value, (list, dict, str, int, bool)):
            serialized[attr] = value
    return serialized
