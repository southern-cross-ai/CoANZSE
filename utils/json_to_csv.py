import json
import os
import re

import numpy as np


def list_files(directory):
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            if re.match(r".*textpos.*.json", file):
                file_path = os.path.join(root, file)
                file_paths.append(file_path)
    return file_paths


def clean(file_paths, csv_path):
    all_data = np.array([])
    
    for file_path in file_paths:
        print(f"Handling {file_path}")
        
        with open(file_path) as f:
            data = json.load(f)
        
        data = np.array(data)
        data = np.array([d['text'] for d in data])
        
        for i in range(len(data)):
            # e.g., g' day -> g'day
            data[i] = re.sub(r"\s'", "'", data[i], flags=re.IGNORECASE)
            # print(s)
            # e.g., remove [Music]
            data[i] = re.sub(r"(\[\w*\])\s", r" ", data[i], flags=re.IGNORECASE)
            # print(s)
            # capitalise the first letter
            data[i] = data[i][0].upper() + data[i][1:]
            # print(s)
            # remove any multiple spaces
            data[i] = re.sub(r"\s{2,}", r" ", data[i])
            # print(s)
            # change i into I
            data[i] = re.sub(r" i ", r" I ", data[i])
            # print(s)
            # e.g., change "i've" into "I've"
            data[i] = re.sub(r"i'(\w+)", r"I'\1", data[i])
            # print(s)
            # remove " _" at the very end
            data[i] = data[i][:-2]
            # print(s)
        
        print(f"Saving into {csv_path + '/' + file_path.split('/')[-1].replace('.json', '.csv')}")
        np.savetxt(csv_path + '/' + file_path.split('/')[-1].replace('.json', '.csv'), data, delimiter=',', fmt="%s")
        all_data = np.hstack((all_data, data))

    print(f"Merging finished. Saving into {csv_path + '/' + 'textpos.csv'}")
    np.savetxt(csv_path + '/' + 'textpos.csv', all_data, delimiter=',', fmt="%s")

    
if __name__ == '__main__':
    # path for holding all json files
    directory = "/Users/yifan/Documents/GitHub/github_dataset/CoANZSE/cleaned_dataset"
    # path to save transformed csv files
    csv_path = "/Users/yifan/Documents/GitHub/github_dataset/CoANZSE/cleaned_dataset"
    clean(list_files(directory), csv_path)