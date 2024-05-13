import pandas as pd
import matplotlib.pyplot as plt
import os


# Set the path to the folder containing the CSV files
folder_path = "C:/Users/xxi1/Desktop/single_tree_burning/read_file/CSVfiles"

    # read .fds file
file_path = os.path.join(folder_path, "raw.fds")
with open(file_path) as file:
    # use read() to read the txt in the file
    fds_file = file.read()

# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a CSV file
    if filename.endswith(".csv"):
        # Get the full path to the file
        file_path = os.path.join(folder_path, filename)

        #get the file name without .csv
        filename = filename[:-4]

        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Filter the DataFrame to only include rows where time is greater than 0
        filtered_df = df[df['Time (s)'] > 0]

        # Reset the index of the filtered DataFrame to start from 0
        filtered_df = filtered_df.reset_index(drop=True)

        # Create the output string
        output_string = ''
        for i in range(filtered_df.index.start,filtered_df.index.stop):
            output_string += f"&RAMP ID='burner_RAMP_Q', T={filtered_df['Time (s)'][i]}, F={filtered_df['Heat Release Rate (kW)'][i]}\n"
        # Create a new directory
        os.mkdir(filename)
        print(filename)

        for meshSize in [10,20,30]:
          print(meshSize)

          path_file_mesh_size = filename+'/'+str(meshSize)
          os.mkdir(path_file_mesh_size)

          filtered_df.to_csv(path_file_mesh_size+'/experiment.csv', index = False)


          # #create the output ramp file path
          file_path = os.path.join(filename)

          # Write the output string to a text file
          with open(path_file_mesh_size+'/RAMP.txt', 'w') as f:
              f.write(output_string)

          search_text = "&MESH ID='Mesh01', IJK=50,50,50, XB=0.0,3.0,0.0,3.0,0.0,3.0/"
          replace_text = f"&MESH ID='Mesh01', IJK={meshSize},{meshSize},{meshSize}, XB=0.0,3.0,0.0,3.0,0.0,3.0/"
          fds_file = fds_file.replace(search_text, replace_text)
          with open(path_file_mesh_size+'/output.fds', 'w') as f:
              f.write(fds_file)

        