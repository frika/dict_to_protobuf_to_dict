# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sample.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sample.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0csample.proto\"\xd9\x03\n\x0bMainMessage\x12\r\n\x05\x61_str\x18\x01 \x01(\t\x12>\n\x13int_to_lst_ints_map\x18\x02 \x03(\x0b\x32!.MainMessage.IntToLstIntsMapEntry\x12\x1a\n\x07\x61n_enum\x18\x03 \x01(\x0e\x32\t.SomeEnum\x12\x0e\n\x06\x61n_int\x18\x04 \x01(\x05\x12\x10\n\x08lst_ints\x18\x05 \x03(\x05\x12=\n\x12str_to_message_map\x18\x06 \x03(\x0b\x32!.MainMessage.StrToMessageMapEntry\x12\x35\n\x0estr_to_int_map\x18\x07 \x03(\x0b\x32\x1d.MainMessage.StrToIntMapEntry\x1aJ\n\x14IntToLstIntsMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.ListOfIntsMessage:\x02\x38\x01\x1aG\n\x14StrToMessageMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.SomeSubMessage:\x02\x38\x01\x1a\x32\n\x10StrToIntMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"B\n\x0eSomeSubMessage\x12\r\n\x05\x61_str\x18\x01 \x01(\t\x12\x0e\n\x06\x61_long\x18\x02 \x01(\x03\x12\x11\n\tlst_longs\x18\x03 \x03(\x03\"%\n\x11ListOfIntsMessage\x12\x10\n\x08lst_ints\x18\x01 \x03(\x05*!\n\x08SomeEnum\x12\t\n\x05\x66irst\x10\x00\x12\n\n\x06second\x10\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_SOMEENUM = _descriptor.EnumDescriptor(
  name='SomeEnum',
  full_name='SomeEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='first', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='second', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=599,
  serialized_end=632,
)
_sym_db.RegisterEnumDescriptor(_SOMEENUM)

SomeEnum = enum_type_wrapper.EnumTypeWrapper(_SOMEENUM)
first = 0
second = 1



_MAINMESSAGE_INTTOLSTINTSMAPENTRY = _descriptor.Descriptor(
  name='IntToLstIntsMapEntry',
  full_name='MainMessage.IntToLstIntsMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='MainMessage.IntToLstIntsMapEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='MainMessage.IntToLstIntsMapEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=291,
  serialized_end=365,
)

_MAINMESSAGE_STRTOMESSAGEMAPENTRY = _descriptor.Descriptor(
  name='StrToMessageMapEntry',
  full_name='MainMessage.StrToMessageMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='MainMessage.StrToMessageMapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='MainMessage.StrToMessageMapEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=367,
  serialized_end=438,
)

_MAINMESSAGE_STRTOINTMAPENTRY = _descriptor.Descriptor(
  name='StrToIntMapEntry',
  full_name='MainMessage.StrToIntMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='MainMessage.StrToIntMapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='MainMessage.StrToIntMapEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=440,
  serialized_end=490,
)

_MAINMESSAGE = _descriptor.Descriptor(
  name='MainMessage',
  full_name='MainMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a_str', full_name='MainMessage.a_str', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int_to_lst_ints_map', full_name='MainMessage.int_to_lst_ints_map', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='an_enum', full_name='MainMessage.an_enum', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='an_int', full_name='MainMessage.an_int', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lst_ints', full_name='MainMessage.lst_ints', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='str_to_message_map', full_name='MainMessage.str_to_message_map', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='str_to_int_map', full_name='MainMessage.str_to_int_map', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MAINMESSAGE_INTTOLSTINTSMAPENTRY, _MAINMESSAGE_STRTOMESSAGEMAPENTRY, _MAINMESSAGE_STRTOINTMAPENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=490,
)


_SOMESUBMESSAGE = _descriptor.Descriptor(
  name='SomeSubMessage',
  full_name='SomeSubMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a_str', full_name='SomeSubMessage.a_str', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='a_long', full_name='SomeSubMessage.a_long', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lst_longs', full_name='SomeSubMessage.lst_longs', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=492,
  serialized_end=558,
)


_LISTOFINTSMESSAGE = _descriptor.Descriptor(
  name='ListOfIntsMessage',
  full_name='ListOfIntsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lst_ints', full_name='ListOfIntsMessage.lst_ints', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=560,
  serialized_end=597,
)

