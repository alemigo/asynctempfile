# asynctempfile

Async interface for the standard tempfile module.  Implements the following 
4 classes:

- TemporaryFile
- NamedTemporaryFile
- SpooledTemporaryFile
- TemporaryDirectory

Blocking methods are delegated to threadpools using loop.run_in_executor(). 
Non-blocking methods and properties retain a sync interface.  SpooledTemporaryFile only delegates if the in-memory stream is rolled to 
disk.  New instances of the above classes return wrapped with a context 
manager allowing use with async with and async for.

### Credit

An extension of github.com/Tinche/aiofiles 

### Examples
```
import asynctempfile

async with asynctempfile.TemporaryFile('wb+') as f:
    await f.write(b'Hello, World!')
```
```
import asynctempfile

async with asynctempfile.NamedTemporaryFile('wb+') as f:
    await f.write(b'Line1\n Line2')
    await f.seek(0)
    async for line in f:
        print(line)
```
### Dependencies

aiofiles

