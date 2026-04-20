import math 

class NumericalIntegration:
    @staticmethod
    def f(x: float) -> float:
        return math.cos(math.exp(x / 3) + x)
 
    @staticmethod
    def rectangles(a: float, b: float, h: float) -> float:
        n = round((b - a) / h)
        total = 0.0
        for i in range(n):
            x_mid = a + (i + 0.5) * h
            total += NumericalIntegration.f(x_mid)
        return total * h
 
    @staticmethod
    def trapezoids(a: float, b: float, h: float) -> float:
        n = round((b - a) / h)
        xs = [a + i * h for i in range(n + 1)]
        ys = [NumericalIntegration.f(x) for x in xs]
        total = (ys[0] + ys[-1]) / 2 + sum(ys[1:-1])
        return total * h
 
    @staticmethod
    def simpson(a: float, b: float, h: float) -> float:
        n = round((b - a) / h)
        if n % 2 != 0:
            n -= 1
        xs = [a + i * h for i in range(n + 1)]
        ys = [NumericalIntegration.f(x) for x in xs]
        total = ys[0] + ys[n]
        for i in range(1, n):
            total += (4 if i % 2 != 0 else 2) * ys[i]
        return total * h / 3
 
    
    @classmethod
    def run(cls) -> None:
        print("=" * 55)
        print("РІВЕНЬ 1 — Обчислення визначеного інтеграла")
        print("  ∫ cos(e^(x/3) + x) dx")
        print("=" * 55)
 
        a = float(input("Введіть нижню межу a: "))
        b = float(input("Введіть верхню межу b: "))
        h = float(input("Введіть крок h: "))
 
        r = cls.rectangles(a, b, h)
        t = cls.trapezoids(a, b, h)
        s = cls.simpson(a, b, h)
 
        print(f"\n{'Метод':<25} {'Значення':>15}")
        print("-" * 42)
        print(f"{'Прямокутників':<25} {r:>15.8f}")
        print(f"{'Трапецій':<25} {t:>15.8f}")
        print(f"{'Сімпсона':<25} {s:>15.8f}")