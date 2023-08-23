from utils import sqs_utils, data_utils, db_utils

def main():
    # Get messages from SQS
    messages = sqs_utils.get_messages_from_queue('http://localhost:4566/000000000000/my-test-queue')
    for message in messages:
        # Transform the data
        processed_data = data_utils.convert_to_json(message)
        # Mask the PII data
        masked_data = data_utils.mask_pii(processed_data)
        # Write to Postgres
        db_utils.write_to_postgres(masked_data)

if __name__ == "__main__":
    main()
