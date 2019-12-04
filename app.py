from flask import Flask, render_template, request
import pyautogui
import string
from random import choice
import sys
import socket 


app = Flask(__name__, static_url_path='/static')

app.debug = True
app.secret_key = "nothingfornow"


CODE = None
PORT = 5151

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/next", methods=['POST'])
def next_slide():
    print('next')
    pyautogui.press('right')
    return ''

@app.route("/code", methods=['POST'])
def code():
    code = dict(request.form)['code']
    print(code)
    if code == CODE:
        print('True')
        return {'success': True}        
    else:
        return {'fail': True}


@app.route("/prev", methods=['POST'])
def prev_slide():
    print('prev')
    pyautogui.press('left')
    return ''

@app.route("/end", methods=['POST'])
def end_presentation():
    print('end')
    pyautogui.press('esc')
    return ''

def generate_code():
    sample = string.ascii_lowercase + string.ascii_uppercase
    code = ''
    for i in range(4):
        code += choice(sample)
    return code


  
def get_Host_name_IP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Visit http://{}:{} on any device in the same ntwork".format(host_ip, PORT))
    except: 
        print("Unable to get IP") 


if __name__ == "__main__":
    CODE = generate_code()
    get_Host_name_IP()
    print('Enter this code when asked {}'.format(CODE))
    app.run(host='0.0.0.0', port=PORT)