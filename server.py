from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route("/dojo")          # The "@" decorator associates this route with the function immediately following
def dojo():
    return 'have it say "Dojo!'   

@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hi, " + name


@app.route('/repeat/<string:username>/<int:num>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, num):
    return f"Hello {username * num}"




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 