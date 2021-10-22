import re


# DMS to DEG
def dms2deg(list):
    result = []
    if '度' in list[0]:
        for latlon in list:
            if '経' in latlon:
                d = re.findall(r'経(.*?)度+', latlon)
            elif '緯' in latlon:
                d = re.findall(r'緯(.*?)度+', latlon)
            m = re.findall(r'度(.*?)分+', latlon)
            s = re.findall(r'分(.*?)秒+', latlon)
            x = float(d[0])+float(m[0])/60+float(s[0])/3600
            result.append(x)
    elif '°' in list[0]:
        for latlon in list:
            d = re.findall(r'(.*?)°+', latlon)
            m = re.findall(r'°(.*?)′+', latlon)
            s = re.findall(r'′(.*?)″+', latlon)
            x = float(d[0])+float(m[0])/60+float(s[0])/3600
            result.append(x)
    else:
        print('error')
        return list
    return result
