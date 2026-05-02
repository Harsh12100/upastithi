# 🎓 Upastithi — AI Attendance System

> Smart attendance powered by **Face Recognition** and **Voice AI** — fast, accurate, effortless.

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?style=flat-square&logo=streamlit)
![Supabase](https://img.shields.io/badge/Supabase-Database-green?style=flat-square&logo=supabase)
![dlib](https://img.shields.io/badge/dlib-Face%20Recognition-orange?style=flat-square)

---

## ✨ Features

### 👩‍🏫 Teacher Portal
- Login with username & password
- Create and manage subjects
- Take attendance using **AI face recognition** (upload classroom photos)
- Take attendance using **Voice AI** (record classroom audio)
- View detailed attendance records with session-wise stats
- Share subject enrollment codes with students

### 🧑‍🎓 Student Portal
- Login using **Face ID** (no password needed!)
- Enroll in subjects using subject code
- Register voice profile for voice attendance
- Track attendance stats per subject
- Unenroll from subjects

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| Database | Supabase (PostgreSQL) |
| Face Recognition | dlib + face_recognition_models |
| Face Classification | scikit-learn SVM |
| Voice Recognition | Resemblyzer + librosa |
| Auth | bcrypt password hashing |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Harsh12100/upastithi.git
cd upastithi
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up Supabase
Create a project on [supabase.com](https://supabase.com) and set up these tables:
- `teachers` — id, username, password, name
- `students` — id, name, face_embedding, voice_embedding
- `subjects` — id, name, subject_code, section, teacher_id
- `subject_students` — id, subject_id, student_id, student_name
- `attendance_logs` — id, subject_id, student_id, student_name, timestamp, is_present

### 4. Configure secrets
Create `.streamlit/secrets.toml`:
```toml
SUPABASE_URL = "your-supabase-url"
SUPABASE_KEY = "your-supabase-anon-key"
```

### 5. Run the app
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
upastithi/
├── app.py                  # Entry point
├── requirements.txt
├── .streamlit/
│   └── secrets.toml        # 🔒 Not pushed to GitHub
└── src/
    ├── components/         # UI components
    │   ├── dialog_enroll.py
    │   ├── dialog_attendance_results.py
    │   ├── dialog_voice_attendance.py
    │   ├── dialog_add_photo.py
    │   ├── subject_card.py
    │   ├── header.py
    │   └── footer.py
    ├── database/
    │   ├── config.py       # Supabase client
    │   └── db.py           # Database functions
    ├── pipelines/
    │   ├── face_pipeline.py   # Face recognition
    │   └── voice_pipeline.py  # Voice recognition
    ├── screens/
    │   ├── home_screen.py
    │   ├── student_screen.py
    │   └── teacher_screen.py
    └── ui/
        └── base_layout.py  # Global styles
```

---

## 🔒 Security Notes

- Passwords are hashed using **bcrypt**
- Supabase credentials are stored in `.streamlit/secrets.toml` (gitignored)
- Never commit your `secrets.toml` to GitHub

---

## 📸 Screenshots

> Student Dashboard — track attendance across enrolled subjects

> Teacher Dashboard — take AI attendance with photos or voice

---

## 🙏 Credits

Built with ❤️ by **Harsh** using Streamlit, Supabase, and open-source AI libraries.
