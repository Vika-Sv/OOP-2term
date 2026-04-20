from integration import NumericalIntegration
from rootfinder import RootFinder
from eulersolver import EulerSolver 


def main() -> None:
    menu = {
        "1": ("Рівень 1 — Інтегрування", NumericalIntegration),
        "2": ("Рівень 2 — Корені рівняння", RootFinder),
        "3": ("Рівень 3 — Диференціальне рівняння (Ейлер)", EulerSolver),
        "0": ("Вихід", None),
    }
    while True:
        print("\n" + "=" * 55)
        print("  ЧИСЕЛЬНІ МЕТОДИ — Варіант 3")
        print("=" * 55)
        for key, (title, _) in menu.items():
            print(f"  [{key}] {title}")
        choice = input("\nОберіть завдання: ").strip()
 
        if choice == "0":
            print("До побачення!")
            break
        elif choice in menu and menu[choice][1] is not None:
            print()
            try:
                menu[choice][1].run()
            except ValueError:
                print("Помилка: введено некоректне число.")
        else:
            print("Невірний вибір, спробуйте ще раз.")
 
 
if __name__ == "__main__":
    main()