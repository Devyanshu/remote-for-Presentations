import string
from random import choice
import socket 
from tkinter import *
from tkinter import messagebox

from flask import Flask, render_template, request
import pyautogui


root = Tk()
root.geometry("500x110")
root.title('Remote for Presentations')

app = Flask(__name__, static_url_path='/static')

app.debug = True
app.secret_key = "nothingfornow"


CODE = None
PORT = 5555

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/next", methods=['POST'])
def next_slide():
    pyautogui.press('right')
    return ''

@app.route("/code", methods=['POST'])
def code():
    code = dict(request.form)['code']
    if code == CODE:
        print('True')
        return {'success': True}        
    else:
        return {'fail': True}


@app.route("/prev", methods=['POST'])
def prev_slide():
    pyautogui.press('left')
    return ''

@app.route("/end", methods=['POST'])
def end_presentation():
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
        return "Visit http://{}:{} on any device in the same network".format(host_ip, PORT)
    except: 
        return ''


if __name__ == "__main__":
    CODE = generate_code()
    ip = get_Host_name_IP()
    details = ''

    if ip:
        details = ip + '''\n and enter '{}' when asked'''.format(CODE)
    else: 
        details = 'Please check your network and run again'


    label = Label(root, text = details).place(x = 10,y = 20)  
    button = Button(root, text = "Start session", command=root.quit).place(x = 180,y = 70)
    root.mainloop()
    root.quit()
    app.run(host='0.0.0.0', port=PORT)