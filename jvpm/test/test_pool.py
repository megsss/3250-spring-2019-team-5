from unittest import TestCase
from jvpm.parsing.Parser import *
class TestPool(TestCase):
    def test_pool(self):
        p = Parser(b'\xca\xfe\xba\xbe\x00\x00\x004\x00"\n\x00\n\x00\x13\x06@\x13\xe1G\xae\x14z\xe1\x05\x00\x00\x00\x00\x00\x01\xe2@\t\x00\x14\x00\x15\n\x00\x16\x00\x17\n\x00\x16\x00\x18\x07\x00\x19\x07\x00\x1a\x01\x00\x06<init>\x01\x00\x03()V\x01\x00\x04Code\x01\x00\x0fLineNumberTable\x01\x00\x04main\x01\x00\x16([Ljava/lang/String;)V\x01\x00\nSourceFile\x01\x00\x0bDouble.java\x0c\x00\x0b\x00\x0c\x07\x00\x1b\x0c\x00\x1c\x00\x1d\x07\x00\x1e\x0c\x00\x1f\x00 \x0c\x00\x1f\x00!\x01\x00\x06Double\x01\x00\x10java/lang/Object\x01\x00\x10java/lang/System\x01\x00\x03out\x01\x00\x15Ljava/io/PrintStream;\x01\x00\x13java/io/PrintStream\x01\x00\x07println\x01\x00\x04(D)V\x01\x00\x04(J)V\x00!\x00\t\x00\n\x00\x00\x00\x00\x00\x02\x00\x01\x00\x0b\x00\x0c\x00\x01\x00\r\x00\x00\x00\x1d\x00\x01\x00\x01\x00\x00\x00\x05*\xb7\x00\x01\xb1\x00\x00\x00\x01\x00\x0e\x00\x00\x00\x06\x00\x01\x00\x00\x00\x01\x00\t\x00\x0f\x00\x10\x00\x01\x00\r\x00\x00\x00?\x00\x03\x00\x05\x00\x00\x00\x17\x14\x00\x02H\x14\x00\x04B\xb2\x00\x06\'\xb6\x00\x07\xb2\x00\x06!\xb6\x00\x08\xb1\x00\x00\x00\x01\x00\x0e\x00\x00\x00\x16\x00\x05\x00\x00\x00\x05\x00\x04\x00\x06\x00\x08\x00\x07\x00\x0f\x00\x08\x00\x16\x00\t\x00\x01\x00\x11\x00\x00\x00\x02\x00\x12')
        p.get_magic()
        p.get_minor_version()
        p.get_major_version()
        p.get_constant_pool_count()
        p.get_all_constants()
        self.assertEqual(len(p.jvm.constant_pool),34)