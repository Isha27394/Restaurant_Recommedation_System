# 🍽️ Restaurant Recommendation System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.10+-orange.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

# Project Overview

Restaurant Recommendation System is a machine learning-based web application that helps users discover personalized dining options based on their preferences. The system uses Content-Based Filtering to recommend restaurants that share similar characteristics such as cuisine, location, and restaurant type.

The application provides fast and accurate recommendations using a precomputed similarity model and features a user-friendly interface built with Flask and modern web technologies.

# 🎯 Key Features
Personalized Recommendations using Content-Based Filtering
Top 10 Similar Restaurants based on user selection
Machine Learning Model using Cosine Similarity
Web Interface built with Flask
Real-time Results with high performance
🏗️ Technical Architecture
User → Select Restaurant → Flask App → ML Model → Similarity Calculation → Recommendation → Display Result

# ⚙️ Model Workflow
Step	Process	Description
1	Data Cleaning	Handles missing values, removes duplicates, cleans ratings
2	Feature Engineering	Combines cuisines, type, and location into single feature
3	Vectorization	Converts text data into numerical form using CountVectorizer
4	Similarity	Uses Cosine Similarity to find similar restaurants
5	Export	Saves model as restaurant.pkl for fast access
# 📁 Project Structure
Restaurant-Recommendation-System/
├── Flask/
│   ├── app1.py                     # Flask application
│   ├── restaurant.pkl              # Trained similarity model
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── templates/
│   │   ├── index.html              # Home page
│   │   ├── recommend.html          # Recommendation page
│   │   └── result.html             # Result page
├── Model/
│   └── build_model.py              # Model training script
├── data/                           # Dataset files
├── requirements.txt
├── README.md
└── LICENSE
# 🚀 Getting Started
# Prerequisites
Python 3.8+
pip installed
Installation
Clone the repository
git clone https://github.com/your-username/Restaurant-Recommendation-System.git
cd Restaurant-Recommendation-System
Create a virtual environment
python -m venv venv
venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
Build the model
cd Model
python build_model.py
Run the Flask application
cd Flask
python app1.py
Open in browser
http://127.0.0.1:5000

# 📊 Dataset

The model is trained using the Zomato Bangalore Restaurants Dataset, which includes:

Restaurant Names
Cuisines
Ratings
Location
Restaurant Type
# 🧠 Model Training
Run the training script:
python build_model.py
The script performs:
Data Cleaning
Feature Engineering
Vectorization
Similarity Calculation
Model Saving
# 🌐 Web Application
Pages
Home Page (index.html) – Select restaurant
Recommendation Page (recommend.html) – Input selection
Result Page (result.html) – Display recommendations
Usage
Open the web application
Select a restaurant from dropdown
Click submit
View Top 10 recommended restaurants with similarity scores
# 📈 Use Cases
Restaurant Discovery: Find similar dining places
Food Apps: Enhance recommendation systems
User Personalization: Improve user experience
Business Insights: Analyze similar restaurants
# 🤝 Contributing
Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add feature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
# 📄 License

This project is licensed under the MIT License.

# 👨‍💻 Author

Isha Gaikwad

# 🙏 Acknowledgments
Zomato Dataset
Scikit-learn for ML tools
Flask for web framework
