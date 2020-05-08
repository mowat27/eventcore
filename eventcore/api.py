from flask import Flask
import json

app = Flask('eventcore_api')


@app.route('/')
def index():
    return json.dumps({"items": []})


if __name__ == "__main__":
    app.run(debug=True)
