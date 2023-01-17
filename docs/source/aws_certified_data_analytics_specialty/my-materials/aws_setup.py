import boto3
import botocore


class AwsCloudGuruSetuper:
    def __init__(self, aws_access_key_id: str = None, aws_secret_access_key: str = None, region_name: str = None):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.region_name = region_name

        self.ses = boto3.Session(aws_access_key_id=self.aws_access_key_id,
                                 aws_secret_access_key=self.aws_secret_access_key,
                                 region_name=self.region_name)

    def s3_create_bucket(self, bucket_name):
        s3 = self.ses.client('s3')
        try:
            s3.create_bucket(Bucket=bucket_name)
            s3.list_objects_v2(Bucket=bucket_name)
        except Exception:
            resp = s3.list_objects_v2(Bucket=bucket_name)
            if resp['ResponseMetadata']['HTTPStatusCode'] != 200:
                raise Exception(
                    'bucket exist and you dont have permission to read - change bucket name')

    def ec2_create_keypair(self, key_name: str = None, key_type: str = 'rsa', key_format: str = 'ppk', ignore_errors: bool = False):
        if key_type not in ['rsa', 'ed25519'] or key_format not in ['pem', 'ppk']:
            raise Exception('key_type or key_format have value which is not possible')
        ec2 = self.ses.client('ec2')
        try:
            resp = ec2.create_key_pair(KeyName=key_name,
                            KeyType=key_type,
                            KeyFormat=key_format)
            with open(f'./{key_name}.{key_format}', 'w') as file:
                file.write(resp['KeyMaterial'])
        except botocore.exceptions.ClientError as e:
            if not ignore_errors:
                raise(e)

    def ec2_list_imageids(self, name_prefix: str = 'Ubuntu*'):
        ec2 = self.ses.client('ec2')
        resp = ec2.describe_images(Filters=[{'Name': 'name', 'Values': [name_prefix]}])

        return [{image['ImageId']: f"{image['Name']} ({image['Architecture']})"} for image in resp['Images']]

    def ec2_create_instance(self, instance_type: str = 't2.micro', key_name: str = None,
                            imageid: str = None, min_count: int = 1, max_count: int = 1):

        if imageid is None:
            imageid = self.ec2_list_imageids(name_prefix='Ubuntu 22.04 Base')[0]

        ec2 = self.ses.resource('ec2')
        resp = ec2.create_instances(
            ImageId=list(imageid.keys())[0],
            MinCount=min_count,
            MaxCount=max_count,
            InstanceType=instance_type,
            KeyName=key_name
        )

        return [instance.id for instance in resp]


if __name__ == '__main__':
    aws = AwsCloudGuruSetuper()

    aws.ec2_create_keypair(key_name='mg', key_format='pem', ignore_errors=True)
    aws.s3_create_bucket('test-mg-nowy-999')
    print(aws.ec2_create_instance(key_name='mg'))
