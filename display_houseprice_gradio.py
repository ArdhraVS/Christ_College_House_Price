import gradio as gr
import joblib
import pandas as pd
import os

# Load model
model = joblib.load("MultilinearRegression_HousePrice_model.pkl")

def predict_result(area, bedrooms, floors):

    input_data = pd.DataFrame({
        "Area": [area],
        "Bedrooms": [bedrooms],
        "Floors" : [floors]
    })

    prediction = model.predict(input_data)[0]

demo = gr.Interface(
    fn=predict_result,

    inputs=[
        gr.Number(
            label="Enter Area",
            minimum=300,
            maximum=3000,
            value=300
        ),

        gr.Number(
            label="Enter number of bedrooms",
            minimum=0,
            maximum=10,
            value=3
        ),
        gr.Number(
            label="Enter number of floors",
            minimum=0,
            maximum=10,
            value=3
        )
    ],

    outputs=gr.Textbox(label="Prediction"),

    title="House price Prediction",

    description="Predict House Price based on Area, Bedrooms, and Floors"
)


if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )
