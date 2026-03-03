from Animal import Animal
from Habitet import Habitat 
from Dog import Dog
from Owl import Owl
from Lizard import Lizard
from Owner import Owner

def _show_all(owner: Owner):
    print(f"\n{'─'*65}")
    print(f"  Owner: {owner.name}   |   animals: {len(owner.animals)}")
    print(f"{'─'*65}")
    for a in owner.animals:
        alive  = "alive  " if a.alive else "DEAD   "
        happy  = "happy  " if a.happy else "unhappy"
        hungry = "hungry" if a.hungry else "full  "
        meals  = len(a._meals)
        print(f"  [{a.name}] {a.kind():<8}  {alive}  {happy}  {hungry}"
              f"  meals:{meals}/{a.MAX_MEALS}  "
              f"eyes:{a.eyes} legs:{a.legs} wings:{a.wings}  "
              f"{a.habitat.value}")
    print(f"{'─'*65}")


def _choose(owner: Owner, only_alive: bool = True) -> Animal | None:
    pool = [a for a in owner.animals if (a.alive if only_alive else True)]
    if not pool:
        print("  No animals available.")
        return None
    for i, a in enumerate(pool, 1):
        mark = " [DEAD]" if not a.alive else ""
        print(f"    {i}. {a.name} ({a.kind()}){mark}")
    try:
        return pool[int(input("  #: ")) - 1]
    except (ValueError, IndexError):
        print("  Invalid choice.")
        return None


def _pick_habitat() -> Habitat:
    print("  Habitat:  1-Owner's home  2-Pet shop  3-Wild")
    return {
        "1": Habitat.OWNER,
        "2": Habitat.PET_SHOP,
        "3": Habitat.WILD,
    }.get(input("  Choice: ").strip(), Habitat.OWNER)


def _add_animal(owner: Owner):
    print("  Species:  1-Dog  2-Owl  3-Lizard  4-Custom")
    kind = input("  Choice: ").strip()
    name = input("  Name: ").strip()
    if not name:
        print("  Name cannot be empty.")
        return
    habitat = _pick_habitat()
    cls = {"1": Dog, "2": Owl, "3": Lizard}.get(kind)
    if cls:
        owner.adopt(cls(name, habitat))
        print(f"  + {name} ({cls.__name__}) added.")
        return
    if kind == "4":
        _add_custom(owner, name, habitat)
        return
    print("  Invalid species.")


def _add_custom(owner: Owner, name: str, habitat: Habitat):
    species = input("  Species name (e.g. Parrot): ").strip() or "Animal"
    try:
        eyes  = int(input("  Eyes  (default 2): ").strip() or "2")
        legs  = int(input("  Legs  (default 4): ").strip() or "4")
        wings = int(input("  Wings (default 0): ").strip() or "0")
    except ValueError:
        print("  Invalid number, using defaults.")
        eyes, legs, wings = 2, 4, 0

    CustomAnimal = type(species, (Animal,), {
        "kind": lambda self: species
    })
    owner.adopt(CustomAnimal(name, eyes=eyes, legs=legs, wings=wings, habitat=habitat))
    print(f"  + {name} ({species}) added.")


MENU = """
  1. Show all animals
  2. Feed
  3. Clean
  4. Run
  5. Fly
  6. Walk / crawl
  7. Add animal
  8. Release animal
  0. Exit"""


def run():
    print("=" * 42)
    print("   Animal Simulation")
    print("=" * 42)
    owner_name = input("Your name: ").strip() or "Owner"
    owner = Owner(owner_name)

    owner.adopt(Dog("Barsik"))
    owner.adopt(Owl("Buba"))
    owner.adopt(Lizard("Liza", Habitat.WILD))

    while True:
        for a in owner.animals:
            a._tick_day()
            if a.alive and a.hungry:
                for cb in a._on_hungry:
                    cb(a)

        print(MENU)
        choice = input("  Choice: ").strip()

        if choice == "0":
            print("\n  Goodbye!")
            break

        elif choice == "1":
            _show_all(owner)

        elif choice == "2":
            a = _choose(owner)
            if a:
                if a.eat():
                    print(f"  + {a.name} ate. Today: {len(a._meals)}/5")
                else:
                    print(f"  - {a.name} refused (max meals reached or dead).")

        elif choice == "3":
            a = _choose(owner)
            if a:
                if a.clean():
                    print(f"  + Cleaned {a.name}'s space.")
                else:
                    print(f"  - Cannot clean: animal is wild or dead.")

        elif choice == "4":
            a = _choose(owner)
            if a:
                if a.run():
                    print(f"  + {a.name} ({a.kind()}) is running!")
                else:
                    print(f"  - {a.name} cannot run — hungry or dead.")

        elif choice == "5":
            a = _choose(owner)
            if a:
                if a.fly():
                    print(f"  + {a.name} ({a.kind()}) is flying!")
                elif a.wings == 0:
                    print(f"  - {a.name} has no wings.")
                else:
                    print(f"  - {a.name} cannot fly — hungry or dead.")

        elif choice == "6":
            a = _choose(owner)
            if a:
                if a.walk():
                    verb = "crawls" if isinstance(a, Lizard) else "walks"
                    print(f"  + {a.name} ({a.kind()}) {verb}.")
                else:
                    print(f"  - {a.name} is dead.")

        elif choice == "7":
            _add_animal(owner)

        elif choice == "8":
            a = _choose(owner, only_alive=False)
            if a:
                owner.release(a)
                print(f"  + {a.name} released.")

        else:
            print("  Invalid choice.")


if __name__ == "__main__":
    run()