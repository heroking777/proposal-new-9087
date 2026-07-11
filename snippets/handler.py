from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy database to store sponsorships
sponsorships = []

@app.route('/api/sponsorships', methods=['POST'])
def create_sponsorship():
    data = request.get_json()
    
    # Validate input
    if not all(key in data for key in ['company_name', 'organization_name']):
        return jsonify({'error': 'Missing required fields'}), 400
    
    sponsorship_id = len(sponsorships) + 1
    new_sponsorship = {
        'id': sponsorship_id,
        'company_name': data['company_name'],
        'organization_name': data['organization_name']
    }
    
    sponsorships.append(new_sponsorship)
    
    return jsonify(new_sponsorship), 201

@app.route('/api/sponsorships', methods=['GET'])
def get_all_sponsorships():
    return jsonify(sponsorships)

if __name__ == '__main__':
    app.run(debug=True)