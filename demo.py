import json
import boto3
from pymilvus import connections, Collection
import os

# 连接到 Milvus
def connect_to_milvus():
    host = os.environ['MILVUS_HOST']
    port = os.environ['MILVUS_PORT']
    connections.connect(host=host, port=port)

# 从 S3 下载文件
def download_from_s3(bucket, key):
    s3 = boto3.client('s3')
    local_file_path = f"/tmp/{key.split('/')[-1]}"
    s3.download_file(bucket, key, local_file_path)
    return local_file_path

# 将文件加载到 Milvus
def load_to_milvus(file_path, collection_name):
    # 这里需要根据您的具体需求实现文件处理和向量化逻辑
    # 以下是一个简单的示例
    collection = Collection(collection_name)
    # 假设文件内容是 JSON 格式的向量数据
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    vectors = data['vectors']
    collection.insert(vectors)

def lambda_handler(event, context):
    connect_to_milvus()

    # 从事件中获取 S3 桶和对象信息
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # 下载文件
    local_file_path = download_from_s3(bucket, key)

    # 加载到 Milvus
    collection_name = os.environ['MILVUS_COLLECTION']
    load_to_milvus(local_file_path, collection_name)

    return {
        'statusCode': 200,
        'body': json.dumps('File successfully loaded into Milvus')
    }
