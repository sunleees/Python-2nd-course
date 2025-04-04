import psycopg2
import random

PGHOST='ep-odd-block-a27ph1lv-pooler.eu-central-1.aws.neon.tech'
PGDATABASE='neondb'
PGUSER='neondb_owner'
PGPASSWORD='npg_Kzj1I6PHvdhX'
PORT = 5432


# with psycopg2.connect(dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PORT) as connection:
#     with connection.cursor() as cursor:
#         query = """
#             CREATE TABLE IF NOT EXISTS topic (
#                 id SERIAL PRIMARY KEY,
#                 name VARCHAR(50) NOT NULL,
#                 created_at DATE NOT NULL
#             )
#         """
#         cursor.execute(query)
#
#         query = """
#             CREATE TABLE IF NOT EXISTS "user" (
#                 id SERIAL PRIMARY KEY,
#                 username VARCHAR(50) NOT NULL,
#                 email VARCHAR(50) UNIQUE NOT NULL,
#                 registered_at DATE NOT NULL
#             );
#
#             CREATE TABLE IF NOT EXISTS posts (
#                 id SERIAL PRIMARY KEY,
#                 user_id INTEGER REFERENCES "user"(id),
#                 topic_id INTEGER REFERENCES topic(id),
#                 content TEXT NOT NULL,
#                 created_at DATE NOT NULL
#             );
#         """
#         cursor.execute(query)

