# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/mrp/protobuf/GetKeyboardSessionMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/mrp/protobuf/GetKeyboardSessionMessage.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n2pyatv/mrp/protobuf/GetKeyboardSessionMessage.proto\x1a(pyatv/mrp/protobuf/ProtocolMessage.proto:3\n\x19getKeyboardSessionMessage\x12\x10.ProtocolMessage\x18\x1d \x01(\t')
  ,
  dependencies=[pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.DESCRIPTOR,])


GETKEYBOARDSESSIONMESSAGE_FIELD_NUMBER = 29
getKeyboardSessionMessage = _descriptor.FieldDescriptor(
  name='getKeyboardSessionMessage', full_name='getKeyboardSessionMessage', index=0,
  number=29, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)

DESCRIPTOR.extensions_by_name['getKeyboardSessionMessage'] = getKeyboardSessionMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(getKeyboardSessionMessage)

# @@protoc_insertion_point(module_scope)
