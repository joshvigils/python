import os
from google.cloud import secretmanager

client = secretmanager.SecretManagerServiceClient()
secret_name = "MyPoCsecret"
project_id = "wmt-sm-dev"
request = {"name": f"projects/{project_id}/secrets/{secret_name}/versions/latest"}
response = client.access_secret_version(request)
secret_string = response.payload.data.decode("UTF-8")


def secret_hello(request):
    return secret_string