_MAINMESSAGE_INTTOLSTINTSMAPENTRY.fields_by_name['value'].message_type = _LISTOFINTSMESSAGE
_MAINMESSAGE_INTTOLSTINTSMAPENTRY.containing_type = _MAINMESSAGE
_MAINMESSAGE_STRTOMESSAGEMAPENTRY.fields_by_name['value'].message_type = _SOMESUBMESSAGE
_MAINMESSAGE_STRTOMESSAGEMAPENTRY.containing_type = _MAINMESSAGE
_MAINMESSAGE_STRTOINTMAPENTRY.containing_type = _MAINMESSAGE
_MAINMESSAGE.fields_by_name['int_to_lst_ints_map'].message_type = _MAINMESSAGE_INTTOLSTINTSMAPENTRY
_MAINMESSAGE.fields_by_name['an_enum'].enum_type = _SOMEENUM
_MAINMESSAGE.fields_by_name['str_to_message_map'].message_type = _MAINMESSAGE_STRTOMESSAGEMAPENTRY
_MAINMESSAGE.fields_by_name['str_to_int_map'].message_type = _MAINMESSAGE_STRTOINTMAPENTRY
DESCRIPTOR.message_types_by_name['MainMessage'] = _MAINMESSAGE
DESCRIPTOR.message_types_by_name['SomeSubMessage'] = _SOMESUBMESSAGE
DESCRIPTOR.message_types_by_name['ListOfIntsMessage'] = _LISTOFINTSMESSAGE
DESCRIPTOR.enum_types_by_name['SomeEnum'] = _SOMEENUM

MainMessage = _reflection.GeneratedProtocolMessageType('MainMessage', (_message.Message,), dict(

  IntToLstIntsMapEntry = _reflection.GeneratedProtocolMessageType('IntToLstIntsMapEntry', (_message.Message,), dict(
    DESCRIPTOR = _MAINMESSAGE_INTTOLSTINTSMAPENTRY,
    __module__ = 'sample_pb2'
    # @@protoc_insertion_point(class_scope:MainMessage.IntToLstIntsMapEntry)
    ))
  ,

  StrToMessageMapEntry = _reflection.GeneratedProtocolMessageType('StrToMessageMapEntry', (_message.Message,), dict(
    DESCRIPTOR = _MAINMESSAGE_STRTOMESSAGEMAPENTRY,
    __module__ = 'sample_pb2'
    # @@protoc_insertion_point(class_scope:MainMessage.StrToMessageMapEntry)
    ))
  ,

  StrToIntMapEntry = _reflection.GeneratedProtocolMessageType('StrToIntMapEntry', (_message.Message,), dict(
    DESCRIPTOR = _MAINMESSAGE_STRTOINTMAPENTRY,
    __module__ = 'sample_pb2'
    # @@protoc_insertion_point(class_scope:MainMessage.StrToIntMapEntry)
    ))
  ,
  DESCRIPTOR = _MAINMESSAGE,
  __module__ = 'sample_pb2'
  # @@protoc_insertion_point(class_scope:MainMessage)
  ))
_sym_db.RegisterMessage(MainMessage)
_sym_db.RegisterMessage(MainMessage.IntToLstIntsMapEntry)
_sym_db.RegisterMessage(MainMessage.StrToMessageMapEntry)
_sym_db.RegisterMessage(MainMessage.StrToIntMapEntry)

SomeSubMessage = _reflection.GeneratedProtocolMessageType('SomeSubMessage', (_message.Message,), dict(
  DESCRIPTOR = _SOMESUBMESSAGE,
  __module__ = 'sample_pb2'
  # @@protoc_insertion_point(class_scope:SomeSubMessage)
  ))
_sym_db.RegisterMessage(SomeSubMessage)

ListOfIntsMessage = _reflection.GeneratedProtocolMessageType('ListOfIntsMessage', (_message.Message,), dict(
  DESCRIPTOR = _LISTOFINTSMESSAGE,
  __module__ = 'sample_pb2'
  # @@protoc_insertion_point(class_scope:ListOfIntsMessage)
  ))
_sym_db.RegisterMessage(ListOfIntsMessage)


_MAINMESSAGE_INTTOLSTINTSMAPENTRY.has_options = True
_MAINMESSAGE_INTTOLSTINTSMAPENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_MAINMESSAGE_STRTOMESSAGEMAPENTRY.has_options = True
_MAINMESSAGE_STRTOMESSAGEMAPENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_MAINMESSAGE_STRTOINTMAPENTRY.has_options = True
_MAINMESSAGE_STRTOINTMAPENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)