from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Teacher
from .schema import TeacherSchema

principal_resources = Blueprint('principal_resources',__name__)

@principal_resources.route('/teachers',methods=['GET'],strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    teacher_list = Teacher.get_all_techers()
    teacher_dump = TeacherSchema().dump(teacher_list,many=True)
    return APIResponse.respond(data=teacher_dump)

