
import paho.mqtt.client as mqtt

from speck import SpeckCipher
my_speck = SpeckCipher(0x123456789ABCDEF00FEDCBA987654321)

#msg = "Hello World"

#enc_msg= my_speck.encrypt(msg)

msg = "Hello World".encode('utf-8')

hex_msg = msg.hex()

msg_hex= hex(hex_msg)

enc_msg = my_speck.encrypt(msg_hex)

mqttc = mqtt.Client("digitest")  # Create instance of client with client ID “digitest”
mqttc.connect("127.0.0.1", 1883)  # Connect to (broker, port, keepalive-time)
mqttc.loop_start()  # Start networking daemon
mqttc.publish("test/mqtt", enc_msg )  # Publish message to “digitest /test1” topic
mqttc.loop_stop()  # Kill networking daemon
 