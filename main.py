from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    api_url = None
    api_data = None
    error = None
    if request.method == 'POST':
        try:
            api_url = request.form['apiUrl']
            response = requests.get(api_url)
            response.raise_for_status()
            api_data = response.json()
        except KeyError:
            error = "API URL is required."
        except requests.exceptions.RequestException as e:
            error = f"Error fetching data from API: {e}"
    return render_template('index.html', api_url=api_url, api_data=api_data, error=error)


if __name__ == '__main__':
    app.run(debug=True)
