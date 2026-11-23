import sqlite3
import random
import matplotlib.pyplot as plt

DATABASE_NAME = "population_SD.bd"

def create_database():
    """Create the population database and add 2025 city population."""

    cities = [
        ("Bradenton", 2025, 58014),
        ("Sarasota", 2025, 58458),
        ("Tampa", 2025, 413554),
        ("Palmetto", 2025, 13562),
        ("Lakewood Ranch", 2025, 46142),
        ("Parrish", 2025, 43855),
        ("Ruskin", 2025, 30000),
        ("Venice", 2025, 30477),
        ("North Port", 2025, 96551),
        ("St. Petersburg", 2025, 264033)
    ]

    # Connect to the database.
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        # Create the population table.
        cursor.execute("""CREATE TABLE IF NOT EXISTS population (city TEXT, year INTEGER, population INTEGER)""")

        # Clear old data so the program can run again.
        cursor.execute("DELETE FROM population")

        # Insert the 2025 population for each city.
        cursor.executemany("""INSERT INTO population VALUES (?,?,?)""", cities)

        connection.commit()

def simulate_population():
    """Simulate population growth and decline for the next 20 years."""

    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        # Get all cities and their 2025 populations.
        cursor.execute("SELECT city, population FROM population WHERE year = 2025")

        cities = cursor.fetchall()

        for city, starting_population in cities:
            current_population = starting_population

            # Create population values for 2026 through 2045.
            for year in range(2026, 2046):

                # Generate a different growth or decline rate each year.
                growth_rate = random.uniform(-0.02, 0.03)

                current_population = int(current_population * (1 + growth_rate))

                cursor.execute("INSERT INTO population VALUES (?,?,?)", (city, year, current_population))

            connection.commit()

def show_population(city):
    """Display the population growth and decline for the selected city."""

    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        cursor.execute(
            """SELECT year, population FROM population WHERE city = ? ORDER BY year""", (city,))

        results = cursor.fetchall()

    years = []
    populations = []

    for year, population in results:
        years.append(year)
        populations.append(population)

    # Display the population data.
    print(f"\nPopulation Data for {city}")
    print("-" * 35)

    for year, population in results:
        print(f"{year}: {population:,}")

    # Create the population graph.
    plt.plot(years, populations, marker="o")
    plt.title(f"Population Growth and Decline for {city}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid()
    plt.show()

def main():
    """Run the Florida population analysis program."""

    cities = [
        "Bradenton",
        "Sarasota",
        "Tampa",
        "Palmetto",
        "Lakewood Ranch",
        "Parrish",
        "Ruskin",
        "Venice",
        "North Port",
        "St. Petersburg"]

    create_database()
    simulate_population()

    print("Florida Cities")
    print("-" * 30)

    for number in range(len(cities)):
        print(f"{number + 1}. {cities[number]}")

    choice = int(input("\nChoose a city number (1-10): "))

    if 1 <= choice <= 10:
        selected_city = cities[choice - 1]
        show_population(selected_city)
    else:
        print("\nInvalid choice. Try again.")

if __name__ == "__main__":
    main()

