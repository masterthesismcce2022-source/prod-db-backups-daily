import os
import datetime
import backup_config
from botocore.exceptions import ClientError

def create_db_dump():
    """
    Simulates a PostgreSQL dump.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"db_dump_{timestamp}.sql"
    print(f"[*] Creating database dump: {filename}...")
    # Simulate dump creation
    with open(filename, "w") as f:
        f.write("-- PostgreSQL database dump\n")
        f.write("SELECT * FROM users;\n")
    return filename

def upload_to_s3(filename):
    """
    Uploads the dump to S3 using the config credentials.
    """
    s3 = backup_config.get_s3_client()
    
    try:
        print(f"[*] Uploading {filename} to bucket {backup_config.BUCKET_NAME}...")
        s3.upload_file(filename, backup_config.BUCKET_NAME, filename)
        print("[+] Upload successful!")
    except ClientError as e:
        print(f"[-] Upload failed: {e}")
    finally:
        # Cleanup local file
        if os.path.exists(filename):
            os.remove(filename)

if __name__ == "__main__":
    print("--- Starting Hourly DB Backup ---")
    dump_file = create_db_dump()
    upload_to_s3(dump_file)
