from flask import Blueprint
from auth.controllers.operating_hours_controller import (
    create_operating_hours_logic,
    get_operating_hours_logic,
    update_operating_hours_logic,
    delete_operating_hours_logic,
)

operating_hours_blueprint = Blueprint('operating_hours', __name__)

@operating_hours_blueprint.route('/operating_hours', methods=['POST'])
def create_operating_hours():
    """
    Create new operating hours
    ---
    tags:
      - OperatingHours
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - day
            - open_time
            - close_time
          properties:
            day:
              type: string
              example: "Monday"
            open_time:
              type: string
              format: time
              example: "08:00:00"
            close_time:
              type: string
              format: time
              example: "18:00:00"
    responses:
      201:
        description: Operating hours created successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: Operating hours created successfully
            hours_id:
              type: integer
              example: 3
      400:
        description: Invalid input
      500:
        description: Internal server error
    """
    return create_operating_hours_logic()

@operating_hours_blueprint.route('/operating_hours', methods=['GET'])
def get_operating_hours():
    """
    Get all operating hours
    ---
    tags:
      - OperatingHours
    responses:
      200:
        description: List of all operating hours
        schema:
          type: array
          items:
            type: object
            properties:
              hours_id:
                type: integer
                example: 1
              day:
                type: string
                example: "Monday"
              open_time:
                type: string
                format: time
                example: "08:00:00"
              close_time:
                type: string
                format: time
                example: "18:00:00"
      500:
        description: Internal server error
    """
    return get_operating_hours_logic()

@operating_hours_blueprint.route('/operating_hours/<int:hours_id>', methods=['PUT'])
def update_operating_hours(hours_id):
    """
    Update operating hours by ID
    ---
    tags:
      - OperatingHours
    consumes:
      - application/json
    parameters:
      - name: hours_id
        in: path
        required: true
        type: integer
        example: 1
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - day
            - open_time
            - close_time
          properties:
            day:
              type: string
              example: "Tuesday"
            open_time:
              type: string
              format: time
              example: "09:00:00"
            close_time:
              type: string
              format: time
              example: "17:00:00"
    responses:
      200:
        description: Operating hours updated successfully
      400:
        description: Invalid input
      404:
        description: Operating hours not found
      500:
        description: Internal server error
    """
    return update_operating_hours_logic(hours_id)

@operating_hours_blueprint.route('/operating_hours/<int:hours_id>', methods=['DELETE'])
def delete_operating_hours(hours_id):
    """
    Delete operating hours by ID
    ---
    tags:
      - OperatingHours
    parameters:
      - name: hours_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Operating hours deleted successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: Operating hours deleted successfully
      404:
        description: Operating hours not found
      500:
        description: Internal server error
    """
    return delete_operating_hours_logic(hours_id)
