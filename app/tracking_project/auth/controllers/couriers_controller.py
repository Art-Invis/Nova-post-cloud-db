from flask import request, jsonify
from auth.service.couriers_service import CouriersService

def create_courier_logic():
    try:
        data = request.get_json()
        new_courier = CouriersService.create_courier(data['name'], data['phone'], data['vehicle_type'])
        return jsonify({"message": "Courier created successfully", "courier_id": new_courier.courier_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_couriers_logic():
    try:
        couriers = CouriersService.get_all_couriers()
        result = [{"courier_id": c.courier_id, "name": c.name, "phone": c.phone, "vehicle_type": c.vehicle_type} for c in couriers]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_courier_by_id_logic(courier_id):
    try:
        courier = CouriersService.get_courier_by_id(courier_id)
        return jsonify({"courier_id": courier.courier_id, "name": courier.name, "phone": courier.phone, "vehicle_type": courier.vehicle_type}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_courier_logic(courier_id):
    try:
        data = request.get_json()
        updated_courier = CouriersService.update_courier(courier_id, data['name'], data['phone'], data['vehicle_type'])
        return jsonify({"message": "Courier updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def delete_courier_logic(courier_id):
    try:
        success = CouriersService.delete_courier(courier_id)
        return jsonify({"message": "Courier deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
