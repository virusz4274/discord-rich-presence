import sys
from types import DynamicClassAttribute
#from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,  QApplication, QMainWindow
from PyQt5.uic import loadUi
from pypresence import Presence
import time
import json

data = {}
index = 0


def opendata():
    global data
    try:
        with open('profiles.json') as json_file:
            data = json.load(json_file)
    except:
        data['Profiles'] = []
        savedata()
    

def savedata():
    global data
    with open('profiles.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)

def newdata(presence_data):
    global data
    data['Profiles'].append({
        'profile name':presence_data[0],
        'client id':presence_data[1],
        'state':presence_data[2],
        'details':presence_data[3],
        'large image':presence_data[4],
        'large image text':presence_data[5],
        'small image':presence_data[6],
        'small image text':presence_data[7],
        'button 1 state':presence_data[8],
        'button 1 label':presence_data[9],
        'button 1 url':presence_data[10],
        'button 2 state':presence_data[11],
        'button 2 label':presence_data[12],
        'button 2 url':presence_data[13],
        'timer state':presence_data[14]
    })


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi("main_ui.ui",self)
        self.initUI()

    def initUI(self):
        self.load_saved_list()
        self.load_saved.clicked.connect(self.load_saved_fn)
        self.new_profile.clicked.connect(self.new_profile_fn)
        self.startstop.clicked.connect(self.startstop_fn)
        self.save.clicked.connect(self.save_file)
        self.delete_saved.clicked.connect(self.delete)
        
    def load_saved_list(self):
        global data
        self.saved_list.clear()
        for profiles in data['Profiles']:
            self.saved_list.addItem(profiles['profile name'])

    def load_saved_fn(self):
        global index
        print("load button pressed")
        index = self.saved_list.currentIndex()
        self.load_inputs()

    def new_profile_fn(self):
        self.profile_val.clear(),
        self.client_id_val.clear(),
        self.state_val.clear(),
        self.details_val.clear(),
        self.large_image_key_val.clear(),
        self.large_image_text_val.clear(),
        self.small_image_key_val.clear(),
        self.small_image_text_val.clear(),
        self.button_1.setChecked(False),
        self.button_1_label_val.clear(),
        self.button_1_url_val.clear(),
        self.button_2.setChecked(False),
        self.button_2_label_val.clear(),
        self.button_2_url_val.clear(),
        self.timer.setChecked(False)
        presence_data = self.take_inputs()
        presence_data[0] = 'New Profile'
        newdata(presence_data)
        savedata()
        self.load_saved_list()

    def startstop_fn(self):
        presence_data = self.take_inputs()
        start_presence(presence_data)

    def save_file(self):
        presence_data = self.take_inputs()
        data['Profiles'].pop(index)
        data['Profiles'].append({
        'profile name':presence_data[0],
        'client id':presence_data[1],
        'state':presence_data[2],
        'details':presence_data[3],
        'large image':presence_data[4],
        'large image text':presence_data[5],
        'small image':presence_data[6],
        'small image text':presence_data[7],
        'button 1 state':presence_data[8],
        'button 1 label':presence_data[9],
        'button 1 url':presence_data[10],
        'button 2 state':presence_data[11],
        'button 2 label':presence_data[12],
        'button 2 url':presence_data[13],
        'timer state':presence_data[14]
        })
        savedata()
        self.load_saved_list()

    def delete(self):
        global data,index
        index = self.saved_list.currentIndex()
        data['Profiles'].pop(index)
        savedata()
        self.load_saved_list()

        
    def take_inputs(self):
        presence_data =[self.profile_val.text(),
        self.client_id_val.text(),
        self.state_val.text(),
        self.details_val.text(),
        self.large_image_key_val.text(),
        self.large_image_text_val.text(),
        self.small_image_key_val.text(),
        self.small_image_text_val.text(),
        self.button_1.checkState(),
        self.button_1_label_val.text(),
        self.button_1_url_val.text(),
        self.button_2.checkState(),
        self.button_2_label_val.text(),
        self.button_2_url_val.text(),
        self.timer.checkState()
        ]
        return presence_data

    def load_inputs(self):
        global data,index
        load_data = data["Profiles"][index]
        self.profile_val.setText(load_data["profile name"])
        self.client_id_val.setText(load_data["client id"])
        self.state_val.setText(load_data["state"])
        self.details_val.setText(load_data["details"])
        self.large_image_key_val.setText(load_data["large image"])
        self.large_image_text_val.setText(load_data["large image text"])
        self.small_image_key_val.setText(load_data["small image"])
        self.small_image_text_val.setText(load_data["small image text"])
        self.button_1.setChecked(load_data["button 1 state"]==2)
        self.button_1_label_val.setText(load_data["button 1 label"])
        self.button_1_url_val.setText(load_data["button 1 url"])
        self.button_2.setChecked(load_data["button 2 state"]==2)
        self.button_2_label_val.setText(load_data["button 2 label"])
        self.button_2_url_val.setText(load_data["button 2 url"])
        self.timer.setChecked(load_data["timer state"]==2)



def MyApp():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

def start_presence(presence_data):
    print("rich presence started")
    RPC = Presence(presence_data[1])  # Initialize the client class    
    RPC.connect() # Start the handshake loop
    # Set the presence
    start_time = int(time.time())
    if presence_data[14] == 2:
        if  presence_data[8] == 2 and presence_data[11] == 2:
            RPC.update(state=presence_data[2], details=presence_data[3], large_image=presence_data[4], large_text=presence_data[5], small_image=presence_data[6], small_text=presence_data[7], start=start_time, buttons=[{"label": presence_data[9], "url":presence_data[10]}, {"label": presence_data[12], "url":presence_data[13]}])
        elif presence_data[8] == 2:
            RPC.update(state=presence_data[2], details=presence_data[3], large_image=presence_data[4], large_text=presence_data[5], small_image=presence_data[6], small_text=presence_data[7], start=start_time, buttons=[{"label": presence_data[9], "url":presence_data[10]}])
        else:
            RPC.update(state=presence_data[2], details=presence_data[3], large_image=presence_data[4], large_text=presence_data[5], small_image=presence_data[6], small_text=presence_data[7], start=start_time)
    else:
        if  presence_data[8] == 2 and presence_data[11] == 2:
            RPC.update(state=presence_data[2], details=presence_data[3], large_image=presence_data[4], large_text=presence_data[5], small_image=presence_data[6], small_text=presence_data[7],buttons=[{"label": presence_data[9], "url":presence_data[10]}, {"label": presence_data[12], "url":presence_data[13]}])
        elif presence_data[8] == 2:
            RPC.update(state=presence_data[2], details=presence_data[3], large_image=presence_data[4], large_text=presence_data[5], small_image=presence_data[6], small_text=presence_data[7], buttons=[{"label": presence_data[9], "url":presence_data[10]}])
        else:
            RPC.update(state=presence_data[2], details=presence_data[3], large_image=presence_data[4], large_text=presence_data[5], small_image=presence_data[6], small_text=presence_data[7])
    while True:
        time.sleep(15) # Can only update rich presence every 15 seconds

opendata()
MyApp()
