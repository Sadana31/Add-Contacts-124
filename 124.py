from flask import Flask,jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'Name': u'Renuka',
        'number': u'9940048341', 
        'Type': "Family"
    },
    {
        'id': 2,
        'Name': u'Sadana',
        'number': u'994140043', 
        'Type': "Business"
    }
]

@app.route("/add-contact", methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the contact!"
        },400)

    contact = {
        'id': contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'number': request.json.get('number', ""),
        'Type': request.json['Type']
    }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message": "contact added succesfully!"
    })

@app.route("/get-contact")
def get_contact():
    return jsonify({
        "contact" : contacts
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)