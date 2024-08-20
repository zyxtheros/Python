import websocket
import time
from dash import Dash, html, Input, Output, callback_context
import dash_daq as daq


# set up the websocket connection
ws = websocket.WebSocket()
ws.connect("ws://192.168.4.1/")

# set up the dash app
app = Dash(__name__)

app.layout = html.Div([
    html.Button('Angle 0', id='btn-angle0'),
    html.Button('Angle 90', id='btn-angle90'),
    html.Button('Angle 180', id='btn-angle180'),
    html.Div(id='container-button-timestamp')
])
# define the callback elements
@app.callback(
    Output('container-button-timestamp', 'children'),
    Input('btn-angle0', 'n_clicks'),
    Input('btn-angle90', 'n_clicks'),
    Input('btn-angle180', 'n_clicks')
)
def displayClick(btn1, btn2, btn3):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    if 'btn-angle0' in changed_id:
        ws.send("SERVO:0,23") # send the command over websocket 
        msg = 'Angle set to 0'
    elif 'btn-angle90' in changed_id:
        ws.send("SERVO:90,23") # send the command over websocket 
        msg = 'Angle set to 90'
    elif 'btn-angle180' in changed_id:
        ws.send("SERVO:180,23") # send the command over websocket 
        msg = 'Angle set to 180'
    else:
        msg = 'None of the buttons have been clicked yet, no angle set'
    return html.Div(msg)

i = 0
nrOfMessages = 30

if __name__ == '__main__':
    app.run_server(host="127.0.0.1", port=1100) # run the dash server

    while i<nrOfMessages:
        ws.send("Soft AP mode: message nr " + str(i))
        result = ws.recv()
        print(result)
        i=i+1
        time.sleep(1)
 
ws.close()
