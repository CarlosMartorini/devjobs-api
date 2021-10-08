from flask import jsonify, request, current_app
from app.models.education_model import EducationModel



def get_education():

    degree = ""
    school = ""
    date_from = ""
    date_to = ""
    description = ""

    return jsonify({"degree" : degree, "school" : school, "date_from": date_from, "date_to": date_to, "description" : description}), 200


def create_education():

    degree = ""
    school = ""
    date_from = ""
    date_to = ""
    description = ""

    return jsonify({"degree" : degree, "school" : school, "date_from": date_from, "date_to": date_to, "description" : description}), 201





def delete_education(id):

    return jsonify({"msg" : "education deleted"}), 204