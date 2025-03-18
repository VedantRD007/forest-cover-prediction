
import gradio as gr
import pickle 
import numpy as np
import pandas as pd


def predict(Elevation, Aspect, Slope, Horizontal_Distance_To_Hydrology,
       Vertical_Distance_To_Hydrology, Horizontal_Distance_To_Roadways,
       Hillshade_9am, Hillshade_Noon, Hillshade_3pm,
       Horizontal_Distance_To_Fire_Points, Wilderness_Area, Soil_Type):
    tst = pd.DataFrame([[Elevation, Aspect, Slope, Horizontal_Distance_To_Hydrology,
       Vertical_Distance_To_Hydrology, Horizontal_Distance_To_Roadways,
       Hillshade_9am, Hillshade_Noon, Hillshade_3pm,
       Horizontal_Distance_To_Fire_Points, Wilderness_Area, Soil_Type]],
          columns=['Elevation', 'Aspect', 'Slope', 'Horizontal_Distance_To_Hydrology',
       'Vertical_Distance_To_Hydrology', 'Horizontal_Distance_To_Roadways',
       'Hillshade_9am', 'Hillshade_Noon', 'Hillshade_3pm',
       'Horizontal_Distance_To_Fire_Points', 'Wilderness_Area', 'Soil_Type'])    
    filehandler = open("forest.pkl", "rb")
    bm_loaded = pickle.load(filehandler)
    filehandler.close()
    return bm_loaded.predict(tst)[0] 
      


with gr.Blocks() as demo:
    with gr.Row():
      Elevation = gr.Number(label='Elevation')
      Aspect = gr.Number(label='Aspect')
      Slope = gr.Number(label='Slope')
    with gr.Row():
      Horizontal_Distance_To_Hydrology = gr.Number(label='Horizontal Distance To Hydrology')
      Vertical_Distance_To_Hydrology = gr.Number(label='Vertical Distance To Hydrology')
      Horizontal_Distance_To_Roadways = gr.Number(label='Horizontal Distance To Roadways')
    with gr.Row():
      Hillshade_9am = gr.Number(label='Hillshade 9 am')
      Hillshade_Noon = gr.Number(label='Hillshade Noon')
      Hillshade_3pm = gr.Number(label='Hillshade 3 pm')
    with gr.Row():
      Horizontal_Distance_To_Fire_Points = gr.Number(label='Horizontal Distance To Fire_Points')
      Wilderness_Area = gr.Dropdown(label='Wilderness Area', choices=[1,2,3,4])
      Soil_Type = gr.Dropdown(label='Soil Type', choices=list(np.arange(1,41)))
    with gr.Row(): 
      Cover = gr.Text(label='Cover Type:') 
    with gr.Row():  
      button = gr.Button(value="Which Cover Type?")
      button.click(predict,
            inputs=[Elevation, Aspect, Slope, Horizontal_Distance_To_Hydrology,
       Vertical_Distance_To_Hydrology, Horizontal_Distance_To_Roadways,
       Hillshade_9am, Hillshade_Noon, Hillshade_3pm,
       Horizontal_Distance_To_Fire_Points, Wilderness_Area, Soil_Type],
            outputs=[Cover])



demo.launch()