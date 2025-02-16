# automatically generated by the FlatBuffers compiler, do not modify

# namespace: zkinterface

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# A single R1CS constraint between variables.
#
# - Represents the linear combinations of variables A, B, C such that:
#       (A) * (B) = (C)
# - A linear combination is given as a sequence of (variable ID, coefficient).
class BilinearConstraint(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsBilinearConstraint(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BilinearConstraint()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def BilinearConstraintBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x7A\x6B\x69\x66", size_prefixed=size_prefixed)

    # BilinearConstraint
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # BilinearConstraint
    def LinearCombinationA(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from zkinterface.Variables import Variables
            obj = Variables()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # BilinearConstraint
    def LinearCombinationB(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from zkinterface.Variables import Variables
            obj = Variables()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # BilinearConstraint
    def LinearCombinationC(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from zkinterface.Variables import Variables
            obj = Variables()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def BilinearConstraintStart(builder): builder.StartObject(3)
def BilinearConstraintAddLinearCombinationA(builder, linearCombinationA): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(linearCombinationA), 0)
def BilinearConstraintAddLinearCombinationB(builder, linearCombinationB): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(linearCombinationB), 0)
def BilinearConstraintAddLinearCombinationC(builder, linearCombinationC): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(linearCombinationC), 0)
def BilinearConstraintEnd(builder): return builder.EndObject()
