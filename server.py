from flask import Flask, request, jsonify
from prime_factors import find_prime_factors

app = Flask(__name__)

@app.route('/receive_message', methods=['POST'])
def receive_message():
    data = request.get_json()
    print(f"data recieved {data}")

    # Test if the request has the number key
    try:
        number_to_evaluate = data['number']
        print(f"number to evaluate {number_to_evaluate}")
    except Exception as e:
        error_string = f"There was an error in trying to access the 'number' key. Make sure you have the 'number' key in the body of your request."
        response = {"status": "Failure", "message": error_string}
        return jsonify(response), 400 # Bad request return

    # Test if the request passes in a number
    try:
        number_converted_to_int = int(number_to_evaluate)
    except Exception as e:
        error_string = f"An error occured in trying to convert your call to an integer. Make sure you are passing in a valid integer. The error is: {e}"
        response = {"status": "Failure", "message": error_string}
        return jsonify(response), 400 # Bad request return
    
    # Test if the number is > 1
    if number_converted_to_int < 2:
        error_string = "The number must be greater than 1"
        response = {"status": "Failure", "message": error_string}
        return jsonify(response), 400 # Bad request return
    
    # Try to return the prime factors
    try:
        prime_factors = find_prime_factors(number_converted_to_int)
        print(f"prime factors: {prime_factors}")
    except Exception as e:
        error_string = f"An error occured in finding the prime factors. Reach out to the developers. The error is: {e}"
        response = {"status": "Failure", "message": error_string}
        return jsonify(response), 500 # Server side error
    
    # Send a response back to the caller
    response = {"status": "Success", "message": prime_factors}
    return jsonify(response), 200


if __name__ == '__main__':
    # Run the server on localhost:50000
    app.run(debug=True, port=50000)
