from contextlib import AsyncExitStack

from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver

_exit_stack = AsyncExitStack()
_checkpointer = None


async def initialize_checkpointer(database_url: str):
    global _checkpointer

    if _checkpointer is None:
        context = AsyncPostgresSaver.from_conn_string(database_url)

        _checkpointer = await _exit_stack.enter_async_context(context)

        await _checkpointer.setup()

    return _checkpointer


async def close_checkpointer():
    await _exit_stack.aclose()


def get_checkpointer():
    if _checkpointer is None:
        raise RuntimeError("Checkpointer not initialized")

    return _checkpointer