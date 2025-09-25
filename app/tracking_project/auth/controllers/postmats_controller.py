from flask import request, jsonify
from auth.service.postmats_service import PostmatsService

def create_postmat_logic():
    try:
        data = request.get_json()
        if not data.get('location') or not data.get('status') or not data.get('branch_id'):
            return jsonify({"error": "Location, status, and branch_id are required"}), 400

        new_postmat = PostmatsService.create_postmat(
            data['location'], data['status'], data['branch_id']
        )
        return jsonify({"message": "Postmat created successfully", "postmat_id": new_postmat.postmat_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_postmats_logic():
    try:
        postmats = PostmatsService.get_all_postmats()
        result = [
            {"postmat_id": p.postmat_id, "location": p.location, "status": p.status, "branch_id": p.branch_id}
            for p in postmats
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_postmat_by_id_logic(postmat_id):
    try:
        postmat = PostmatsService.get_postmat_by_id(postmat_id)
        return jsonify({
            "postmat_id": postmat.postmat_id,
            "location": postmat.location,
            "status": postmat.status,
            "branch_id": postmat.branch_id
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_postmat_logic(postmat_id):
    try:
        data = request.get_json()
        if not data.get('location') or not data.get('status') or not data.get('branch_id'):
            return jsonify({"error": "Location, status, and branch_id are required"}), 400

        updated_postmat = PostmatsService.update_postmat(
            postmat_id, data['location'], data['status'], data['branch_id']
        )
        return jsonify({"message": "Postmat updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def delete_postmat_logic(postmat_id):
    try:
        success = PostmatsService.delete_postmat(postmat_id)
        return jsonify({"message": "Postmat deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
