from flask import Flask, render_template
from static import wrangling_data
import plotly, json
import plotly.graph_objs as go

ids,figure_json = wrangling_data.plot1()

# set up our applications
app = Flask(__name__)

# create index route
@app.route('/')
def index():
    # send the json figure to the font end
    return render_template('index.html',
                           figure_json = figure_json,
                           ids = ids)

if __name__ == '__main__':
    app.run(debug=True)



