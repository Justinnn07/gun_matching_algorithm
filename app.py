from flask import Flask, request, jsonify
from datetime import datetime
from helpers import calculate_ashtakoota

app = Flask(__name__)
    



@app.route('/guna-milan', methods=['POST'])
def guna_milan_match():
    try:
        data = request.json  # Assuming JSON input

        if 'dob_user' not in data or 'dob_partner' not in data:
            return jsonify({'error': 'Missing date of birth values'}), 400

        dob_user = datetime.strptime(data['dob_user'], '%Y-%m-%d')
        dob_partner = datetime.strptime(data['dob_partner'], '%Y-%m-%d')

        compatibility_score = calculate_ashtakoota(dob_user, dob_partner)

        return jsonify({'compatibility_score':  compatibility_score })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
