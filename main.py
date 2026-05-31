def clamp_stat(value, minimum, maximum):
    if value < minimum:
        return minimum
    elif value > maximum:
        return maximum
    else:
        return value


def get_friendship_level(relationship_score):
    if relationship_score >= 30:
        return "Close Friend"
    elif relationship_score >= 20:
        return "Friend"
    elif relationship_score >= 10:
        return "Acquaintance"
    else:
        return "Stranger"


def get_norma_dialogue(norma_relationship):
    friendship_level = get_friendship_level(norma_relationship)

    if friendship_level == "Close Friend":
        return "Norma saves you a seat before you even make it to the counter. Somehow, she already knows you need tea."
    elif friendship_level == "Friend":
        return "Norma pats the chair beside her and asks how you have really been adjusting to the city."
    elif friendship_level == "Acquaintance":
        return "Norma waves you over like she expected to see you today."
    else:
        return "Norma gives you a polite smile over her tea and offers a piece of advice you did not ask for."


def show_stats(player_name, money, energy, mood, reputation):
    print("\n--- Player Stats ---")
    print(f"Name: {player_name}")
    print(f"Money: ${money}")
    print(f"Energy: {energy}")
    print(f"Mood: {mood}")
    print(f"Reputation: {reputation}")


def show_relationships(norma_relationship, greta_relationship, lou_relationship):
    norma_level = get_friendship_level(norma_relationship)
    greta_level = get_friendship_level(greta_relationship)
    lou_level = get_friendship_level(lou_relationship)

    print("\n--- Relationships ---")
    print(f"Norma: {norma_relationship} - {norma_level}")
    print(f"Greta: {greta_relationship} - {greta_level}")
    print(f"Lou: {lou_relationship} - {lou_level}")


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


def apartment_actions(money, energy, mood, reputation):
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

    return money, energy, mood, reputation


def coffee_shop_actions(money, energy, mood, reputation, norma_relationship):
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
        print(f"\n{get_norma_dialogue(norma_relationship)}")
        energy -= 5
        mood += 3
        reputation += 2
        norma_relationship += 5
    else:
        print("\nYou hover near the counter awkwardly and then leave.")

    return money, energy, mood, reputation, norma_relationship


def temp_agency_actions(money, energy, mood, reputation):
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

    return money, energy, mood, reputation


def bookstore_actions(money, energy, mood, reputation):
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

    return money, energy, mood, reputation


def park_subway_actions(money, energy, mood, reputation):
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

    return money, energy, mood, reputation


def music_venue_actions(money, energy, mood, reputation, greta_relationship):
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
        greta_relationship += 5
    else:
        print("\nYou linger near the door and leave before the first song starts.")

    return money, energy, mood, reputation, greta_relationship


def choose_activity(
    time_slot,
    money,
    energy,
    mood,
    reputation,
    norma_relationship,
    greta_relationship,
    lou_relationship,
):
    print(f"\n--- {time_slot} ---")

    location = choose_location()

    if location == "Apartment":
        money, energy, mood, reputation = apartment_actions(
            money, energy, mood, reputation
        )

    elif location == "Coffee Shop":
        money, energy, mood, reputation, norma_relationship = coffee_shop_actions(
            money, energy, mood, reputation, norma_relationship
        )

    elif location == "Temp Agency":
        money, energy, mood, reputation = temp_agency_actions(
            money, energy, mood, reputation
        )

    elif location == "Bookstore":
        money, energy, mood, reputation = bookstore_actions(
            money, energy, mood, reputation
        )

    elif location == "Park/Subway Station":
        money, energy, mood, reputation = park_subway_actions(
            money, energy, mood, reputation
        )

    elif location == "Music Venue":
        money, energy, mood, reputation, greta_relationship = music_venue_actions(
            money, energy, mood, reputation, greta_relationship
        )

    else:
        print("\nYou lose time wandering without a clear plan.")
        energy -= 5
        mood -= 3
        reputation -= 1

    money = clamp_stat(money, 0, 9999)
    energy = clamp_stat(energy, 0, 100)
    mood = clamp_stat(mood, 0, 100)
    reputation = clamp_stat(reputation, -100, 100)

    return (
        money,
        energy,
        mood,
        reputation,
        norma_relationship,
        greta_relationship,
        lou_relationship,
    )


