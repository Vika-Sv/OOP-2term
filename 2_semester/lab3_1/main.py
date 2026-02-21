class ConsoleUI:
    """External Observer that handles all console output."""
    @staticmethod
    def log_info(message: str):
        print(f"[ANIMAL STATUS]: {message}")

    @staticmethod
    def log_death(name: str, reason: str):
        print(f"[FATAL EVENT]: {name} died due to {reason}!")

def main():
    # Setup UI
    ui = ConsoleUI()

    # 1. Initialize Entities
    shop = PetShop("Happy Paws Store")
    alice = Owner("Alice Smith")
    
    dog = Dog("Buddy")
    owl = Owl("Hedwig")
    lizard = Lizard("Rango")

    # 2. Subscribing UI to Domain Events (The "Glue")
    for animal in [dog, owl, lizard]:
        animal.on_state_changed.subscribe(ui.log_info)
        animal.on_death.subscribe(ui.log_death)

    # 3. Simulation - Demonstration of Rules
    print("--- 1. PET SHOP STAGE ---")
    shop.receive_animal(dog)
    shop.care.last_cleaning = datetime.datetime.now() # Simulate cleaning
    shop.care.update_happiness(shop.stock)

    print("\n--- 2. ADOPTION STAGE ---")
    alice.adopt(dog, from_shop=shop)
    alice.adopt(owl)

    print("\n--- 3. ACTIVITY & FEEDING RULES ---")
    dog.eat()
    dog.perform_activity() # Normal RunStrategy
    
    # Simulate hunger logic (> 8 hours)
    owl.last_meal_time = datetime.datetime.now() - datetime.timedelta(hours=9)
    owl.perform_activity() # Should trigger Crawl fallback

    print("\n--- 4. SURVIVAL RULES ---")
    # Lizard dies because it wasn't fed today (0 meals)
    lizard.meals_today = 0
    lizard.check_survival()

    print("\n--- 5. WILDLIFE ---")
    Wild.release(owl, alice.pets)

if __name__ == "__main__":
    main()