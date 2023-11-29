import boto3

# Remplacez les valeurs ci-dessous par vos informations d'identification
aws_access_key_id = 'AKIATXLSC2EHLDOKMKVO'
aws_secret_access_key = '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'
region_name = 'eu-west-3'

# Créez une instance du client DynamoDB
dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key,
                          region_name=region_name)

# Maintenant vous êtes connecté à DynamoDB et pouvez interagir avec vos tables
# Par exemple, pour obtenir la liste des tables existantes :
table_list = list(dynamodb.tables.all())
for table in table_list:
    print(table.scan())