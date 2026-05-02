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

disease = {
    "common_cold": ["runny nose", "sneezing", "sore throat", "cough", "mild fever"],
    "influenza": ["high fever", "body aches", "fatigue", "chills", "dry cough"],
    "covid_19": ["fever", "dry cough", "loss of taste", "fatigue", "shortness of breath"],
    "pneumonia": ["cough", "fever", "shortness of breath", "chest pain", "fatigue"],
    "bronchitis": ["persistent cough", "mucus", "fatigue", "shortness of breath", "slight fever"],
    "asthma": ["wheezing", "shortness of breath", "chest tightness", "cough", "rapid breathing"],
    "tuberculosis": ["chronic cough", "blood in sputum", "weight loss", "night sweats", "fever"],
    "sinusitis": ["facial pain", "nasal congestion", "headache", "runny nose", "fever"],
    "allergic_rhinitis": ["sneezing", "runny nose", "itchy eyes", "nasal congestion", "postnasal drip"],
    
    "diabetes_type_2": ["increased thirst", "frequent urination", "fatigue", "blurred vision", "slow healing wounds"],
    "hypertension": ["headache", "dizziness", "chest pain", "blurred vision", "fatigue"],
    "coronary_artery_disease": ["chest pain", "shortness of breath", "fatigue", "palpitations", "dizziness"],
    "heart_failure": ["shortness of breath", "fatigue", "swelling in legs", "rapid heartbeat", "persistent cough"],
    "stroke": ["sudden numbness", "confusion", "trouble speaking", "vision problems", "loss of balance"],
    
    "anemia": ["fatigue", "pale skin", "shortness of breath", "dizziness", "cold hands"],
    "leukemia": ["fatigue", "frequent infections", "weight loss", "easy bruising", "fever"],
    "lymphoma": ["swollen lymph nodes", "fever", "night sweats", "weight loss", "fatigue"],
    
    "migraine": ["severe headache", "nausea", "vomiting", "light sensitivity", "aura"],
    "epilepsy": ["seizures", "confusion", "loss of awareness", "staring spells", "muscle jerks"],
    "parkinsons_disease": ["tremor", "slow movement", "stiffness", "balance problems", "speech changes"],
    "alzheimer_disease": ["memory loss", "confusion", "difficulty thinking", "behavior changes", "disorientation"],
    
    "depression": ["persistent sadness", "loss of interest", "fatigue", "sleep problems", "difficulty concentrating"],
    "anxiety_disorder": ["excessive worry", "restlessness", "rapid heartbeat", "sweating", "fatigue"],
    
    "gastroenteritis": ["diarrhea", "vomiting", "abdominal cramps", "fever", "dehydration"],
    "peptic_ulcer": ["burning stomach pain", "bloating", "nausea", "heartburn", "weight loss"],
    "irritable_bowel_syndrome": ["abdominal pain", "bloating", "diarrhea", "constipation", "gas"],
    "hepatitis": ["jaundice", "fatigue", "abdominal pain", "dark urine", "nausea"],
    
    "kidney_stones": ["severe pain", "blood in urine", "nausea", "vomiting", "frequent urination"],
    "chronic_kidney_disease": ["fatigue", "swelling", "shortness of breath", "nausea", "confusion"],
    
    "urinary_tract_infection": ["burning urination", "frequent urination", "cloudy urine", "pelvic pain", "fever"],
    
    "arthritis": ["joint pain", "stiffness", "swelling", "reduced motion", "redness"],
    "osteoporosis": ["bone weakness", "fractures", "back pain", "loss of height", "stooped posture"],
    
    "eczema": ["itching", "redness", "dry skin", "cracks", "inflammation"],
    "psoriasis": ["scaly skin", "red patches", "itching", "dry skin", "burning sensation"],
    "acne": ["pimples", "oily skin", "blackheads", "whiteheads", "inflammation"],
    
    "dengue": ["high fever", "joint pain", "rash", "headache", "bleeding gums"],
    "malaria": ["fever", "chills", "sweating", "headache", "nausea"],
    "typhoid": ["high fever", "weakness", "abdominal pain", "constipation", "headache"],
    
    "chickenpox": ["rash", "itching", "fever", "fatigue", "loss of appetite"],
    "measles": ["rash", "fever", "cough", "runny nose", "red eyes"],
    
    "hypothyroidism": ["fatigue", "weight gain", "cold sensitivity", "dry skin", "depression"],
    "hyperthyroidism": ["weight loss", "rapid heartbeat", "sweating", "nervousness", "tremor"],
    "appendicitis": ["abdominal pain", "nausea", "vomiting", "fever", "loss of appetite"],
    "pancreatitis": ["upper abdominal pain", "nausea", "vomiting", "fever", "rapid pulse"],
    "gallstones": ["abdominal pain", "nausea", "vomiting", "jaundice", "indigestion"],
    "celiac_disease": ["diarrhea", "bloating", "fatigue", "weight loss", "anemia"],
    "crohns_disease": ["diarrhea", "abdominal pain", "fatigue", "weight loss", "fever"],
    "ulcerative_colitis": ["bloody diarrhea", "abdominal pain", "fatigue", "weight loss", "urgency"],

    "conjunctivitis": ["red eyes", "itching", "tearing", "discharge", "burning sensation"],
    "glaucoma": ["eye pain", "blurred vision", "headache", "nausea", "vision loss"],
    "cataract": ["blurred vision", "faded colors", "glare sensitivity", "night vision issues", "double vision"],

    "otitis_media": ["ear pain", "hearing loss", "fever", "fluid drainage", "irritability"],
    "tonsillitis": ["sore throat", "fever", "swollen tonsils", "difficulty swallowing", "bad breath"],
    "laryngitis": ["hoarseness", "dry throat", "cough", "voice loss", "throat irritation"],

    "bronchiolitis": ["wheezing", "cough", "shortness of breath", "fever", "fatigue"],
    "pleurisy": ["chest pain", "shortness of breath", "cough", "fever", "fatigue"],

    "deep_vein_thrombosis": ["leg pain", "swelling", "redness", "warm skin", "cramps"],
    "pulmonary_embolism": ["shortness of breath", "chest pain", "cough", "rapid heart rate", "dizziness"],

    "varicose_veins": ["swollen veins", "aching pain", "heaviness", "itching", "skin discoloration"],

    "multiple_sclerosis": ["fatigue", "vision problems", "numbness", "weakness", "balance issues"],
    "meningitis": ["stiff neck", "fever", "headache", "nausea", "sensitivity to light"],
    "encephalitis": ["fever", "headache", "confusion", "seizures", "fatigue"],

    "schizophrenia": ["hallucinations", "delusions", "disorganized thinking", "lack of motivation", "social withdrawal"],
    "bipolar_disorder": ["mood swings", "mania", "depression", "fatigue", "impulsivity"],

    "sleep_apnea": ["snoring", "breathing pauses", "daytime fatigue", "headache", "irritability"],
    "insomnia": ["difficulty sleeping", "fatigue", "irritability", "poor concentration", "daytime sleepiness"],

    "obesity": ["weight gain", "fatigue", "breathlessness", "joint pain", "snoring"],

    "gout": ["joint pain", "redness", "swelling", "warmth", "limited motion"],

    "lupus": ["fatigue", "joint pain", "rash", "fever", "hair loss"],
    "scleroderma": ["skin thickening", "joint pain", "fatigue", "raynaud phenomenon", "digestive issues"],

    "fibromyalgia": ["widespread pain", "fatigue", "sleep problems", "memory issues", "headache"],

    "carpal_tunnel_syndrome": ["hand numbness", "tingling", "weakness", "pain", "grip difficulty"],

    "herpes_simplex": ["blisters", "itching", "pain", "fever", "swollen lymph nodes"],
    "shingles": ["painful rash", "burning sensation", "blisters", "fever", "fatigue"],

    "hpv_infection": ["warts", "itching", "bleeding", "discomfort", "skin growth"],
    "hiv": ["fever", "fatigue", "weight loss", "night sweats", "swollen lymph nodes"],

    "rabies": ["fever", "agitation", "difficulty swallowing", "hallucinations", "hydrophobia"],

    "tetanus": ["muscle stiffness", "jaw locking", "spasms", "difficulty swallowing", "fever"],

    "whooping_cough": ["severe cough", "whooping sound", "vomiting", "fatigue", "runny nose"],

    "polio": ["muscle weakness", "paralysis", "fever", "fatigue", "headache"],

    "ringworm": ["circular rash", "itching", "redness", "scaly skin", "hair loss"],

    "scabies": ["intense itching", "rash", "burrows", "red bumps", "skin sores"],

    "vitiligo": ["skin depigmentation", "patches", "hair whitening", "sun sensitivity", "skin discoloration"],

    "heatstroke": ["high body temperature", "confusion", "dry skin", "dizziness", "nausea"],

    "hypothermia": ["shivering", "confusion", "slurred speech", "fatigue", "slow breathing"],

    "food_poisoning": ["vomiting", "diarrhea", "abdominal pain", "fever", "nausea"],

    "lactose_intolerance": ["bloating", "diarrhea", "gas", "abdominal pain", "nausea"],

    "pcos": ["irregular periods", "weight gain", "acne", "hair growth", "infertility"],

    "endometriosis": ["pelvic pain", "heavy periods", "fatigue", "painful intercourse", "infertility"],

    "erectile_dysfunction": ["difficulty erection", "reduced libido", "anxiety", "low confidence", "stress"],

    "prostatitis": ["pelvic pain", "urinary issues", "painful urination", "fever", "chills"],

    "benign_prostatic_hyperplasia": ["frequent urination", "weak urine flow", "urgency", "night urination", "incomplete emptying"],

    "skin_cancer": ["new growth", "changing mole", "bleeding", "itching", "ulcer"],

    "breast_cancer": ["lump", "breast pain", "nipple discharge", "skin changes", "swelling"],

    "lung_cancer": ["chronic cough", "chest pain", "weight loss", "fatigue", "shortness of breath"],

    "colon_cancer": ["blood in stool", "abdominal pain", "weight loss", "fatigue", "diarrhea"],

    "prostate_cancer": ["urinary difficulty", "blood in urine", "pelvic pain", "erectile issues", "bone pain"],

    "hepatocellular_carcinoma": ["abdominal pain", "weight loss", "jaundice", "fatigue", "nausea"],

    "amyotrophic_lateral_sclerosis": ["muscle weakness", "speech difficulty", "swallowing issues", "cramps", "fatigue"],

    "bell_palsy": ["facial drooping", "loss of taste", "eye dryness", "headache", "facial pain"],

    "vertigo": ["dizziness", "balance issues", "nausea", "vomiting", "spinning sensation"],

    "motion_sickness": ["nausea", "vomiting", "dizziness", "sweating", "fatigue"],

    "sunburn": ["red skin", "pain", "blisters", "peeling", "fever"],

    "allergic_contact_dermatitis": ["rash", "itching", "redness", "swelling", "blisters"],

    "drug_allergy": ["rash", "itching", "swelling", "breathing difficulty", "fever"]

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