def show_day_summary(
    day,
    money,
    energy,
    mood,
    reputation,
    norma_relationship,
    greta_relationship,
    lou_relationship,
):
    print(f"\nDay {day} ends.")
    print("You look out at the city lights and wonder what tomorrow will bring.")

    print("\n--- Day Summary ---")
    print(f"Money: ${money}")
    print(f"Energy: {energy}")
    print(f"Mood: {mood}")
    print(f"Reputation: {reputation}")

    show_relationships(norma_relationship, greta_relationship, lou_relationship)


def play_day(
    day,
    player_name,
    money,
    energy,
    mood,
    reputation,
    norma_relationship,
    greta_relationship,
    lou_relationship,
):
    print("\n====================")
    print(f"Day {day}")
    print("====================")

    show_stats(player_name, money, energy, mood, reputation)
    show_relationships(norma_relationship, greta_relationship, lou_relationship)

    (
        money,
        energy,
        mood,
        reputation,
        norma_relationship,
        greta_relationship,
        lou_relationship,
    ) = choose_activity(
        "Morning",
        money,
        energy,
        mood,
        reputation,
        norma_relationship,
        greta_relationship,
        lou_relationship,
    )
    show_stats(player_name, money, energy, mood, reputation)

    (
        money,
        energy,
        mood,
        reputation,
        norma_relationship,
        greta_relationship,
        lou_relationship,
    ) = choose_activity(
        "Afternoon",
        money,
        energy,
        mood,
        reputation,
        norma_relationship,
        greta_relationship,
        lou_relationship,
    )
    show_stats(player_name, money, energy, mood, reputation)

    (
        money,
        energy,
        mood,
        reputation,
        norma_relationship,
        greta_relationship,
        lou_relationship,
    ) = choose_activity(
        "Evening",
        money,
        energy,
        mood,
        reputation,
        norma_relationship,
        greta_relationship,
        lou_relationship,
    )
    show_stats(player_name, money, energy, mood, reputation)

    show_day_summary(
        day,
        money,
        energy,
        mood,
        reputation,
        norma_relationship,
        greta_relationship,
        lou_relationship,
    )

    return (
        money,
        energy,
        mood,
        reputation,
        norma_relationship,
        greta_relationship,
        lou_relationship,
    )


def main():
    print("Welcome to Big City.")
    print("You have fourteen days to build a life.\n")

    player_name = input("What is your name? ")

    money = 100
    energy = 100
    mood = 50
    reputation = 0
    day = 1

    norma_relationship = 0
    greta_relationship = 0
    lou_relationship = 0

    print(f"\nWelcome to the city, {player_name}.")

    while day <= 14:
        (
            money,
            energy,
            mood,
            reputation,
            norma_relationship,
            greta_relationship,
            lou_relationship,
        ) = play_day(
            day,
            player_name,
            money,
            energy,
            mood,
            reputation,
            norma_relationship,
            greta_relationship,
            lou_relationship,
        )

        day += 1

    print("\nThe demo period ends.")
    print("Your first chapter in Big City comes to an end.")

    print("\n--- Final Stats ---")
    print(f"Money: ${money}")
    print(f"Energy: {energy}")
    print(f"Mood: {mood}")
    print(f"Reputation: {reputation}")

    print("\n--- Final Relationships ---")
    print(f"Norma: {norma_relationship}")
    print(f"Greta: {greta_relationship}")
    print(f"Lou: {lou_relationship}")


if __name__ == "__main__":
    main()