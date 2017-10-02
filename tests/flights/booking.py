import unittest
from app.setup import BaseTest


class BookingTest(BaseTest):
    def test_the_first_one(self):
        pass
        self.logger.info("Test 1")
        self.logger.warn("Test 1")
        self.logger.error("Test 1")
        self.logger.critical("Test 1")

    # def test_the_second_one(self):
    #     pass
    #     self.logger.info("Test 2")
    #     self.logger.warn("Test 2")
    #     self.logger.error("Test 2")
    #     self.logger.critical("Test 2")
    #
    # def test_the_third_one(self):
    #     pass
    #     self.logger.info("Test 3")
    #     self.logger.warn("Test 3")
    #     self.logger.error("Test 3")
    #     self.logger.critical("Test 3")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BookingTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
