# 🚀 3D Command-Center Portfolio | Django 5.0

A high-performance, interactive portfolio dashboard built to showcase full-stack engineering and backend architecture. This project departs from traditional static resumes, utilizing a custom 3D perspective engine and a "Command Center" UI.

**Live Demo:** [https://my-portfolio-ab-3.onrender.com/](https://my-portfolio-ab-3.onrender.com/)

---

## 🛠️ Technical Architecture

### **Backend Core**
* **Framework:** Django 5.0 (Python 3.12)
* **Static Asset Management:** WhiteNoise (optimized for production delivery)
* **Environment Control:** Decoupled settings for Production/Local environments.

### **Frontend & UX**
* **Visual Engine:** Pure JavaScript 3D Perspective Engine (Mouse-tracking tilt effect).
* **Styling:** Tailwind CSS 4.0 (Custom dark-mode configuration).
* **Iconography:** Specialized SVG brand integration for GitHub and LinkedIn.

---

## 🏗️ Project Structure

```text
My_Portfolio/
├── portfolio/          # Main project configuration (Settings/WSGI)
├── profil/             # Core application (3D Views/Templates)
│   ├── static/         # Brand assets & JavaScript Logic
│   └── templates/      # 3D Dashboards (Contact, Projects, Education)
├── requirements.txt    # Optimized production dependencies
└── manage.py           # Project entry point
