from pathlib import Path
# from matplotlib.ticker import MaxNLocator
import pandas as pd
# import matplotlib.pyplot as plt

IMDB_TOP_1000_CSV_PATH = Path(__file__).parent / "imdb_top_1000.csv"

pd.set_option("display.max_rows", 20)
pd.set_option("display.min_rows", 20)
pd.set_option("display.width", None)


def load_movies() -> pd.DataFrame:
    df = pd.read_csv(IMDB_TOP_1000_CSV_PATH)
    df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors="coerce")
    df["Released_Year"] = df["Released_Year"].fillna(-1).astype(int)
    return df


def print_section(title: str) -> None:
    print(f"\n--- {title} ---")


def run_analysis(df: pd.DataFrame) -> None:
    # Task 1: Display movies released after 2018
    print_section("Movies released after 2018")
    recent_movies = df[df["Released_Year"] > 2018]
    print(recent_movies[["Director", "Series_Title", "Released_Year"]])

    # Task 2: Display 10 directors with the most movies
    print_section("Top 10 directors by movie count")
    print(df["Director"].value_counts().head(10))

    # Task 3: Find year with the most movies released and display titles
    print_section("Year with the most releases and movie titles")
    top_year = df["Released_Year"].value_counts().idxmax()
    movies_from_top_year = df[df["Released_Year"] == top_year]
    print(movies_from_top_year[["Series_Title", "Released_Year"]])

    # Task 4: Sort movies by year from the oldest to the newest, after that sort by title
    print_section("Movies sorted by year and title")
    sorted_df = df.sort_values(
        by=["Released_Year", "Series_Title"], ascending=True
    )
    print(sorted_df[["Series_Title", "Released_Year"]])

    # Task 5: Find the best rated movie from the 2000s and sort them by rating (ascending)
    print_section("Best rated movies from the 2000s")
    movies_from_2000s = df[df["Released_Year"] >= 2000].sort_values(
        by="IMDB_Rating", ascending=False
    )
    print(movies_from_2000s[[
        "Series_Title",
        "Director",
        "IMDB_Rating"
    ]].head(10))

    # Task 6: Find 5 years in which movies had the most mean votes
    print_section("Top 5 years by mean IMDB rating")
    mean_ratings_by_year = df.groupby("Released_Year")["IMDB_Rating"].mean()
    print(mean_ratings_by_year.nlargest(5))

    # Task 7: Find 5 years in which movies had the most mean votes but take only years from 2000
    print_section("Top 5 years (>= 2000) by mean IMDB rating")
    mean_ratings_since_2000 = df[
        df["Released_Year"] >= 2000
    ].groupby("Released_Year")["IMDB_Rating"].mean()
    print(mean_ratings_since_2000.nlargest(5))

    # Task 8: Find 5 best years from 2000 and title of best movie in each and add those data into new dataframe
    print_section("Best movie in each of top 5 years since 2000")
    top_years = mean_ratings_since_2000.nlargest(5).index
    best_movies_each_year = pd.concat(
        [
            df[df["Released_Year"] == year].nlargest(1, "IMDB_Rating")
            for year in top_years
        ],
        ignore_index=True,
    )
    print(best_movies_each_year[[
        "Series_Title",
        "Released_Year",
        "IMDB_Rating"
    ]])

    # Task 9: Find 10 actors that played in the most movies with rating greater than 8.0
    print_section("Top 10 actors in movies rated >= 8.0")
    high_rated = df[df["IMDB_Rating"] >= 8.0]
    all_actors = (
        high_rated[["Star1", "Star2", "Star3", "Star4"]]
        .melt(value_name="Actor")
        .drop("variable", axis=1)
    )
    print(all_actors.value_counts().nlargest(10))

    # Task 10: Find 10 directors that directed the most movies with rating greater than 8.0
    print_section("Top 10 directors in movies rated >= 8.0")
    high_rated_directors = high_rated[["Director"]].value_counts()
    print(high_rated_directors.nlargest(10))

    # Task 11: Find 10 directors that directed the most movies that were released in 2000 or later
    #  with rating greater than 8.0
    print_section(
        "Top 10 directors in movies rated >= 8.0 released since 2000"
    )
    high_rated_since_2000 = df[
        (df["IMDB_Rating"] >= 8.0) &
        (df["Released_Year"] >= 2000)
    ]
    print(high_rated_since_2000[["Director"]].value_counts().nlargest(10))

    # Task 12: Find number of movies from each year starting from 1990
    print_section("Movie counts by year from 1990")
    movie_counts = df[
        df["Released_Year"] >= 1990
    ].groupby("Released_Year").size()
    print(movie_counts)


def main() -> None:
    movies = load_movies()
    run_analysis(movies)


if __name__ == "__main__":
    main()


# Jupyter notes:
# movie_counts.plot(kind="bar", color="blue")
# plt.title("Number of movies from each year starting from 1990")
# plt.xlabel("Year")
# plt.ylabel("Number of movies")
# plt.grid(True)
# plt.show()
#
# runtimes = df["Runtime"].str.replace(" min", "").astype(int).sort_values()
# plt.hist(runtimes, bins=10, color="blue", edgecolor="black")
# plt.xlabel("Runtime (minutes)")
# plt.ylabel("Number of movies")
# plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=10))
# plt.show()
