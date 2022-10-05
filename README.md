### Filter CommandMk2 Aiogram 3

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

---

Improved command filter

```python
class RestrictModel(BaseModel):
    period: date
    reason: Optional[str]


@router.message(CommandMk2('ban {period} {reason}', response_model=RestrictModel, response_model_name='vars'))
async def ban_user(message: Message, period: date, reason: Optional[str]):
    ...
```

Diff:

- Command arguments parsing, not just leaving single string like built-in aiogram filter
- Command arguments separation and validation using Pydantic model.
