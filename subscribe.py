import paho.mqtt.client as mqtt


from speck import SpeckCipher

from struct import *

my_speck = SpeckCipher(0x123456789ABCDEF00FEDCBA987654321)


def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
    client.subscribe("test/mqtt")  # Subscribe to the topic “digitest/test1”, receive any messages published on it


def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
    print("Message received-> " + msg.topic + str(msg.payload.decode('utf-8')))  # Print a received msg

    newmsg= str(msg.payload.decode('utf-8'))  # Print a received msg)
    intmsg = int(newmsg)
    dec_msg= my_speck.decrypt(intmsg)
    dec_msg_hex= hex(dec_msg)

    
    print(str(dec_msg_hex))




client = mqtt.Client("digi_mqtt_test")  # Create instance of client with client ID “digi_mqtt_test”
client.on_connect = on_connect  # Define callback function for successful connection
client.on_message = on_message  # Define callback function for receipt of a message
# client.connect("m2m.eclipse.org", 1883, 60)  # Connect to (broker, port, keepalive-time)
client.connect('127.0.0.1', 1883)
client.loop_forever()  # Start networking daemon