from flask import Blueprint
from auth.controllers.delivery_address_controller import (
    create_address_logic,
    get_addresses_logic,
    get_address_by_id_logic,
    update_address_logic,
    delete_address_logic,
)

delivery_address_blueprint = Blueprint('delivery_addresses', __name__)

@delivery_address_blueprint.route('/addresses', methods=['POST'])
def create_address():
    """
    Create a new delivery address
    ---
    tags:
      - DeliveryAddress
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - address
            - delivery_instructions
          properties:
            address:
              type: string
              example: "Lviv, Halytska 5"
            delivery_instructions:
              type: string
              example: "Leave at reception"
    responses:
      201:
        description: Address created successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: Address created successfully
            address_id:
              type: integer
              example: 7
      400:
        description: Invalid input
      500:
        description: Internal server error
    """
    return create_address_logic()

@delivery_address_blueprint.route('/addresses', methods=['GET'])
def get_addresses():
    """
    Get all delivery addresses
    ---
    tags:
      - DeliveryAddress
    responses:
      200:
        description: List of all delivery addresses
        schema:
          type: array
          items:
            type: object
            properties:
              address_id:
                type: integer
                example: 1
              address:
                type: string
                example: "Kyiv, Shevchenka 10"
              delivery_instructions:
                type: string
                example: "Call before delivery"
      500:
        description: Internal server error
    """
    return get_addresses_logic()

@delivery_address_blueprint.route('/addresses/<int:address_id>', methods=['GET'])
def get_address_by_id(address_id):
    """
    Get delivery address by ID
    ---
    tags:
      - DeliveryAddress
    parameters:
      - name: address_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Delivery address details
        schema:
          type: object
          properties:
            address_id:
              type: integer
              example: 1
            address:
              type: string
              example: "Kyiv, Shevchenka 10"
            delivery_instructions:
              type: string
              example: "Call before delivery"
      404:
        description: Address not found
      500:
        description: Internal server error
    """
    return get_address_by_id_logic(address_id)

@delivery_address_blueprint.route('/addresses/<int:address_id>', methods=['PUT'])
def update_address(address_id):
    """
    Update delivery address by ID
    ---
    tags:
      - DeliveryAddress
    consumes:
      - application/json
    parameters:
      - name: address_id
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
            - address
            - delivery_instructions
          properties:
            address:
              type: string
              example: "Lviv, Halytska 5"
            delivery_instructions:
              type: string
              example: "Ring the bell twice"
    responses:
      200:
        description: Address updated successfully
      400:
        description: Invalid input
      404:
        description: Address not found
      500:
        description: Internal server error
    """
    return update_address_logic(address_id)

@delivery_address_blueprint.route('/addresses/<int:address_id>', methods=['DELETE'])
def delete_address(address_id):
    """
    Delete delivery address by ID
    ---
    tags:
      - DeliveryAddress
    parameters:
      - name: address_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Address deleted successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: Address deleted successfully
      404:
        description: Address not found
      500:
        description: Internal server error
    """
    return delete_address_logic(address_id)
