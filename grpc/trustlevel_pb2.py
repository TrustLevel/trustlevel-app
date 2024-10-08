# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trustlevel.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='trustlevel.proto',
  package='trustlevel',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10trustlevel.proto\x12\ntrustlevel\"\x1d\n\x05Input\x12\x14\n\x0cinput_string\x18\x01 \x01(\t\"1\n\nBiasOutput\x12\r\n\x05score\x18\x01 \x01(\x01\x12\x14\n\x0c\x65xplanations\x18\x02 \x03(\t2Q\n\x11ServiceDefinition\x12<\n\rdetermineBias\x12\x11.trustlevel.Input\x1a\x16.trustlevel.BiasOutput\"\x00\x62\x06proto3')
)




_INPUT = _descriptor.Descriptor(
  name='Input',
  full_name='trustlevel.Input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_string', full_name='trustlevel.Input.input_string', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=61,
)


_BIASOUTPUT = _descriptor.Descriptor(
  name='BiasOutput',
  full_name='trustlevel.BiasOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='score', full_name='trustlevel.BiasOutput.score', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='explanations', full_name='trustlevel.BiasOutput.explanations', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=112,
)

DESCRIPTOR.message_types_by_name['Input'] = _INPUT
DESCRIPTOR.message_types_by_name['BiasOutput'] = _BIASOUTPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Input = _reflection.GeneratedProtocolMessageType('Input', (_message.Message,), dict(
  DESCRIPTOR = _INPUT,
  __module__ = 'trustlevel_pb2'
  # @@protoc_insertion_point(class_scope:trustlevel.Input)
  ))
_sym_db.RegisterMessage(Input)

BiasOutput = _reflection.GeneratedProtocolMessageType('BiasOutput', (_message.Message,), dict(
  DESCRIPTOR = _BIASOUTPUT,
  __module__ = 'trustlevel_pb2'
  # @@protoc_insertion_point(class_scope:trustlevel.BiasOutput)
  ))
_sym_db.RegisterMessage(BiasOutput)



_SERVICEDEFINITION = _descriptor.ServiceDescriptor(
  name='ServiceDefinition',
  full_name='trustlevel.ServiceDefinition',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=114,
  serialized_end=195,
  methods=[
  _descriptor.MethodDescriptor(
    name='determineBias',
    full_name='trustlevel.ServiceDefinition.determineBias',
    index=0,
    containing_service=None,
    input_type=_INPUT,
    output_type=_BIASOUTPUT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICEDEFINITION)

DESCRIPTOR.services_by_name['ServiceDefinition'] = _SERVICEDEFINITION

# @@protoc_insertion_point(module_scope)
