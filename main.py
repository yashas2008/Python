"""A menu-driven tour of common Python language features.

Run with: python main.py
Requires Python 3.10 or newer.
"""

from pathlib import Path
from time import perf_counter


def show_types_and_variables():
    """Numbers, strings, booleans, None, conversions, and formatted strings."""
    age = 20
    price = 4.99
    name = "Ada"
    is_learning = True
    middle_name = None

    print(f"Integer: {age}, float: {price}, string: {name!r}")
    print(f"Boolean: {is_learning}, no value: {middle_name}")
    print(f"Type of age: {type(age).__name__}")
    print(f"Convert text to a number: int('12') + 3 = {int('12') + 3}")
    print(f"String methods: {name.upper()}, {name.lower()}")


def show_collections():
    """Lists, tuples, dictionaries, sets, indexing, and useful iteration."""
    fruits = ["apple", "banana", "pear"]  # Mutable ordered collection
    coordinates = (10, 20)  # Immutable ordered collection
    person = {"name": "Ada", "language": "Python"}  # Key/value pairs
    unique_numbers = {1, 2, 2, 3}  # Sets keep unique values

    fruits.append("orange")
    print(f"List: {fruits}; first item: {fruits[0]}; slice: {fruits[:2]}")
    print(f"Tuple: {coordinates}; dictionary lookup: {person['name']}")
    print(f"Set removes duplicates: {unique_numbers}")
    print("Enumerate:", list(enumerate(fruits, start=1)))
    print("Zip:", list(zip(("Ada", "Grace"), (36, 45))))


def show_control_flow():
    """Conditions, loops, and comprehensions."""
    number = 7

    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

    print("for loop:")
    for item in ("red", "green", "blue"):
        print(f"  - {item}")

    countdown = 3
    while countdown > 0:
        print(f"  countdown: {countdown}")
        countdown -= 1

    squares = [value**2 for value in range(1, 6)]
    even_squares = [value for value in squares if value % 2 == 0]
    print(f"List comprehension (squares): {squares}")
    print(f"Filtered comprehension (even squares): {even_squares}")


def describe_greeting(name: str, greeting: str = "Hello") -> str:
    """A function with a type hint, default argument, and return value."""
    return f"{greeting}, {name}!"


def show_functions():
    """Parameters, defaults, return values, *args, **kwargs, and lambda."""

    def total(*numbers: int) -> int:
        return sum(numbers)

    def introduce(**details: str) -> str:
        return ", ".join(f"{key}={value}" for key, value in details.items())

    double = lambda value: value * 2

    print(describe_greeting("Ada"))
    print(describe_greeting("Grace", greeting="Welcome"))
    print(f"*args example: total(2, 3, 4) = {total(2, 3, 4)}")
    print(f"**kwargs example: {introduce(name='Lin', role='developer')}")
    print(f"Lambda example: double(5) = {double(5)}")


def show_errors():
    """Handle expected errors with try/except/else/finally."""
    text = "not a number"
    try:
        number = int(text)
    except ValueError as error:
        print(f"Could not convert {text!r}: {error}")
    else:
        print(f"Converted value: {number}")
    finally:
        print("The conversion attempt is finished.")


def show_files():
    """Read and write a small text file using a context manager."""
    demo_file = Path(__file__).with_name("python_demo.txt")

    with demo_file.open("w", encoding="utf-8") as file:
        file.write("Python can read and write text files.\n")

    with demo_file.open("r", encoding="utf-8") as file:
        contents = file.read()

    print(f"Wrote and read {demo_file.name}: {contents.strip()}")
    print("The 'with' statement closes the file automatically.")


class Animal:
    """A small class: data and behavior grouped into one type."""

    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "some sound"


class Dog(Animal):
    """A Dog inherits from Animal and overrides its speak method."""

    def speak(self) -> str:
        return "woof"


def show_classes():
    dog = Dog("Milo")
    print(f"{dog.name} says {dog.speak()}")
    print("Dog is an Animal:", isinstance(dog, Animal))


def show_generators_and_decorators():
    """Generators yield values lazily; decorators wrap functions."""

    def countdown(start: int):
        while start > 0:
            yield start
            start -= 1

    def timed(function):
        def wrapper(*args, **kwargs):
            started = perf_counter()
            result = function(*args, **kwargs)
            elapsed = perf_counter() - started
            print(f"Function took {elapsed:.6f} seconds")
            return result

        return wrapper

    @timed
    def add_up_to(limit: int) -> int:
        return sum(range(limit + 1))

    print(f"Generator values: {list(countdown(3))}")
    print(f"Sum: {add_up_to(100_000)}")


def show_modules_and_types():
    """Imports reuse code; type hints document expected values."""
    from math import sqrt

    def hypotenuse(width: float, height: float) -> float:
        return sqrt(width**2 + height**2)

    print(f"sqrt comes from the math module: sqrt(81) = {sqrt(81)}")
    print(f"Type-hinted function: hypotenuse(3, 4) = {hypotenuse(3, 4)}")
    print("Python also includes many standard-library modules.")


DEMOS = {
    "1": ("Types and variables", show_types_and_variables),
    "2": ("Collections", show_collections),
    "3": ("Conditions, loops, comprehensions", show_control_flow),
    "4": ("Functions", show_functions),
    "5": ("Errors and exceptions", show_errors),
    "6": ("Files and context managers", show_files),
    "7": ("Classes and inheritance", show_classes),
    "8": ("Generators and decorators", show_generators_and_decorators),
    "9": ("Modules and type hints", show_modules_and_types),
}


def main():
    print("Python feature tour")
    while True:
        print("\nChoose a topic:")
        for key, (title, _) in DEMOS.items():
            print(f"  {key}. {title}")
        print("  0. Exit")

        choice = input("> ").strip()
        if choice == "0":
            print("Goodbye!")
            break

        demo = DEMOS.get(choice)
        if demo is None:
            print("Please enter a number from 0 to 9.")
            continue

        print(f"\n--- {demo[0]} ---")
        demo[1]()


if __name__ == "__main__":
    main()
