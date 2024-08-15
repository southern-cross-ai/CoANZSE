import os
import re

import numpy as np


def list_files(directory):
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            if re.match(r".*textpos.*.csv", file):
                file_path = os.path.join(root, file)
                file_paths.append(file_path)
    return file_paths


def combine(csv_paths, save_path)
    all_csv = pd.DataFrame([])

    for file_path in csv_paths:
        print(f"Combining {file_path}")
        df = pd.read_csv(csv_paths[0], escapechar=',', header=None)
        all_csv = pd.concat((all_csv, df))

    print(f"Saving into {save_path + '/' + 'textpos.csv'}")
    all_csv.to_csv(save_path + '/' + 'textpos.csv', index=False, header=None, encoding='utf-8')
    


if __name__ == "__main__":
    # path for holding all csv files
    csv_path = '/Users/yifan/Documents/GitHub/github_dataset/CoANZSE/cleaned_dataset/csv'
    # path to save combined csv file
    save_path = '/Users/yifan/Documents/GitHub/github_dataset/CoANZSE/cleaned_dataset/csv'
    combine(list_files(csv_path), save_path)