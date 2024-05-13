import pandas as pd
import matplotlib.pyplot as plt
import os

# Provide the root directory you want to start the search from
root_directory = 'C:/Users/xxi1/Desktop/single_tree_burning/read_file'

for root, dirs, files in os.walk(root_directory):
    # Check if both 'experiment.csv' and 'hrr.csv' exist in the current directory
    if 'examples_cat_hrr.csv' in files and 'experiment.csv' in files:
        experiment_csv_path = os.path.join(root, 'experiment.csv')
        simulation_csv_path = os.path.join(root, 'examples_cat_hrr.csv')
        df_exp = pd.read_csv(experiment_csv_path)
        df_sim = pd.read_csv(simulation_csv_path,skiprows=[0])

        plt.plot(df_sim['Time'] ,df_sim['HRR'] )
        plt.plot(df_exp['Time (s)'] ,df_exp['Heat Release Rate (kW)'] )
        plt.xlim([0,1])
        plt.savefig(f"{root}"+'.jpg')

        print(f"Found both 'experiment.csv' and 'hrr.csv' in: {root}")

