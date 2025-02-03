# 🩺 Fetal Health Classification  

## 📌 Project Overview  
Accurate **fetal health classification** is critical in prenatal care, helping healthcare professionals detect potential complications early. This project leverages **machine learning, specifically the Random Forest algorithm**, to classify fetal health conditions based on physiological measurements.  

The solution includes **data preprocessing, model training, hyperparameter tuning, and a Flask-based web application** for real-time predictions. The project is also **containerized using Docker** for seamless deployment.

---

## 📊 Dataset and Preprocessing  
The dataset consists of multiple physiological features used to determine fetal health. The key preprocessing steps include:  

- **Feature Selection:** The target variable (`fetal_health`) is separated from the feature matrix (`X`).  
- **Normalization:** StandardScaler is applied to ensure features have a uniform scale, preventing dominance by any particular feature.  
- **Data Splitting:** A 70-30 train-test split is used to validate the model.  
- **Saving Scaler:** The `scaler.sav` file is created to ensure consistent scaling for new predictions.  

---

## 🌳 Model Training & Performance  

The **Random Forest classifier** is chosen for its robustness and ability to handle complex decision boundaries.  

### 🔹 Initial Training:  
- **Model:** Random Forest with default parameters.  
- **Validation:** Cross-validation to assess generalization.  
- **Accuracy:** **93.8%**  

### 🔹 Hyperparameter Tuning (GridSearchCV):  
To improve performance, the following parameters were optimized:  
- Number of estimators  
- Maximum depth  
- Feature selection strategy  
- Splitting criterion (Gini vs. Entropy)  
- Parallel processing settings  

✅ **Final Accuracy After Tuning:** **94.35%**  

---

## 🚀 Flask Web Application  

A **Flask-based web app** was developed to provide a simple interface for users to interact with the model.  

### 🔹 Features:  
- **Home Page (`/`)** – Displays the landing page.  
- **Exploratory Data Analysis (`/eda`)** – Visualizes insights from the dataset.  
- **Prediction (`/predictions`)** – Accepts user inputs, scales them, and returns fetal health predictions.  

### 🔹 Implementation:  
- **Model and Scaler Loading:** Pre-trained model is loaded via `pickle`.  
- **Flask Initialization:** `app = Flask(__name__)` is used for routing.  
- **Deployment:** Runs on `0.0.0.0:5000` in debug mode.  

---

## 🐳 Docker Deployment  

The Flask app is containerized using **Docker**, making it easy to deploy anywhere.  

### 🔹 Build the Docker Image:  
```sh
docker build -t fetal-health .
```  

### 🔹 Run the Container:  
```sh
docker run -p 5000:5000 fetal-health
```  

📍 **Access the Web App:** Open `http://localhost:5000` in a browser.  

---

## 📌 Summary  

✅ **Machine Learning Model:** Random Forest (94.35% accuracy)  
✅ **Tech Stack:** Python, Flask, Docker  
✅ **Functionality:** Data preprocessing, model training, hyperparameter tuning, and web-based prediction  
✅ **Deployment:** Dockerized Flask API for seamless accessibility  

This project serves as an end-to-end solution for fetal health classification, combining **machine learning, web development, and containerization** to create an efficient and scalable tool.  

💡 **Future Improvements:**  
- Integrate additional models (e.g., XGBoost, Deep Learning) for better accuracy.  
- Enhance the web interface with interactive visualizations.  
- Deploy the model using cloud platforms (e.g., AWS, GCP).  

---

### 📬 Contributions & Feedback  
Feel free to contribute, suggest improvements, or report issues! 🚀  
