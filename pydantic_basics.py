from pydantic import BaseModel, Field
class FileModel(BaseModel):
    id:str
    url:str
    filename:str
    directory:str

class CourseModel(BaseModel):
    id :str
    title:str
    max_Score: int = Field(alias="maxScore")
    min_Score: int = Field(alias="minScore")
    description: str
    preview_File: f
    estimatedTime: str

course_default_mode = CourseModel(
    id="course-id",
    title="Playwright",
    maxScore= 10,
    minScore=2,
    description="text",
    esitmatedTime="2"
)
course_dict= {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 10,
    "minScore": 2,
    "description": "text",
    "estimatedTime": "2 weeks"}

course_dict_model = CourseModel(**course_dict)

