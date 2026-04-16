from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name:str
    age: int
    email:EmailStr
    weight: float
    height: float
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight/(self.height**2),2)

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.height)
    print(patient.weight)
    print(patient.bmi)

p1 = {'name':'max', 'age':27, 'email':'abc@gmail.com', 'height':1.2, 'weight':76.8, 'allergies':['pollen','dust'],'contact_details':{'ph':'456', 'add':'new south west'}}

patient1= Patient(**p1)

insert_patient_data(patient1)