# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/mrp/protobuf/KeyboardMessage.proto

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
from pyatv.mrp.protobuf import TextEditingAttributes_pb2 as pyatv_dot_mrp_dot_protobuf_dot_TextEditingAttributes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/mrp/protobuf/KeyboardMessage.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n(pyatv/mrp/protobuf/KeyboardMessage.proto\x1a(pyatv/mrp/protobuf/ProtocolMessage.proto\x1a.pyatv/mrp/protobuf/TextEditingAttributes.proto\"L\n\x0fKeyboardMessage\x12\r\n\x05state\x18\x01 \x01(\x05\x12*\n\nattributes\x18\x03 \x01(\x0b\x32\x16.TextEditingAttributes:;\n\x0fkeyboardMessage\x12\x10.ProtocolMessage\x18\x1c \x01(\x0b\x32\x10.KeyboardMessage')
  ,
  dependencies=[pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.DESCRIPTOR,pyatv_dot_mrp_dot_protobuf_dot_TextEditingAttributes__pb2.DESCRIPTOR,])


KEYBOARDMESSAGE_FIELD_NUMBER = 28
keyboardMessage = _descriptor.FieldDescriptor(
  name='keyboardMessage', full_name='keyboardMessage', index=0,
  number=28, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_KEYBOARDMESSAGE = _descriptor.Descriptor(
  name='KeyboardMessage',
  full_name='KeyboardMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='KeyboardMessage.state', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='KeyboardMessage.attributes', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=210,
)

_KEYBOARDMESSAGE.fields_by_name['attributes'].message_type = pyatv_dot_mrp_dot_protobuf_dot_TextEditingAttributes__pb2._TEXTEDITINGATTRIBUTES
DESCRIPTOR.message_types_by_name['KeyboardMessage'] = _KEYBOARDMESSAGE
DESCRIPTOR.extensions_by_name['keyboardMessage'] = keyboardMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeyboardMessage = _reflection.GeneratedProtocolMessageType('KeyboardMessage', (_message.Message,), dict(
  DESCRIPTOR = _KEYBOARDMESSAGE,
  __module__ = 'pyatv.mrp.protobuf.KeyboardMessage_pb2'
  # @@protoc_insertion_point(class_scope:KeyboardMessage)
  ))
_sym_db.RegisterMessage(KeyboardMessage)

keyboardMessage.message_type = _KEYBOARDMESSAGE
pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(keyboardMessage)

# @@protoc_insertion_point(module_scope)
