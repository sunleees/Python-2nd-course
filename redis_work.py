import time
import redis

r = redis.Redis(
    host='redis-16394.crce175.eu-north-1-1.ec2.redns.redis-cloud.com',
    port=16394,
    decode_responses=True,
    username="default",
    password="p4qoFIis6O3m7eMzwKXD6NdBRBaATeH7",
)




r.set('myFavoriteCar', 'Porsche 911 GT3 RS')
r.set('MyFavoritePet', 'Cat', ex=7200)
r.lpush('Products', "Яйця", "Вівсянка", "Банани", "Молоко", "Куряче філе", "Огірки", "Рис", "Натуральний йогурт", "Горіхи (мікс)", "Твердий сир")
r.expire('Products', 604800)
r.hset('CakeRecipe', mapping={"flour": 250, "sugar": 300, "eggs": 3, "milk": 500, "butter": 100, "baking_powder": 10, "vanilla": 1, "salt": 1})
r.hset('CakeRecipe', mapping={"sugar": 500})
r.delete('CakeRecipe')

pubsub = r.pubsub()
pubsub.subscribe("School")

messages = [
    "Завтра контрольна робота з математики",
    "Ми будемо мати тест по біології на наступному тижні",
    "Не забудьте про контрольну роботу з історії!",
    "Уроки з англійської будуть цікавими на наступному тижні",
    "Тестування з фізики буде на цьому тижні",
    "Завтра контрольна робота з хімії, приходьте підготовленими",
    "Немає контрольних робіт в цьому місяці",
    "Завтра контрольна робота з географії",
    "Подивіться на розклад — в п’ятницю буде контрольна робота з літератури",
    "Іспити починаються через тиждень"
]

for message in messages:
        r.publish("School", message)
        time.sleep(2)