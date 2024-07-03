name: Deploy Airflow DAG

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Configure AWS credentials
      uses: aws-actions/configure-aws-credentials@v1
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: us-west-2

    - name: Sync DAGs to S3
      run: aws s3 sync ./dags s3://your-s3-bucket-name/dags

    - name: Sync requirements to S3
      run: aws s3 cp requirements.txt s3://your-s3-bucket-name/requirements.txt
