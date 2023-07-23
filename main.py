from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/map/<lng>/<lat>')
def mapService(lng, lat):
    return render_template('mapRegion.html', lng=float(lng), lat=float(lat))


if __name__ == '__main__':
    app.run(debug=True)