"""
Dépendances:
fastavro
pandas

taper "pip install fastavro pandas"

Utilisation : 
taper "python avro_to_csv.py chemin/vers/fichier.avro accelerometer" si vous voulez les données d'accéleromètre, sinon
mettez 'gyroscope', 'eda', 'temperature', 'tags', 'bvp', 'systolicPeaks' ou 'steps' pour les autres options
Le fichier sera ensuite écrit dans le dossier data/output avec le même nom que le fichier avro mais en csv
"""

import json
import argparse
import os
from typing import Dict
from datetime import datetime, timedelta
from fastavro import reader
import pandas as pd

def load_avro(file_path : str) -> Dict:
    """
    Chargement du fichier avro, et retourne les données sous forme de json

    Args:
        file_path (str): chemin vers le fichier avro

    Returns:
        Dict: Le json contenant les données
    """
    with open(file_path, "rb") as f:
        avro_reader = reader(f)
        records = list(avro_reader)[0]
    return records

def write_json(file_path : str, records : Dict):
    """
    Écrit les données dans un fichier json

    Args:
        file_path (str): chemin vers le fichier json à écrire
        records (Dict): les données à écrire
    """
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(records['rawData'],f,ensure_ascii=True,indent=True)

def make_records_df(records : Dict,field : str = "accelerometer") -> pd.DataFrame:
    """
    Crée un DataFrame à partir des données du fichier avro

    Args:
        records (Dict): Les données du fichier avro
        field (str): Le champ que l'on veut utiliser (accelerometer, temperature, ...)

    Returns:
        pd.DataFrame: Le DataFrame contenant les données
    """
    if field not in records["rawData"].keys():
        print(f"Field {field} is unavailable")
        return None
    
    timestamp_start = datetime.fromtimestamp(records["rawData"][field]["timestampStart"]/1_000_000) # On convertit les milisecondes en secondes
    sampling_period = round(1/records["rawData"][field]["samplingFrequency"],4)
    
    if field == "accelerometer":
        n = len(records["rawData"][field]["x"])
        result = {
            "time" : [timestamp_start + timedelta(seconds = sampling_period*i) for i in range(n)],
            "accel_x" : records["rawData"][field]["x"],
            "accel_y" : records["rawData"][field]["y"],
            "accel_z" : records["rawData"][field]["z"]
        }
    else:
        n = len(records["rawData"][field]["values"])
        result = {
            "time" : [timestamp_start + sampling_period*i for i in range(n)],
            field : records["rawData"][field]["values"]
        }
    
    return pd.DataFrame(result)

def main():
    """
    Fonction main qui permet de convertir un fichier avro en csv
    """
    parser = argparse.ArgumentParser(description="Write one file path for your avro file and the field that you want to make a csv for")
    
    parser.add_argument('file_path', type=str, help=".avro file path")
    parser.add_argument('field', type=str, help="The field that you want to use (accelerometer, temperature, ...)")
    args = parser.parse_args()
    
    split_path = args.file_path.split(os.sep)
    split_path[-2] = "output"
    output_path = f"{os.path.splitext(os.sep.join(split_path))[0]}.csv"
    
    records = load_avro(args.file_path)
    records_df = make_records_df(records,args.field)
    records_df.to_csv(output_path,index=False)
    
if __name__ == "__main__":
    main()