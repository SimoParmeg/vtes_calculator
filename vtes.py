import os
import pandas as pd
import re


CSV_FILES = [f for f in os.listdir('input') if f.endswith('.csv')]

def findReplace(csv_file):
    with open(csv_file, 'r') as f:
        orig_csv = f.read()
    
    new_csv = re.sub(',', '.', orig_csv)

    with open(csv_file, 'w') as f:
        f.write(new_csv)


def calculate_tournament_points(path, name):
    df = pd.read_csv(path, sep=';')
    # print(df.dtypes)
    numero_giocatori = len(df.index)

    if numero_giocatori < 20:
        x = 15
    elif numero_giocatori < 30:
        x = 10
    else:
        x = 5

    df['TournamentPoints'] = ((numero_giocatori / 10) * (df['VP'] + 1)) + (df['GW'] * x)
    df.loc[df['Final'].idxmax(), 'TournamentPoints'] += 50

    df.to_csv(f"./output/{name}", sep=';')


if __name__ == "__main__":
    if not os.path.exists('output'):
        os.mkdir('output')

    print(CSV_FILES)
    for filename in CSV_FILES:
        filepath = os.path.join('input/', filename)
        findReplace(filepath)
        calculate_tournament_points(filepath, filename)
    