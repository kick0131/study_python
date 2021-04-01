# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# from awscrt import io, mqtt, auth, http
from awscrt import io, mqtt
from awsiot import mqtt_connection_builder
import time as t
import json
import logging

ENDPOINT = "<IoTCore endpoint>"
CLIENT_ID = "testDevice"
PATH_TO_CERT = "certificates/50fccc0b22-certificate.pem.crt"
PATH_TO_KEY = "certificates/50fccc0b22-private.pem.key"
PATH_TO_ROOT = "certificates/root.pem"
MESSAGE = "Hello World"
TOPIC = "test/testing"
RANGE = 5

# ログの設定
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def publish(event: object, context: object):
    """IoTCoreにPublishメッセージを送信します

    Args:
        event (object): [description]
        context (object): [description]
    """
    logger.info('=== PUBLISH ===')

    # Spin up resources
    event_loop_group = io.EventLoopGroup(1)
    host_resolver = io.DefaultHostResolver(event_loop_group)
    client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
    mqtt_connection = mqtt_connection_builder.mtls_from_path(
        endpoint=ENDPOINT,
        cert_filepath=PATH_TO_CERT,
        pri_key_filepath=PATH_TO_KEY,
        client_bootstrap=client_bootstrap,
        ca_filepath=PATH_TO_ROOT,
        client_id=CLIENT_ID,
        clean_session=False,
        keep_alive_secs=6
    )
    print("Connecting to {} with client ID '{}'...".format(
        ENDPOINT, CLIENT_ID))
    # Make the connect() call
    connect_future = mqtt_connection.connect()
    # Future.result() waits until a result is available
    connect_future.result()
    logger.info('=== CONNECTED ===')
    # Publish message to server desired number of times.
    for i in range(RANGE):
        data = "{} [{}]".format(MESSAGE, i+1)
        message = {"message": data}
        mqtt_connection.publish(topic=TOPIC, payload=json.dumps(
            message), qos=mqtt.QoS.AT_LEAST_ONCE)
        logger.info(f'{TOPIC} : {json.dumps(message)}')
        t.sleep(0.1)
    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result()

    logger.info('=== PUBLISH END ===')
