from flask import Blueprint,request,jsonify
from app.services.receipts_services import process_receipt,get_receipt_points

receipts_bp = Blueprint("receipts",__name__)

@receipts_bp.route("/receipts/process",methods = ['POST'])
def process_receipts():
  data = request.get_json()
  if not data :
    return jsonify({"error":"Invalid Data"}),400

  # Placeholder for service data to return jsonId
  receipt_id = process_receipt(data)
  return jsonify({"id":receipt_id}),201


@receipts_bp.route("/receipts/<id>/process", methods = ["GET"])
def get_processed_receipt(id):
  # Placeholder for service logic to return points for receipt id
  points = get_receipt_points(id)
  
  if points is None :
    return jsonify({"error": "Receipt not found"}),404
    
  return jsonify({"id":id, "points":points})

