from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCoursesAPISchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileAPISchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client, CreateUserAPISchema


public_users_client = get_public_users_client()

create_user_request = CreateUserAPISchema()
create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

create_file_request = CreateFileAPISchema(

    upload_file='./testdata/files/image.jpg'
)
create_file_response = files_client.create_file(create_file_request)
print("Create file data:", create_file_response)

create_course_request = CreateCoursesAPISchema(
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)
create_course_response=courses_client.create_course(create_course_request)
print("Create course data:", create_course_response)