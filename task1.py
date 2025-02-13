def kwargsAcceptFun(**kwargs):
    """Filters user-related information, validates inputs, and checks major availability at NewUU."""

    required_keys = {"name", "age", "email", "major"}
    valid_majors = {
        "Pedagogy", "Software Engineering", "AI", "Economics",
        "Industrial Management", "Applied Mathematics",
        "Mechanical Engineering", "Chemical Engineering"
    }

    user_info = {}

    for key, value in kwargs.items():
        if key in required_keys:
            # Age validation
            if key == "age" and not isinstance(value, (int, float)):
                return "Error: 'age' must be a number. Are you really a NewUU student?!"
            if key == "email" and "newuu.uz" not in value:
                return "Warning: Only NewUU student emails (@newuu.uz) are allowed. No access!"

            # Major validation
            if key == "major" and value not in valid_majors:
                return f"Error: '{value}' is not a major at NewUU. Are you fooling me?? Are you really NewUU student?!"

            user_info[key] = value

    return user_info if user_info else "No valid user-related data found."




