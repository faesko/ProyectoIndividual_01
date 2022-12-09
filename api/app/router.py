from fastapi import APIRouter
from config import conn
from model import tabla1 ,tabla2 , tabla3
from sqlalchemy import func, select

var1 = APIRouter()