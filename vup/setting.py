import enum


class Type(enum.Enum):
    Auto = 'auto'
    Manual = 'manual'
    Year = 'year'
    Month = 'month'
    Day = 'day'
    Days = 'days'
    Null = 'none'


class _Field:
    def __init__(self, data):
        self.__type = Type(data['type'])


class Setting:
    def __init__(self, data):
        self.__major = _Field(data['major'])
        self.__minor = _Field(data['minor'])
        self.__build = _Field(data['build'])
        self.__revision = _Field(data['revision'])

    @property
    def major(self) -> _Field:
        return self.__major

    @property
    def minor(self) -> _Field:
        return self.__minor

    @property
    def build(self) -> _Field:
        return self.__build

    @property
    def revision(self) -> _Field:
        return self.__revision
