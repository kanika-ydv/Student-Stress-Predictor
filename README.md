# 🧠 Student Stress Level Predictor (ANN-Powered)

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Python](https://img.shields.io/badge/python-3.10-green)
![Deployment](https://img.shields.io/badge/deployment-live-orange)

An interactive, end-to-end Deep Learning web application designed to predict student stress levels based on 20 specialized factors. This project utilizes a **Multi-Layer Perceptron (Artificial Neural Network)** architecture to provide real-time mental health insights through a gamified 3D interface.

## 🚀 Live Demo: https://student-stress-predictor-phi.vercel.app/ 

---
## 📊 System Architecture
The project follows a modern decoupled architecture, where the frontend UI communicates with a dedicated Machine Learning API backend. The detailed workflow, from user input to result display, is illustrated below:

![System Architecture](./architecture.png)
### Workflow Breakdown:
1.  **Student Input:** The process begins with the student filling out the interactive test form on the Vercel-hosted frontend.
2.  **Data Collection & Preprocessing:** The backend API receives the raw input data, handles missing values, and scales the features using a Standard Scaler to prepare them for the model.
3.  **Feature Selection & Modeling:** The most relevant features are fed into the optimized Multi-Layer Perceptron (ANN) model hosted on Render.
4.  **Prediction & Display:** The model generates a stress level classification (Low, Moderate, High), which is sent back to the frontend and visualized instantly via the gauge meter and emoji indicators.
