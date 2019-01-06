import asyncio
import logging

from aioalice import Dispatcher

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)

# Provide your own skill_id and token!
SKILL_ID = '12a34567-c42d-9876-0e3f-123g55h12345'
OAUTH_TOKEN = 'OAuth AQAAAAABCDEFGHI_jklmnopqrstuvwxyz'

# You can create dp instance without auth: `dp = Dispatcher()`,
# but you'll have to provide it in request
dp = Dispatcher(skill_id=SKILL_ID, oauth_token=OAUTH_TOKEN)


async def check_uploaded_images():
    try:
        # Use `await dp.get_images(SKILL_ID, OAUTH_TOKEN)`
        # If tokens were not provided on dp's initialisation
        imgs = await dp.get_images()
    except Exception:
        logging.exception('Oops!')
    else:
        print(imgs)
    # You have to close session manually
    # if you called any request outside web app
    # Session close is added to on_shutdown list
    # in webhhok.configure_app
    await dp.close()


loop = asyncio.get_event_loop()
tasks = [loop.create_task(check_uploaded_images())]
wait_tasks = asyncio.wait(tasks)
loop.run_until_complete(wait_tasks)
loop.close()
