import paho.mqtt.client as mqttClient
import time


def on_connect(client, userdata, flags, rc):

    if rc == 0:
        print('Connected to broker')

        global Connected
        Connected = True

    else:
        print('Connection failed')


def on_message(client, userdata, message):
    print(message.payload)
    print(message.payload.decode("utf-8"))
    print('hi')
    


Connected = False

broker_address = '139.59.97.171'
port = 1883


client = mqttClient.Client('measures')
client.on_connect = on_connect  
client.on_message = on_message  

client.connect(broker_address, port=port) 
client.loop_start()
client.subscribe('measures/#')

while Connected != True:
    time.sleep(0.1)

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print('exiting')
    client.disconnect()
    client.loop_stop()
