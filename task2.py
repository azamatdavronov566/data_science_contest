def typeBasedTransformer(**kwargs):
    transformed = {}

    for key, value in kwargs.items():
        if isinstance(value, (int, float)):  # Square numbers
            transformed[key] = value ** 2
        elif isinstance(value, str):  # Reverse strings
            transformed[key] = value[::-1]
        elif isinstance(value, bool):  # Invert booleans
            transformed[key] = not value
        elif isinstance(value, (list, tuple)):  # Reverse lists/tuples
            transformed[key] = type(value)(reversed(value))
        elif isinstance(value, dict):  # Swap keys and values
            if len(set(value.values())) == len(value):
                transformed[key] = {v: k for k, v in value.items()}
            else:
                transformed[key] = value
        else:
            transformed[key] = value

    return transformed



