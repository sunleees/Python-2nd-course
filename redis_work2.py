import redis

r = redis.Redis(
    host='redis-16394.crce175.eu-north-1-1.ec2.redns.redis-cloud.com',
    port=16394,
    decode_responses=True,
    username="default",
    password="p4qoFIis6O3m7eMzwKXD6NdBRBaATeH7",
)


pubsub = r.pubsub()
pubsub.subscribe("School")

for message in pubsub.listen():
    if message['type'] == 'message':
        message_text = message['data']
        if "контрольна робота" in message_text:
            print(message)