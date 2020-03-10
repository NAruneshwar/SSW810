import unittest
from HW06_Arun_Nalluri import SortedQueue

class SortedQueueTest(unittest.TestCase):
    def test(self):
        q = SortedQueue()
        self.assertIsNone(q.next())
        q.add("Nanda")
        self.assertEqual(str(q), "Nanda")
        q.add("Alejandra")
        self.assertEqual(str(q), "Alejandra, Nanda")
        q.add("Maha")
        self.assertEqual(str(q), "Alejandra, Maha, Nanda")
        self.assertEqual(q.next(), "Alejandra")
        self.assertEqual(q.next(), "Maha")
        self.assertEqual(q.next(), "Nanda")
        self.assertIsNone(q.next())

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2) 
