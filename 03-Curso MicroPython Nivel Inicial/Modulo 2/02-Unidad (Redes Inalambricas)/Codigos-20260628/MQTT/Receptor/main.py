def sub_cb(topic, msg):
    print((topic, msg))


def connect_and_subscribe():
    global client_id, mqtt_server, topic_sub
    client = MQTTClient(client_id, mqtt_server)
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic_sub)
    print("Conectado a %s MQTT broker, suscripto a %s topic" % (mqtt_server, topic_sub))
    return client


def restart_and_reconnect():
    print("Error al conectar con el broker, reconectando....")
    time.sleep(10)
    machine.reset()


try:
    client = connect_and_subscribe()
except OSError as e:
    restart_and_reconnect()

while True:
    try:
        new_message = client.check_msg()
        if new_message != "None":
            client.publish(topic_pub, b"recibido")
        time.sleep(1)
    except OSError as e:
        restart_and_reconnect()
