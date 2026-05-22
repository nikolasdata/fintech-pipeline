import boto3

s3 = boto3.client("s3")

bucket = "nikolasdata-fintech-pipeline"

files = ["eur_usd_raw.csv", "eur_usd_transformed.csv"]

for file in files:
    s3.upload_file(file, bucket, file)
    print(f"Uploaded {file} to s3://{bucket}/{file}")