import locale
import sys
import re
import base64
import json
import aws.loginit
import os

logger = aws.loginit.uselogger(__name__)


def parse_idtoken(idtoken: str):
    """IDトークンペイロード部取得

    CognitoのIDトークンからペイロード部を抽出する

    Parameters
    ----------
    idtoken : str
        IDトークン（ピリオドで区切られたBASE64エンコードされた文字列）

    Returns
    -------
    str
        IDトークンペイロード部
    """
    logger.info(f'{sys._getframe().f_code.co_name} start')
    logger.info(f'{idtoken}')

    repatter = re.compile('\\.')
    separaterIdx = [m.start() for m in repatter.finditer(idtoken)]
    logger.info(f'{separaterIdx}')
    logger.info(idtoken[separaterIdx[0] + 1:separaterIdx[1]])

    logger.info(f'{sys._getframe().f_code.co_name} end')
    return idtoken[separaterIdx[0] + 1:separaterIdx[1]]


def encode_idtoken(idtoken_payload: str):
    """IDトークンペイロード部解析

    CognitoのIDトークンペイロード部の内容をBASE64デコードし、属性情報を表示する

    Parameters
    ----------
    idtoken_payload : str
        IDトークンペイロード部
    """
    dictdata = json.loads(base64.b64decode(idtoken_payload).decode())
    logger.info(dictdata)
    logger.info(type(dictdata))
    logger.info(dictdata['cognito:username'])


if __name__ == '__main__':
    logger.info(f'テスト開始 (default encodeing={locale.getpreferredencoding()})')

    # 同じディレクトリに存在するファイルを指定
    tokenfilepath = os.path.join(os.path.dirname(__file__), 'idtoken')
    idtoken = ''
    with open(tokenfilepath, mode='r', encoding='utf_8') as f:
        idtoken = f.read()
    payload = parse_idtoken(idtoken)
    sampledata = 'a.bb.ccc'
    parse_idtoken(sampledata)
    encode_idtoken(payload)
