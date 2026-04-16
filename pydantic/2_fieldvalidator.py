from pydantic import BaseModel, EmailStr, field_validator, Field, model_validator
from typing import List, Dict

class Patient(BaseModel):
    name:str
    age: int
    weight: float
    email: EmailStr
    allergies: List[str]
    contact_details: Dict[str, str]


    ## Adding email field validator to check validate domain
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domain = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError('Not a valid Domain')

        return value
    ## Transforming data through field validator
    @field_validator('name')
    @classmethod
    def capitalise_name(cls,value):
        return value.upper()


def insert_pateint_details(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)

p1 = {'name':'max', 'age':65, 'weight':'72.5', 'email':'abc@hdfc.com', 'allergies':['pollen', 'dust'], 'contact_details':{'ph':'1123', 'add':'101, sk building', 'emergency':'123'}}

patient1 = Patient(**p1)

insert_pateint_details(patient1)