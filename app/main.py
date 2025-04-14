from kafka import KafkaProducer, KafkaConsumer
import time
def produce_message():
    producer=KafkaProducer(bootstrap_server='localhost:9092')
    message=b'Hello, KAFKA!'
    producer.send('test-topic',message)
    producer.flush()
    print('Сообщение отправлено: ' + message)

def consume_message():
    consumer=KafkaConsumer(
        'test-topic', 
        bootstrap_server='localhost:9092', 
        auto_offset_reset='earliest', 
        consumer_timeout_ms=5000)
    
    for message in consumer:
        print('Сообщение получено: ' + str(message.value))
        time.sleep(1)

if __name__=='main':
    produce_message()
    time.sleep(2)
    consume_message()
              
