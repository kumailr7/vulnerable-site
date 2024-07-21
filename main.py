from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Welcome to Python Website</h1>
        <form action="/search" method="get">
            <label for="query">Search:</label>
            <input type="text" id="query" name="query">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/search')
def search():
    query = request.args.get('query', '')
    return render_template_string(f'''
        <h1>Welcome to Python Website</h1>
        <p>You searched for: <strong>{query}</strong></p>
        <div id="search-result">
            <p>Displaying results for <em>{query}</em></p>
            <script>
                // Simulate some JavaScript behavior
                document.getElementById('search-result').innerHTML += '<p>Extra info about "<span>{query}</span>"</p>';
            </script>
            <img src="x" onerror="this.src='https://via.placeholder.com/150'; alert('XSS');">
        </div>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
