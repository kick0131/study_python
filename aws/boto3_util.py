import boto3
from boto3.session import Session


def createAwsServiceClient(service: str, profile: str = None):
    """create aws service client

    usage
    client = createAwsServiceClient('dynamodb', profile=hoge)

    Parameters
    ----------
    service : str
        boto3 servicename
        ec2
        dynamodb
    profile : str, optional
        aws profile name, by default None
    """
    if(profile is not None):
        session = Session(profile_name=profile)
        return session.client(service, verify=False)
    # Lambda等、プロファイル指定が無いケース
    else:
        return boto3.client(service)


def createAwsServiceResource(service: str, profile: str = None):
    """create aws service client

    usage
    client = createAwsServiceResource('dynamodb', profile=hoge)

    Parameters
    ----------
    service : str
        boto3 servicename
        ec2
        dynamodb
    profile : str, optional
        aws profile name, by default None
    """
    if(profile is not None):
        session = Session(profile_name=profile)
        return session.resource(service, verify=False)
    # Lambda等、プロファイル指定が無いケース
    else:
        return boto3.resource(service)
