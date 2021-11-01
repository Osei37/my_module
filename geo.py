import re

# [sw_lon, sw_lat, nw_lon, ne_lat] 
# -> [[s_lat, w_lon], [s_lat, e_lon], [n_lat, e_lon], [n_lat, w_lon]]
def change_degrees(list):
    result = []
    sw = [list[1], list[0]]
    se = [list[1], list[2]]
    ne = [list[3], list[2]]
    nw = [list[3], list[0]]
    result = [sw, se, ne, nw]
    return result


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

# DEG to DMS
def deg2dms(list):
    result = []
    return result
