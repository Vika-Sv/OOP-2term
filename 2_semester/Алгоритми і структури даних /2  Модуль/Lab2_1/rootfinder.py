import math

class RootFinder:
    @staticmethod
    def f(x: float) -> float:
        return x**3 - 2 * x
 
    @staticmethod
    def df(x: float) -> float:
        return 3 * x**2 - 2
 
    @staticmethod
    def _find_subintervals(a: float, b: float, step: float = 0.25) -> list:
        intervals = []
        x = a
        while x < b - 1e-12:
            x2 = min(x + step, b)
            if RootFinder.f(x) * RootFinder.f(x2) <= 0:
                intervals.append((x, x2))
            x = x2
        return intervals
 
    @staticmethod
    def bisection(a: float, b: float, eps: float = 1e-7) -> tuple:
        if RootFinder.f(a) * RootFinder.f(b) > 0:
            return None, 0
        iterations = 0
        while (b - a) / 2 > eps:
            mid = (a + b) / 2
            if RootFinder.f(mid) == 0:
                return mid, iterations
            if RootFinder.f(a) * RootFinder.f(mid) < 0:
                b = mid
            else:
                a = mid
            iterations += 1
        return (a + b) / 2, iterations
 
    @staticmethod
    def newton(a: float, b: float, eps: float = 1e-7) -> tuple:
        if RootFinder.f(a) * RootFinder.f(b) > 0:
            return None, 0
        x = a if RootFinder.f(a) * RootFinder.df(a) > 0 else b
        iterations = 0
        while True:
            fx  = RootFinder.f(x)
            dfx = RootFinder.df(x)
            if dfx == 0:
                break
            dx = fx / dfx
            x -= dx
            iterations += 1
            if abs(dx) < eps or iterations > 1000:
                break
        return x, iterations
 
    @staticmethod
    def chord(a: float, b: float, eps: float = 1e-7) -> tuple:
        if RootFinder.f(a) * RootFinder.f(b) > 0:
            return None, 0
        a0, b0 = a, b
        iterations = 0
        while iterations < 1000:
            fa, fb = RootFinder.f(a0), RootFinder.f(b0)
            if fb == fa:
                break
            x = a0 - fa * (b0 - a0) / (fb - fa)
            if abs(x - a0) < eps:
                return x, iterations
            if RootFinder.f(a0) * RootFinder.f(x) < 0:
                b0 = x
            else:
                a0 = x
            iterations += 1
        return a0, iterations
 
    @classmethod
    def run(cls) -> None:
        print("=" * 55)
        print("РІВЕНЬ 2 — Знаходження коренів рівняння")
        print("  y(x) = x³ − 2x = 0")
        print("=" * 55)
 
        a   = float(input("Введіть ліву межу інтервалу a: "))
        b   = float(input("Введіть праву межу інтервалу b: "))
        eps = float(input("Введіть точність ε (напр. 0.0001): "))
 
        intervals = cls._find_subintervals(a, b)
 
        if not intervals:
            print(f"\nНа інтервалі [{a}, {b}] коренів не знайдено.")
            return
 
        print(f"\nЗнайдено {len(intervals)} підінтервал(ів) зі зміною знаку:\n")
 
        fmt = lambda v, it: (f"{v:.8f}", str(it)) if v is not None else ("—", "—")
 
        for i, (ia, ib) in enumerate(intervals, 1):
            print(f"  Корінь #{i}  підінтервал [{ia:.4f}, {ib:.4f}]")
            print(f"  {'Метод':<30} {'Корінь':>15}  {'Ітерацій':>10}")
            print("  " + "-" * 58)
 
            v, it = fmt(*cls.bisection(ia, ib, eps))
            print(f"  {'Половинного ділення':<30} {v:>15}  {it:>10}")
 
            v, it = fmt(*cls.newton(ia, ib, eps))
            print(f"  {'Дотичних (Ньютон)':<30} {v:>15}  {it:>10}")
 
            v, it = fmt(*cls.chord(ia, ib, eps))
            print(f"  {'Хорд':<30} {v:>15}  {it:>10}")
            print()