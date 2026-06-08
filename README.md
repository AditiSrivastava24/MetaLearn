# 🧠 MetaLearn

MetaLearn is an intelligent adaptive quiz platform designed to personalize the learning experience for every user. Unlike traditional quiz systems that present the same questions to everyone, MetaLearn dynamically adjusts question difficulty in real time based on a learner's performance, confidence level, accuracy, and number of attempts.

The platform leverages machine learning principles and adaptive learning techniques to ensure that users are consistently challenged at the right level, helping them learn more effectively while maintaining engagement.

Additionally, MetaLearn features secure Firebase Authentication and a live leaderboard powered by Firebase Database, creating a competitive and motivating learning environment.

---

## 🚀 Features

* Adaptive question difficulty adjustment
* Machine learning-driven learning experience
* Firebase Authentication for secure user login and registration
* Live leaderboard with real-time updates
* Performance analytics and progress tracking
* Confidence-based assessment system
* Accuracy tracking across quizzes
* Personalized learning paths
* Dynamic question selection
* Responsive and user-friendly interface

---

## 🎯 Problem Statement

Traditional quiz systems provide the same set of questions to every learner regardless of their skill level. This often results in:

* Easy questions becoming repetitive for advanced learners
* Difficult questions discouraging beginners
* Inefficient learning experiences
* Poor engagement and retention

MetaLearn addresses this problem by continuously analyzing user performance and adapting question difficulty to match the learner's current ability level.

---

## 🧠 Adaptive Learning Algorithm

MetaLearn evaluates multiple factors after every question to determine the difficulty of the next question.

### Parameters Considered

#### ✅ Correctness

Determines whether the user's answer was correct or incorrect.

* Correct Answer → Difficulty Increases
* Incorrect Answer → Difficulty Decreases

#### 📊 Accuracy

Measures overall user performance.

```text
Accuracy = (Correct Answers / Total Questions) × 100
```

Higher accuracy leads to more challenging questions.

#### 💭 Confidence Score

Users provide a confidence score before submitting an answer.

Example:

```text
1 = Not Confident
10 = Extremely Confident
```

Interpretation:

* High Confidence + Correct Answer → Significant Increase in Difficulty
* Low Confidence + Correct Answer → Moderate Increase
* High Confidence + Incorrect Answer → Indicates Misconception
* Low Confidence + Incorrect Answer → Easier Question Recommended

#### 🔄 Number of Attempts

Tracks how many attempts are needed before arriving at the correct answer.

* Fewer Attempts → Higher Difficulty
* More Attempts → Lower Difficulty

---

## 🔥 Difficulty Adjustment Logic

### Increase Difficulty When

* User answers correctly
* Confidence score is high
* Accuracy remains above threshold
* Fewer attempts are required

### Decrease Difficulty When

* User answers incorrectly
* Confidence score is low
* Multiple attempts are needed
* Accuracy falls below threshold

### Example Flow

```text
Question 1 (Easy)
↓
Correct Answer
Confidence = 9/10
↓
Question 2 (Medium)

Question 2
↓
Correct Answer
Confidence = 10/10
↓
Question 3 (Hard)

Question 3
↓
Wrong Answer
Confidence = 3/10
↓
Question 4 (Medium)
```

---

## 🏆 Live Leaderboard

MetaLearn includes a real-time leaderboard powered by Firebase Database.

The leaderboard updates instantly whenever a user completes a quiz or improves their score.

### Leaderboard Features

* Real-time score updates
* Global rankings
* Performance-based scoring
* Accuracy tracking
* User competition and engagement
* Instant synchronization across devices

### Ranking Factors

Users are ranked using:

* Total Score
* Accuracy Percentage
* Number of Correct Answers
* Quiz Completion Rate
* Difficulty Levels Cleared

---

## 🔐 Firebase Authentication

MetaLearn uses Firebase Authentication to manage user accounts securely.

### Authentication Features

* User Registration
* User Login
* Secure Session Management
* Password Authentication
* Authentication State Tracking

### Benefits

* Secure user management
* Easy integration
* Scalable architecture
* Cross-platform support

---

## ☁️ Firebase Database

Firebase Realtime Database / Firestore is used to store:

* User profiles
* Quiz scores
* Leaderboard data
* Quiz history
* Learning progress
* Performance statistics

### Database Benefits

* Real-time synchronization
* Cloud storage
* Fast read/write operations
* Scalable architecture
* Cross-device accessibility

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn
* NumPy
* Pandas

### Database & Authentication

* Firebase Authentication
* Firebase Firestore / Realtime Database

### Development Tools

* Git
* GitHub
* VS Code

---

## 📁 Project Structure

```bash
MetaLearn/
│
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── quiz.html
│   ├── leaderboard.html
│   ├── styles.css
│   └── app.js
│
├── backend/
│   ├── app.py
│   ├── adaptive_engine.py
│   ├── scoring.py
│   ├── recommendation.py
│   └── requirements.txt
│
├── firebase/
│   ├── firebaseConfig.js
│   ├── auth.js
│   └── database.js
│
├── dataset/
│   └── questions.json
│
├── models/
│   └── adaptive_model.pkl
│
├── screenshots/
│
├── README.md
│
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/MetaLearn.git
cd MetaLearn
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Firebase

Create a Firebase project and enable:

* Authentication
* Firestore or Realtime Database

Add your Firebase configuration:

```javascript
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT.firebaseapp.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_BUCKET",
  messagingSenderId: "YOUR_SENDER_ID",
  appId: "YOUR_APP_ID"
};
```

### 4. Run the Backend

```bash
python app.py
```

### 5. Launch the Frontend

Open:

```bash
index.html
```

Or run your preferred frontend development server.

---

## 📊 Performance Metrics

| Metric                 | Purpose                          |
| ---------------------- | -------------------------------- |
| Correctness            | Determines difficulty adjustment |
| Accuracy               | Tracks overall performance       |
| Confidence Score       | Measures certainty of knowledge  |
| Attempts               | Measures learning difficulty     |
| Quiz Score             | Used for leaderboard rankings    |
| Difficulty Progression | Tracks learning growth           |

---

## 🎓 Educational Benefits

* Personalized learning experience
* Improved knowledge retention
* Reduced learner frustration
* Continuous skill progression
* Enhanced engagement through gamification
* Data-driven assessment

---

## 📈 Future Enhancements

* AI-generated questions using Gemini/OpenAI APIs
* Subject-wise adaptive learning modules
* Personalized study recommendations
* Achievement badges and streaks
* Multiplayer quiz battles
* Detailed analytics dashboard
* Mobile application support
* Learning reports and insights
* Admin panel for question management

---

## 👩‍💻 Author

**Aditi Srivastava**

B.Tech Computer Science Engineering

Machine Learning & AI Enthusiast

* GitHub: https://github.com/your-github
* LinkedIn: https://linkedin.com/in/your-profile

---

## 📄 License

This project is licensed under the MIT License.

---

## 🌟 Project Summary

MetaLearn is a machine learning-powered adaptive quiz platform that personalizes question difficulty based on user accuracy, confidence score, correctness, and number of attempts. By integrating Firebase Authentication, Firebase Database, and a real-time leaderboard, MetaLearn creates an engaging and competitive learning environment while ensuring each learner receives a customized educational experience tailored to their performance.

⭐ If you found this project useful, consider giving it a star on GitHub!
