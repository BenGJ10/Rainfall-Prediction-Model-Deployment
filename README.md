# 🌧️ Rainfall Prediction Model Deployment

## 📌 Project Overview  
This project aims to **predict rainfall** using various **atmospheric parameters** such as temperature, humidity, pressure, and wind speed. The machine learning model is built using **Random Forest Classifier**, trained on the `rainfall.csv` dataset from Kaggle. The model is deployed using **Flask** and will be soon hosted on **AWS EC2**.

---

## 🚀 Features  
✅ **Rainfall Prediction:** Predicts the likelihood of rainfall based on input weather conditions.  
✅ **User-Friendly Web Interface:** Interactive form to input weather parameters.  
✅ **Flask-Based Backend:** Lightweight and efficient API for model inference.  
✅ **Modern UI:** Clean and professional front-end using **HTML, CSS, and JavaScript**.  
✅ **Deployment Ready:** Designed for deployment on **AWS EC2**. Will deploy soon.  

---

## 📂 Project Structure  

```
Rainfall-Prediction-Model-Deployment/
│── Datasets/                  # Dataset files (CSV)
│── Models/                     # Saved ML model (.pkl)
│── static/                     # CSS and static assets
│── templates/                  # HTML templates for the web UI
│── README.md                   # Project documentation
│── Rainfall Prediction.ipynb    # Jupyter Notebook for model training
│── main.py                      # Flask application
│── requirements.txt              # Dependencies
```

---

## 🛠️ Tech Stack  

### 🔹 **Machine Learning**  
- Python 🐍  
- Pandas, NumPy  
- Scikit-Learn (Random Forest)  

### 🔹 **Web Framework**  
- Flask (for API and backend)  
- HTML, CSS, JavaScript (for frontend)  

### 🔹 **Deployment**  
- Soon on AWS..

---

## 📊 Dataset  

The dataset (`rainfall.csv`) contains the following **features**:  

| Feature        | Description |
|---------------|------------|
| `day`         | Day of the month |
| `pressure`    | Atmospheric pressure |
| `maxtemp`     | Maximum temperature |
| `temperature` | Average temperature |
| `mintemp`     | Minimum temperature |
| `dewpoint`    | Dew point temperature |
| `humidity`    | Relative humidity |
| `cloud`       | Cloud coverage percentage |
| `rainfall`    | Rainfall amount (target variable) |
| `sunshine`    | Hours of sunshine |
| `winddirection` | Wind direction |
| `windspeed`   | Wind speed |

---

## ⚙️ Installation and Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/BenGJ10/Rainfall-Prediction-Model-Deployment.git
cd Rainfall-Prediction-Model-Deployment
```

### 2️⃣ Create a Virtual Environment (optional but recommended)  
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Flask Application  
```bash
python main.py
```
Visit **`http://127.0.0.1:5000/`** in your browser.

---


## 🤝 Contributing  
🔹 Fork the repo  
🔹 Create a new branch (`git checkout -b feature-name`)  
🔹 Commit your changes (`git commit -m "Added new feature"`)  
🔹 Push the branch (`git push origin feature-name`)  
🔹 Open a Pull Request  

---

## 📝 License  
This project is **open-source** and free to use under the **MIT License**.  

---

## 📩 Contact  
📧 Email: [bengj1015@gmail.com](mailto:bengj1015@gmail.com)  
🔗 GitHub: [BenGJ10](https://github.com/BenGJ10)  
