from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema
from clients.files.files_client import CreateFileAPISchema, CreateFileResponseSchema
from clients.files.files_schema import FileSchema, GetFileResponseSchema
from tools.asserations.base import assert_equal
from tools.asserations.errors import assert_validation_error_response, assert_internal_error_response


def assert_create_file_response(request: CreateFileAPISchema, response: CreateFileResponseSchema):
    expected_url = f"http://localhost:8000/static/{request.directory}/{request.filename}"
    assert_equal(str(response.file.url), expected_url, "url")
    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory, "directory")


def assert_file(actual: FileSchema, expected: FileSchema):
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.url, expected.url, "id")
    assert_equal(actual.filename, expected.filename, "id")
    assert_equal(actual.directory, expected.directory, "id")


def assert_get_file_response(
        get_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema):
    assert_file(get_file_response.file, create_file_response.file)


def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    expected = ValidationErrorResponseSchema(
        details=[ValidationErrorSchema(type="string_too_short", input="", context={"min_length": 1},
                                       message="String should have at least 1 character",
                                       location=["body", "filename"])])
    assert_validation_error_response(actual, expected)


def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    expected = ValidationErrorResponseSchema(
        details=[ValidationErrorSchema(type="string_too_short", input="", context={"min_length": 1},
                                       message="String should have at least 1 character",
                                       location=["body", "directory"])])
    assert_validation_error_response(actual, expected)


def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    expected = InternalErrorResponseSchema(details="File not found")
    assert_internal_error_response(actual, expected)


def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    expected = ValidationErrorResponseSchema(details=[ValidationErrorSchema(type="uuid_parsing", location=["path",
                                                                                                           "file_id"],
                                                                            message="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                                                                            input="incorrect-file-id", context={
            "error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"})])
    assert_validation_error_response(actual, expected)
