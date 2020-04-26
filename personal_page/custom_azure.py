from storages.backends.azure_storage import AzureStorage
import os

class AzureMediaStorage(AzureStorage):
    account_name = 'webpageblob' # Must be replaced by your <storage_account_name>
    account_key = os.environ["AZURE_ACCOUNT_KEY"]
    azure_container = 'uploaded-media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'webpageblob' # Must be replaced by your storage_account_name
    account_key = os.environ["AZURE_ACCOUNT_KEY"]
    azure_container = 'static'
    expiration_secs = None