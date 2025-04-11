import boto3

ACCESS_KEY = 'e5e87ede6c862531b59a283bfebca80d'
SECRET_KEY = 'f315a2eabe802cb3cdde50d3287e07ce17266ca96a440020ba004d7e4f6d0ae1'
BUCKET_NAME = 'group25022025'
ENDPOINT = 'https://f617d2ef7efe773c811bfd2127ade693.r2.cloudflarestorage.com/group25022025'
PUBLIC_URL = 'https://pub-868f509dfcb24895838ff73db7650ffe.r2.dev'

s3client = boto3.client(
    's3',
    endpoint_url=ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name='EEUR'
)


# UPLOAD FILE
s3client.upload_file('spring.jpeg', BUCKET_NAME, 'Platon.jpeg')


