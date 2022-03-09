from datetime import datetime, timezone, timedelta

UTC = timezone.utc
JST = timezone(timedelta(hours=+9), 'JST')


def formatdatetimeSample(dt: datetime):
    """フォーマット指定の時刻取得

    書式指定
    https://docs.python.org/ja/3/library/datetime.html#strftime-and-strptime-behavior

    Parameters
    ----------
    dt : datetime
        [description]
    """
    TimeFmt = '%Y/%m/%dT%H:%M:%S%z'

    # Timezone指定あり
    newdt = datetime.fromtimestamp(dt.timestamp(), JST)
    return newdt.strftime(TimeFmt)


OneItem = {
    'CreatedId': '2015',
    'getDataTime': formatdatetimeSample(datetime.now()),
    'info': {
        'plot': 'Nothing happens at all.',
        'rating': 0
    }
}

MultiItem = [
    {
        'CreatedId': '2015',
        'getDataTime': formatdatetimeSample(datetime.now()),
        'info': {
            'plot': 'Nothing happens at all.',
            'rating': 0
        }
    },
    {
        'CreatedId': '2016',
        'getDataTime': formatdatetimeSample(datetime.now()),
        'info': {
            'plot': 'Wonderful.',
            'rating': 5
        }
    },
    {
        'CreatedId': '2017',
        'getDataTime': formatdatetimeSample(datetime.now()),
        'info': {
            'plot': 'No comment.',
            'rating': 2
        }
    }
]
