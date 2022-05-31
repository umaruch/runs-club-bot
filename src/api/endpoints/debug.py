from aiohttp.web import Response, Request


async def hello_world(request: Request) -> Response:
    return Response(text="Hello, World")