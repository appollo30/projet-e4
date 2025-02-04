import glob
import pandas as pd
from src.avro_to_csv import load_avro, make_records_df

def main():
    """
    Prend toutes les données avro dans le dossier data/input, les charge, 
    les transforme en DataFrame et les concatène.
    Le DataFrame est ensuite sauvegardé dans data/cleaned/records.csv
    """
    file_paths = glob.glob("data/input/*.avro")

    records = []

    for file_path in file_paths:
        record_df = make_records_df(load_avro(file_path))
        records.append(record_df)

    records_df = pd.concat(records)

    records_df.to_csv("data/cleaned/records.csv", index=False)

if __name__ == "__main__":
    main()
