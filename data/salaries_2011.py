import collections
from decimal import Decimal

def import_salaries(f):
    rows = [e.split("\t") for e in open(f).readlines()]
    filter_row = lambda i: [e[i] for e in rows]

    teams, lasts, firsts, pos = [filter_row(e) for e in range(4)]
    base = [Decimal(e[-2]) for e in rows if e[-2]]

    guaranteed = [Decimal(e[-1]) for e in rows if e[-1] not in ("$\n", "")]

    Salary = collections.namedtuple("Salary", ['team', 'last_name', 'first_name', 'position', 'base', 'guaranteed'])

    for e in zip(teams, lasts, firsts, pos, base, guaranteed):
        yield Salary(*e)


get_salaries = lambda f: list(import_salaries(f))


sorted_salaries = lambda f: sorted(get_salaries(f), key=lambda k: -k.guaranteed)
    


    
