from flask import Flask, render_template, request, abort
from vehicle import Vehicle
from config import WEB_PORT

app = Flask(__name__)

vehicle = Vehicle()

handle_map = {
    'forward': vehicle.forward,
    'left': vehicle.left,
    'right': vehicle.right,
    'pause': vehicle.stop,
    'backward': vehicle.backward,
}


@app.route('/', methods=['GET'])
def main_page():
    return render_template("index.html")


@app.route('/handle', methods=['GET'])
def handle():
    try:
        operation = request.args.get('type', '')
    except ValueError:
        abort(404)
    else:
        if operation in handle_map.iterkeys():
            handle_map[operation]()
        else:
            abort(404)
    return 'ok'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=WEB_PORT, debug=False)
