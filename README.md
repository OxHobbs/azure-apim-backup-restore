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

#### apim-backup.py


