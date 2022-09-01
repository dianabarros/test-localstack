import boto3

endpoint_url="http://localstack:4567"
sns = boto3.client('sns',
                      endpoint_url=endpoint_url,
                      aws_access_key_id="dummy",
                      aws_secret_access_key="dummy",
                      aws_session_token="dummy",
                      region_name="eu-central-1"
                    )
sns.list_topics()
topic_name="order-creation-events"
sns.create_topic(Name=topic_name)

sqs = boto3.client('sqs',
                      endpoint_url=endpoint_url,
                      aws_access_key_id="dummy",
                      aws_secret_access_key="dummy",
                      aws_session_token="dummy",
                      region_name="eu-central-1"
                    )
sqs.list_queues()
queue_name="dummy-queue"
sqs.create_queue(QueueName=queue_name)

arn_prefix="arn:aws:sns:eu-central-1:000000000000:"

sns.subscribe(
    TopicArn=arn_prefix+topic_name,
    Protocol="sqs",
    Endpoint=endpoint_url+"/000000000000/"+queue_name,
)
sns.publish(
    TopicArn=arn_prefix+topic_name,
    Message="hello world"
)
sqs.receive_message(QueueUrl=endpoint_url+"/000000000000/"+queue_name)