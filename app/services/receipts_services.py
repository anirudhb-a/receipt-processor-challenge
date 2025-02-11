import uuid
import math
import hashlib
from datetime import datetime

# In-memory storage for receipts (receipt_id -> points)
receipts_db = {}

def generate_receipt_id(data):
    """
    Generates a unique deterministic ID based on receipt content using SHA-256.
    
    Args:
        data (dict): The receipt data.

    Returns:
        str: A hash-based unique ID.
    """
    receipt_string = str(data)  # Convert the receipt data to string
    receipt_hash = hashlib.sha256(receipt_string.encode()).hexdigest()  # Generate hash
    return receipt_hash[:16]  # Shorten the hash for readability

def process_receipt(data):
    """
    Processes a receipt, calculates points, and stores it only if not duplicated.
    
    Args:
        data (dict): The receipt data.
    
    Returns:
        str: The generated receipt ID.
    """
    receipt_id = generate_receipt_id(data)  # Generate deterministic ID

    # Check if the receipt already exists
    if receipt_id in receipts_db:
        return receipt_id  # Return existing ID without re-processing

    # Extract receipt details
    retailer = data.get("retailer", "")
    total = float(data.get("total", 0.0))
    items = data.get("items", [])
    purchase_date = data.get("purchaseDate", "")
    purchase_time = data.get("purchaseTime", "")

    # Calculate points
    points = 0
    
    # 1️⃣ One point for every alphanumeric character in the retailer name
    points += sum(1 for char in retailer if char.isalnum())

    # 2️⃣ 50 points if the total is a round dollar amount with no cents
    if total.is_integer():
        points += 50

    # 3️⃣ 25 points if the total is a multiple of 0.25
    if total % 0.25 == 0:
        points += 25

    # 4️⃣ 5 points for every two items on the receipt
    points += (len(items) // 2) * 5

    # 5️⃣ If the trimmed length of the shortDescription is a multiple of 3, multiply price by 0.2, round up
    for item in items:
        description = item.get("shortDescription", "").strip()
        price = float(item.get("price", 0.0))

        if len(description) % 3 == 0:
            points += math.ceil(price * 0.2)

    # 6️⃣ 5 points if the total is greater than 10.00
    if total > 10.00:
        points += 5

    # 7️⃣ 6 points if the day in the purchase date is odd
    try:
        purchase_day = int(datetime.strptime(purchase_date, "%Y-%m-%d").day)
        if purchase_day % 2 == 1:
            points += 6
    except ValueError:
        pass  # Ignore if date format is incorrect

    # 8️⃣ 10 points if the time of purchase is after 2:00pm and before 4:00pm
    try:
        purchase_time_obj = datetime.strptime(purchase_time, "%H:%M")
        if purchase_time_obj.hour == 14:  # 2:00 PM to 3:59 PM
            points += 10
    except ValueError:
        pass  # Ignore if time format is incorrect

    # Store the receipt data
    receipts_db[receipt_id] = points  # Store only points for now

    return receipt_id

def get_receipt_points(receipt_id):
    """
    Retrieves the points for a given receipt ID.

    Args:
        receipt_id (str): The receipt ID.

    Returns:
        int or None: The points associated with the receipt, or None if not found.
    """
    return receipts_db.get(receipt_id)
