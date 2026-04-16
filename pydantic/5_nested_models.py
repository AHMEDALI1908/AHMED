from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pincode: str

class Patient(BaseModel):
    name:str
    age:int
    address:Address

ad1 = {'city':'mumbai', 'state':'maharashtra', 'pincode':'400008'}
address1 = Address(**ad1)

p1 = {'name':'max', 'age':35, 'address':address1}
patient1 = Patient(**p1)

print(patient1)
print(patient1.address.city)
print(patient1.address.pincode)