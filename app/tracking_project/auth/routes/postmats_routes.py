from flask import Blueprint
from auth.controllers.postmats_controller import (
    create_postmat_logic,
    get_postmats_logic,
    get_postmat_by_id_logic,
    update_postmat_logic,
    delete_postmat_logic,
)

postmats_blueprint = Blueprint('postmats', __name__)

@postmats_blueprint.route('/postmats', methods=['POST'])
def create_postmat():
    """
    Create a new postmat
    ---
    tags:
      - Postmats
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - location
            - status
            - branch_id
          properties:
            location:
              type: string
              example: "Kyiv, Shevchenka 10"
            status:
              type: string
              example: "active"
            branch_id:
              type: integer
              example: 1
    responses:
      201:
        description: Postmat created successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: Postmat created successfully
            postmat_id:
              type: integer
              example: 5
      400:
        description: Invalid input
      500:
        description: Internal server error
    """
    return create_postmat_logic()

@postmats_blueprint.route('/postmats', methods=['GET'])
def get_postmats():
    """
    Get all postmats
    ---
    tags:
      - Postmats
    responses:
      200:
        description: List of all postmats
        schema:
          type: array
          items:
            type: object
            properties:
              postmat_id:
                type: integer
                example: 1
              location:
                type: string
                example: "Kyiv, Shevchenka 10"
              status:
                type: string
                example: "active"
              branch_id:
                type: integer
                example: 3
      500:
        description: Internal server error
    """
    return get_postmats_logic()

@postmats_blueprint.route('/postmats/<int:postmat_id>', methods=['GET'])
def get_postmat_by_id(postmat_id):
    """
    Get postmat by ID
    ---
    tags:
      - Postmats
    parameters:
      - name: postmat_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Postmat details
        schema:
          type: object
          properties:
            postmat_id:
              type: integer
              example: 1
            location:
              type: string
              example: "Kyiv, Shevchenka 10"
            status:
              type: string
              example: "active"
            branch_id:
              type: integer
              example: 3
      404:
        description: Postmat not found
      500:
        description: Internal server error
    """
    return get_postmat_by_id_logic(postmat_id)

@postmats_blueprint.route('/postmats/<int:postmat_id>', methods=['PUT'])
def update_postmat(postmat_id):
    """
    Update postmat by ID
    ---
    tags:
      - Postmats
    consumes:
      - application/json
    parameters:
      - name: postmat_id
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
            - location
            - status
            - branch_id
          properties:
            location:
              type: string
              example: "Lviv, Halytska 5"
            status:
              type: string
              example: "inactive"
            branch_id:
              type: integer
              example: 2
    responses:
      200:
        description: Postmat updated successfully
      400:
        description: Invalid input
      404:
        description: Postmat not found
      500:
        description: Internal server error
    """
    return update_postmat_logic(postmat_id)

@postmats_blueprint.route('/postmats/<int:postmat_id>', methods=['DELETE'])
def delete_postmat(postmat_id):
    """
    Delete postmat by ID
    ---
    tags:
      - Postmats
    parameters:
      - name: postmat_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Postmat deleted successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: Postmat deleted successfully
      404:
        description: Postmat not found
      500:
        description: Internal server error
    """
    return delete_postmat_logic(postmat_id)
