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

def choose_location():
    print("\nWhere would you like to go?")
    print("1. Apartment")
    print("2. Coffee Shop")
    print("3. Temp Agency")
    print("4. Bookstore")
    print("5. Park/Subway Station")
    print("6. Music Venue")

    choice = input("\nChoose a location: ")

    if choice == "1":
        print("\nYou return to your overpriced studio. It is small, but it is yours for now.")
        return "Apartment"
    elif choice == "2":
        print("\nYou step into the coffee shop. The windows are fogged with rain and conversation.")
        return "Coffee Shop"
    elif choice == "3":
        print("\nYou arrive at the temp agency. The fluorescent lights hum, and yes, there is a watercooler.")
        return "Temp Agency"
    elif choice == "4":
        print("\nYou enter the bookstore. The shelves lean slightly, crowded with paperbacks and possibility.")
        return "Bookstore"
    elif choice == "5":
        print("\nYou make your way toward the park and subway entrance, where the city seems to breathe around you.")
        return "Park/Subway Station"
    elif choice == "6":
        print("\nYou find a small music venue tucked between a laundromat and a closed pharmacy.")
        return "Music Venue"
    else:
        print("\nYou wander without choosing a clear destination.")
        return "Nowhere"

def choose_activity(time_slot, money, energy, mood, reputation):
    print(f"\n--- {time_slot} ---")

    location = choose_location()

    if location == "Apartment":
        print("\nWhat would you like to do at your apartment?")
        print("1. Rest")
        print("2. Journal")

        choice = input("\nChoose an option: ")

        if choice == "1":
            print("\nYou crawl back into bed and let the city noise fade into the background.")
            energy += 30
            mood += 5
        elif choice == "2":
            print("\nYou write a few messy thoughts in your journal and feel slightly more grounded.")
            mood += 10
            energy -= 5
        else:
            print("\nYou pace around your apartment and lose track of time.")

    elif location == "Coffee Shop":
        print("\nWhat would you like to do at the coffee shop?")
        print("1. Buy coffee")
        print("2. Chat with Norma")

        choice = input("\nChoose an option: ")

        if choice == "1":
            print("\nYou buy an overpriced latte. At least the foam art was pretty.")
            money -= 4
            energy += 10
            mood += 5
        elif choice == "2":
            print("\nNorma smiles over her tea and gives you advice you did not ask for, but probably needed.")
            energy -= 5
            mood += 3
            reputation += 2
        else:
            print("\nYou hover near the counter awkwardly and then leave.")

    elif location == "Temp Agency":
        print("\nWhat would you like to do at the temp agency?")
        print("1. Work a temp shift")
        print("2. Ask about better assignments")

        choice = input("\nChoose an option: ")

        if choice == "1":
            print("\nYou take a temp shift filing paperwork at an office. There's a watercooler.")
            money += 65
            energy -= 25
            mood -= 5
            reputation += 5
        elif choice == "2":
            print("\nYou ask about better assignments. The receptionist sizes you up over her glasses.")
            energy -= 5
            reputation += 3
        else:
            print("\nYou miss your chance to speak up and shuffle back outside.")

    elif location == "Bookstore":
        print("\nWhat would you like to do at the bookstore?")
        print("1. Browse books")
        print("2. Attend beat poetry reading")

        choice = input("\nChoose an option: ")

        if choice == "1":
            print("\nYou browse the shelves and find comfort in other people's sentences.")
            mood += 8
            energy -= 5
        elif choice == "2":
            print("\nYou attend a beat poetry reading in the back corner. It is strange, sincere, and somehow exactly what you needed.")
            mood += 10
            energy -= 10
            reputation += 2
        else:
            print("\nYou get lost between the shelves and forget what you came in for.")

    elif location == "Park/Subway Station":
        print("\nWhat would you like to do near the park and subway?")
        print("1. Walk through the park")
        print("2. People-watch")

        choice = input("\nChoose an option: ")

        if choice == "1":
            print("\nYou walk through the park and pet a few dogs.")
            energy -= 5
            mood += 10
        elif choice == "2":
            print("\nYou sit near the subway entrance and watch the city hurry past.")
            energy -= 3
            mood += 5
        else:
            print("\nYou stand in everyone's way until someone mutters at you.")

    elif location == "Music Venue":
        print("\nWhat would you like to do at the music venue?")
        print("1. Go to a concert")
        print("2. Talk to Greta")

        choice = input("\nChoose an option: ")

        if choice == "1":
            print("\nYou see a local band in a crowded room with sticky floors and perfect noise.")
            money -= 25
            energy -= 15
            mood += 20
        elif choice == "2":
            print("\nGreta grins and talks your ear off about bands you've never heard of.")
            energy -= 5
            mood += 8
            reputation += 2
        else:
            print("\nYou linger near the door and leave before the first song starts.")

    else:
        print("\nYou lose time wandering without a clear plan.")
        energy -= 5
        mood -= 3

    money = clamp_stat(money, 0, 9999)
    energy = clamp_stat(energy, 0, 100)
    mood = clamp_stat(mood, 0, 100)
    reputation = clamp_stat(reputation, -100, 100)

    return money, energy, mood, reputation


def show_day_summary(day, money, energy, mood, reputation):
    print(f"\nDay {day} ends.")
    print("You look out at the city lights and wonder what tomorrow will bring.")

    print("\n--- Day Summary ---")
    print(f"Money: ${money}")
    print(f"Energy: {energy}")
    print(f"Mood: {mood}")
    print(f"Reputation: {reputation}")


def play_day(day, player_name, money, energy, mood, reputation):
    print("\n====================")
    print(f"Day {day}")
    print("====================")

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

    while day <= 2:
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
    main()