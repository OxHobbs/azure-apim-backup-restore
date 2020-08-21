# Azure API Management Backup/Restore

## Overview

This project has two command line scripts that provide the functionality of
performing a backup/restore of an Azure API Management instance.  It works by 
using the Python SDK to perform a backup/restore option to backup/restore to/from
an Azure Storage Account.
Authentication is handled via a service principal.

Some reasons to backup an API management instance could be for the following:

* Disaster Recovery scenarios
* Migrating an Azure APIM instance to another region
* Migrating an Azure APIM to a new tenant and subscription

## Usage

### Pre-reqs

* Python 3
* `azure-mgmt-apiinstance` package
* Service Principal with permissions to the Azure APIM instance and the storage account where
the backup will be stored.

### Parameters

#### apim_backup.py
 
 **NOTE**: The service principal parameters may be provided via environment variables rather than interactively 
 through the CLI.  The environment variables are: CLIENT_ID, CLIENT_KEY, TENANT_ID and SUBSCRIPTION_ID.
 Arguments provided via the CLI take precedence over environment variables.

- `-g, --resource-gorup`: Resource group that contains the API Management instance
- `-n, --name`: The name of the API Management instance to be backed up
- `--storage-account`: The name of the storage account where the backup will be stored
- `--container`: The storage account container where the backup file will be stored
- `--storage-account-key`: The key to the storage account
- `--client-id`: The client ID of the service principal
- `--client-key`: The secret key for the service principal
- `--tenant-id`: The tenant ID for the service principal
- `--subscription-id`: The subscription ID where the APIM instance is hosted

##### Examples

```bash
# CLIENT_ID, CLIENT_KEY, TENANT_ID, SUBSCRIPTION_ID all stored in environment vars
apim_restore.py -g "apim-rg" -n "apim-instance" --storage-account "apimsa" --container "backups" --storage-account-key "<saKey>"
```

```bash
apim_restore.py -g "apim-rg" -n "apim-instance" --storage-account "apimsa" --container "backups" --storage-account-key "<saKey>" \
  --client-id <clientId> --tenant-id <tenantId> --subscription-id <subId> --client-key <clientKey>
```

#### apim_restore.py

 **NOTE**: The service principal parameters may be provided via environment variables rather than interactively 
 through the CLI.  The environment variables are: CLIENT_ID, CLIENT_KEY, TENANT_ID and SUBSCRIPTION_ID.
 Arguments provided via the CLI take precedence over environment variables.

- `-g, --resource-gorup`: Resource group that contains the API Management instance
- `-n, --name`: The name of the API Management instance to be restored
- `--storage-account`: The name of the storage account where the backup is stored
- `--container`: The storage account container where the backup file is stored
- `--backup-file-name`: The name of the backup file to be used for restoration
- `--storage-account-key`: The key to the storage account
- `--client-id`: The client ID of the service principal
- `--client-key`: The secret key for the service principal
- `--tenant-id`: The tenant ID for the service principal
- `--subscription-id`: The subscription ID where the APIM instance is hosted

##### Examples

```bash
# CLIENT_ID, CLIENT_KEY, TENANT_ID, SUBSCRIPTION_ID all stored in environment vars
apim_restore.py -g "apim-rg" -n "apim-instance" --storage-account "apimsa" --container "backups" --backup-file-name "apimbackup08020414 --storage-account-key "<saKey>"
```

```bash
apim_restore.py -g "apim-rg" -n "apim-instance" --storage-account "apimsa" --container "backups" --backup-file-name "apimbackup08020414 --storage-account-key "<saKey>" \
  --client-id <clientId> --tenant-id <tenantId> --subscription-id <subId> --client-key <clientKey>
```