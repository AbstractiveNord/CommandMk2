Usage
==================

.. code-block:: python

    class AddingNote(BaseModel):
        note: str
        timestamp: Optional[date]

    @router.message(CommandMk2('add { note } { timestamp }', response_model=AddingNote, response_model_name='vars'))
    async def add_note(message: Message, note: str, timestamp: Optional[date]) -> None:
        ...
