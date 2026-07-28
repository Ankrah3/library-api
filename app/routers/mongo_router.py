from fastapi import APIRouter
from app.mongo import mongo_db
from app.schemas import MemberCreate

router = APIRouter(prefix="/mongo/members", tags=["MongoDB"])

@router.post("/")
def create_member(member: MemberCreate):
    result = mongo_db.members.insert_one(member.model_dump())
    return {"inserted_id": str(result.inserted_id)}

@router.get("/")
def list_members():
    members = list(mongo_db.members.find({}, {"_id": 0}))
    return members