# 🍔 FoodieExpress – AI-Powered Food Delivery Platform

FoodieExpress is a **full-stack food delivery web application** designed to provide seamless end-to-end user interaction with scalable backend services and AI-driven recommendations. The project demonstrates full-stack development skills using **React, Flask, RESTful APIs, and SQLite**.

---

## 🚀 Features

* View food menu with real-time data from backend APIs
* RESTful API integration between frontend and backend
* Category-based food recommendations (AI logic)
* Scalable backend architecture with Flask
* Clean and responsive React frontend
* Database integration using SQLite

---

## 🛠 Tech Stack

### Frontend

* React
* JavaScript
* HTML5
* CSS3

### Backend

* Python
* Flask
* Flask-SQLAlchemy
* RESTful APIs

### Database

* SQLite

### Tools & Platforms

* Git & GitHub
* Postman (API Testing)
* Heroku (Deployment Ready)

---

## 📁 Project Structure

```
FoodieExpress/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── database.db
│
├── frontend/
│   ├── package.json
│   └── src/
│       ├── App.js
│       ├── index.js
│       ├── components/
│       │   └── FoodList.js
│       └── App.css
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Git-punit/FoodieExpress--AI-Powered-Food-Delivery-Platform
cd FoodieExpress
```

---

### 2️⃣ Backend Setup

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Backend will run at:

```
http://127.0.0.1:5000
```

---

### 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend will run at:

```
http://localhost:3000
```

---

## 🔌 API Endpoints

### Get All Food Items

```
GET /api/foods
```

### Add Food Item

```
POST /api/foods
```

```json
{
  "name": "Pizza",
  "price": 250,
  "category": "Fast Food"
}
```

### Get Recommendations

```
GET /api/recommend/<category>
```

---

## 🧪 API Testing

* APIs tested using **Postman**
* Ensured reliability, performance, and error handling

---

## 📌 Resume Description (ATS-Friendly)

> Built a scalable full-stack food delivery application using **React, Flask, RESTful APIs, and SQLite**. Implemented backend services, database integration, API testing, and cloud-ready deployment.

---

## 🔮 Future Enhancements

* User authentication (JWT)
* Cart and order management
* ML-based recommendation system
* Payment gateway integration
* Cloud deployment (AWS / Heroku)
* Docker and Kubernetes support

---

## 👤 Author

**Punit Yadav**
📧 Email: [workwithpunit247@gmail.com](mailto:workwithpunit247@gmail.com)
🔗 GitHub & LinkedIn: Available on profile

---

⭐ If you like this project, feel free to **star the repository** and contribute!
