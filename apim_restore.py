import os
import time
import argparse
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.apimanagement import ApiManagementClient
from datetime import datetime as dt


parser = argparse.ArgumentParser(prog='restore_apim',
                                 description='Tool to restore Azure API Management from a backup \
                                 stored in a Storage Account')

parser.add_argument('-g', '--resource-group',
                    help='Resource group name that contains the destination API Management instance',
                    required=True)
parser.add_argument('-n', '--name',
                    help='The name of the API Management instance to which the restore will go.',
                    required=True)
parser.add_argument('--storage-account',
                    help='The name of the storage account where the backup is stored.',
                    required=True)
parser.add_argument('--container',
                    help='The name of the storage container where the backup is stored',
                    required=True)
parser.add_argument('--storage-account-key',
                    help='The storage account access key',
                    required=True)
parser.add_argument('--backup-file-name',
                    help='The name of the backup file within the container to be used for restoration',
                    required=True)
parser.add_argument('--client-id',
                    help='The client ID of the service principal used for authentication',
                    default=os.environ.get('CLIENT_ID'))
parser.add_argument('--client-key',
                    help='The key for the service principal',
                    default=os.environ.get('CLIENT_KEY'))
parser.add_argument('--tenant-id',
                    help='The tenant ID of the service principal',
                    default=os.environ.get('TENANT_ID'))
parser.add_argument('--subscription-id',
                    help='The subscription ID where the API Management instance is hosted',
                    default=os.environ.get('SUBSCRIPTION_ID'))

args = parser.parse_args()


client = args.client_id
key = args.client_key
sub_id = args.subscription_id
tenant_id = args.tenant_id

api_settings = {
    'rg': args.resource_group,
    'name': args.name,
    'parameters': {
        'storage_account': args.storage_account,
        'access_key': args.storage_account_key,
        'container_name': args.container,
        'backup_name': args.backup_file_name,
    },
}

spn = ServicePrincipalCredentials(client, key, tenant=tenant_id)
apim_client = ApiManagementClient(spn, sub_id)
print('Starting the restore process, this will take some time to complete.')
poller = apim_client.api_management_service.restore(resource_group_name=api_settings['rg'],
                                                    service_name=api_settings['name'],
                                                    parameters=api_settings['parameters'])

start_time = dt.utcnow()
while not poller.done():
    time.sleep(20)
    diff = dt.utcnow() - start_time
    print("Waiting for the restore to complete, current status is {}, time elapsed is {} seconds\r".format(
        poller.status(),
        diff.seconds))


final_status = poller.status()

if final_status == 'Succeeded':
    print('The restore was successfully completed\n\tstorage account: {}\n\tfilename: {}\n\trestored to: {}'.format(
        api_settings['parameters']['storage_account'],
        api_settings['parameters']['backup_name'],
        api_settings['name']))
else:
    print('Something went wrong! Final status: {}'.format(final_status))
