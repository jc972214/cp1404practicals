"""Wimbledon Exercise
Note: I got stuck and probably looked at the solutions too much for this one"""

FILENAME = "wimbledon.csv"


def main():
    wimbledon_data = get_wimbledon_data(FILENAME)
    champion_to_count = process_wimbledon_data(wimbledon_data)
    countries = process_wimbledon_countries(wimbledon_data)
    display_wimbledon_data(champion_to_count, countries)


def process_wimbledon_countries(data):
    countries = set()
    for datum in data:
        countries.add(datum[1])
    return countries


def display_wimbledon_data(champion_to_count, countries):
    print("Wimbledon Champions:")
    for champion in champion_to_count:
        print(f"{champion}: {champion_to_count[champion]}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(country for country in sorted(countries)))



def process_wimbledon_data(data):
    champion_to_count = {}
    for datum in data:
        try:
            champion_to_count[datum[2]] += 1
        except KeyError:
            champion_to_count[datum[2]] = 1
    return champion_to_count


def get_wimbledon_data(filename):
    wimbledon_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for row in in_file:
            line = row.strip().split(",")
            wimbledon_data.append(line)
    return wimbledon_data


main()
