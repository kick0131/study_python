import logging
import sys
import re
import base64
import json
logging.basicConfig(
    level=logging.DEBUG,            # ログレベル
    format=' %(asctime)s - %(levelname)s - %(message)s')


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
    logging.info(f'{sys._getframe().f_code.co_name} start')
    logging.info(f'{idtoken}')

    repatter = re.compile('\\.')
    separaterIdx = [m.start() for m in repatter.finditer(idtoken)]
    logging.info(f'{separaterIdx}')
    logging.info(idtoken[separaterIdx[0] + 1:separaterIdx[1]])

    logging.info(f'{sys._getframe().f_code.co_name} end')
    return idtoken[separaterIdx[0] + 1:separaterIdx[1]]


def decode_idtoken(idtoken_payload: str):
    """IDトークンペイロード部解析

    CognitoのIDトークンペイロード部の内容をBASE64デコードし、属性情報を表示する

    Parameters
    ----------
    idtoken_payload : str
        IDトークンペイロード部
    """
    dictdata = json.loads(base64.b64decode(idtoken_payload).decode())
    logging.info(dictdata)
    logging.info(type(dictdata))
    logging.info(dictdata['cognito:username'])
    return dictdata


if __name__ == '__main__':
    logging.error('テスト開始')
    payload = parse_idtoken('eyJraWQiOiJ6V2ZDODFGdjBWcWZCRVhKU3R6SHlCaHQxTklnV1VtejZkdDdnc25RaFBZPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJkYWFhYzZkZS03ZDUzLTQ0NGItOTZhNC1mYzhjM2Q2ODY0NGUiLCJhdWQiOiI1cjBzdGpvYmJvdDF2cGw5OHNiNzE1MTl1bSIsImV2ZW50X2lkIjoiZjIyOGQxODYtNWVjMS00NzlhLWFhOWEtZjU4MTA3MzUyYzQyIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE1OTQ5ODgwMjYsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1ub3J0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1ub3J0aGVhc3QtMV80WTVRS0dsNzUiLCJjb2duaXRvOnVzZXJuYW1lIjoidGVzdHVzZXJAbWFpbC5jb20iLCJleHAiOjE1OTQ5OTE2MjYsImlhdCI6MTU5NDk4ODAyNywiZW1haWwiOiJ0ZXN0dXNlckBtYWlsLmNvbSJ9.cgOOjniLfUg5Bv8br0SnLk05LdiwD01MZumxw0sM_hl9ZWs4rznehwawTSeJRjWeem2RCkzvh2SJ2E__6ysnaBP0O8V6JC65rMLS5cs3XlFqcph-sWllXmDLYKZIzfLMgLtBIIomMkSRRko01dxoMISDqhcBf2IOd0ZwY0xtihBQ4lLpbuWKllR3AYL_pGYfLgfSN1XPnxAqJ-BC9qpHaxeuEXLpLejO8DfFYKrEee0hRHp_fowoG76xI4T3LAQEu2r2M4KC7D2n7vKPm_e8_R9lOm9z8S3mt-sYNSu8RJ34-CFvw5hEmqPU3FBAUPX5Z1zfGWfcGZzM0KtrxsOa-A')
    sampledata = 'a.bb.ccc'
    parse_idtoken(sampledata)
    decode_idtoken(payload)
