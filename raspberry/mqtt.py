import paho.mqtt.client as mqtt
import requests
import os
import pickle

OWNER = "00000000000"

def on_connect(client, userdata, flags, rc):
    """Callback that will be executed when the connection with the MQTT broker is established"""
    if rc == 0:
        print("Successful Connection")
        client.subscribe(f"ssmai/encodings/{OWNER}")
    else:
        print(f"Connection fail. Return code: {rc}")


def on_message(client, userdata, msg):
    """Callback that will be executed when the message is published successfully"""
    message = str(msg.payload.decode())
    print(message)
    messages = message.split(': ')
    filename = messages[1]
    if messages[0] == "ADDED":
        get_encoding(filename)
    elif messages[0] == "DELETED":
        delete_encoding(filename)


def get_encoding(filename):
    """Download the encoding file from the server"""
    url = f"http://127.0.0.1:8000/encoding/{filename}"
    path = f"./encoding/{filename}.pkl"

    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        # pickle.dump(response.content, open(path, 'wb'))
        with open(path, "wb") as file:
            file.write(response.content)
        print("File successfully downloaded and saved.")
    else:
        print("Failed to download the file.")


def delete_encoding(filename):
    """Delete the encoding file from the server"""
    path = f"./encoding/{filename}.pkl"
    try:
        os.remove(path)
        print("File removed successfully.")
    except FileNotFoundError:
        print("File not found.")

def main():
    # MQTT client configuration
    client = mqtt.Client()

    # Definition of callback functions
    client.on_connect = on_connect
    client.on_message = on_message

    # Connection to the MQTT broker
    broker = "127.0.0.1" 
    porta = 1883 
    client.connect(broker, porta, 60)

    # Loop to maintain connection and process incoming messages
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("Interruption of the connection with the MQTT broker")
        client.disconnect()

if __name__ == "__main__":
    main()