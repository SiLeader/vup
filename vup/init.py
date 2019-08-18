from . import setting


def __default_value(t: setting.Type):
    return {
        setting.Type.Auto: 'auto',
        setting.Type.Manual: 'manual',
        setting.Type.Year: 'year',
        setting.Type.Month: 'month',
        setting.Type.Day: 'day',
        setting.Type.Days: 'days',
        setting.Type.Null: '',
    }[t]
    pass


def init(args):
    pref = {
        p: {
            'type': setting.Type(getattr(args, '{}_type'.format(p))),
        }
        for p in ('major', 'minor', 'build', 'revision')
    }

    pref = {
        p: {
            'type': v['type']
        }
        for p, v in pref.items()
    }
