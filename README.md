
# Python CI + Docker Build & Push
[![Python CI + Docker Build & Push](https://github.com/Learning-DevOps-LLC/python-ci-cd-demo/actions/workflows/ci-docker.yml/badge.svg?branch=main)](https://github.com/Learning-DevOps-LLC/python-ci-cd-demo/actions/workflows/ci-docker.yml)

# Docker Pulls
[![Docker Pulls](https://img.shields.io/docker/pulls/ashishsingh2110/python-ci-cd-demo.svg)](https://hub.docker.com/r/ashishsingh2110/python-ci-cd-demo)

# Deployed
[![Deployed](https://img.shields.io/badge/Live-Demo-green)](https://python-ci-cd-demo-wg2r.onrender.com/)


# 🚀 Python CI/CD Demo with Docker & GitHub Actions

This project demonstrates a simple Python web app using **Flask**, deployed with CI/CD pipelines using **GitHub Actions** and optionally **Docker + Render**.

---

## 📦 Project Structure

python-ci-cd-demo/
├── app.py # Flask web app
├── test_app.py # Pytest test file
├── requirements.txt # Python dependencies
├── Dockerfile # Docker build config
├── .github/
│ └── workflows/
│ └── ci-cd.yml # GitHub Actions pipeline

---

## 🌐 Live Demo

> Example URLs (if hosted):

- **Production**: https://python-prod.onrender.com  
- **Staging**: https://python-staging.onrender.com

---

## ✅ Features

- ✅ Automated testing with `pytest`
- ✅ Docker image build & push to Docker Hub
- ✅ Multi-branch support (`main`, `staging`, etc.)
- ✅ Optional: Render auto-deploy
- ✅ GitHub Actions for CI/CD

---

## 🧪 Running Locally

1. **Install dependencies**  
   ```
   pip install -r requirements.txt
Run the app


python app.py
Test it


pytest
🐳 Docker Usage
Build image:


docker build -t python-ci-cd-demo .
Run container:


docker run -p 5000:5000 python-ci-cd-demo
⚙️ GitHub Actions Workflow
Triggers:

On push and pull_request to main (or staging/dev if configured)

Builds, tests, and pushes Docker image

🔐 Secrets Required
In GitHub repo → Settings → Secrets → Actions:

DOCKER_USERNAME

DOCKER_PASSWORD

🚀 Deployment (Optional: Render)
Login to Render

Create a Web Service

Select branch (e.g., main or staging)

Set build command:


pip install -r requirements.txt
Start command:


python app.py
Port: 5000

👨‍💻 Author
Ashish Singh
🔗 GitHub: Learning-DevOps-LLC

📄 License
This project is licensed under the MIT License.


---

Let me know if you want to:
- Add badges (build passing, Docker pull count, etc.)
- Auto-deploy from different branches
- Include images/diagrams in README







