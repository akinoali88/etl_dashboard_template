'''
Generated Dash application factory module.
Includes functions to create Plotly figures and initialize the Dash app.
'''

from dash import Dash, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import pandas as pd



def create_dash_app(df: pd.DataFrame,) -> Dash:
    '''
    Create and configure a Dash application for xyz.

    Parameters:    
        df : pd.DataFrame
            insert details


    Returns:
        Dash
            Configured Dash application instance with interactive layout, callbacks, and graphs.

    Notes:
        - a
        - b
    '''

    # load bootstrap figure templates    

    dbc_theme = 'set theme'

    load_figure_template('dbc_theme')
    dbc_css = 'https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css'

    app = Dash(__name__, external_stylesheets=[dbc.themes.dbc_theme, dbc_css, dbc.icons.BOOTSTRAP])

    # Define the app layout
    app.layout = dbc.Container([

            # Store the data as JSON in the browser/app state
            dcc.Store(id='main-data', data=df.to_json(orient='records')),
            
            dbc.Tabs([

                # --- Home page tab ---
                dbc.Tab([
                    render_home_tab()],
                    label='<insert tab 1 name>',
                    label_class_name='bg-primary-subtle text-grey',
                    ),

                # --- Tab 2 ---
                dbc.Tab([
                    render_page2(
                        df, slider_parameters, default_child)],
                    label='<insert tab 2 name>',
                    label_class_name='bg-primary-subtle text-grey',
                    ),

                # --- etc ---
                dbc.Tab([]),
                    ]) # Close dcc.Tabs
        ],
        fluid=True,
        className='bg-success',
        style={'minHeight': '100vh'}) # Close dbc.Container

    return app
