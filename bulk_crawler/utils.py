import asyncio
from functools import wraps
import inspect

def chunker(seq, size):
    """
    return a sequence/list in chunks of size=size
    Args:
        seq: list
        size: int - chunk size
    Returns:
        seq or list of chunks
    """
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def bulk_func_asyncer(size):
    def decorator(func):

        if not inspect.iscoroutinefunction(func):
            raise TypeError('Decorator only works on async functions')

        @wraps(func)
        async def wrapper(*args):

            sig = inspect.signature(wrapper)
            params = sig.parameters
            if len(params) > 1:
                raise TypeError('Functions using bulk_func_asyncer can only accept 1 argument, got {}'.format(len(params)))

            list_of_seqs = chunker(*args, size)
            response = await asyncio.gather(*map(func, list_of_seqs))
            flat_response = [item for sublist in response for item in sublist]

            return flat_response

        return wrapper

    return decorator


