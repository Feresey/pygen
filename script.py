import os
import tokenize
import pickle
import argparse


def findFiles(**kwargs):
    files_num = kwargs['files_num']
    dir = kwargs['dir']

    arr_paths = []
    for dirpath, _, filenames in os.walk(dir):
        actual_filenames = [f for f in filenames if f.endswith(".py")]
        for filename in actual_filenames:
            arr_paths.append(os.path.join(dirpath, filename))
            if len(arr_paths) == files_num:
                return arr_paths


def aggFilesToFile(paths):
    data = []
    for p in paths:
        with open(p, 'rb') as f:
            for s in tokenize.tokenize(f.readline):
                data.append(s.string.split(' '))
    data = [i for s in data for i in s]
    with open("final.txt", "wb") as fp:
        pickle.dump(data, fp)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='py150_files/data/')
    parser.add_argument('--files_num', type=int, default=1000)

    args = vars(parser.parse_args())

    paths = findFiles(**args)
    aggFilesToFile(paths)
