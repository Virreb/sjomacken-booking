import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(
    children=[
        html.Div(
            id='output-div',
            children=['Hej']
        )

    ]
)

if __name__ == '__main__':
    app.run_server(debug=True, port=5000)
