## Copyright (c) Cognitect, Inc.
## All rights reserved.

import collections

class Keyword(object):
    def __init__(self, value):
        assert isinstance(value, basestring)
        self.str = value

    def __hash__(self):
        return hash(self.str)

    def __eq__(self, other):
        return isinstance(other, Keyword) and self.str == other.str

    def __call__(self, mp):
        return mp[self] # Maybe this should be .get()

    def __repr__(self):
        return "<Keyword " + self.str + ">"

    def __str__(self):
        return self.str

class Symbol(object):
    def __init__(self, value):
        assert isinstance(value, basestring)
        self.str = value

    def __hash__(self):
        return hash(self.str)

    def __eq__(self, other):
        return isinstance(other, Symbol) and self.str == other.str

    def __ne__(self, other):
        return not self == other

    def __call__(self, mp):
        return mp[self]

    def __repr__(self):
        return self.str

    def __str__(self):
        return self.str

kw_cache = {}

class _KWS(object):
    def __getattr__(self, item):
        value = self(item)
        setattr(self, item, value)
        return value

    def __call__(self, str):
        if str in kw_cache:
            return kw_cache[str]
        else:
            kw_cache[str] = Keyword(str)
            return kw_cache[str]

kws = _KWS()

class TaggedValue(object):
    def __init__(self, tag, data):
        self.tag = tag
        self.value = data
    def __eq__(self, other):
        if isinstance(other, TaggedValue):
            return self.tag == other.tag and \
                   self.value == other.value
        return False

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        if isinstance(self.value, list):
            return reduce(lambda a, b: hash(a) ^ hash(b), self.value, 0)
        return hash(self.value)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "#"+self.tag + " " + repr(self.value)

class Set(TaggedValue):
    def __init__(self, data):
        TaggedValue.__init__(self, "set", data)

class CMap(TaggedValue):
    def __init__(self, data):
        TaggedValue.__init__(self, "cmap", data)

class Vector(TaggedValue):
    def __init__(self, data):
        TaggedValue.__init__(self, "vector", data)

class Array(TaggedValue):
    def __init__(self, data):
        TaggedValue.__init__(self, "array", data)

class List(TaggedValue):
    def __init__(self, data):
        TaggedValue.__init__(self, "list", data)

class URI(TaggedValue):
    def __init__(self, data):
        TaggedValue.__init__(self, "uri", data)

from collections import Mapping, Hashable
class frozendict(Mapping, Hashable):
    def __init__(self, *args, **kwargs):
        self._dict = dict(*args, **kwargs)
    def __len__(self):
        return len(self._dict)
    def __iter__(self):
        return iter(self._dict)
    def __getitem__(self, key):
        return self._dict[key]
    def __hash__(self):
        return hash(frozenset(self._dict.items()))
    def __repr__(self):
        return 'frozendict(%r)' % (self._dict,)

