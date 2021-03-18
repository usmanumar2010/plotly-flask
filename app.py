from flask import Flask, render_template

import json
import plotly
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
import numpy as np
import dash
import psycopg2
import pandas as pd
app = Flask(__name__)
app.debug = True


@app.route('/')
def index():


    years_list = ['2016','2017','2018','2019','2020','2021']
    yearly_revenue =[1000,2000,3000,1500,900,500]
    months=[1,2,3,4,5,6,7,8,9,10,11,12]
    rng = pd.date_range('1/1/2011', periods=7500, freq='H')
    ts = pd.Series(np.random.randn(len(rng)), index=rng)
    card1 = 111
    card2 = 222
    graphs = [

        dict(
           data=[
                 dict(
                    x=months,
                    y=[2,3,4,5,6,1,2,9,8,4,0,8],
                     name=2019,
                    type='line'
                  ),
                   dict(
                       x=months,
                       y=[1,2,3,4,5,6,7,8,9,10,11,12],
                       name=2020,
                       type='line'
                   ),
                   dict(
                       x=months,
                       y=[2, 3, 4, 5, 6, 1, 2, 9, 8, 4, 0, 8],
                       name=2021,
                       type='line'
                   )
                 ],
        ),

        dict(
            data=[
                dict(
                    x=years_list,
                    y=yearly_revenue,
                    type='bar'
                ),
            ],
            layout=dict(
                title='second graph'
            )
        ),

        dict(
            data=[
                dict(
                    x=[1, 2, 3],
                    y=[10, 20, 30],
                    type='scatter'
                ),
            ],
            layout=dict(
                title='first graph'
            )
        ),

        dict(
            data=[
                dict(
                    x=ts.index,  # Can use the pandas data structures directly
                    y=ts
                )
            ]
        ),

        dict(
            data=[
                dict(
                    x=["a","b","c"],  # Can use the pandas data structures directly
                    y=[1,3,4],
                    type='line'
                ),
                dict(
                    x=["a", "b", "c"],  # Can use the pandas data structures directly
                    y=[2, 7, 8],
                    type='line'

                )

            ]
        )



    ]




    # Add "ids" to each of the graphs to pass up to the client
    # for templating
    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    cards=card1,card2
    return render_template('layouts/index.html',
                           ids=ids,
                           graphJSON=graphJSON,cards=cards)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
