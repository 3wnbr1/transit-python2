from constants import *
from class_hash import ClassDict
from transit_types import Keyword, Symbol, URI
import uuid
import datetime, time
import dateutil

class NoneHandler(object):
    @staticmethod
    def tag(_):
        return '_'
    @staticmethod
    def rep(_):
        return None
    @staticmethod
    def string_rep(n):
        return None

class IntHandler(object):
    @staticmethod
    def tag(i):
        return 'i'
    @staticmethod
    def rep(i):
        return i
    @staticmethod
    def string_rep(i):
        return str(i)

class FloatHandler(object):
    @staticmethod
    def tag(_):
        return "f"
    @staticmethod
    def rep(f):
        return str(f)
    @staticmethod
    def string_rep(f):
        return FloatHandler.rep(f)

class StringHandler(object):
    @staticmethod
    def tag(s):
        return 's'
    @staticmethod
    def rep(s):
        return s
    @staticmethod
    def string_rep(s):
        return s

class BooleanHandler(object):
    @staticmethod
    def tag(_):
        return '?'
    @staticmethod
    def rep(b):
        return b
    @staticmethod
    def string_rep(b):
        return b and 't' or 'f'

class ArrayHandler(object):
    @staticmethod
    def tag(a):
        return 'array'
    @staticmethod
    def rep(a):
        return a
    @staticmethod
    def string_rep(a):
        return None

class MapHandler(object):
    @staticmethod
    def tag(m):
        return 'map'
    @staticmethod
    def rep(m):
        return m
    @staticmethod
    def string_rep(m):
        return None

class KeywordHandler(object):
    @staticmethod
    def tag(k):
        return ':'
    @staticmethod
    def rep(k):
        return str(k)
    @staticmethod
    def string_rep(k):
        return str(k)

class SymbolHandler(object):
    @staticmethod
    def tag(s):
        return '$'
    @staticmethod
    def rep(s):
        return str(s)
    @staticmethod
    def string_rep(s):
        return str(s)

class UuidHandler(object):
    mask = pow(2, 64) - 1
    @staticmethod
    def tag(_):
        return "u"
    @staticmethod
    def rep(u):
        i = u.int
        return (i >> 64, i & UuidHandler.mask)
    @staticmethod
    def string_rep(u):
        return str(u)

class UriHandler(object):
    @staticmethod
    def tag(_):
        return "r"
    @staticmethod
    def rep(u):
        return u.data
    @staticmethod
    def string_rep(u):
        return u.data

class DateTimeHandler:
    epoch = datetime.datetime(1970, 1, 1).replace(tzinfo=dateutil.tz.tzutc())
    @staticmethod
    def tag(_):
        return "t"
    @staticmethod
    def rep(d):
        td = d - DateTimeHandler.epoch
        return long((td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 1e3)

    @staticmethod
    def string_rep(d):
        return d.isoformat()

class Handler(ClassDict):
    def __init__(self):
        super(Handler, self).__init__()
        self[type(None)] = NoneHandler
        self[bool] = BooleanHandler
        self[str] = StringHandler
        self[list] = ArrayHandler
        self[tuple] = ArrayHandler
        self[dict] = MapHandler
        self[int] = IntHandler
        self[float] = FloatHandler
        self[long] = IntHandler
        self[Keyword] = KeywordHandler
        self[Symbol] = SymbolHandler
        self[uuid.UUID] = UuidHandler
        self[URI] = UriHandler
        self[datetime.datetime] = DateTimeHandler
