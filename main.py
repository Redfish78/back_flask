from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/names')
def name_list():
    list_of_name = ['Frédéric', 'Jean-Yves', 'Michel', 'Mickaël']
    print(list_of_name)
    return jsonify(list_of_name)


if __name__ == '__main__':
    app.run()




