from pydantic import BaseModel, EmailStr, field_validator, model_validator
from typing import List, Dict

class Patient(BaseModel):
    name:str
    age:int
    email: EmailStr
    allergies: List[str]
    contact_details: Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError("Enter the emergency contact for patient above 60")
        return model

    # to validate email is from valid domain
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domain = ['hdfc.com', 'icici.com']

        if value.split('@')[-1] not in valid_domain:
            raise ValueError("Email from not valid domian")
        return value


    
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.allergies)
    print(patient.contact_details)

p1 = {'name':'max', 'age':'70', 'email':'abc@hdfc.com', 'allergies':['pollen', 'dust'],
      'contact_details':{'phone':'267', 'add':'res2, 3 now', 'emergency':'878'}}


patient1 = Patient(**p1)

insert_patient_data(patient1)