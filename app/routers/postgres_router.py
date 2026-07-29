from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.database import get_pg_db
from app.models import Member
from app.schemas import MemberCreate, MemberOut

router = APIRouter(prefix="/postgres/members", tags=["PostgreSQL"])

@router.post("/", response_model=MemberOut)
def create_member(member: MemberCreate, db: Session = Depends(get_pg_db)):
    db_member = Member(**member.model_dump())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

# 1. Updated list_members with query parameters (search & limit)
@router.get("/", response_model=list[MemberOut])
def list_members(
    search: str | None = Query(None, description="Filter members by name"),
    limit: int = Query(10, description="Limit the number of results"),
    db: Session = Depends(get_pg_db)
):
    query = db.query(Member)
    if search:
        query = query.filter(Member.full_name.ilike(f"%{search}%"))
    return query.limit(limit).all()

# 2. New endpoint to get a single member by their ID path parameter
@router.get("/{member_id}", response_model=MemberOut)
def get_member(member_id: int, db: Session = Depends(get_pg_db)):
    db_member = db.query(Member).filter(Member.member_id == member_id).first()
    if not db_member:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member