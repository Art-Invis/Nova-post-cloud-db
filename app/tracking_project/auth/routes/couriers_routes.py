from flask import Blueprint
from flask_jwt_extended import jwt_required
from auth.controllers.couriers_controller import (
    create_courier_logic,
    get_couriers_logic,
    get_courier_by_id_logic,
    update_courier_logic,
    delete_courier_logic,
)

couriers_blueprint = Blueprint('couriers', __name__)

@couriers_blueprint.route('/couriers', methods=['POST'])
@jwt_required()
def create_courier():
    """
    Create a new courier (🔒 JWT required)
    ---
    tags:
      - Couriers
    security:
      - BearerAuth: []
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - name
            - phone
            - vehicle_type
          properties:
            name:
              type: string
              example: "Oksana Danylko"
            phone:
              type: string
              example: "+380671234567"
            vehicle_type:
              type: string
              enum: ["Car", "Bike", "Van"]
              example: "Bike"
    responses:
      201:
        description: Courier created successfully
      401:
        description: Missing or invalid token
      400:
        description: Invalid input
    """
    return create_courier_logic()

@couriers_blueprint.route('/couriers', methods=['GET'])
@jwt_required()
def get_couriers():
    """
    Get all couriers (🔒 JWT required)
    ---
    tags:
      - Couriers
    responses:
      200:
        description: List of couriers
        schema:
          type: array
          items:
            type: object
            properties:
              courier_id:
                type: integer
                example: 1
              name:
                type: string
                example: "Oksana Danylko"
              phone:
                type: string
                example: "+380671234567"
              vehicle_type:
                type: string
                example: "Bike"
      500:
        description: Internal server error
    """
    return get_couriers_logic()

@couriers_blueprint.route('/couriers/<int:courier_id>', methods=['GET'])
@jwt_required()
def get_courier_by_id(courier_id):
    """
    Get courier by ID (🔒 JWT required)
    ---
    tags:
      - Couriers
    parameters:
      - name: courier_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Courier object
        schema:
          type: object
          properties:
            courier_id:
              type: integer
              example: 1
            name:
              type: string
              example: "Oksana Danylko"
            phone:
              type: string
              example: "+380671234567"
            vehicle_type:
              type: string
              example: "Bike"
      404:
        description: Courier not found
      500:
        description: Internal server error
    """
    return get_courier_by_id_logic(courier_id)

@couriers_blueprint.route('/couriers/<int:courier_id>', methods=['PUT'])
@jwt_required()
def update_courier(courier_id):
    """
    Update courier by ID (🔒 JWT required)
    ---
    tags:
      - Couriers
    consumes:
      - application/json
    parameters:
      - name: courier_id
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
            - name
            - phone
            - vehicle_type
          properties:
            name:
              type: string
              example: "Oksana Danylko"
            phone:
              type: string
              example: "+380671234567"
            vehicle_type:
              type: string
              enum: ["Car", "Bike", "Van"]
              example: "Van"
    responses:
      200:
        description: Courier updated successfully
      400:
        description: Invalid input
      404:
        description: Courier not found
      500:
        description: Internal server error
    """
    return update_courier_logic(courier_id)

@couriers_blueprint.route('/couriers/<int:courier_id>', methods=['DELETE'])
@jwt_required()
def delete_courier(courier_id):
    """
    Delete courier by ID (🔒 JWT required)
    ---
    tags:
      - Couriers
    parameters:
      - name: courier_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Courier deleted successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: Courier deleted successfully
      404:
        description: Courier not found
      500:
        description: Internal server error
    """
    return delete_courier_logic(courier_id)
