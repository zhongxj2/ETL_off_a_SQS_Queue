# ETL Mask PII Project
## Set up
### Requirements
- Python 3.9
- Docker
- Docker Compose
- AWS CLI
- PSQL 
### Set up the enviroment
1. ```
   git clone https://github.com/zhongxj2/ETL_off_a_SQS_Queue.git
   ```
2. ```
   cd ETL_off_a_SQS_Queue
   ```
3. ```
   docker-compose up -d
   ```

## Commands to Test
### PSQL
- Connect to PSQL
```
psql -d postgres -U postgres -p 5432 -h localhost -W
```
- Create Table
```
CREATE TABLE IF NOT EXISTS user_logins(
user_id varchar(128),
device_type varchar(32),
masked_ip varchar(256),
masked_device_id varchar(256),
locale varchar(32),
app_version integer,
create_date date
);
```
- Query Data from Table
```
select * from user_logins;
```
### AWS SQS
- List Existing SQS Queues:
To check if you've already created a queue in LocalStack:
```
aws --endpoint-url=http://localhost:4566 sqs list-queues
```
- Create a New SQS Queue (if needed):
If you find out that you haven't created the queue you need, you can create a new one:
```
aws --endpoint-url=http://localhost:4566 sqs create-queue --queue-name my-test-queue
```
- Send the JSON to the queue:
```
aws --endpoint-url=http://localhost:4566 sqs send-message --queue-url http://localhost:4566/000000000000/my-test-queue --message-body file://data.json
```
- Receive a message from the queue:
```
aws --endpoint-url=http://localhost:4566 sqs receive-message --queue-url http://localhost:4566/000000000000/my-test-queue
``` 
- Delete the message using its receipt handle:
After getting the ReceiptHandle from the previous command (let's say it's YourReceiptHandleHere), you can delete the message:
```
aws --endpoint-url=http://localhost:4566 sqs delete-message --queue-url http://localhost:4566/000000000000/my-test-queue --receipt-handle $YourReceiptHandleHere
```
Replace $YourReceiptHandleHere with the actual receipt handle from the received message.

## Questions
### How would you deploy this application in production?
I would consider deploying the application on a container orchestration platform like Kubernetes or AWS ECS for easy scaling and management. Continuous integration and continuous deployment (CI/CD) would be implemented to ensure smooth deployment cycles.
### What other components would you want to add to make this production ready?
-Logging: Integrate a robust logging mechanism like ELK stack (Elasticsearch, Logstash, Kibana) or Graylog.
-Monitoring: Use tools like Prometheus and Grafana.
-Backup: Regular database backups.
-Error Handling & Retries: For failed database writes or SQS reads.
-Security: Implement proper security mechanisms, encrypt sensitive data, and ensure network security.
### How can this application scale with a growing dataset.
By using container orchestration platforms like Kubernetes, we can easily scale up the application containers. For the database, consider using cloud-based managed databases like Amazon RDS for Postgres, which can be scaled vertically and horizontally.
### How can PII be recovered later on?
The current method hashes the PII data, making it irreversible. If recovery is needed, consider using reversible encryption methods and securely store the encryption keys.
### What are the assumptions you made?
-The SQS messages are not too large; if they were, we'd need batch processing or streaming.
-The data structure is consistent across messages; else, more robust error handling would be needed.
