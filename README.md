# 🎓 Student Performance Prediction Using ANN
🚀 **Live Interactive App:**
https://student-performance001.streamlit.app/

## 📌 About the Project

This project is about predicting a student's **final grade** using an Artificial Neural Network (ANN).

The model uses different student-related information such as study hours, attendance, previous grades, sleep, motivation, time management, and other factors to predict the student's final performance.

The main goal of this project is to build a machine learning model that can learn from student data and give a predicted final grade out of **100**.

---

## 🚀 What We Did

In this project, we completed the following steps:

* 🧹 Cleaned and prepared the data
* 🔤 Converted categorical data into numerical form
* 📏 Scaled the input features using `StandardScaler`
* 🧠 Built an Artificial Neural Network
* 🔬 Tested different ANN architectures
* 📊 Compared model performance
* ✅ Selected the best-performing model
* 🎯 Tested the model on unseen data
* 👤 Created an interactive user-input prediction system
* ⚠️ Added input validation and error handling

---

## 🧠 ANN Architectures Tested

We tested three different neural network architectures:

| Model   | Architecture           |
| ------- | ---------------------- |
| Model 1 | 32 → 64 → 32 → 1       |
| Model 2 | 32 → 128 → 64 → 1      |
| Model 3 | 32 → 128 → 64 → 32 → 1 |

After comparing the results, **32 → 64 → 32 → 1** performed the best.

---

## 🏆 Best Model Results

| Metric |   Score |
| ------ | ------: |
| MAE    |  4.0172 |
| MSE    | 25.2974 |
| RMSE   |  5.0297 |

The model with the lowest error was selected as the final model.

---

## 📋 Features Used

The model uses the following student information:

* Age
* Study Hours
* Attendance
* Sleep Hours
* Previous Grade
* Assignments Completed
* Practice Tests Taken
* Group Study Hours
* Notes Quality
* Time Management
* Motivation Level
* Mental Health Score
* Screen Time
* Social Media Hours
* Family Income
* Parent Education
* Internet Access
* Gender
* Device Type
* School Type
* Extracurricular Activities

---

## ⚙️ How the Prediction Works

The system follows a simple process:

**👤 User Input**
↓
**✅ Input Validation**
↓
**🔤 Feature Encoding**
↓
**📏 Feature Scaling**
↓
**🧠 ANN Model**
↓
**🎯 Predicted Final Grade**

The final result is shown as a score **out of 100**.

---

## 🛠️ Technologies Used

* 🐍 Python
* 🐼 Pandas
* 🔢 NumPy
* 🤖 TensorFlow / Keras
* 📊 Scikit-learn
* 📈 Matplotlib
* 📓 Jupyter Notebook

---

## 📁 Project Files

```text
Student-Performance-ANN/
│
├── notebook.ipynb
├── app.py
├── student_performance_model.keras
├── student_scaler.pkl
├── requirements.txt
└── README.md
```

### 📄 File Description

**`notebook.ipynb`**
Contains data preprocessing, model training, architecture comparison, evaluation, graphs, and results.

**`app.py`**
Contains the interactive prediction system.

**`student_performance_model.keras`**
The trained ANN model used for making predictions.

**`student_scaler.pkl`**
The StandardScaler used to prepare user input before prediction.

**`requirements.txt`**
Contains the Python libraries required to run the project.

**`README.md`**
Project information and documentation.

---

## 📊 Model Evaluation

The models were evaluated using:

### MAE — Mean Absolute Error

Shows the average difference between the actual and predicted grades.

### MSE — Mean Squared Error

Gives more importance to larger prediction errors.

### RMSE — Root Mean Squared Error

Shows the prediction error in a form that is easier to understand because it uses the same scale as the target value.

For all three metrics, **lower values mean better performance**.

---

## 💡 Final Result

The **32 → 64 → 32 → 1** ANN architecture was selected as the final model because it achieved the lowest MAE, MSE, and RMSE among the tested architectures.

The model was able to learn the relationship between student-related factors and final grades and produce predictions close to the actual results.

---

## 🎯 Future Improvements

This project can be improved further by:

* 🌐 Creating a web interface using Streamlit
* 📊 Adding more visualizations
* 🔄 Testing additional ANN architectures
* ⚙️ Tuning model parameters
* 📈 Adding more student data
* 🚀 Deploying the model as a web application

---

## 👨‍💻 Project Summary

This project demonstrates how **Artificial Neural Networks can be used to predict student performance**.

From data preprocessing to model training, evaluation, and user-based prediction, the complete machine learning workflow was implemented.





