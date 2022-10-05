import datetime

import pytest
from aiogram.filters import CommandObject
from aiogram.types import Chat, Message

from command_mk2 import CommandMk2
from tests.mocked_bot import MockedBot


@pytest.mark.asyncio
async def test_recognition():
    command = CommandMk2('start')
    response = await command(
        Message(
            message_id=1,
            chat=Chat(
                id=1,
                type="private",
            ),
            text='/start',
            date=datetime.datetime.now(),
        ),
        MockedBot(),
    )
    command_obj: CommandObject = response.pop('command')
    assert command_obj.command == 'start'
    assert command_obj.mention is None


@pytest.mark.asyncio
async def test_filtration():
    command = CommandMk2('start')
    bad_response = await command(
        Message(
            message_id=1,
            chat=Chat(
                id=1,
                type="private",
            ),
            text='/not_start',
            date=datetime.datetime.now(),
        ),
        MockedBot(),
    )
    assert bad_response is False


@pytest.mark.parametrize('schema', [['start', 'ban']])
@pytest.mark.parametrize('input_command', ['/start', '/ban'])
@pytest.mark.asyncio
async def test_multiple_schemas(schema: str, input_command: str):
    command = CommandMk2(*schema)
    response = await command(
        Message(
            message_id=1,
            chat=Chat(
                id=1,
                type="private",
            ),
            text=input_command,
            date=datetime.datetime.now(),
        ),
        MockedBot(),
    )
    command_obj: CommandObject = response.pop('command')
    assert command_obj.command is not None
    assert command_obj.mentioned is False
