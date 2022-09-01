Configuring dummy AWS creds for testing

```
aws configure set aws_access_key_id "dummy" --profile test-profile
aws configure set aws_secret_access_key "dummy" --profile test-profile
aws configure set region "eu-central-1" --profile test-profile
aws configure set output "table" --profile test-profile
```


Creating SNS topic

`aws --endpoint-url=http://localhost:4567 sns create-topic --name order-creation-events --region eu-central-1 --profile test-profile --output table | cat`


Creating SQS queue

`aws --endpoint-url=http://localhost:4567 sqs create-queue --queue-name dummy-queue --profile test-profile --region eu-central-1 --output table | cat`


Subscribing to topic

`aws --endpoint-url=http://localhost:4567 sns subscribe --topic-arn   arn:aws:sns:eu-central-1:000000000000:order-creation-events --profile test-profile  --protocol sqs --notification-endpoint http://localstack:4567/000000000000/dummy-queue --output table | cat`


Send message to topic

`aws sns publish --endpoint-url=http://localhost:4567 --topic-arn arn:aws:sns:eu-central-1:000000000000:order-creation-events --message "Hello World" --profile test-profile --region eu-central-1 --output json | cat`


Receive message on queue

`aws --endpoint-url=http://localhost:4567 sqs receive-message --queue-url http://localhost:4567/000000000000/dummy-queue --profile test-profile --region eu-central-1 --output json | cat`


Send message to queue

```
aws --endpoint-url=http://localhost:4567 sqs send-message  --queue-url http://localhost:4567/000000000000/dummy-queue --profile test-profile --region eu-central-1  --message-body '{
          "event_id": "7456c8ee-949d-4100-a0c6-6ae8e581ae15",
          "event_time": "2021-11-26T16:00:47Z",
          "data": {
            "test": 83411
        }
      }' | cat
```



[[source](https://medium.com/@anchan.ashwithabg95/using-localstack-sns-and-sqs-for-devbox-testing-fa09de5e3bbb)]