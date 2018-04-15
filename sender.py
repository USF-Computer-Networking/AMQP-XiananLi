
/user/bin/env python

import pika;

url = 'amqp://axqoqmag:F6YYV-urFsNOap_GsAar2g-9ZrQ9RSZO@otter.rmq.cloudamqp.com/axqoqmag'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.basic_publish(exchange='', routing_key='hello', body='Hello Viewers!')

