# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: multi_list.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='multi_list.proto',
  package='Proto.Config',
  syntax='proto3',
  serialized_pb=b'\n\x10multi_list.proto\x12\x0cProto.Config\"\x91\x01\n\x16multilist_entry_object\x12\x0c\n\x04name\x18\x01 \x01(\t\x12<\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32..Proto.Config.multilist_entry_object.DataEntry\x1a+\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"T\n\x10multilist_object\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x32\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32$.Proto.Config.multilist_entry_objectB5\n net.ktc.miles.model.proto.configB\x0fMultiListObjectH\x01\x62\x06proto3'
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MULTILIST_ENTRY_OBJECT_DATAENTRY = _descriptor.Descriptor(
  name='DataEntry',
  full_name='Proto.Config.multilist_entry_object.DataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Proto.Config.multilist_entry_object.DataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Proto.Config.multilist_entry_object.DataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=180,
)

_MULTILIST_ENTRY_OBJECT = _descriptor.Descriptor(
  name='multilist_entry_object',
  full_name='Proto.Config.multilist_entry_object',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Proto.Config.multilist_entry_object.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='Proto.Config.multilist_entry_object.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MULTILIST_ENTRY_OBJECT_DATAENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=180,
)


_MULTILIST_OBJECT = _descriptor.Descriptor(
  name='multilist_object',
  full_name='Proto.Config.multilist_object',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Proto.Config.multilist_object.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='Proto.Config.multilist_object.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=182,
  serialized_end=266,
)

_MULTILIST_ENTRY_OBJECT_DATAENTRY.containing_type = _MULTILIST_ENTRY_OBJECT
_MULTILIST_ENTRY_OBJECT.fields_by_name['data'].message_type = _MULTILIST_ENTRY_OBJECT_DATAENTRY
_MULTILIST_OBJECT.fields_by_name['data'].message_type = _MULTILIST_ENTRY_OBJECT
DESCRIPTOR.message_types_by_name['multilist_entry_object'] = _MULTILIST_ENTRY_OBJECT
DESCRIPTOR.message_types_by_name['multilist_object'] = _MULTILIST_OBJECT

multilist_entry_object = _reflection.GeneratedProtocolMessageType('multilist_entry_object', (_message.Message,), dict(

  DataEntry = _reflection.GeneratedProtocolMessageType('DataEntry', (_message.Message,), dict(
    DESCRIPTOR = _MULTILIST_ENTRY_OBJECT_DATAENTRY,
    __module__ = 'multi_list_pb2'
    # @@protoc_insertion_point(class_scope:Proto.Config.multilist_entry_object.DataEntry)
    ))
  ,
  DESCRIPTOR = _MULTILIST_ENTRY_OBJECT,
  __module__ = 'multi_list_pb2'
  # @@protoc_insertion_point(class_scope:Proto.Config.multilist_entry_object)
  ))
_sym_db.RegisterMessage(multilist_entry_object)
_sym_db.RegisterMessage(multilist_entry_object.DataEntry)

multilist_object = _reflection.GeneratedProtocolMessageType('multilist_object', (_message.Message,), dict(
  DESCRIPTOR = _MULTILIST_OBJECT,
  __module__ = 'multi_list_pb2'
  # @@protoc_insertion_point(class_scope:Proto.Config.multilist_object)
  ))
_sym_db.RegisterMessage(multilist_object)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), b'\n net.ktc.miles.model.proto.configB\017MultiListObjectH\001')
_MULTILIST_ENTRY_OBJECT_DATAENTRY.has_options = True
_MULTILIST_ENTRY_OBJECT_DATAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001')
# @@protoc_insertion_point(module_scope)
