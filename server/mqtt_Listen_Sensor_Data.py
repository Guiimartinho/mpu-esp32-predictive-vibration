import paho.mqtt.client as mqtt
from store_Sensor_Data_to_DB import sensor_Data_Handler

# MQTT Settings 
MQTT_Broker = "ec2-3-90-96-154.compute-1.amazonaws.com" #"192.168.0.25"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "equipment/#"

#Subscribe to all Sensors at Base Topic
def on_connect(mqtt_client, obj, flags, rc):
	mqttc.subscribe(MQTT_Topic, 0)

#Save Data into DB Table
def on_message(mqtt_client, obj, msg):
	sensor_Data_Handler(msg.topic, msg.payload)


def on_subscribe(mqtt_client, obj, mid, granted_qos):
	pass

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

# Continue the network loop
mqttc.loop_forever()
