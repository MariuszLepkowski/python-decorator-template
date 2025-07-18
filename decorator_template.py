from functools import wraps


def parametrized_decorator(param1=None, param2=None):  # Funkcja zwracająca dekorator
    def actual_decorator(func):  # Właściwy dekorator
        @wraps(func)  # Zachowuje nazwę i dokumentację funkcji
        def wrapped_function(*args, **kwargs):  # Wrapper
            print(f"[DEBUG] Przed funkcją {func.__name__} (param1={param1}, param2={param2})")

            result = func(*args, **kwargs)  # Wywołanie oryginalnej funkcji

            print(f"[DEBUG] Po funkcji {func.__name__}, zwrócono: {result}")
            return result  # Możesz zmodyfikować wynik, jeśli trzeba

        return wrapped_function  # Zwracamy wrapper, czyli udekorowaną wersję `func`

    return actual_decorator  # Zwracamy właściwy dekorator


from functools import wraps


def decorator_template(param1=None, param2=None):
    """
    A universal decorator template with optional parameters.

    :param param1: Description of the first parameter
    :param param2: Description of the second parameter
    """

    def actual_decorator(func):
        @wraps(func)  # Preserves function metadata (name, docstring, etc.)
        def wrapper(*args, **kwargs):
            # 🔹 Code to execute BEFORE the function runs
            print(f"[DEBUG] Calling {func.__name__} with param1={param1}, param2={param2}")

            # 🔹 Call the original function and capture the result
            result = func(*args, **kwargs)

            # 🔹 Code to execute AFTER the function runs
            print(f"[DEBUG] {func.__name__} returned: {result}")

            return result  # Optionally, modify the result if needed

        return wrapper  # Return the modified function

    return actual_decorator  # Return the actual decorator


