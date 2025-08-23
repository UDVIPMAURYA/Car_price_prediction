
# 🚗 Car Price Prediction App

A **Machine Learning Web Application** built with **Streamlit** that predicts car prices based on various features such as engine size, horsepower, fuel type, etc. The project demonstrates the complete workflow of data preprocessing, feature engineering, model building, evaluation, and deployment.

---

## 📌 Features

- Interactive **Streamlit Web App**
- Input car details manually and get an instant **Predicted Price**
- Multiple ML Models compared: Ridge, Lasso, RandomForest, XGBoost
- Best model automatically selected and deployed
- Beautiful **visualizations** for model evaluation and predictions
- Ready-to-deploy on **Streamlit Cloud / GitHub**

---

## 🛠 Tech Stack

- **Python 3.10+**
- **Streamlit**
- **Pandas, NumPy**
- **Scikit-learn**
- **XGBoost**
- **Matplotlib, Seaborn**
- **Joblib** (for saving/loading models)

---

## 📂 Project Structure

```
├── app.py                     # Streamlit App
├── best_carprice_model.joblib # Trained ML model pipeline
├── processed_data.csv         # Cleaned & Feature-engineered dataset
├── requirements.txt           # Dependencies
├── README.md                  # Project Documentation
└── notebooks/                 # Jupyter notebooks (EDA, training, evaluation)
```

---

## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/UDVIPMAURYA/car-price-prediction-app.git
   cd car-price-prediction-app
   ```

2. Create a virtual environment & activate:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate    # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## 📊 Model Performance

| Model        | R² Score | MAE (log-price) | RMSE (log-price) |
|--------------|----------|-----------------|------------------|
| Ridge        | 0.908    | 0.117           | 0.150            |
| Lasso        | 0.885    | 0.128           | 0.168            |
| RandomForest | 0.917    | 0.110           | 0.142            |
| XGBoost      | 0.925    | 0.107           | 0.135            |

✅ **XGBoost** performed the best and is used as the final deployed model.

---

## 📈 Visualizations

- **Actual vs Predicted Prices**
- **Distribution of Prices**
- **Cross-validation Scores Comparison**

---

## 🌐 Deployment

You can deploy this app easily on **Streamlit Cloud**:

1. Push code to GitHub
2. Go to [Streamlit Cloud](https://share.streamlit.io)
3. Select repository → branch → `app.py`
4. Deploy 🚀

The app will be live at:
```
https://udvipmaurya-car-price-prediction.streamlit.app
```

---

## 🤝 Contributing

Contributions are welcome!  
If you find a bug or want to improve this project, feel free to fork and open a pull request.

---

## 👨‍💻 Author

**Udvip Maurya**  
🎓 Diploma Student in Computer Science & Engineering  
💡 Passionate about Machine Learning & AI  
📧 Contact: udvipmaurya@gmail.com  

---

⭐ If you like this project, don’t forget to **star the repo** on GitHub!
