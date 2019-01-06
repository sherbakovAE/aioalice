from aioalice.dispatcher import UnQliteStorage
from unqlite import UnQLite
import unittest

db = UnQLite()

ID = "faes3245kj345hk"
TEST_DATA = {"state": "DEFAULT", "data": {"hand": 1}}


class TestUnQliteStorage(unittest.TestCase):
    def test_store(self):
        db[ID] = TEST_DATA
        self.assertEqual(UnQliteStorage.repair_from_store(db[ID]), TEST_DATA)

    def test_search(self):
        self.assertEqual(db.exists(ID), False)
        db[ID] = TEST_DATA
        self.assertEqual(db.exists(ID), True)


if __name__ == '__main__':
    unittest.main()
