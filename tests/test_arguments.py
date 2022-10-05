from datetime import date, datetime
from typing import Optional

import pytest
from aiogram.filters import CommandObject
from aiogram.types import Chat, Message
from pydantic import BaseModel

from command_mk2 import CommandMk2
from tests.mocked_bot import MockedBot


@pytest.mark.asyncio
async def test_model_auto_name() -> None:
    class RestrictModel(BaseModel):
        period: Optional[date]
        reason: Optional[str]

    command = CommandMk2('ban {period} {reason}', response_model=RestrictModel)
    response = await command.__call__(
        Message(
            message_id=1,
            chat=Chat(
                id=1,
                type='private',
            ),
            text='/ban 2022-10-22 hacker',
            date=datetime.now(),
        ),
        MockedBot(),
    )
    command_obj: CommandObject = response.get('command')
    assert command_obj.command == 'ban'
    assert command_obj.mentioned is False
    assert response.get('restrict_model')


@pytest.mark.asyncio
async def test_model_variables():
    class RestrictModel(BaseModel):
        period: Optional[date]
        reason: Optional[str]

    command = CommandMk2('ban {period} {reason}', response_model=RestrictModel, response_model_name='vars')
    response = await command.__call__(
        Message(
            message_id=1,
            chat=Chat(
                id=1,
                type='private',
            ),
            text='/ban 2022-10-22 hacker',
            date=datetime.now(),
        ),
        MockedBot(),
    )
    command_obj: CommandObject = response.get('command')
    assert command_obj.command == 'ban'
    assert command_obj.mentioned is False
    assert response.get('period')
    assert response.get('reason')


@pytest.mark.asyncio
async def test_partial_variables():
    class RestrictModel(BaseModel):
        period: Optional[date]
        reason: Optional[str]

    command = CommandMk2('ban {period} {reason}', response_model=RestrictModel, response_model_name='vars')
    response = await command.__call__(
        Message(
            message_id=1,
            chat=Chat(
                id=1,
                type='private',
            ),
            text='/ban 2022-10-22',
            date=datetime.now(),
        ),
        MockedBot(),
    )
    command_obj: CommandObject = response.get('command')
    assert command_obj.command == 'ban'
    assert command_obj.mentioned is False
    assert response.get('period')
    assert response.get('reason') is None


@pytest.mark.asyncio
async def test_no_variables():
    class RestrictModel(BaseModel):
        period: Optional[date]
        reason: Optional[str]

    command = CommandMk2('ban {period} {reason}', response_model=RestrictModel, response_model_name='vars')
    response = await command.__call__(
        Message(
            message_id=1,
            chat=Chat(
                id=1,
                type='private',
            ),
            text='/ban',
            date=datetime.now(),
        ),
        MockedBot(),
    )
    command_obj: CommandObject = response.get('command')
    assert command_obj.command == 'ban'
    assert command_obj.mentioned is False
    assert response.get('period') is None
    assert response.get('reason') is None
