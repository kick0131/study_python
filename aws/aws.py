# ★注意★
# セキュリティ上、本ファイルは非公開とすること！！！
#
import sys,boto3

# boto3について
# 高レベルAPI（Resources）と低レベルAPI（Clients）の2つが存在する
# 高レベル：ec2,s3
# 低レベル：全て


global rdsInstanceName
global ec2InstanceName
#ec2.Instance(id='i-0a9999513a7946a22')
#ec2.Instance(id='i-03a88fcea85b630ac')
#ec2.Instance(id='i-0b5cb7d1fd00cbdf9')
rdsInstanceName = 'sampledb'
ec2InstanceName = 'i-0a9999513a7946a22'

# -------------------------------------------------------------------
# sub func
# -------------------------------------------------------------------

# AWS Lambda定義用
def lambda_handler(event, context):
    dbinstance = 'testdb' #対象のDBインスタンス識別子
    rds = boto3.client('rds')
    result = rds.start_db_instance(DBInstanceIdentifier = dbinstance) #start RDS
    print(result)
    return 0

# boto3ライブラリ初期化
# AWS接続先定義がある為、アカウント情報は非公開とすること
def botoInitialize():
    print(sys._getframe().f_code.co_name)
    global session
    session = boto3.Session(aws_access_key_id='AKIAJHO5J767QPY7OYUQ',
            aws_secret_access_key='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',
            region_name='ap-northeast-1')

# 動作確認用
def funcStr(flg):
    print(sys._getframe().f_code.co_name)

    if flg == 'start':
        print(flg)
    elif flg == 'stop':
        print(flg)
    elif flg == 'ec2':
        print(flg)
        ec2 = boto3.resource(flg)
        for i in ec2.instances.all():
            print(i)


# RDS操作
def rdsAction(flg):
    print(sys._getframe().f_code.co_name)

    rds = boto3.client('rds')

    if flg == 'start':
        print(flg)
        responce = rds.start_db_instance(
            DBInstanceIdentifier = rdsInstanceName
        )

    elif flg == 'stop':
        print(flg)
        responce = rds.stop_db_instance(
            DBInstanceIdentifier = rdsInstanceName
        )
    else:
        print('RDS操作が選択されませんでした')

    print(rds)

# -------------------------------------------------------------------
# main
# -------------------------------------------------------------------
try:
    print('main start')

    # AWS接続先の設定
#    botoInitialize()

    # EC2インスタンス一覧の表示
#    ec2 = session.resource('ec2')
#    for i in ec2.instances.all():
#        print(i)

    action = 'stop'
#    funcStr(action)
    rdsAction(action)

except:
    print('何かしらのエラー発生')




