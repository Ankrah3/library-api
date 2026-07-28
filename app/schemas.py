from pydantic import BaseModel, EmailStr

class MemberCreate(BaseModel):
    full_name: str
    email: EmailStr

class MemberOut(MemberCreate):
    member_id: int
    class Config:
        from_attributes = True