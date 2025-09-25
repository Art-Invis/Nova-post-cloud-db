from flask import request, jsonify
from auth.service.delivery_address_service import DeliveryAddressService

def create_address_logic():
    try:
        data = request.get_json()
        if not data.get('address'):
            return jsonify({"error": "Address is required"}), 400

        new_address = DeliveryAddressService.create_address(
            data['address'], data.get('delivery_instructions')
        )
        return jsonify({
            "message": "Address created successfully",
            "address_id": new_address.address_id,
            "address": new_address.address,
            "delivery_instructions": new_address.delivery_instructions
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_addresses_logic():
    try:
        addresses = DeliveryAddressService.get_all_addresses()
        result = [{"address_id": a.address_id, "address": a.address, "delivery_instructions": a.delivery_instructions} for a in addresses]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_address_by_id_logic(address_id):
    try:
        address = DeliveryAddressService.get_address_by_id(address_id)
        if address:
            result = {
                "address_id": address.address_id,
                "address": address.address,
                "delivery_instructions": address.delivery_instructions
            }
            return jsonify(result), 200
        return jsonify({"error": "Address not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_address_logic(address_id):
    try:
        data = request.get_json()
        if not data.get('address'):
            return jsonify({"error": "Address is required"}), 400

        updated_address = DeliveryAddressService.update_address(
            address_id, data['address'], data.get('delivery_instructions')
        )
        if updated_address:
            return jsonify({
                "message": "Address updated successfully",
                "address_id": updated_address.address_id,
                "address": updated_address.address,
                "delivery_instructions": updated_address.delivery_instructions
            }), 200
        return jsonify({"error": "Address not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def delete_address_logic(address_id):
    try:
        success = DeliveryAddressService.delete_address(address_id)
        if success:
            return jsonify({"message": "Address deleted successfully"}), 200
        return jsonify({"error": "Address not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
