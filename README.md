# face-recognition

📌 Project Overview

This project is a Face Recognition System built using Flask, OpenCV, Docker, and Kubernetes.
It allows users to upload an image and detects whether a human face is present using computer vision techniques.
🧠 Features
📷 Face detection using OpenCV
🌐 REST API using Flask
🐳 Containerized with Docker
☸️ Deployed using Kubernetes
⚡ Simple and scalable architecture

🏗️ Project Structure

face_recognition/
│
├── app.py                 # Flask backend
├── Dockerfile            # Docker configuration
├── deployment.yaml       # Kubernetes deployment
├── service.yaml          # Kubernetes service
├── requirements.txt      # Dependencies
└── README.md             # Documentation
⚙️ Technologies Used

Python
Flask
OpenCV
Docker
Kubernetes

🚀 How to Run (Docker)
🔹 Step 1: Build Image
docker build -t face-recognition-app .
🔹 Step 2: Run Container
docker run -p 5000:5000 face-recognition-app
🔹 Step 3: Access Backend

Open:

http://localhost:5000
☸️ Run with Kubernetes
Apply Deployment
kubectl apply -f deployment.yaml
Apply Service
kubectl apply -f service.yaml
Check Pods
kubectl get pods
Access Application
http://localhost:30007
🔗 API Endpoint
POST /recognize

Upload an image file to detect faces.
Example Response:
{
  "result": ["Face Detected"]
}
<img width="1435" height="737" alt="image" src="https://github.com/user-attachments/assets/36f4d9ed-66b5-4909-94bf-01545db6d60d" />

<img width="470" height="159" alt="image" src="https://github.com/user-attachments/assets/cd728e3b-def9-4ee3-87b7-44ccefe6c0ed" />


⚠️ Notes
Ensure Docker Desktop is running
Enable Kubernetes in Docker Desktop
Ports used:
Docker → 5000
Kubernetes → 30007

🎯 Future Enhancements
Face identification (recognize person name)
Real-time webcam detection
Attendance system
Cloud deployment (AWS/GCP)

👩‍💻 Author
Priyankka Dwarampudi

⭐ Conclusion

This project demonstrates how to combine Computer Vision + DevOps tools (Docker & Kubernetes) to build a scalable application.
