import json
import sys
import boto3
ec2 = boto3.client('ec2')
def lambda_handler(event, context):
    # TODO implement
    if sys.argv[1] == 'ON':
        response = ec2.monitor_instances(InstanceIds=['INSTANCE_ID'])
    else:
        response = ec2.unmonitor_instances(InstanceIds=['INSTANCE_ID'])
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }