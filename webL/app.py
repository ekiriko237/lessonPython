#  create '23.xx.xx
#  s.nakamori from webL import app
from flask import render_template


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
    return render_template(
       'index.html'
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

