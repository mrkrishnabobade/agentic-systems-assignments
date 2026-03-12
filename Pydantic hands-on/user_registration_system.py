from pydantic import BaseModel, EmailStr, Field

class Address(BaseModel):
    city: str = Field(min_length=3)
    pincode: str = Field(pattern="^[0-9]{6}$")

class User(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    age: int = Field(ge=18)
    address: Address
    is_premium: bool= False

user_data = {
    "user_id": 101,
    "name": "Krishna",
    "email": "krishna@gmail.com",
    "age": 22,
    "address": {
        "city": "Pune",
        "pincode": "411001"
    }    
}

user = User(**user_data)

print("User registered successfully")
print(user)