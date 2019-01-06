from aiohttp import web
from aioalice import Dispatcher, get_new_configured_app

WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 3001

dp_first = Dispatcher(name="first", path="/first")

dp_second = Dispatcher(name="second", path="/second")


@dp_first.request_handler()
async def handle_all_requests(alice_request):
    return alice_request.response('Привет! Я первый навык')


@dp_second.request_handler()
async def handle_all_requests(alice_request):
    return alice_request.response("Приятно познакомится, я второй навык")


if __name__ == '__main__':
    app = get_new_configured_app(dispatchers=[dp_first, dp_second])
    web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)
