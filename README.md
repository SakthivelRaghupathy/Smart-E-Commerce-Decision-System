# SMART E-COMMERCE DECISION SYSTEM

Smart Product Analysis & Comparison Web Application for discovering, comparing, analyzing, and tracking products across multiple platforms.

---

## 📌 Overview

ProductAnalytrix is a modern full-stack web application that helps users:

* 🔍 Search products intelligently
* 📊 Compare products visually
* 💡 Get smart buying suggestions
* 💰 Analyze pricing & deal quality
* ❤️ Save favorite products
* 👤 Manage profile & preferences
* 🔐 Login securely using OTP authentication

The platform is designed with a scalable backend architecture using FastAPI and an interactive frontend using HTML, CSS, and JavaScript.

---

# ✨ Key Features

## 🔐 Authentication System

* User registration
* OTP-based login system
* Secure verification flow
* JWT-ready backend architecture

Frontend pages:

* `register.html`
* `login.html`
* `verification.html`

Implemented using:

* OTP generation
* Email verification
* Authentication routes





---

## 🔎 Product Search & Selection

Users can:

* Search products by category
* Filter by brand
* Set min/max budget
* Select products for analysis
* Save products to profile

Frontend page:

* `product-details.html`

Features include:

* Product filtering
* Product cards
* Choice selection
* Save functionality
* Analyze flow



---

## 📊 Product Analysis Dashboard

The analysis page provides:

* Product comparison table
* Rating comparison charts
* Price comparison charts
* Deal score analysis
* Buy navigation

Frontend page:

* `analyse.html`

Charts powered by:

* Chart.js



---

## 💡 Best Buying Suggestions

Users can:

* View best deals
* Compare alternative sellers
* Find cheapest purchase options

Frontend page:

* `suggestion4.html`



---

## 👤 User Profile System

Users can:

* View saved products
* Upload profile image
* Remove saved products
* Logout
* Delete account

Frontend page:

* `profile.html`



---

# 🏗 Backend Architecture

The backend follows a production-style scalable architecture.

## 📂 Final Backend Structure

```bash
backend/
│
├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── dependencies.py
│   │
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── init_db.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── otp.py
│   │   ├── saved_product.py
│   │
│   ├── schemas/
│   │   ├── auth_schema.py
│   │   ├── product_schema.py
│   │   └── profile_schema.py
│   │
│   ├── services/
│   │   ├── otp_service.py
│   │   ├── serpapi_service.py
│   │   ├── analysis_service.py
│   │   ├── choice_service.py
│   │   └── profile_service.py
│   │
│   ├── routers/
│   │   ├── auth_router.py
│   │   ├── product_router.py
│   │   ├── analysis_router.py
│   │   └── profile_router.py
│   │
│   └── utils/
│       ├── scoring.py
│       └── market_insight.py
│
├── requirements.txt
├── .env
└── run.py
```

Backend structure reference:




---

# ⚙️ Tech Stack

## Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js

## Backend

* FastAPI
* Python
* SQLAlchemy
* JWT Authentication
* OTP Verification

## Database

* SQLite / PostgreSQL (scalable support)

## APIs & Data Sources

* SerpAPI
* Amazon Product APIs

Product API research files:





---

# 🔄 Application Flow

## 1️⃣ User Registration

User creates account using:

* Username
* Email
* Gender

---

## 2️⃣ OTP Login

User:

* Enters username/email
* Receives OTP
* Verifies OTP
* Gets authenticated

---

## 3️⃣ Product Search

User can:

* Search products
* Filter products
* Add to comparison list

---

## 4️⃣ Product Analysis

Application compares:

* Ratings
* Prices
* Features
* Deal quality

Visual charts are generated dynamically.

---

## 5️⃣ Buying Suggestions

System shows:

* Best deal
* Alternative platforms
* Smart buying recommendations

---

## 6️⃣ Profile Management

Users can:

* Save products
* Remove products
* Upload avatar
* Logout securely

---

# 📈 Future Enhancements

Planned features:

* AI recommendation engine
* Real-time price tracking
* Wishlist notifications
* Historical price graphs
* Multi-platform scraping
* Admin dashboard
* Dark mode
* Mobile responsiveness improvements

---

# 🔐 Security Features

* OTP authentication
* JWT-ready structure
* Modular backend
* Secure route architecture
* Separated business logic
* Clean API layer

---

# 🚀 How to Run the Project

## 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd ProductAnalytrix
```

---

## 2️⃣ Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

## 3️⃣ Configure Environment Variables

Create `.env`

```env
SECRET_KEY=your_secret_key
SERPAPI_KEY=your_serpapi_key
JWT_EXPIRE_MINUTES=60
```

---

## 4️⃣ Run Backend

```bash
uvicorn app.main:app --reload
```

Backend runs at:

```bash
http://127.0.0.1:8000
```

---

## 5️⃣ Run Frontend

Open frontend HTML files using:

* VS Code Live Server
  OR
* Any static server

Start from:

```bash
register.html
```

or

```bash
login.html
```

---

# 📌 API Endpoints

## Authentication

```http
POST /auth/register
POST /auth/generate-otp
POST /auth/verify-otp
```

## Products

```http
POST /products/search
POST /products/save
POST /products/choice/add
DELETE /products/choice/remove
```

## Analysis

```http
GET /analysis
```

## Profile

```http
GET /profile
```

---

# 🧠 Project Goals

This project aims to:

* Simplify smart product purchasing
* Improve comparison experience
* Provide visual buying insights
* Create scalable full-stack architecture
* Learn modern web development practices

---

# 👨‍💻 Developer

Developed by Sakthivel R

A modern product analytics platform focused on smart purchasing decisions and scalable architecture.

---

# 📄 License

This project is for educational and development purposes.
