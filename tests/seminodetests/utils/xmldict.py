# Copyright 2009-2011, wiredobjects - http://www.wiredobjects.eu
# All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Based on http://code.activestate.com/recipes/577442/ [BSD]


# import std
import unittest
# import third party
# import local
from seminode.utils.xmldict import XML2Dict


class XML2DictTest(unittest.TestCase):
    """
    To be written...
    """

    def test_xml_simple(self):
        """
        Test a simple xml structure
        """
        data = """<message>
            <sender>sendername</sender>
            <recipient>recipientname</recipient>
            <body>this is a message</body>
        </message>
        """
        result = XML2Dict().parse(data)
        self.assertIsInstance(result, dict)
        self.assertTrue(result.has_key('message'))
        self.assertIsInstance(result['message'], dict)
    
    def test_xml_empty_text(self):
        """
        Test a xml structure containing empty text tags
        """
        data = """<message>
            <sender></sender>
        </message>"""
        result = XML2Dict().parse(data)
        self.assertIsInstance(result, dict)
        self.assertTrue(result.has_key('message'))
        self.assertIsNone(result['message']['sender'])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(XML2DictTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
