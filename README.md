# PostgreSQL S3 Backup Utility

Simple script to automate daily database dumps and upload them to our S3 archive bucket.

## Usage

1. Install dependencies:
   ```bash
   pip install boto3
   ```

2. Run the backup:
   ```bash
   python main_backup.py
   ```

## TODO
- [ ] Add compression (gzip)
- [ ] Fix hardcoded credentials in `backup_config.py` (Need to figure out how to use `.env` files)
- [ ] Add retention policy

## License
MIT
