# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spbt_config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import probe_engine_config_pb2 as probe__engine__config__pb2
import mobile_app_config_pb2 as mobile__app__config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='spbt_config.proto',
  package='Proto.Config',
  syntax='proto3',
  serialized_pb=b'\n\x11spbt_config.proto\x12\x0cProto.Config\x1a\x19probe_engine_config.proto\x1a\x17mobile_app_config.proto\"\x83\x01\n\x12\x61pplication_config\x12\x38\n\rengine_config\x18\x01 \x01(\x0b\x32!.Proto.Config.probe_engine_config\x12\x33\n\napp_config\x18\x02 \x01(\x0b\x32\x1f.Proto.Config.mobile_app_configB7\n net.ktc.miles.model.proto.configB\x11\x41pplicationConfigH\x01\x62\x06proto3'
  ,
  dependencies=[probe__engine__config__pb2.DESCRIPTOR,mobile__app__config__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_APPLICATION_CONFIG = _descriptor.Descriptor(
  name='application_config',
  full_name='Proto.Config.application_config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='engine_config', full_name='Proto.Config.application_config.engine_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_config', full_name='Proto.Config.application_config.app_config', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=219,
)

_APPLICATION_CONFIG.fields_by_name['engine_config'].message_type = probe__engine__config__pb2._PROBE_ENGINE_CONFIG
_APPLICATION_CONFIG.fields_by_name['app_config'].message_type = mobile__app__config__pb2._MOBILE_APP_CONFIG
DESCRIPTOR.message_types_by_name['application_config'] = _APPLICATION_CONFIG

application_config = _reflection.GeneratedProtocolMessageType('application_config', (_message.Message,), dict(
  DESCRIPTOR = _APPLICATION_CONFIG,
  __module__ = 'spbt_config_pb2'
  # @@protoc_insertion_point(class_scope:Proto.Config.application_config)
  ))
_sym_db.RegisterMessage(application_config)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), b'\n net.ktc.miles.model.proto.configB\021ApplicationConfigH\001')
# @@protoc_insertion_point(module_scope)