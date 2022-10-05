You can describe the types of arguments using Pydantic model

.. code-block:: python

    class AddingNote(BaseModel):
        note: str
        timestamp: Optional[date]

    CommandMk2('add { note } { timestamp }', response_model=AddingNote)

You will recieve ValidatonError if note from command will be empty,
because note is not Optional.You can user aiogram error_handler for that error.

.. code-block:: python

    @router.message(CommandMk2('add { note } { timestamp }', response_model=AddingNote, response_model_name='vars'))
    async def add_note(message: Message, note: str, timestamp: Optional[date]) -> None:
        """Typical handler.

        Note and timestamp is typed properly.
        """
