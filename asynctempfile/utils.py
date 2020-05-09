import asyncio
from types import coroutine
import functools


def cond_delegate_to_executor(*attrs):
    def cls_builder(cls):
        for attr_name in attrs:
            setattr(cls, attr_name, _make_cond_delegate_method(attr_name))
        return cls
    return cls_builder


def _make_cond_delegate_method(attr_name):
    """For spooled temp files, delegate only if rolled to file object"""
    @coroutine
    def method(self, *args, **kwargs):
        if self._file._rolled:
            cb = functools.partial(getattr(self._file, attr_name),
                                   *args, **kwargs)
            return (yield from self._loop.run_in_executor(self._executor, cb))
        else:
            return getattr(self._file, attr_name)(*args, **kwargs)
    return method
