import websocket
from dash import Dash, html, Input, Output
import dash_daq as daq
import os
import webbrowser

# set up the websocket connection
ws = websocket.WebSocket()
address = "ws://192.168.4.1/"
ws.connect(address)

# Build the web app
app = Dash(__name__)

app.layout = html.Div([
    daq.Knob(id='servo-knob', max = 180, value = 90, scale = {'interval':15}),
    html.Div(id='knob-result')
])



@app.callback(Output('knob-result', 'children'), Input('servo-knob', 'value'))
def update_output(value):
    ws.send(f'SERVO:{value},23') # send the command over websocket 
    return f'Servo angle: {value}'+u"\N{DEGREE SIGN}"


# Run app
PORT = 1100
def main():
    
    # The reloader has not yet run - open the browser
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new("http://localhost:{}".format(PORT))

    # Otherwise, continue as normal
    app.run(host="127.0.0.1", port=PORT)

if __name__=='__main__':
    main()