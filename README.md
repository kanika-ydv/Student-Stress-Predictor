# 🧠 Student Stress Level Predictor (ANN-Powered)

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Python](https://img.shields.io/badge/python-3.10-green)
![Deployment](https://img.shields.io/badge/deployment-live-orange)

An interactive, end-to-end Deep Learning web application designed to predict student stress levels based on 20 specialized factors. This project utilizes a **Multi-Layer Perceptron (Artificial Neural Network)** architecture to provide real-time mental health insights through a gamified 3D interface.

## 🚀 Live Demo: https://student-stress-predictor-phi.vercel.app/ 

---

## 📊 System Architecture
The project follows a modern decoupled architecture for high scalability and performance:

```mermaid
graph TD
    User((User)) -->|Inputs| UI[Interactive 3D UI - Vercel]
    UI -->|JSON Data| API[FastAPI - Render]
    API -->|Pre-process| Scaler[Standard Scaler]
    Scaler -->|Scaled Vector| Model[ANN MLP Model]
    Model -->|Class Prediction| API
    API -->|Response| UI
    UI -->|Visualization| Gauge[Percentage Gauge Meter]
