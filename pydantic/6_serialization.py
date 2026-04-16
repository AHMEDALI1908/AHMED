from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pincode: str

class Patient(BaseModel):
    name:str
    gender:str = 'Male'
    age: int
    address:Address

ad1 ={'city':'mumbai', 'state':'maharashtra', 'pincode':'400008'}
address1 = Address(**ad1)
p1 = {'name':'max', 'age':'29', 'address':address1}
patient1 = Patient(**p1)

print(patient1)

py_dump = patient1.model_dump()
print(py_dump)

js_dump = patient1.model_dump_json()
print(js_dump)

py_dump1 = patient1.model_dump(include=['name'])
print(py_dump1)

py_dump2 = patient1.model_dump(include={'address':['city', 'pincode']})
print(py_dump2)