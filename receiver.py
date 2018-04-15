/user/bin/env python

import pika;

url = 'amqp://axqoqmag:F6YYV-urFsNOap_GsAar2g-9ZrQ9RSZO@otter.rmq.cloudamqp.com/axqoqmag'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
  print " [x] Received %r" %(body)
  
channel.basic_consume(callback, queue='hello', no_ack=True)

channel.start_consuming()
