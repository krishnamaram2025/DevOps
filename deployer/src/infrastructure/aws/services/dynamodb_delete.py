import boto3

def delete_dax_table(dyn_resource=None):
    if dyn_resource is None:
        dyn_resource = boto3.resource('dynamodb')
    table = dyn_resource.Table('terraform_locks')
    table.delete()
    print(f"Deleting {table.name}...")
    table.wait_until_not_exists()

if __name__ == '__main__':
    delete_dax_table()
    print("Table deleted!")

