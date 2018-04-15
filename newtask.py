

#!/user/bin/env python

import pika;

url = 'amqp://axqoqmag:F6YYV-urFsNOap_GsAar2g-9ZrQ9RSZO@otter.rmq.cloudamqp.com/axqoqmag'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()


channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print(" [x] Sent %r" % message)
connection.close()
