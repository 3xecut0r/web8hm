import pika

from models import Contacts
import connect


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='email_queue', durable=True)


def send_email_message(contact):
    contact.email_sent = True
    contact.save()
    return f"Sent email message for contact: {contact.id}"


def callback(ch, method, properties, body):
    contact_id = body.decode()
    obj_contact = Contacts.objects.get(id=contact_id)
    print(send_email_message(obj_contact))
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='email_queue', on_message_callback=callback)


if __name__ == '__main__':
    channel.start_consuming()

