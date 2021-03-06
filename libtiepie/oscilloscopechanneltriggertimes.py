from .api import api
from .const import *
from .library import library
from .exceptions import *


class OscilloscopeChannelTriggerTimes(object):
    """"""

    def __init__(self, handle, ch):
        self._handle = handle
        self._ch = ch

    def __getitem__(self, index):
        try:
            value = api.ScpChTrGetTime(self._handle, self._ch, index)
            library.check_last_status_raise_on_error()
            return value
        except InvalidIndexError:
            raise IndexError()
        except NotSupportedError:
            if api.ScpChHasTrigger(self._handle, self._ch) == BOOL8_TRUE:
                raise IndexError()
            else:
                raise

    def __setitem__(self, index, value):
        try:
            api.ScpChTrSetTime(self._handle, self._ch, index, value)
            library.check_last_status_raise_on_error()
        except InvalidIndexError:
            raise IndexError()
        except NotSupportedError:
            if api.ScpChHasTrigger(self._handle, self._ch) == BOOL8_TRUE:
                raise IndexError()
            else:
                raise

    def __len__(self):
        return self.count

    def _get_count(self):
        return api.ScpChTrGetTimeCount(self._handle, self._ch)

    def verify(self, index, value):
        value = api.ScpChTrVerifyTime(self._handle, self._ch, index, value)
        library.check_last_status_raise_on_error()
        return value

    count = property(_get_count)
