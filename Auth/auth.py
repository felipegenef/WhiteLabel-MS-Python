import jwt
from flask import request,jsonify
import os
from functools import wraps

def verify_jwt(token):
    try:
        payload = jwt.decode(token, os.environ["JWT_SECRET"], algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None  # Token expired
    except jwt.InvalidTokenError:
        return None  # Invalid token
    
def jwt_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Check if JWT token is present in the Authorization header
        token = request.headers.get('Authorization', None)
        if not token:
            return jsonify({"error": "JWT token missing"}), 401

        # Verify and decode the token
        payload = verify_jwt(token)
        if not payload:
            return jsonify({"error": "Invalid or expired JWT token"}), 401

        # Add token data to the request context
        request.jwt_payload = payload

        # Call the original function with the request context
        return func(*args, **kwargs)

    return wrapper

