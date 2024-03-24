
from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/change_color', methods=['GET'])
def change_color():
    color = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
    return jsonify({'color': color})

if __name__ == '__main__':
    app.run()
