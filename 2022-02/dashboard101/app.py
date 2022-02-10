# Import required packages
import pandas as pd
import plotly.express as px

# Web app imports
import dash
from dash.dependencies import Input, Output, State
from dash import dcc
from dash import html

# %% Data processing and results to show

# Create sample data set
df = pd.DataFrame({
    "University": ["UoA", "UoA", "UoA", "RGU", "RGU", "RGU"],
    "Students": [2000, 2500, 3000, 4500, 3000, 5000],
    "Year": ["3022", "3023", "3024", "3022", "3023", "3024"]
})


# %% Initiate web application
# Server variable is essential to deploy in Heroku. Not always mentioned in the documentation
app = dash.Dash(__name__)
server = app.server
app.title = 'My cool app v2'  # This is the heading in the browser tab

# Create layout
app.layout = html.Div([
    # Heading of the app
    html.Div([
        html.H1(children='My super cool web app v2'),  # Children here is the text of H1 html tag
        html.H3(children='by Carlos (copied from Arturo)')
    ], className='app-heading'), # Class name is used as the identifier for CSS or other styling

    # Instructions paragraph
    html.Div([
        html.P('This web app is an example to showcase how to deploy using heroku and dash')
    ], className='Instructions'),

    # Radio to change the parameters
    html.Div([
        html.Label('Radio Items'),
        dcc.RadioItems(id="university-input", options=[{'label':'University of Aberdeen', 'value':'UoA'},
                                                       {'label':'Robert Gordon University', 'value':'RGU'}],
                       value='UoA', labelStyle={"display":"block"}
                       )
    ]),
    # Container for the plot
    html.Div([
        dcc.Graph(
            id="plot-universities"
        )
    ], className='plot-section')
])

# App callbacks


@app.callback(
    Output(component_id='plot-universities', component_property='figure'),
    [Input(component_id='university-input', component_property='value')])
# Create function to plot
def plot_num_students(university):
    data = df[df['University'] == university]
    fig = px.bar(data, x='Year', y='Students')
    # Automate title of plot to change with university selected
    title_text = 'Number of students in ' + university + ' for future years 3022-3024'
    fig.update_layout(title=title_text)
    return fig


# Render the server to run the app
if __name__ == '__main__':
    app.run_server(debug=True)
