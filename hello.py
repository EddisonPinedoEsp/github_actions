def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


def is_even(n: int) -> bool:
    return n % 2 == 0


def multiply(a: int, b: int) -> int:
    """Multiplica dos números; se deja sin pruebas para simular baja cobertura."""
    return a * b


def subtract(a: int, b: int) -> int:
    """Resta dos números; se deja sin pruebas para simular el fallo."""
    return a - b


def divide(a: float, b: float) -> float:
    """Divide dos números; se deja sin pruebas para probar el umbral."""
    return a / b



if __name__ == "__main__":
    print(greet("GitHub Actions"))
    print(f"2 + 3 = {add(2, 3)}")
    print(f"4 is even: {is_even(4)}")