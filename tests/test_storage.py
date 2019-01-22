from aioalice.dispatcher import SqliteStorage
import unittest
import aiounittest
from datetime import datetime

sd = SqliteStorage()

USER_ID = "faes3245kj345hk"
TEST_DATA = {"state": "DEFAULT", "data": {"hand": 1, "check": False, "start": datetime.now()}}


class TestSqliteDictStorage(aiounittest.AsyncTestCase):
    async def test_store(self):
        sd.data[USER_ID] = TEST_DATA
        self.assertEqual(sd.data[USER_ID], TEST_DATA)

    async def test_delete(self):
        sd.data[USER_ID] = TEST_DATA
        await sd.delete(USER_ID)
        self.assertEqual(USER_ID in sd.data, False)

    async def test_state(self):
        await sd.set_state(USER_ID, TEST_DATA['state'])
        self.assertEqual(await sd.get_state(USER_ID), TEST_DATA['state'])

    async def test_data(self):
        await sd.set_data(USER_ID, TEST_DATA['data'])
        self.assertEqual(await sd.get_data(USER_ID), TEST_DATA['data'])


if __name__ == '__main__':
    unittest.main()
