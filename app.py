from flask import Flask, jsonify, request # type: ignore
from Camera.cognex_telnet import capture_image_via_telnet_dummy, capture_image_via_telnet

app = Flask(__name__)

# 1 Capture an image using Cognex Telnet
@app.route('/capture', methods=['GET'])
def capture():
    filename = request.args.get("filename")  # Get filename from query parameter
    
    if not filename:
        return jsonify({"error": "Filename parameter is required"}), 400
    
    result = capture_image_via_telnet(filename)
    
    if "Error" in result:
        return jsonify({"error": result}), 500

    return jsonify({"message": result}), 200

# Dummy Capture API
@app.route('/capture_dummy', methods=['GET'])
def capture_dummy():
    filename = request.args.get("filename")  # Get filename from query parameter
    
    if not filename:
        return jsonify({"error": "Filename parameter is required"}), 400
    
    result = capture_image_via_telnet_dummy(filename)
    return jsonify({"result": result}), 200

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "running"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)