#!/user/bin/env python

import pika;

url = 'amqp://axqoqmag:F6YYV-urFsNOap_GsAar2g-9ZrQ9RSZO@otter.rmq.cloudamqp.com/axqoqmag'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()
