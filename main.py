import pandas as pd     #(version 1.0.0)

import dash             #(version 1.9.1) pip install dash==1.9.1
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import requests
import json
import dash_table
import dash_bootstrap_components as dbc

#from script import get_total_sms

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

#-------------------------------------------------------------------------------


def update_all_sms():
    query = {'find': 'allsms'}

    data = requests.post('https://enigmatic-woodland-58661.herokuapp.com/statistics', json = query).json()

    string_dict = data['response']

    data_json = json.loads(string_dict)

    data_df = pd.DataFrame(data_json)

    print(data_df)
    return([
            dash_table.DataTable(
                id ='table',
                columns=[{"name": i, "id": i} for i in data_df.columns],
                data=data_df.to_dict('records'),

                style_header={
                'backgroundColor': 'rgb(230, 230, 230)',
                'fontWeight': 'bold'
                },
                style_data_conditional=[


                    {
                        'if': {'row_index': 'odd'},
                        'backgroundColor': 'rgb(248, 248, 248)'
                    }
                ],

                style_as_list_view=True

            )
        
    ])


def get_all_sms():
    query = {'find': 'allsms'}

    data = requests.post('https://enigmatic-woodland-58661.herokuapp.com/statistics', json = query).json()

    string_dict = data['response']

    data_json = json.loads(string_dict)

    data_df = pd.DataFrame(data_json)

    return (
        [
            html.Div(
            id = "data",
            style={'width': '50%', 'display': 'inline-block'},
            children = [
                html.Div(
                    children = [
                        html.P(style ={
                                        'textAlign': 'center',
                                        'fontWeight': 'bold',


                                       },
                                children ="Total SMS"
                                       ),
                                
                        html.H3(
                                id='n_total_sms',
                                style = {'textAlign': 'center',
                                          'fontWeight': 'bold'
                                        },
                                children = '{}'.format(len(data_df)),

                        )
                    ]
                )
            ]
            
        )

        ]
    )

#-------------------------------------------------------------------------------
app.layout = html.Div([
    dcc.Interval(
                id='my_interval',
                disabled=False,     #if True the counter will no longer update
                n_intervals=0,      #number of times the interval has passed
                interval=60*1000,  #increment the counter n_intervals every 5 minutes
                max_intervals=100,  #number of times the interval will be fired.
                                    #if -1, then the interval has no limit (the default)
                                    #and if 0 then the interval stops running.
    ),
    dcc.Interval(
                id='new_interval',
                disabled=False,     #if True the counter will no longer update
                n_intervals=0,      #number of times the interval has passed
                interval=60*1000,  #increment the counter n_intervals every 5 minutes
                max_intervals=100,  #number of times the interval will be fired.
                                    #if -1, then the interval has no limit (the default)
                                    #and if 0 then the interval stops running.
    ),
#-----------------------------------------------------------------
#THE LAYOUT STARTS HERE

    html.Div([
        html.Div([
            html.H1('ULANGA',
            style={'fontWeight': 'bold'}
            ),

        ], style={'width': '60%', 'display': 'inline-block'}),

        html.Div([
            html.H2('MAENDELEO SHIRIKISHI'),
        ], style={'width': '40%', 'display': 'inline-block'}
        ),

    ]),
    html.Div([
        html.H4('JUMBE KUHUSU MATATIZO NA SEHEMU HUSIKA'),
        html.Div(id="SMS", children=update_all_sms()
        )
            
        ], style={'width': '50%', 'display': 'inline-block'}
        ),
    html.Div([
        html.Div(id="stats", children=get_all_sms())
        ], style={'width': '50%', 'display': 'inline-block'}
    ),
        
    
        
        
    

])

#-------------------------------------------------------------------------------
# we here want to get the panel for statistics with regards to issues that are no
# been communicated by the citizens


#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Callback to update table
@app.callback(Output("SMS", "children"), [Input("my_interval", "n_intervals")])
def update_table(n_intervals):
    return update_all_sms()



@app.callback(Output("stats", "children"), [Input("new_interval", "n_intervals")])
def update_stats(n_intervals):
   return get_all_sms()

#-------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)