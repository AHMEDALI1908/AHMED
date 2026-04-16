from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Optional, Dict

class Patient(BaseModel):
    name: str 
    age: int = Field(gt=0, lt=150)
    email: EmailStr
    weight: float = Field(gt=0, strict=True)
    linkedin_url: AnyUrl
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    username = patient.email.split('@')[0]
    print(username)
    print(patient.linkedin_url)
    print(patient.contact_details)
    print("Data inserted")

patient_info ={'name':'max', 'age':'30', 'email':'maxx@g.com', 'weight':72.5,'linkedin_url':'https:linkedin', 'contact_details':{'ph_no':'28347', 'address':'101, st street'}}

p1 = Patient(**patient_info)

insert_patient_data(p1)