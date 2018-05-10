from flask import Flask
from flask import jsonify

from palindromy.palindromes_analyser import palindromes_in_json_keys, count_palindromes

import pkg_resources

app = Flask(__name__)

# This code below is only a workaround to keep a complete test within the time constraints

# It should be changed to read dynamically, but kept this way to deliver a first version
# one option is to post first the whole dataset for analyses, or post together with the GET request
# Another option is to use a POST, and post the content for analysis, receiving back the results
path = 'sample_data/jsons.json'
input_data = pkg_resources.resource_string(__name__, path).splitlines()


@app.route('/')
def running():
    return 'service running!'


@app.route('/palindromes', methods=['GET'])
def palindromes():
    return jsonify(palindromes_in_json_keys(input_data))


@app.route('/palindromes/count', methods=['GET'])
def palindromes_count():
    return jsonify(count_palindromes(input_data))


if __name__ == '__main__':
    app.run()
