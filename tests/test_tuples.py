from .utils import TranspileTestCase


class TupleTests(TranspileTestCase):
    def test_creation(self):
        self.assertBlock(
            python="""
                a = 1
                b = 2
                c = 3
                d = 4
                e = 5
                x = (a, b, c, d, e)
                """,
            java="""
                 Code (140 bytes)
                     Max stack: 5
                     Max locals: 6
                     Bytecode: (96 bytes)
                           0: <NEW org/python/Object>
                           3: <DUP>
                           4: <ICONST_1>
                           5: <INVOKESPECIAL org/python/Object.<init> (I)V>
                           8: <ASTORE_0>
                           9: <NEW org/python/Object>
                          12: <DUP>
                          13: <ICONST_2>
                          14: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          17: <ASTORE_1>
                          18: <NEW org/python/Object>
                          21: <DUP>
                          22: <ICONST_3>
                          23: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          26: <ASTORE_2>
                          27: <NEW org/python/Object>
                          30: <DUP>
                          31: <ICONST_4>
                          32: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          35: <ASTORE_3>
                          36: <NEW org/python/Object>
                          39: <DUP>
                          40: <ICONST_5>
                          41: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          44: <ASTORE 4>
                          46: <NEW org/python/Object>
                          49: <DUP>
                          50: <NEW java/util/ArrayList>
                          53: <DUP>
                          54: <ICONST_5>
                          55: <INVOKESPECIAL java/util/ArrayList.<init> (I)V>
                          58: <DUP>
                          59: <ALOAD_0>
                          60: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          63: <POP>
                          64: <DUP>
                          65: <ALOAD_1>
                          66: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          69: <POP>
                          70: <DUP>
                          71: <ALOAD_2>
                          72: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          75: <POP>
                          76: <DUP>
                          77: <ALOAD_3>
                          78: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          81: <POP>
                          82: <DUP>
                          83: <ALOAD 4>
                          85: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          88: <POP>
                          89: <INVOKESPECIAL org/python/Object.<init> (Ljava/util/ArrayList;)V>
                          92: <ASTORE 5>
                          94: <ACONST_NULL>
                          95: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (26 bytes)
                             Line numbers (6 total):
                                 0: 2
                                 9: 3
                                 18: 4
                                 27: 5
                                 36: 6
                                 59: 7
                """)

    def test_const_creation(self):
        self.assertBlock(
            python="""
                x = (1, 2, 3, 4, 5)
                """,
            java="""
                 Code (107 bytes)
                     Max stack: 7
                     Max locals: 1
                     Bytecode: (83 bytes)
                           0: <NEW org/python/Object>
                           3: <DUP>
                           4: <NEW java/util/ArrayList>
                           7: <DUP>
                           8: <ICONST_5>
                           9: <INVOKESPECIAL java/util/ArrayList.<init> (I)V>
                          12: <DUP>
                          13: <NEW org/python/Object>
                          16: <DUP>
                          17: <ICONST_1>
                          18: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          21: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          24: <POP>
                          25: <DUP>
                          26: <NEW org/python/Object>
                          29: <DUP>
                          30: <ICONST_2>
                          31: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          34: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          37: <POP>
                          38: <DUP>
                          39: <NEW org/python/Object>
                          42: <DUP>
                          43: <ICONST_3>
                          44: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          47: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          50: <POP>
                          51: <DUP>
                          52: <NEW org/python/Object>
                          55: <DUP>
                          56: <ICONST_4>
                          57: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          60: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          63: <POP>
                          64: <DUP>
                          65: <NEW org/python/Object>
                          68: <DUP>
                          69: <ICONST_5>
                          70: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          73: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          76: <POP>
                          77: <INVOKESPECIAL org/python/Object.<init> (Ljava/util/ArrayList;)V>
                          80: <ASTORE_0>
                          81: <ACONST_NULL>
                          82: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (6 bytes)
                             Line numbers (1 total):
                                 0: 2
                """)

    def test_getitem(self):
        self.assertBlock(
            python="""
                x = (1, 2)
                a = x[1]
                """,
            java="""
                 Code (85 bytes)
                     Max stack: 7
                     Max locals: 2
                     Bytecode: (57 bytes)
                           0: <NEW org/python/Object>
                           3: <DUP>
                           4: <NEW java/util/ArrayList>
                           7: <DUP>
                           8: <ICONST_2>
                           9: <INVOKESPECIAL java/util/ArrayList.<init> (I)V>
                          12: <DUP>
                          13: <NEW org/python/Object>
                          16: <DUP>
                          17: <ICONST_1>
                          18: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          21: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          24: <POP>
                          25: <DUP>
                          26: <NEW org/python/Object>
                          29: <DUP>
                          30: <ICONST_2>
                          31: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          34: <INVOKEVIRTUAL java/util/ArrayList.add (Ljava/lang/Object;)Z>
                          37: <POP>
                          38: <INVOKESPECIAL org/python/Object.<init> (Ljava/util/ArrayList;)V>
                          41: <ASTORE_0>
                          42: <ALOAD_0>
                          43: <NEW org/python/Object>
                          46: <DUP>
                          47: <ICONST_1>
                          48: <INVOKESPECIAL org/python/Object.<init> (I)V>
                          51: <INVOKEVIRTUAL org/python/Object.__getitem__ (Lorg/python/Object;)Lorg/python/Object;>
                          54: <ASTORE_1>
                          55: <ACONST_NULL>
                          56: <ARETURN>
                     Exceptions: (0)
                     Attributes: (1)
                         LineNumberTable (10 bytes)
                             Line numbers (2 total):
                                 0: 2
                                 42: 3
                """)
