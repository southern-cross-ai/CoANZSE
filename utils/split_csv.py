import argparse
import os
import pandas as pd

def split_csv(load_path, num_chunk, save_path='.', old_sep='|', new_sep=','):
    if save_path is None:
        # if no save path is specified, save to the current directory
        save_path = '.'
    elif not os.path.exists(save_path):
        # create save path if it does not exist
        os.makedirs(save_path, exist_ok=True)
        
    # unzip and save into CSV files if necessary
    if load_path.split('.')[-1] == 'gz':
        print(f'Unzipping {load_path}')
        os.system(f'gzip -d -k {load_path}')
        load_path = load_path.replace('.gz', '')
        print(f'Saved into {load_path}\n')

    # calculate the chunk size of each CSV file
    num_rows = int(os.popen(f'wc -l {load_path}').read().split()[0])
    chunk_size = int(num_rows / num_chunk)
    print(f"{num_rows} rows in total. Each CSV file will approximately have {chunk_size} rows.\n")
    
    # read the large CSV file
    print(f"Loading from {load_path}")
    df = pd.read_csv(load_path, sep=old_sep, chunksize=chunk_size)
    
    # save into small CSV files
    for i, chunk in enumerate(df):
        file_name = load_path.split('/')[-1].replace('.csv', f'_{i}.csv')
        full_path = f'{save_path}/{file_name}'
        print(f"Splitting and saving into {full_path}")
        chunk.to_csv(full_path, sep=new_sep, index=False)
    
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--load_path', type=str, required=True,
                        help='Load your large CSV/GZ file from this path. \
                            If it is a GZ file, it will be automatically unzipped.')
    parser.add_argument('-s', '--save_path', type=str, required=False, default=None,
                        help='Save split CSV files into this path. \
                            Default path is the current path.')
    parser.add_argument('-n', '--num_chunk', type=int, required=False, default=4,
                        help='Number of CSV files you want to split the large CSV file into. \
                        Default number is 4.')
    parser.add_argument('--old_sep', type=str, required=False, default='|',
                        help='Separators used in your large CSV file. \
                        Default separator is "|".')
    parser.add_argument('--new_sep', type=str, required=False, default=',',
                        help='New separators used in your split CSV files. \
                        Default separator is ",".')
    args = parser.parse_args()
    split_csv(args.load_path, args.num_chunk, args.save_path, args.old_sep, args.new_sep)
    