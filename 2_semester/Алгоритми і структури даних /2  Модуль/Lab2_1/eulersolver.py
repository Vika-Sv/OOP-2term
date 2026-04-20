import math 

class EulerSolver:
    @staticmethod
    def f(x: float, y: float) -> float:
        return math.exp(x) - y
 
    @staticmethod
    def solve(x0: float, y0: float, x_end: float, h: float) -> list:
        results = [(x0, y0)]
        x, y = x0, y0
        n = round((x_end - x0) / h)
        for _ in range(n):
            y = y + h * EulerSolver.f(x, y)
            x += h
            results.append((round(x, 10), y))
        return results
 
    @classmethod
    def run(cls) -> None:
        print("=" * 55)
        print("РІВЕНЬ 3 — Розв'язання ДР методом Ейлера")
        print("  dy/dx = e^x − y")
        print("=" * 55)
 
        x0    = float(input("Введіть початкове значення x₀: "))
        y0    = float(input("Введіть початкову умову y(x₀) = y₀: "))
        x_end = float(input("Введіть кінцеве значення x: "))
        h     = float(input("Введіть крок h: "))
 
        results = cls.solve(x0, y0, x_end, h)
 
        print(f"\n{'i':>4}  {'x':>12}  {'y':>18}")
        print("-" * 38)
        for i, (x, y) in enumerate(results):
            print(f"{i:>4}  {x:>12.4f}  {y:>18.8f}")