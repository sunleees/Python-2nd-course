"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='redis-16394.crce175.eu-north-1-1.ec2.redns.redis-cloud.com',
    port=16394,
    decode_responses=True,
    username="default",
    password="p4qoFIis6O3m7eMzwKXD6NdBRBaATeH7",
)



#create new key
#r.set('mykey', 'secret_data')
r.set('mykeyTTL', 'secret_dataTTL', ex=3600)