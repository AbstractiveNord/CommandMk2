Filter CommandMk2 supports the argument mask in the command:

.. code-block:: python

    from command_mk2 import CommandMk2
    CommandMk2('add { note } { timestamp }')

This variables can be optionally provided by the user.
Variables after "timestamp" will not be parsed.

.. code-block:: python

    @router.message(CommandMk2('add { note } { timestamp }'))
    async def add_note(message: Message, note: Optional[str], timestamp: Optional[str]) -> None:
        """Typical handler.

        Note and timestamp is str for now, in next examples i will show typed arguments.
        """
