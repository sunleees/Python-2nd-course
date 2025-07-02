import pika.adapters.blocking_connection
import json
from config import get_connection
from time import sleep


# def produce_message(channel: pika.adapters.blocking_connection.BlockingChannel):
#     QUEUE = 'news'
#     channel.queue_declare(queue=QUEUE)
#
#     message = 'hello kitty ))) {item}'
#     for item in range(221):
#         channel.basic_publish(
#             exchange='',
#             routing_key=QUEUE,
#             body=message.format(item=item)
#         )


def produce_logs(channel: pika.adapters.blocking_connection.BlockingChannel):
    QUEUE = 'logs'
    channel.queue_declare(queue=QUEUE)

    for i in range(100):
        message = {
            "event": "user_registered",
            "user_id": i+1
        }
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE,
            body=json.dumps(message)
        )


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            produce_logs(channel)
            produce_logs(channel)


if __name__ == "__main__":
    main()
