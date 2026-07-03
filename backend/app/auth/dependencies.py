from fastapi import Depends, HTTPException, Request, status
from app.auth.models import CurrentUser
from app.auth.verifier import ClerkVerifier


async def get_current_user(
    request: Request,
) -> CurrentUser:

    try:
        return await ClerkVerifier.verify(request)

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )