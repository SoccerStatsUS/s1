import datetime

BIOS_PATH = "/home/chris/www/soccer/data/bios.csv"


def load_bios():
    f = open(BIOS_PATH)
    mapping = {}
    header = ['name', '_', 'pos', 'feet', 'inches', 'weight', 'month', 'day', 'year', '_', 'college', 'birthplace']
    for line in f:
        if line.endswith("\n"):
            line = line[:-1]
        items = line.split('\t')
        try:
            d = dict(zip(header, items))
        except:
            import pdb; pdb.set_trace()
            pass
        names = d['name'].split(',')
        if len(names) == 2:
            last_name, first_name = names
        else:
            first_name = ''
            last_name = d['name']
        full_name = ("%s %s" % (first_name, last_name)).strip()
        d['last_name'] = last_name
        d['first_name'] = first_name
        if d['year'] and d['month'] and d['day']:
            if int(d['year']) < 100:
                d['year'] = int(d['year']) + 1900
            d['birthdate'] = datetime.date(int(d['year']), int(d['month']), int(d['day']))
        else:
            d['birthdate'] = None
        mapping[full_name] = d

    return mapping        
    



    

        
        
