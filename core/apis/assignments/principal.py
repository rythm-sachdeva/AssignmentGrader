from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Teacher, Assignment
from .schema import TeacherSchema , AssignmentSchema

principal_resources = Blueprint('principal_resources',__name__)

@principal_resources.route('/teachers',methods=['GET'],strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    teacher_list = Teacher.get_all_techers()
    teacher_dump = TeacherSchema().dump(teacher_list,many=True)
    return APIResponse.respond(data=teacher_dump)

@principal_resources.route('/assignments',methods=['GET'],strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    all_assignments = Assignment.get_assignments_by_teacher()
    all_assignments_dump = AssignmentSchema().dump(all_assignments, many=True)
    return APIResponse.respond(data=all_assignments_dump)

