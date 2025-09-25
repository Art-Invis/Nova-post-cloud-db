from flask import request, jsonify
from auth.service.receivers_service import ReceiversService

def create_receiver_logic():
    try:
        data = request.get_json()
        required_fields = ['name', 'email', 'phone']
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        new_receiver = ReceiversService.create_receiver(data)
        return jsonify({
            "message": "Receiver created successfully",
            "receiver_id": new_receiver.receiver_id,
            "name": new_receiver.name,
            "email": new_receiver.email,
            "phone": new_receiver.phone
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_receivers_logic():
    try:
        receivers = ReceiversService.get_all_receivers()
        result = [
            {"receiver_id": r.receiver_id, "name": r.name, "email": r.email, "phone": r.phone}
            for r in receivers
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_receiver_by_id_logic(receiver_id):
    try:
        receiver = ReceiversService.get_receiver_by_id(receiver_id)
        if receiver:
            return jsonify({
                "receiver_id": receiver.receiver_id,
                "name": receiver.name,
                "email": receiver.email,
                "phone": receiver.phone
            }), 200
        return jsonify({"error": "Receiver not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_receiver_logic(receiver_id):
    try:
        data = request.get_json()
        updated_receiver = ReceiversService.update_receiver(
            receiver_id, data.get('name'), data.get('email'), data.get('phone')
        )
        return jsonify({"message": "Receiver updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def delete_receiver_logic(receiver_id):
    try:
        success = ReceiversService.delete_receiver(receiver_id)
        return jsonify({"message": "Receiver deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
