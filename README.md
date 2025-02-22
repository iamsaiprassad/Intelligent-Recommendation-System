# **Intelligent Recommendation System**

## **📌 Project Overview**
The **Intelligent Recommendation System** is a **hybrid recommendation engine** built using **Django** and **Scikit-learn**, designed to provide personalized content recommendations via a **REST API**. It combines **Collaborative Filtering** and **Content-Based Filtering** to generate accurate suggestions for users based on their interactions and preferences.

## **🚀 Features**
✅ Hybrid Recommendation Model (**Collaborative + Content-Based Filtering**)  
✅ REST API for easy integration with web & mobile applications  
✅ Optimized **SQL queries** for efficient data retrieval  
✅ Scalable architecture using **Django and PostgreSQL/MySQL**  
✅ Machine Learning pipeline powered by **Scikit-learn**  

## **🛠️ Technologies Used**
- **Framework**: Django (Python)
- **Machine Learning**: Scikit-learn
- **Database**: PostgreSQL / MySQL
- **API**: Django REST Framework (DRF)

## **📥 Installation & Setup**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/iamsaiprassad/Intelligent-Recommendation-System.git
cd Intelligent-Recommendation-System
```

### **2️⃣ Create & Activate Virtual Environment**
```bash
python -m venv venv  # Create virtual environment
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Database**
- Configure your **PostgreSQL/MySQL** database in `.env` or settings file.
- Run database migrations:
```bash
python manage.py migrate
```

### **5️⃣ Run the Application**
```bash
python manage.py runserver
```

## **📡 API Endpoints**
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/api/recommendations/<user_id>` | Get personalized recommendations for a user |
| POST | `/api/train` | Train or update the recommendation model |
| GET | `/api/health` | Check API health status |

## **📝 Example Usage**
```bash
curl -X GET http://127.0.0.1:8000/api/recommendations/101
```

## **📌 Future Enhancements**
🚀 Integrate **Deep Learning-based recommendation models**  
🚀 Implement **real-time streaming recommendations**  
🚀 Scale system with **distributed databases**  

## **👨‍💻 Author**
**Sai Prassad**  
🔗 [GitHub](https://github.com/iamsaiprassad) | [LinkedIn](https://www.linkedin.com/in/saiprassad)  
