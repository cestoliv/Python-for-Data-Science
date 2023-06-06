import matplotlib.pyplot as plt
from load_csv import load


def get_values(row):
    """
        Take an array and return a new array with the values
        as float (replacing human readable format)
    """
    vals = []
    for i in row:
        vals.append(
            float(
                i.replace('k', 'e3')
                .replace('M', 'e6')
            )
        )
    return vals


def main():
    """
        Display a graph that compare the population projection
        of France vs Belgium
    """
    try:
        df = load("population_total.csv")
    except Exception as e:
        print(e)
        exit(0)

    # Check Dataframe
    if 'country' not in df.columns:
        print("Not the expected CSV file")
        exit(0)

    df = df.set_index('country')

    # Check that DF contains France
    if 'France' not in df.index or 'Belgium' not in df.index:
        print("Not the expected CSV file")
        exit(0)
    country_1 = df.loc['France']
    country_2 = df.loc['Belgium']

    # Check that every columns can be parsed as int
    try:
        [int(x) for x in country_1.index]
        [int(x) for x in country_2.index]
    except Exception:
        print("Not the expected CSV file")
        exit(0)

    def yformatter(x, pos):
        if x >= 1_000_000:
            return f'{int(x/1_000_000)}M'
        if x >= 100_000:
            return f'{int(x/1_000)}k'
        return str(x)
    plt.gca().yaxis.set_major_formatter(yformatter)

    plt.plot(
        country_1.index[:2050-1800],
        get_values(country_1[:2050-1800]),
        label='France',
        c='g'
    )
    plt.plot(
        country_2.index[:2050-1800],
        get_values(country_2[:2050-1800]),
        label='Belgium',
        c='b'
        )
    plt.title('Population Projections')
    plt.ylabel('Population')
    plt.xlabel('Year')
    plt.legend(loc="lower right")
    plt.xticks([x for x in country_1.index[:2050-1800] if (int(x) % 40 == 0)])
    plt.yticks([20_000_000, 40_000_000, 60_000_000])  # May vary
    plt.show()


if __name__ == "__main__":
    main()
