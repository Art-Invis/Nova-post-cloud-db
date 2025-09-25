from flask import jsonify
from auth.service.branches_senders_service import BranchesSendersService

def get_branches_with_senders_logic():
    try:
        relations = BranchesSendersService.get_all_branch_sender_relations()
        branches_dict = {}

        for relation in relations:
            branch_id = relation.branch.branch_id
            if branch_id not in branches_dict:
                branches_dict[branch_id] = {
                    "branch_id": branch_id,
                    "branch_address": relation.branch.address,
                    "branch_ip": relation.branch.branch_ip,
                    "phone": relation.branch.phone,
                    "senders": []
                }
            branches_dict[branch_id]["senders"].append({
                "sender_id": relation.sender.sender_id,
                "full_name": relation.sender.full_name,
                "phone": relation.sender.phone,
                "email": relation.sender.email
            })
        
        return jsonify(list(branches_dict.values())), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_branches_and_senders_logic():
    try:
        relations = BranchesSendersService.get_all_branch_sender_relations()
        branch_result = {}
        sender_result = {}

        for relation in relations:
            branch_id = relation.branch.branch_id
            sender_id = relation.sender.sender_id

            if branch_id not in branch_result:
                branch_result[branch_id] = {
                    "branch_id": branch_id,
                    "branch_address": relation.branch.address,
                    "branch_ip": relation.branch.branch_ip,
                    "phone": relation.branch.phone,
                    "senders": []
                }
            branch_result[branch_id]["senders"].append({
                "sender_id": sender_id,
                "full_name": relation.sender.full_name,
                "phone": relation.sender.phone,
                "email": relation.sender.email
            })

            if sender_id not in sender_result:
                sender_result[sender_id] = {
                    "sender_id": sender_id,
                    "full_name": relation.sender.full_name,
                    "phone": relation.sender.phone,
                    "email": relation.sender.email,
                    "branches": []
                }
            sender_result[sender_id]["branches"].append({
                "branch_id": branch_id,
                "branch_address": relation.branch.address,
                "branch_ip": relation.branch.branch_ip,
                "phone": relation.branch.phone
            })

        response = {
            "branches": list(branch_result.values()),
            "senders": list(sender_result.values())
        }

        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
