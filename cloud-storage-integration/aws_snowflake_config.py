import configparser
import boto3

def getProp():
	global config
	config = configparser.RawConfigParser()
	config.read('../configuration.properties')
	return True

# make s3 connection
def aws_s3_connection():
    try:
        check = getProp()
        access_key = config['AWS']['access_key']
        secret_key = config['AWS']['secret_key']
        bucket_name = config['s3-bucket']['bucket']
        s3_client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
        return s3_client, bucket_name
    except Exception as e:
        print("Exception in aws_s3_connection func: ",e)
        print('S3 Connection Faileddd')
        
def snowflake_connection():
    try:
        getProp()        
        user=config['SNOWFLAKE']['User']
        password=config['SNOWFLAKE']['Password']
        account=config['SNOWFLAKE']['Account']
        warehouse=config['SNOWFLAKE']['Warehouse']
        database=config['SNOWFLAKE']['Database']
        schema=config['SNOWFLAKE']['Schema']

        return user, password, account, warehouse, database, schema
    except Exception as e:
        print(e)
        print('Cannot get snowflake credentials.check configuration properties')
    return 'Failed Connection'