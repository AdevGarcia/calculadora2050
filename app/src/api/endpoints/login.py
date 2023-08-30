from datetime import timedelta
from typing import Any
from pydantic.networks import EmailStr
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.src.modules.token import schemas as schemas_token
from app.src.modules.user import schemas as schemas_user
from app.src.modules.msg import schemas as schemas_msg
from app.src.modules.user import models as models_user

from app.src.crud.crud_user import user as crud_user

from app.src.db import deps
from app.src.core import security
from app.src.core.config import settings
from app.src.core.security import get_password_hash
from app.src.utils import verify_password_reset_token

router = APIRouter()


@router.post("/login/access-token", response_model=schemas_token.Token)
def login_access_token(
    db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = crud_user.authenticate(
        db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not crud_user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.post("/login/create-user", response_model=schemas_user.User)
def create_user_profile(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(...),
    email: EmailStr = Body(...),
    full_name: str = Body(None),
) -> Any:
    """
    Create new user without the need to be logged in.
    """
    user = crud_user.get_by_email(db, email=email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="This username is not available.",
        )
    # Create user auth
    user_in = schemas_user.UserCreateUpdate(password=password, email=email, full_name=full_name)
    user = crud_user.create(db, obj_in=user_in)
    return user


@router.post("/login/test-token", response_model=schemas_user.User)
def test_token(current_user: models_user.User = Depends(deps.get_current_user)) -> Any:
    """
    Test access token
    """
    return current_user


# @router.post("/password-recovery/{email}", response_model=schemas_msg.Msg)
# def recover_password(email: str, db: Session = Depends(deps.get_db)) -> Any:
#     """
#     Password Recovery
#     """
#     user = crud_user.get_by_email(db, email=email)

#     if not user:
#         raise HTTPException(
#             status_code=404,
#             detail="The user with this username does not exist in the system.",
#         )
#     password_reset_token = generate_password_reset_token(email=email)
#     send_reset_password_email(
#         email_to=user.email, email=email, token=password_reset_token
#     )
#     return {"msg": "Password recovery email sent"}


@router.post("/reset-password/", response_model=schemas_msg.Msg)
def reset_password(
    token: str = Body(...),
    new_password: str = Body(...),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Reset password
    """
    email = verify_password_reset_token(token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = crud_user.get_by_email(db, email=email)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system.",
        )
    elif not crud_user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    hashed_password = get_password_hash(new_password)
    user.hashed_password = hashed_password
    db.add(user)
    db.commit()
    return {"msg": "Password updated successfully"}


# @router.get("/tester", response_model=schemas_msg.Msg)
# def test_endpoint() -> Any:
#     """
#     Test current endpoint.
#     """
#     return {"msg": "Message returned ok."}
