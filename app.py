from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the homepage
@app.route("/")
def home():
    return "Hello, World! Welcome to my Flask app."

# Run the local development server
if __name__ == "__main__":
    app.run(debug=True)
