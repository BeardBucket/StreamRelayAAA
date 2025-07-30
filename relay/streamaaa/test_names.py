from unittest import TestCase
from .names import generate_name_f

class Test(TestCase):
    def test_generate_name_f(self):
        CNT=5
        tnames=generate_name_f(num=CNT)()
        self.assertTrue(isinstance(tnames, str))
        count=0
        for tname in tnames:
            if tname[0].isupper():
                count+=1
        self.assertEqual(count,CNT)
