import json
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Load the restaurant data from the JSON file
def load_restaurant_data():
    """Reads the JSON file and returns the list of restaurants."""
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("Error: data.json not found. Check your file path.")
        return []

@app.route('/')
def index():
    """Renders the main page, passing the restaurant data to the template."""
    restaurants = load_restaurant_data()
    return render_template('index.html', restaurants=restaurants)

# Run the app
if __name__ == '__main__':
    # Set debug=True for automatic reloads during development
    app.run(debug=True)