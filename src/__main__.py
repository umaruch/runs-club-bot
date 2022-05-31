from aiohttp import web

from src.core.builder import build_application


if __name__ == "__main__":
    web.run_app(build_application())