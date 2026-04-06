from Enteties.Animal import Animal, Habitat
from BBL.AnimalService import AnimalService
from Enteties.Owner import Owner
from Factories.Animalfactory import FACTORIES, CustomFactory


def _show_all(owner: Owner) -> None:
    print(f"\n{'─'*70}")
    print(f"  Owner: {owner.name}   |   animals: {len(owner.animals)}")
    print(f"{'─'*70}")
    for a in owner.animals:
        alive  = "alive  " if a.alive  else "DEAD   "
        happy  = "happy  " if a.happy  else "unhappy"
        hungry = "hungry" if a.hungry else "full   "
        print(
            f"  [{a.name:<10}] {a.kind():<8}  {alive}  {happy}  {hungry}"
            f"  meals:{a.meals_today}/{a.MAX_MEALS}"
            f"  eyes:{a.eyes} legs:{a.legs} wings:{a.wings}"
            f"  {a.habitat.value}"
        )
    print(f"{'─'*70}")
 
 
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
 
 
def _add_animal(owner: Owner) -> None:
    species_list = list(FACTORIES.keys())
    for i, s in enumerate(species_list, 1):
        print(f"    {i}. {s}")
    print(f"    {len(species_list)+1}. Custom")
 
    choice = input("  Choice: ").strip()
    name   = input("  Name: ").strip()
    if not name:
        print("  Name cannot be empty.")
        return
    habitat = _pick_habitat()
 
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(species_list):
            factory = FACTORIES[species_list[idx]]
            owner.adopt(factory.create(name, habitat))
            print(f"  + {name} ({species_list[idx]}) added.")
            return
    except ValueError:
        pass
 
    if choice == str(len(species_list) + 1):
        _add_custom(owner, name, habitat)
    else:
        print("  Invalid species.")
 
 
def _add_custom(owner: Owner, name: str, habitat: Habitat) -> None:
    species = input("  Species name (e.g. Parrot): ").strip() or "Animal"
    try:
        eyes  = int(input("  Eyes  (default 2): ").strip() or "2")
        legs  = int(input("  Legs  (default 4): ").strip() or "4")
        wings = int(input("  Wings (default 0): ").strip() or "0")
    except ValueError:
        print("  Invalid number — using defaults.")
        eyes, legs, wings = 2, 4, 0
 
    factory = CustomFactory(species, eyes, legs, wings)
    owner.adopt(factory.create(name, habitat))
    print(f"  + {name} ({species}) added.")
 
 
MENU = """
  1. Show all animals
  2. Feed
  3. Clean
  4. Run
  5. Fly
  6. Add animal
  7. Release animal
  0. Exit"""
 
 
def run() -> None:
    print("=" * 42)
    print("   Animal Simulation")
    print("=" * 42)
    owner_name = input("Your name: ").strip() or "Owner"
    owner = Owner(owner_name)
 
    owner.adopt(FACTORIES["Dog"].create("Barsik"))
    owner.adopt(FACTORIES["Owl"].create("Buba"))
    owner.adopt(FACTORIES["Lizard"].create("Liza", Habitat.WILD))
 
    while True:
        for a in owner.animals:
            AnimalService.tick(a)
 
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
                if AnimalService.eat(a):
                    print(f"  + {a.name} ate. Today: {a.meals_today}/{a.MAX_MEALS}")
                else:
                    print(f"  - {a.name} refused (max meals reached or dead).")
 
        elif choice == "3":
            a = _choose(owner)
            if a:
                if AnimalService.clean(a):
                    print(f"  + Cleaned {a.name}'s space.")
                else:
                    print(f"  - Cannot clean: animal is wild or dead.")
 
        elif choice == "4":
            a = _choose(owner)
            if a:
                if AnimalService.run(a):
                    print(f"  + {a.name} ({a.kind()}) is running!")
                elif a.alive and a.hungry:
                    print(f"  - {a.name} is too weak to run — {a.move_verb()} instead.")
                else:
                    print(f"  - {a.name} is dead.")
 
        elif choice == "5":
            a = _choose(owner)
            if a:
                if AnimalService.fly(a):
                    print(f"  + {a.name} ({a.kind()}) is flying!")
                elif a.wings == 0:
                    print(f"  - {a.name} has no wings.")
                elif a.alive and a.hungry:
                    print(f"  - {a.name} is too weak to fly — {a.move_verb()} instead.")
                else:
                    print(f"  - {a.name} is dead.")
 
        elif choice == "6":
            _add_animal(owner)
 
        elif choice == "7":
            a = _choose(owner, only_alive=False)
            if a:
                owner.release(a)
                print(f"  + {a.name} released.")
 
        else:
            print("  Invalid choice.")
 