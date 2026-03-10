from pydantic import BaseModel, EmailStr, Field, ValidationError


# Creating a model for user registration
class UserRegister(BaseModel):
    username: str = Field(min_length=5)
    email: EmailStr
    age: int = Field(ge=18)


# Trying with valid user data
try:
    user = UserRegister(
        username="krishna123",
        email="krishna@gmail.com",
        age=22
    )

    print("User registered successfully")
    print(user)

except ValidationError as error:
    print("Validation error:")
    print(error)


print("\nChecking invalid data example...\n")


# Trying with invalid data
try:
    user2 = UserRegister(
        username="abc",      # less than 5 characters
        email="krishna.com", # invalid email
        age=16               # less than 18
    )

except ValidationError as error:
    print("Invalid user data")
    print(error)