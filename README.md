# AMQP-XiananLi


RabbitMQ is a message broker: it accepts and forwards messages. 

The small demonstration I wrote is basically providing a function that
senders sending simple text messages to receiver by using RabbitMQ.

The first program send.py is used for users to typy in simple text messages
to the queue.
 
Then the recevie.py will receive messages from the queue to display it on the screen.

The newtask and work programs are used to accept different works to allocate 
into different time frames to accomplish the work.

The log and receivelog programs are used for implementing logging system in order to 
emit log messages and receive and print messages.

references links:
// https://www.rabbitmq.com/tutorials/tutorial-one-python.html
// https://www.rabbitmq.com/tutorials/tutorial-two-python.html
// https://www.rabbitmq.com/tutorials/tutorial-three-python.html
// https://www.youtube.com/watch?v=BKDoxM9KOJY
