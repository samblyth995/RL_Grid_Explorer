#imports
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import plotly.express as px

#from Grid_game import GridEnvironment

#csv handing
def import_data_file(csv_file):
    
    df=pd.read_csv(csv_file)
    #print(df.head()) 
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
   
def visualize_agent_movement():
   
    # Create a figure and axis
    #df = px.data.gapminder()
    plot_data=[]
    frame = 0
    #truncate to last 100 rows 
    first_steps=steps_coordinates[:10]
    last_steps=steps_coordinates[-20:]
    steps_trunc=first_steps+last_steps
    for plot_step in steps_trunc:
        for x, y in plot_step:
            #0.5offsets the dot so it is in the centre of the plot grid squares
            plot_data.append({'x': x+0.5, 'y': y+0.5, 'frame': frame})
            frame += 1
    
    

    fig = px.scatter(plot_data, x='x', y='y', animation_frame='frame',
         range_x=[0, grid_size], range_y=[0, grid_size])
    fig.update_layout(title_font=dict(family='Droid Serif', size =20),title_text='Highlights of RL Agent Exploration On A Value Network',
                      legend_font=dict(family='Droid Serif',size=18 ),
                      legend_tracegroupgap=20, width=800, height =800) 
                      

    fig.update_traces(marker=dict(size=20, symbol='circle', color='blue',line_width=2))
    fig.add_scatter(x=[1.5], y=[1.5], mode='markers', marker=dict(color='#EECA3B', symbol='diamond', size=30),name ="Obstacle")
    
    fig.add_scatter(x=[5.5], y=[5.5], mode='markers', marker=dict(color='#66AA00', size=30, symbol='hexagram-open'),name ="Goal")
    
    fig.show()
    
#function calls
df=import_data_file("training_runs_optim_VALUE_6_X_6.csv")
data_prep(df)
#grid_env = GridEnvironment()
steps_coordinates= data_prep(df)  # This captures the return value into tuples_of_steps_coo
grid_size = 7

visualize_agent_movement()
