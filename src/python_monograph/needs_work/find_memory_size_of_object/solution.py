#!/usr/bin/env python3
"""Python Monograph: Find Memory Size of Object

Copyright ©2024 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>."""
from inspect import isgetsetdescriptor, ismemberdescriptor
from sys import getsizeof


def method_0(obj: Any, seen: set = None) -> int:
    """Calculate the memory size of a given object in bytes.

    This function recursively traverses the object's attributes and elements (if it's a container),
    summing up their memory sizes. It handles circular references by keeping track of already seen objects.

    Args:
        obj: The object to calculate the memory size of.
        seen: A set of ids of objects that have already been processed.

    Returns:
        The memory size of the object in bytes.

    References:
        https://blog.codinghorror.com/gigabyte-decimal-vs-binary/
        https://physics.nist.gov/cuu/Units/binary.html
        https://ux.stackexchange.com/questions/13815/files-size-units-kib-vs-kb-vs-kb
    """
    size = getsizeof(obj)
    seen = seen or set()
    obj_id = id(obj)

    if obj_id in seen:
        return 0

    seen.add(obj_id)

    if hasattr(obj, '__dict__'):
        for cls in obj.__class__.__mro__:
            if '__dict__' in cls.__dict__:
                d = cls.__dict__['__dict__']
                if isgetsetdescriptor(d) or ismemberdescriptor(d):
                    size += method_0(obj.__dict__, seen)
                break

    if isinstance(obj, dict):
        size += sum((method_0(v, seen) for v in obj.values()))
        size += sum((method_0(k, seen) for k in obj.keys()))
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum((method_0(i, seen) for i in obj))

    if hasattr(obj, '__slots__'):  # can have __slots__ with __dict__
        size += sum(method_0(getattr(obj, s), seen) for s in obj.__slots__ if hasattr(obj, s))

    return size


def method_1(obj: Any) -> int:
    """Calculate the memory size of a given object in bytes.

    This function recursively traverses the object's attributes and elements (if it's a container),
    summing up their memory sizes. It handles circular references by keeping track of already seen objects.

    Args:
        obj: The object to calculate the memory size of.

    Returns:
        The memory size of the object in bytes.

    References:
        https://blog.codinghorror.com/gigabyte-decimal-vs-binary/
        https://physics.nist.gov/cuu/Units/binary.html
        https://ux.stackexchange.com/questions/13815/files-size-units-kib-vs-kb-vs-kb
    """
    size = getsizeof(obj)
    if isinstance(obj, dict):
        size += sum(method_1(v) for v in obj.values())
    elif hasattr(obj, '__dict__'):
        size += method_1(obj.__dict__)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum(method_1(item) for item in obj)
    return size


if __name__ == '__main__':
    print(__doc__)
