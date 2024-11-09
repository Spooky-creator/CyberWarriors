#flask to web page
from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import time
import shutil
import random
import subprocess
app = Flask(__name__)
UPLOAD_FOLDER = "upload"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
def get_uploaded_files():
    
    files = os.listdir(app.config["UPLOAD_FOLDER"])
    sample_files = []
    
    for file in files:
        if os.path.isfile(os.path.join(app.config["UPLOAD_FOLDER"], file)):
          
            if file == "remcos_agent":
                sample_files.append({
                    "name": file,  
                    "status": "Clean",  
                    "threat_level": "threat"  # You can customize this threat level
                })
            else:
                # All other files get similar details
                sample_files.append({
                    "name": file,  # Keep the original filename
                    "status": "clean",  # Initial status, can change after scanning
                    "threat_level": "threat"  # Default threat level
                })
    return sample_files
app = Flask(__name__)
UPLOAD_FOLDER = "upload"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
def get_uploaded_files():
    # List all files in the upload folder
    files = os.listdir(app.config["UPLOAD_FOLDER"])
    # Create sample file details
    sample_files = []
    for file in files:
        if os.path.isfile(os.path.join(app.config["UPLOAD_FOLDER"], file)):
            sample_files.append({
                "name": file,
                "status": "Clean",  # Initial status, can change after scanning
                "threat_level": "threat"  # Default threat level, can change after scanning
            })
    return sample_files
sample_files = [
    {"name": "remcos_agent", "status": "Clean", "threat_level": "threat"},
]

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/upload", methods=["POST"])
def upload_file():
    if "files" not in request.files:
        return "No file part", 400
    files = request.files.getlist("files")
    if not files or files[0].filename == "":
        return "No selected files", 400
    for file in files:
        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
    return render_template("tem.html")

@app.route('/scan')
def scan():
    time.sleep(20)
    sample_files = get_uploaded_files()
    
    # Randomly update the threat level for demonstration purposes (except for remcos_agent)
    for file in sample_files:
        if file["name"] != "remcos_agent.exe":
            file["threat_level"] = "no-threat"# Simulated threat level
            file["status"] = "clean"  # Update status after scanning
    
    file1 = r"C:\Users\Deepa\Downloads\src\rfrfrfr.py"
    process1 = subprocess.run(['python', file1], capture_output=True, text=True)
    print(process1)
    shutil.copy("C:\\Users\\Deepa\\Downloads\\remcos_agent.exe", r"C:\Users\Deepa\OneDrive\Desktop\infected")
    scanned_results = random.sample(sample_files, len(sample_files))
    return jsonify({"results": scanned_results})

if __name__ == "__main__":
    app.run(debug=True)
