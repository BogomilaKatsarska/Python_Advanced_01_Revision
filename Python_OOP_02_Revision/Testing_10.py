'''
Triple A pattern:
- Arrange
- Act
- Assert

def setUp(self):
    self.worker = Worker('Test', 100, 10)
'''


import unittest
# from unittest import TestCase, __main__



class SimpleTest(unittest.TestCase):
    def test_upper(self): #name of methods should start 'test_'
        result = 'foo'.upper()
        expected_result = 'FOO'
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()


class WorkerTest(unittest.TestCase):
    def test_worker_is_initialized_correctly(self):
        worker = Worker('Test', 100, 10)
        self.assertEqual('Test', worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money, msg='Money should be equal to money on init')

    def test_worker_energy_increased_after_rest(self):
        worker = Worker('Test', 100, 10)
        self.assertEqual(10, worker.energy)
        worker.rest()
        self.assertEqual(11, worker.energy)


    def test_worker_works_with_negative_energy_raises(self):
        worker = Worker('Test', 100, 0)
        worker.work()
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy,', str(ex.exception))


    def test_worker_money_is_increased_after_work(self):
        worker = Worker('Test', 100, 0)
        self.assertEqual(0, worker.money)
        worker.work()
        self.assertEqual(100, worker.money)

    def test_get_into(self):
        pass
