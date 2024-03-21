#imports
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import plotly.express as px
import plotly.graph_objects as go

#from Grid_game import GridEnvironment

#csv handing
def import_data_file(csv_file, csv_file2,csv_file3):
    
    df1=pd.read_csv(csv_file)
    df2=pd.read_csv(csv_file2)
    df3=pd.read_csv(csv_file3)
    #print(df.head()) 
    return df1, df2, df3


#data prep
def data_prep1(df):
    tuples_of_steps_coo_df1=[]
    for index, row in df.iterrows():
        coordinate_pairs = row['Path'].split(';')

        indvidual_steps_coo = []
        for pair in coordinate_pairs:
            coordinate_tuple = tuple(map(int, pair.strip('()').split(',')))
            # Strip parentheses and convert pair to tuple
            indvidual_steps_coo.append(coordinate_tuple)
        tuples_of_steps_coo_df1.append(indvidual_steps_coo)
    return tuples_of_steps_coo_df1

    #print(tuples_of_steps_coo)

#prep csv 2

def data_prep2(df):
    tuples_of_steps_coo_df2_policy=[]
    for index, row in df.iterrows():
        coordinate_pairs = row['Path'].split(';')

        indvidual_steps_coo = []
        for pair in coordinate_pairs:
            coordinate_tuple = tuple(map(int, pair.strip('()').split(',')))
            # Strip parentheses and convert pair to tuple
            indvidual_steps_coo.append(coordinate_tuple)
        tuples_of_steps_coo_df2_policy.append(indvidual_steps_coo)
    return tuples_of_steps_coo_df2_policy

#prep csv 3

def data_prep3(df):
    tuples_of_steps_coo_df2_QNET=[]
    for index, row in df.iterrows():
        coordinate_pairs = row['Path'].split(';')

        indvidual_steps_coo = []
        for pair in coordinate_pairs:
            coordinate_tuple = tuple(map(int, pair.strip('()').split(',')))
            # Strip parentheses and convert pair to tuple
            indvidual_steps_coo.append(coordinate_tuple)
        tuples_of_steps_coo_df2_QNET.append(indvidual_steps_coo)
    return tuples_of_steps_coo_df2_QNET


def build_df_for_vis(steps_coordinates_value, steps_coordinates_policy, steps_coordinates_QNET):
    # Create a figure and axis
    #df = px.data.gapminder()
    agent_name='Value'
    plot_data_value=[]
    frame = 0
    #truncate to last 100 rows 
    first_steps=steps_coordinates_value[:10]
    last_steps=steps_coordinates_value[-20:]
    steps_trunc=first_steps+last_steps
    for plot_step in steps_trunc:
        for x, y in plot_step:
            #0.5offsets the dot so it is in the centre of the plot grid squares
            plot_data_value.append({'Agent':agent_name,'x': x+0.5, 'y': y+0.5, 'frame': frame})
            frame += 1

    agent_name='Policy'
    plot_data_policy=[]
    frame = 0
    #truncate to last 100 rows 
    first_steps=steps_coordinates_policy[:10]
    last_steps=steps_coordinates_policy[-20:]
    steps_trunc=first_steps+last_steps
    for plot_step in steps_trunc:
        for x, y in plot_step:
            #0.5offsets the dot so it is in the centre of the plot grid squares
            plot_data_policy.append({'Agent':agent_name,'x': x+0.5, 'y': y+0.5, 'frame': frame})
            frame += 1

    
    agent_name='QNET'
    plot_data_QNET=[]
    frame = 0
    #truncate to last 100 rows 
    first_steps=steps_coordinates_QNET[:10]
    last_steps=steps_coordinates_QNET[-20:]
    steps_trunc=first_steps+last_steps
    for plot_step in steps_trunc:
        for x, y in plot_step:
            #0.5offsets the dot so it is in the centre of the plot grid squares
            plot_data_QNET.append({'Agent':agent_name,'x': x+0.5, 'y': y+0.5, 'frame': frame})
            frame += 1
    ##join all the lists
    plot_data = plot_data_value+plot_data_policy+plot_data_QNET   
    return plot_data



#visualization
   
def visualize_agent_movement(plot_data):

    
    #############visualisation########

    fig = px.scatter(plot_data, x='x', y='y', animation_frame='frame', color='Agent',
            range_x=[0, grid_size], range_y=[0, grid_size])
    fig.update_layout(title_font=dict(family='Droid Serif', size =20),title_text='Highlights of RL Agent Exploration On A Value Network',
                        legend_font=dict(family='Droid Serif',size=18 ),
                        legend_tracegroupgap=20, width=800, height =800) 
                        

    fig.update_traces(marker=dict(size=20, symbol='circle', line_width=2))
    fig.add_scatter(x=[1.5], y=[1.5], mode='markers', marker=dict(color='#EECA3B', symbol='diamond', size=30),name ="Obstacle")

    fig.add_scatter(x=[5.5], y=[5.5], mode='markers', marker=dict(color='#66AA00', size=30, symbol='hexagram-open'),name ="Goal")

    fig.show(autoplay=True)

#function calls
df1, df2, df3 =import_data_file("training_runs_optim_VALUE_6_X_6.csv","training_runs_optim_POLICY_6_X_6.csv", "training_runs_optim_QNET_6_X_6.csv")
data_prep1(df1)
data_prep2(df2)
data_prep2(df3)


#grid_env = GridEnvironment()
steps_coordinates_value= data_prep1(df1)
steps_coordinates_policy=data_prep2(df2)
steps_coordinates_QNET=data_prep3(df3)
  # This captures the return value into tuples_of_steps_coo
grid_size = 7
plot_data = build_df_for_vis(steps_coordinates_value, steps_coordinates_policy,steps_coordinates_QNET)
visualize_agent_movement(plot_data)
