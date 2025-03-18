# 🌳 Forest Cover Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![RandomForest](https://img.shields.io/badge/RandomForest-Algorithm-green)


## 📌 Project Overview
This project predicts **forest cover type** based on geographic and ecological features using a **Random Forest Classifier**. The dataset includes topographical and soil-related attributes, and the model is trained to classify different cover types.

## 🚀 Features
✅ Utilizes **Random Forest Classifier** for high accuracy.  
✅ Processes categorical variables using **One-Hot Encoding**.  
✅ Implements a **Scikit-Learn Pipeline** for efficient preprocessing & modeling.  
✅ Saves the trained model using **Pickle** for future inference.  
✅ Can be deployed in real-world applications for environmental studies.  

## 📂 Repository Structure
```
Forest-Cover-Prediction/
│-- data/                       # Dataset (place dataset files here)
│-- models/                     # Trained models stored here
│-- forest_cover_infer.ipynb    # Model training and preprocessing script
│-- forest_gr.py                # Web interface for predictions 
│-- requirements.txt            # Dependencies
│-- README.md                   # Project documentation


## 📥 Installation
To run this project, clone the repository and install dependencies:
```sh
git clone <https://github.com/VedantRD007/forest-cover-prediction.git>
cd Forest-Cover-Prediction
pip install -r requirements.txt
```

## 🏋️ Training the Model
To train the model on your dataset, run:
```sh
python forest_cover_infer.ipynb
```
## 🎨 Running the Gradio App
To launch the web interface for classification:
```sh
python forest_gr.py
```


## 📊 Dependencies
Ensure you have the following installed (listed in `requirements.txt`):
```
pandas
numpy
scikit-learn
pickle
```

## ☁️ Deployment
This model can be deployed on platforms like:
- **Flask API** (for web-based interaction)
- **AWS Lambda** (serverless execution)
- **Streamlit** (interactive dashboard for predictions)

## 🤝 Contributing
Contributions are welcome! Feel free to submit issues or pull requests to enhance the project.


