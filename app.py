from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        # process the form data
        report_data = {
            'title': request.form['title'],
            'content': request.form['content']
        }
        # render the report template with the data
        return render_template('report.html', data=report_data)
    else:
        # show the form
        return render_template('report.html')

if __name__ == '__main__':
    app.run(debug=True)
