from flask import Flask, request, jsonify, send_from_directory
from cryptography.fernet import Fernet
import subprocess
import os

app = Flask(__name__)

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    message = data.get('message', '')
    encrypted_message = cipher_suite.encrypt(message.encode()).decode()
    return jsonify({'encrypted_message': encrypted_message})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    encrypted_message = data.get('encrypted_message', '')
    decrypted_message = cipher_suite.decrypt(encrypted_message.encode()).decode()
    return jsonify({'decrypted_message': decrypted_message})

@app.route('/secure_delete', methods=['POST'])
def secure_delete():
    data = request.json
    file_path = data.get('file_path', '')
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({'status': 'File securely deleted'})
    return jsonify({'status': 'File not found'})

@app.route('/system_info', methods=['GET'])
def system_info():
    try:
        # Use neofetch to get system information
        system_info_output = subprocess.check_output("neofetch --stdout", shell=True).decode().strip()
        return jsonify({'info': system_info_output})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/start_tor', methods=['POST'])
def start_tor():
    try:
        subprocess.Popen(["tor"])
        return jsonify({'status': 'Tor started successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/stop_tor', methods=['POST'])
def stop_tor():
    try:
        subprocess.call(["pkill", "tor"])
        return jsonify({'status': 'Tor stopped successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/check_wifi_security', methods=['GET'])
def check_wifi_security():
    try:
        # Placeholder for actual WiFi security check logic
        # Simulating WiFi security check for demo purposes
        # In a real scenario, this would check the actual WiFi security settings
        wifi_security_level = "WPA"  # Replace with actual check
        if wifi_security_level == "WPA":
            wifi_security_info = "WiFi is not secure. It is recommended to switch to WPA2 or WPA3 for better security."
        else:
            wifi_security_info = "WiFi is secure."
        return jsonify({'wifi_security': wifi_security_info})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/block_ads', methods=['POST'])
def block_ads():
    try:
        # Placeholder for actual ad-blocking logic
        ad_block_status = "Ads blocked successfully."
        return jsonify({'status': ad_block_status})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/check_updates', methods=['GET'])
def check_updates():
    try:
        # Placeholder for checking updates
        update_status = "All packages are up-to-date."
        return jsonify({'status': update_status})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/install_updates', methods=['POST'])
def install_updates():
    try:
        # Placeholder for installing updates
        update_install_status = "Updates installed successfully."
        return jsonify({'status': update_install_status})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

