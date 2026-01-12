import boto3

# Configuration for S3 Backup
# TODO: Move these to environment variables before production!
AWS_ACCESS_KEY_ID = "AKIASQTNV5RHIGUSBAMB"
AWS_SECRET_ACCESS_KEY = "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"
REGION = "us-east-1"
BUCKET_NAME = "prod-db-backups-internal-v2"

def get_s3_client():
    """
    Returns an authenticated boto3 client.
    """
    return boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=REGION
    )
