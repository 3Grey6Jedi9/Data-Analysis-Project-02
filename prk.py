



d = {
        'name': 'Karl Saygan',
        'guardians': 'Heather Bledsoe',
        'experience': 'YES',
        'height': '42 inches'
    }


for key, value in d.items():
    if key == 'height':
        d[key] = int((value.split(' ')[0]))
        print(type(d[key]))


