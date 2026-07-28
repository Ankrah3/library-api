from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_mysql_db
from app.models import Member
from app.schemas import MemberCreate, MemberOut

router = APIRouter(prefix="/mysql/members", tags=["MySQL"])

@router.post("/", response_model=MemberOut)
def create_member(member: MemberCreate, db: Session = Depends(get_mysql_db)):
    db_member = Member(**member.model_dump())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

@router.get("/", response_model=list[MemberOut])
def list_members(db: Session = Depends(get_mysql_db)):
    return db.query(Member).all()