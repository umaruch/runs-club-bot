from pydantic import BaseModel


class WebAppInitData(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str

class SigninForm(BaseModel):
    user: WebAppInitData
    new_username: str
