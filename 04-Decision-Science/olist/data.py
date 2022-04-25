import os
import pandas as pd


class Olist:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        # Hints 1: Build csv_path as "absolute path" in order to call this method from anywhere.
            # Do not hardcode your path as it only works on your machine ('Users/username/code...')
            # Use __file__ instead as an absolute path anchor independant of your usename
            # Make extensive use of `breakpoint()` to investigate what `__file__` variable is really
        # Hint 2: Use os.path library to construct path independent of Mac vs. Unix vs. Windows specificities

        # go up two levels from current directory and save directory name
        root_dir = os.path.dirname(os.path.dirname(__file__))
        # concatenate root_dir with relative path to csv files
        csv_path = os.path.join(root_dir, "data", "csv")


        # read in names of files in data folder
        file_names = []
        for file in os.listdir(csv_path):
            if file.endswith(".csv"):
                file_names.append(file)

        # for the key names unnecessary string elements are removed
        key_names = []
        for file in file_names:
            key_names.append(file.replace(".csv", "").replace("olist_", "").replace("_dataset",""))

        # create dict
        data = dict()
        for key, file in zip(key_names, file_names):
            data[key] = pd.read_csv(os.path.join(csv_path, file))

        return data

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")

    def file_test(self):
        return(__file__)
