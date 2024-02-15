import configparser
import boto3
import snowflake.connector

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
        connection_name='SNOWFLAKE'
        snowflake_connection = snowflake.connector.connect(
            user=config.get(connection_name, 'User'),
            password=config.get(connection_name, 'Password'),
            account=config.get(connection_name, 'Account'),
            warehouse=config.get(connection_name, 'Warehouse'),
            database=config.get(connection_name, 'Database'),
            schema=config.get(connection_name, 'Schema')
        )
        print('Successfully Connected to Snowflake')   
        return snowflake_connection
    except Exception as e:
        print(e)
        print('Not connected to snowflake')
    return 'Failed Connection'