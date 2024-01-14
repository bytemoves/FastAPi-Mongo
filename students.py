from fastapi import APIRouter

from schemas import Student
from db import collection

student_router = APIRouter()

def student_helper(student):
    return{
        "id":str(student[""]),
        "name":student["name"],
        "age":student["age"]
    }


@student_router.get('/')
async def get_all_student ():
    #list of students
    students = []
    async for student in collection.find():
        students.append(student_helper(student))
        
    return students
        
    
    pass

@student_router.post('/')
async def create_student(student_data:Student):
    new_student = await collection.insert_one({
        "name":student_data.name,
        "age":student_data.age,
        "email":student_data.email
    })
    
    created_student = await collection.find_one({"_id"})
    
    
    pass

@student_router.get('/{student_id:int}')
async def get_student_by_id(student_id:str):
    pass

@student_router.put('/{student_id:int}')
async def update_student(student_id:str):
    pass

@student_router.delete('/{student_id:int}')
async def delete_student(student_id:str):
    pass
