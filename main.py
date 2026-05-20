def clamp_stat(value, minimum, maximum):
    if value < minimum:
        return minimum
    elif value > maximum:
        return maximum
    else:
        return value

def show_stats(player_name, money, energy, mood, reputation):
    print("\n--- Player Stats ---")
    print(f"Name: {player_name}")
    print(f"Money: ${money}")
    print(f"Energy: {energy}")
    print(f"Mood: {mood}")
    print(f"Reputation: {reputation}")


def choose_activity(time_slot, money, energy, mood, reputation):
    print(f"\n--- {time_slot} ---")
    print("\nWhat would you like to do?")
    print("1. Work a temp shift")
    print("2. Rest at your apartment")
    print("3. Visit the coffee shop")
    print("4. Walk through the park")

    choice = input("\nChoose an option: ")

    if choice == "1":
        print("\nYou take a temp shift filing paperwork at an office. There's a watercooler.")
        money += 65
        energy -= 25
        mood -= 5
        reputation += 5
    elif choice == "2":
        print("\nYou silence your alarm and catch some zzzs.")
        energy += 30
        mood += 5
    elif choice == "3":
        print("\nYou visit the coffee shop and buy an overpriced latte. At least the foam art was pretty.")
        money -= 4
        energy += 10
        mood += 5
    elif choice == "4":
        print("\nYou walk through the park and pet a few dogs.")
        energy -= 5
        mood += 10
    else:
        print("\nYou dissociate and lose track of time.")

    money = clamp_stat(money, 0, 9999)
    energy = clamp_stat(energy, 0, 100)
    mood = clamp_stat(mood, 0, 100)
    reputation = clamp_stat(reputation, 0, 100)

    return money, energy, mood, reputation


def show_day_summary(day, money, energy, mood, reputation):
    print(f"\nDay {day} ends.")
    print("You look out at the city lights and wonder what tomorrow will ask of you.")

    print("\n--- Day Summary ---")
    print(f"Money: ${money}")
    print(f"Energy: {energy}")
    print(f"Mood: {mood}")
    print(f"Reputation: {reputation}")


def main():
    print("Welcome to Big City.")
    print("You have fourteen days to build a life.\n")

    player_name = input("What is your name? ")

    money = 100
    energy = 100
    mood = 50
    reputation = 0
    day = 1

    print(f"\nWelcome to the city, {player_name}.")

    while day <= 14:
        money, energy, mood, reputation = play_day(
            day, player_name, money, energy, mood, reputation
        )

        day += 1

    print("\nFourteen days pass.")
    print("Your first chapter in Big City comes to an end.")
    print("\nFinal stats:")
    print(f"Money: ${money}")
    print(f"Energy: {energy}")
    print(f"Mood: {mood}")
    print(f"Reputation: {reputation}")


if __name__ == "__main__":

   def play_day(day, player_name, money, energy, mood, reputation):
    print(f"\n====================")
    print(f"Day {day}")
    print(f"====================")

    show_stats(player_name, money, energy, mood, reputation)

    money, energy, mood, reputation = choose_activity(
        "Morning", money, energy, mood, reputation
    )
    show_stats(player_name, money, energy, mood, reputation)

    money, energy, mood, reputation = choose_activity(
        "Afternoon", money, energy, mood, reputation
    )
    show_stats(player_name, money, energy, mood, reputation)

    money, energy, mood, reputation = choose_activity(
        "Evening", money, energy, mood, reputation
    )
    show_stats(player_name, money, energy, mood, reputation)

    show_day_summary(day, money, energy, mood, reputation)

    return money, energy, mood, reputation
   
   if __name__ == "__main__":
    main()
  