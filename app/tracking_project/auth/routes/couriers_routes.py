from flask import Blueprint
from auth.controllers.couriers_controller import (
    create_courier_logic,
    get_couriers_logic,
    get_courier_by_id_logic,
    update_courier_logic,
    delete_courier_logic,
)

couriers_blueprint = Blueprint('couriers', __name__)

@couriers_blueprint.route('/couriers', methods=['POST'])
def create_courier():
    return create_courier_logic()

@couriers_blueprint.route('/couriers', methods=['GET'])
def get_couriers():
    """
    Get all couriers
    ---
    tags:
      - Couriers
    responses:
      200:
        description: List of couriers
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  courier_id:
                    type: integer
                  name:
                    type: string
                  phone:
                    type: string
    """
    return get_couriers_logic()

@couriers_blueprint.route('/couriers/<int:courier_id>', methods=['GET'])
def get_courier_by_id(courier_id):
    """
    Get courier by ID
    ---
    tags:
      - Couriers
    parameters:
      - name: courier_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Courier object
      404:
        description: Courier not found
    """
    return get_courier_by_id_logic(courier_id)

@couriers_blueprint.route('/couriers/<int:courier_id>', methods=['PUT'])
def update_courier(courier_id):
    return update_courier_logic(courier_id)

@couriers_blueprint.route('/couriers/<int:courier_id>', methods=['DELETE'])
def delete_courier(courier_id):
    return delete_courier_logic(courier_id)
