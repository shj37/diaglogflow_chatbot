from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"student_number": "200597900"})

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the JSON data from the DialogFlow request
    data = request.get_json(silent=True, force=True)
    
    # Extract the necessary information from the request
    # This is a simple example; you may need to modify this based on your specific DialogFlow intents
    intent = data['queryResult']['intent']['displayName']
    
    # Prepare the response
    if intent == "company address enquiry":
        response_text = "Our current address is 123 Barrie Street, Barrie, Ontario, Canada"
    else:
        response_text = "I'm not sure how to respond to that."
    
    # Return the response in the format expected by DialogFlow
    return jsonify({
        "fulfillmentText": response_text,
        "source": "webhook"
    })

if __name__ == '__main__':
    app.run(debug=True)