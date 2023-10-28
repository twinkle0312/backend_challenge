from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

def fetch_data_from_api():
    userid = []
    posts = []
    try:
        api_urlposts = "https://jsonplaceholder.typicode.com/posts"
        api_urlusers = "https://jsonplaceholder.typicode.com/users"
        
        # Send an HTTP GET request to the API endpoint
        response_posts = requests.get(api_urlposts)
        response_users = requests.get(api_urlusers)

        # Check if the request was successful (status code 200)
        if (response_posts.status_code == 200 & response_users.status_code == 200):
            # Parse the response content as JSON
            dataposts = response_posts.json()
            # Parse the response content as JSON
            datausers = response_users.json()
            for i in datausers:
                for j in dataposts:
                    if i["id"] == j["userId"]:
                        userid.append(i["id"])
                        posts.append(j["title"])

            return userid,posts

        else:
            # If the request was not successful, raise an exception
            response_posts.raise_for_status()

    except requests.exceptions.RequestException as e:
        # Handle any request exceptions or errors here
        print("Request Error:", e)

    return None  # Return None if there was an error

@app.route('/idpostdetails', methods=['GET'])

def get_users():
    data = fetch_data_from_api()
    #return data 
    
    if data:
        # Extract the list of user names and emails
        users_info = [{"user_id": user[0], "post_names": user[1]} for user in data]
        users_info =  jsonify(users_info)
        return render_template("display_data.html",users_info =users_info)
    else:
        return jsonify({"error": "Failed to fetch data from the API"})

if __name__ == '__main__':
    app.run(debug=True)