from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)


@api_view()
def root_route(request):
    """
    Endpoint for the root route of the API.

    :param request: The HTTP request object.
    :return: A Response containing a welcome message.
    """
    return Response({
        "message": "Welcome to the Chronosphere DRF API!"
    })


@api_view(['POST'])
def logout_route(request):
    """
    Endpoint for user logout.

    Clears the JWT authentication and refresh cookies.

    :param request: The HTTP request object.
    :return: A Response with cleared authentication cookies.
    """
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response
