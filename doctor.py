from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Smart Doctor API")


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or your frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)
# Disease database
diseases = {
  "cough": ["shortness of breath", "chest pain", "sore throat"],
  "common_cold": ["runny nose", "sore throat", "sneezing", "headache"],
  "diabetes":["increased thirst","blurred vision","increased hunger","unexplained weight loss","frequent urination"],
  "cancer":["lump","thickening","unexplained weight loss","persistent pain"],
  "Arthritis":["stiffness","limited range of motion","deformity","redness and warmth"]
}

class DiagnoseRequest(BaseModel):
    patient_name: str = "Unknown"
    patient_age: str = "Unknown"
    symptoms: List[str]

@app.post("/diagnose")
def diagnose(request: DiagnoseRequest):
    if len(request.symptoms) < 2:
        return {"error": "Please provide at least 2 symptoms in the list."}

    s1 = request.symptoms[0].lower().strip()
    s2 = request.symptoms[1].lower().strip()

    found_disease = None

    for key, val in diseases.items():
        if s1 in val and s2 in val:
            found_disease = key
            break

    if found_disease:
        # Save patient data to file just like the original script
        with open("patient_data.txt", "a") as f:
            f.write(f"patient's name :{request.patient_name} \n")
            f.write(f" patient's age :{request.patient_age}\n")
            f.write(f"symptom 1 :{s1} \n")
            f.write(f"symptom 2 :{s2} \n")
            f.write(f"disease :{found_disease} \n")

        return {"disease": found_disease, "message": f"Disease found: {found_disease}"}
    else:
        return {"disease": None, "message": "No disease found based on the provided symptoms."}
