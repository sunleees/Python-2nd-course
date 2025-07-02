import json
import time

from config import get_connection
import pika


def process_new_message(channel: pika.adapters.blocking_connection.BlockingChannel, method, properties, body):
    data = json.loads(body)  # Парсим JSON из байт
    print(f"Новий лог: {data['event']}, user_id: {data['user_id']}")
    time.sleep(1)  # Інтервал щосекунди
    channel.basic_ack(delivery_tag=method.delivery_tag)



# def consume_message(channel: pika.adapters.blocking_connection.BlockingChannel):
#     QUEUE = 'news'
#     channel.basic_consume(
#         queue=QUEUE,
#         on_message_callback=process_new_message,
#         # auto_ack=True
#     )
#
#     channel.start_consuming()


def consume_logs(channel: pika.adapters.blocking_connection.BlockingChannel):
    QUEUE = 'logs'
    channel.basic_consume(
        queue=QUEUE,
        on_message_callback=process_new_message,
        # auto_ack=True
    )
    channel.start_consuming()


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            consume_logs(channel)


if __name__ == "__main__":
    main()