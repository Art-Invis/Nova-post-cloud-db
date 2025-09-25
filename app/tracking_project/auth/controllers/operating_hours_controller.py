from flask import request, jsonify
from auth.service.operating_hours_service import OperatingHoursService
from datetime import datetime

def validate_time_format(time_str):
    try:
        datetime.strptime(time_str, '%H:%M:%S')
        return True
    except ValueError:
        return False

def create_operating_hours_logic():
    try:
        data = request.get_json()
        if not validate_time_format(data['open_time']) or not validate_time_format(data['close_time']):
            return jsonify({"error": "Invalid time format. Expected format: HH:MM:SS"}), 400

        new_hours = OperatingHoursService.create_operating_hours(
            data['day'], data['open_time'], data['close_time']
        )
        return jsonify({"message": "Operating hours created successfully", "hours_id": new_hours.hours_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_operating_hours_logic():
    try:
        hours = OperatingHoursService.get_all_operating_hours()
        result = [{"hours_id": h.hours_id, "day": h.day, "open_time": str(h.open_time), "close_time": str(h.close_time)} for h in hours]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_operating_hours_logic(hours_id):
    try:
        data = request.get_json()
        if not validate_time_format(data['open_time']) or not validate_time_format(data['close_time']):
            return jsonify({"error": "Invalid time format. Expected format: HH:MM:SS"}), 400

        updated_hours = OperatingHoursService.update_operating_hours(
            hours_id, data['day'], data['open_time'], data['close_time']
        )
        return jsonify({"message": "Operating hours updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def delete_operating_hours_logic(hours_id):
    try:
        success = OperatingHoursService.delete_operating_hours(hours_id)
        if success:
            return jsonify({"message": "Operating hours deleted successfully"}), 200
        return jsonify({"error": "Operating hours not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
