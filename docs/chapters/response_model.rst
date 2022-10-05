Response Model
=============

Options
-------
You have multiple options to recieve a variables, passed with command.

- Contextvars
-------------

.. code-block:: python

    @router.message(CommandMk2('add { note } { timestamp }', response_model=AddingNote,  response_model_name='vars'))
    async def add_note(message: Message, note: str, timestamp: Optional[date]) -> None:

Model fields will be dropped into context.
Take care for naming, you can overlap between existing variables and get problems from nowhere.

- Auto-named response_model
---------------------------

.. code-block:: python

    @router.message(CommandMk2('add { note } { timestamp }', response_model=AddingNote))
    async def add_note(message: Message, adding_note: AddingNote) -> None:

Model will be dropped into context as object, named same as model class but in snake case.

- Custom-named response_model
---------------------------

.. code-block:: python

    @router.message(CommandMk2('add { note } { timestamp }', response_model=AddingNote,
    response_model_name="custom_named_model"))
    async def add_note(message: Message, custom_named_model: AddingNote) -> None:

Model will be dropped into context as object, named as you want.
Be careful with naming.
