def set_AQI(val=0):
    if val <= 50:
        return "优"
    elif val <= 100:
        return '良'
    elif val <= 150:
        return '轻度污染'
    elif val <= 150:
        return '轻度污染'
    elif val <= 200:
        return '中度污染'
    elif val <= 300:
        return '重度污染'
    else:
        return '严重'
