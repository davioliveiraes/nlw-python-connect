from flask import Blueprint, jsonify, request

event_route_bp = Blueprint('event_route', __name__)

from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest

@event_route_bp.route('/event', methods=['POST'])
def create_new_event():
    httpRequest = HttpRequest(body=request.json)
    print(httpRequest.body)

    http_response = HttpResponse({'message': 'Event created successfully!'}, status_code=201)

    return jsonify(http_response.body), http_response.status_code
