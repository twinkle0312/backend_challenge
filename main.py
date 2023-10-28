from flask import Flask, jsonify
import requests

app = Flask(__name__)

def fetch_data_from_jsonplaceholder():
    try:
        api_url = "https://jsonplaceholder.typicode.com/users"
        
        # Send an HTTP GET request to the API endpoint
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json() # Parse the response content as JSON
            return data
        else:
            # If the request was not successful, raise an exception
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        # Handle any request exceptions or errors here
        print("Request Error:", e)

    return None  # Return None if there was an error

@app.route('/users', methods=['GET'])
def get_users():
    data = fetch_data_from_jsonplaceholder()

    if data:
        # Extract the list of user names and emails
        users_info = [{"name": user["name"], "email": user["email"]} for user in data]
        return jsonify(users_info)
    else:
        return jsonify({"error": "Failed to fetch data from the API"})

if __name__ == '__main__':
    app.run(debug=True)