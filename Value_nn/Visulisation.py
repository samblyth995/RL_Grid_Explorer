#imports
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#from Grid_game import GridEnvironment

#csv handing
def import_data_file(csv_file):
    
    df=pd.read_csv(csv_file)
    print(df.head()) 
    return df


#data prep
def data_prep(df):
    tuples_of_steps_coo=[]
    for index, row in df.iterrows():
        coordinate_pairs = row['Path'].split(';')

        indvidual_steps_coo = []
        for pair in coordinate_pairs:
            coordinate_tuple = tuple(map(int, pair.strip('()').split(',')))
            # Strip parentheses and convert pair to tuple
            indvidual_steps_coo.append(coordinate_tuple)
        tuples_of_steps_coo.append(indvidual_steps_coo)
    return tuples_of_steps_coo

    #print(tuples_of_steps_coo)
    

#visualization
    
def visualize_agent_movement(grid_size, steps_coordinates, interval=500):
   
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Initialize the grid
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

    # Function to update the animation
    def update(frame):
        ax.clear()
        for step_coo in steps_coordinates[:frame+1]:
            
            for x, y in step_coo:
                grid[y][x] = 'X'
                

        # Plot the grid
        for i in range(grid_size):
            
            for j in range(grid_size):
                ax.text(j, grid_size - i - 1, grid[i][j], ha='center', va='center')
                ax.set_xticks([i + 0.5 for i in range(grid_size)])
                ax.set_yticks([i + 0.5 for i in range(grid_size)])
                ax.grid(True)
                
        return

    # Create animation
    ani = FuncAnimation(fig, update, frames=len(steps_coordinates), interval=interval)

    plt.show()
    print("Visualization complete!")

    
#function calls
df=import_data_file("training_runs_optim_VALUE_6_X_6.csv")
data_prep(df)
#grid_env = GridEnvironment()
steps_coordinates= data_prep(df)  # This captures the return value into tuples_of_steps_coo
grid_size = 7
visualize_agent_movement(grid_size,steps_coordinates)
