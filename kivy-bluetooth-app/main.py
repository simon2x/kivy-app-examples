# This is a sample Python script.
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import OneLineListItem
from jnius import autoclass

BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
BluetoothDevice = autoclass('android.bluetooth.BluetoothDevice')
BluetoothSocket = autoclass('android.bluetooth.BluetoothSocket')
BluetoothReceiver = autoclass('android.bluetooth.BluetoothReceiver')
UUID = autoclass('java.util.UUID')

KV = '''
Screen:

    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "MDLabel"

        BoxLayout:
            orientation: "horizontal"    
            MDRectangleFlatButton:
                text: "Refresh Devices"
                on_press: app.get_devices('dd')

            MDRectangleFlatButton:
                text: "hello"

        ScrollView:

            MDList:
                id: device_list
'''



def discover_devices():


    mReceiver = BroadcastReceiver()

    # start looking for bluetooth devices
    btAdapter = BluetoothAdapter.getDefaultAdapter()
    if btAdapter.isDiscovering():
        btAdapter.cancelDiscovery()
    btAdapter.startDiscovery()

def get_paired_devices():
    return BluetoothAdapter.getDefaultAdapter().getBondedDevices().toArray()


def get_socket_stream(name):
    pass
    #Logger.info(f"PAIRED: {paired_devices}")
    socket = None
    # for device in paired_devices:  #
    #     Logger.info(device.getName())
        # if device.getName() == name:
        #     print(device.getName())
        #
        #     # socket = device.createInsecureRfcommSocketToServiceRecord(
        #     # UUID.fromString("00001101-0000-1000-8000-00805F9B34FB"))
        #     socket = device.createRfcommSocketToServiceRecord(
        #         UUID.fromString("00001101-0000-1000-8000-00805F9B34FB"))
        #     recv_stream = socket.getInputStream()
        #     send_stream = socket.getOutputStream()
            #break

    #socket.connect()
    # return recv_stream, send_stream


class MainApp(MDApp):

    def build(self):
        screen = Builder.load_string(KV)
        return screen

    def get_devices(self, name):
        print(f'Hi, {name}')
        Logger.info("Get Devices")
        discover_devices()
        for device in get_paired_devices():
            Logger.info(f'{device.getName()}')
            self.ids.device_list.add_widget(MDLabel(text=f"{device.getName()}", halign="center"))


if __name__ == '__main__':
    MainApp().run()