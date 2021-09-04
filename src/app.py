from flask import Flask

app = Flask(__name__) # Created app object or flask object

@app.route('/', methods=['GET'])
def root():
    html = '''
    <html>
        <head>
            <title>String Services</title>
        </head>

        <body>
            <h1>String Services</h1>
            <p>RESTful APIs to perform string operations</p>
            <hr/>
            <h3>List of available string services</h3>
            <ul>
                <li>
                    <a href="/api/string" target="_blank">/api/string</a>: to get all available string APIs.
                </li>
            </ul>
        </body>
    </html>
    '''
    return html

@app.route('/api/string')
def string_apis():
    api = {
        'name': 'String APIs',
        'apis': [
            {
                'name': 'Word Counter',
                'description': 'APIs will return the occurancy of each word in given text as key value pair',
                'endpoint': '/api/string/word-counter?text=<<mytext>>'
            },
            {
                'name': 'Unique Words',
                'description': 'The API will return the list of unique words for a given text',
                'endpoint': '/api/string/unique-words'
            }
        ]
    }

    return api

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
