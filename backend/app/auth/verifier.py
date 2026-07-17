import os
from fastapi import Request
from clerk_backend_api import Clerk
from clerk_backend_api.security.types import AuthenticateRequestOptions
from app.auth.models import CurrentUser
from app.core.config import CLERK_SECRET_KEY

clerk = Clerk(
    bearer_auth=CLERK_SECRET_KEY,
)

options = AuthenticateRequestOptions(
    authorized_parties=[
        "http://localhost:3000",
        "https://multi-agent-financial-intelligence.vercel.app",
    ]
)

class ClerkVerifier:

    @staticmethod
    async def verify(
        request: Request,
    ) -> CurrentUser:

        request_state = clerk.authenticate_request(
            request=request,
            options=options,
        )

        if not request_state.is_signed_in:
            raise Exception("Unauthorized")

        return CurrentUser(
            id=request_state.payload["sub"],
            email=request_state.payload.get("email"),
        )
