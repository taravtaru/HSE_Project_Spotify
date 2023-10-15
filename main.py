import pandas as pd
import argparse
from typing import List, Dict

def open_file(path: str) -> List[List[object]]:
    df = pd.read_csv(path)

    return df.values.tolist()

def most_popular_artist(table: List[List[object]]):
    songs_count = {}
    for i in table:
        if i[7] in songs_count:
            songs_count[i[7]] += 1
        else:
            songs_count[i[7]] = 1
    return max(songs_count, key=songs_count.get)

def get_year_stats(table: List[List[object]]) -> Dict:
    years_count = {}
    for i in table:
        if i[1] in years_count:
            years_count[i[1]] += 1
        else:
            years_count[i[1]] = 1
    return years_count


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="our cute spotify experience")

    parser.add_argument("file_path", type=str, help="input path to the table")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-n", "--number", action="store_true")

    args = parser.parse_args()

    table = open_file(args.file_path)
    if args.verbose:
        print('The amount of songs for each year: ' + str(get_year_stats(table)))
    if args.number:
        print('The most popular artist: ' + most_popular_artist(table))
