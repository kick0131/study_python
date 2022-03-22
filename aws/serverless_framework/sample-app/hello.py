"""データ蓄積機能

.. autosummary::

   data_handler
   validation
   conversion_type
   regist_data

"""
import os
import boto3


def lambda_handler(event, context):
    print('hello')
