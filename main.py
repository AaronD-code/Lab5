import threading

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_sorted_ascending(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

def is_palindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

def safe_add_floats(nums):
    total = 0.0
    for n in nums:
        total += float(n)
    return total

def validate_and_parse_user(data):
    # expects {"name": str, "age": int-like}
    if not isinstance(data, dict):
        raise ValueError("Input must be a dict")

    name = data.get("name")
    age = data.get("age")

    if not isinstance(name, str) or not name.strip():
        raise ValueError("Invalid name")

    try:
        age_int = int(age)
    except Exception:
        raise ValueError("Age must be an integer")

    if age_int < 0:
        raise ValueError("Age must be >= 0")

    return {"name": name.strip(), "age": age_int}


class ThreadCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment_many(self, times):
        for _ in range(times):
            with self.lock:
                self.value += 1