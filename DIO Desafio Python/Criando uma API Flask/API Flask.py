from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/index', methods=['GET'])
def get_data():
    planilha_json = {
        "data": [
            {'Number': "1", 'Name': "Mahesh", 'Age': "25", 'City': "Bangalore", 'Country': "India"},
            {'Number': "2", 'Name': "Alex", 'Age': "26", 'City': "London", 'Country': "UK"},
            {'Number': "3", 'Name': "David", 'Age': "27", 'City': "San Francisco", 'Country': "USA"}
        ]
    }
    return jsonify(planilha_json)

if __name__ == '__main__':
    app.run(debug=True)

