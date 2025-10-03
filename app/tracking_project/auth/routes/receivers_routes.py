from flask import Blueprint
from auth.controllers.receivers_controller import (
    create_receiver_logic,
    get_receivers_logic,
    get_receiver_by_id_logic,
    update_receiver_logic,
    delete_receiver_logic,
)

receivers_blueprint = Blueprint('receivers', __name__)

@receivers_blueprint.route('/receivers', methods=['POST'])
def create_receiver():
    """
    Create a new receiver
    ---
    tags:
      - Receivers
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
            - email
          properties:
            name:
              type: string
              example: "Ivan Petrenko"
            phone:
              type: string
              example: "+380931234567"
            email:
              type: string
              example: "ivan.petrenko@example.com"
    responses:
      201:
        description: Receiver created successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: Receiver created successfully
            receiver_id:
              type: integer
              example: 5
      400:
        description: Invalid input
      500:
        description: Internal server error
    """
    return create_receiver_logic()

@receivers_blueprint.route('/receivers', methods=['GET'])
def get_receivers():
    """
    Get all receivers
    ---
    tags:
      - Receivers
    responses:
      200:
        description: List of all receivers
        schema:
          type: array
          items:
            type: object
            properties:
              receiver_id:
                type: integer
                example: 1
              name:
                type: string
                example: "Ivan Petrenko"
              phone:
                type: string
                example: "+380931234567"
              email:
                type: string
                example: "ivan.petrenko@example.com"
      500:
        description: Internal server error
    """
    return get_receivers_logic()

@receivers_blueprint.route('/receivers/<int:receiver_id>', methods=['GET'])
def get_receiver_by_id(receiver_id):
    return get_receiver_by_id_logic(receiver_id)

@receivers_blueprint.route('/receivers/<int:receiver_id>', methods=['PUT'])
def update_receiver(receiver_id):
    """
    Update receiver by ID
    ---
    tags:
      - Receivers
    consumes:
      - application/json
    parameters:
      - name: receiver_id
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
            - email
          properties:
            name:
              type: string
              example: "Ivan Petrenko"
            phone:
              type: string
              example: "+380931234567"
            email:
              type: string
              example: "ivan.petrenko@example.com"
    responses:
      200:
        description: Receiver updated successfully
      400:
        description: Invalid input
      404:
        description: Receiver not found
      500:
        description: Internal server error
    """
    return update_receiver_logic(receiver_id)

@receivers_blueprint.route('/receivers/<int:receiver_id>', methods=['DELETE'])
def delete_receiver(receiver_id):
    """
    Delete receiver by ID
    ---
    tags:
      - Receivers
    parameters:
      - name: receiver_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Receiver deleted successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: Receiver deleted successfully
      404:
        description: Receiver not found
      500:
        description: Internal server error
    """
    return delete_receiver_logic(receiver_id)