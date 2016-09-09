# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: road_feature.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import actions_pb2 as actions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='road_feature.proto',
  package='Proto.JSON',
  syntax='proto3',
  serialized_pb=b'\n\x12road_feature.proto\x12\nProto.JSON\x1a\ractions.proto\"\x98\x07\n\x0croad_feature\x12\x41\n\x0broadFeature\x18\x01 \x01(\x0b\x32,.Proto.JSON.road_feature.road_feature_object\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x39\n\x08\x66\x65\x61tures\x18\x03 \x03(\x0b\x32\'.Proto.JSON.road_feature.feature_object\x1aL\n\x13road_feature_object\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x11\n\tvalidFrom\x18\x02 \x01(\t\x12\x11\n\talgorithm\x18\x03 \x01(\t\x1a\xad\x05\n\x0e\x66\x65\x61ture_object\x12\x0c\n\x04type\x18\x01 \x01(\t\x12I\n\x08geometry\x18\x02 \x01(\x0b\x32\x37.Proto.JSON.road_feature.feature_object.geometry_object\x12K\n\nproperties\x18\x03 \x01(\x0b\x32\x37.Proto.JSON.road_feature.feature_object.property_object\x1a\xae\x01\n\x0fgeometry_object\x12\x0c\n\x04type\x18\x01 \x01(\t\x12^\n\x0b\x63oordinates\x18\x02 \x03(\x0b\x32I.Proto.JSON.road_feature.feature_object.geometry_object.coordinate_object\x1a-\n\x11\x63oordinate_object\x12\x0b\n\x03lat\x18\x01 \x01(\x01\x12\x0b\n\x03lon\x18\x02 \x01(\x01\x1a\xc3\x02\n\x0fproperty_object\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65vent\x18\x03 \x01(\t\x12\x11\n\tdirection\x18\x04 \x01(\x05\x12\x0c\n\x04type\x18\x05 \x01(\x05\x12\x12\n\nconfidence\x18\x06 \x01(\x02\x12\x16\n\x0e\x62othdirections\x18\x07 \x01(\x05\x12\x14\n\x0ctriggerIndex\x18\x08 \x01(\x05\x12\x10\n\x08required\x18\t \x01(\x08\x12\x15\n\rfeatureZoneId\x18\n \x01(\x05\x12\x18\n\x10maxDetectionTime\x18\x0b \x01(\x05\x12 \n\x18\x64\x65tectionUpdateIntervall\x18\x0c \x01(\x05\x12\x13\n\x0bmaxDistance\x18\r \x01(\x05\x12*\n\x07\x61\x63tions\x18\x0e \x03(\x0b\x32\x19.Proto.JSON.action_objectB3\n\x1enet.ktc.miles.model.proto.JSONB\x0fRoadFeatureJSONH\x01\x62\x06proto3'
  ,
  dependencies=[actions__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ROAD_FEATURE_ROAD_FEATURE_OBJECT = _descriptor.Descriptor(
  name='road_feature_object',
  full_name='Proto.JSON.road_feature.road_feature_object',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='Proto.JSON.road_feature.road_feature_object.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='validFrom', full_name='Proto.JSON.road_feature.road_feature_object.validFrom', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='Proto.JSON.road_feature.road_feature_object.algorithm', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=206,
  serialized_end=282,
)

_ROAD_FEATURE_FEATURE_OBJECT_GEOMETRY_OBJECT_COORDINATE_OBJECT = _descriptor.Descriptor(
  name='coordinate_object',
  full_name='Proto.JSON.road_feature.feature_object.geometry_object.coordinate_object',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lat', full_name='Proto.JSON.road_feature.feature_object.geometry_object.coordinate_object.lat', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lon', full_name='Proto.JSON.road_feature.feature_object.geometry_object.coordinate_object.lon', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=599,
  serialized_end=644,
)

_ROAD_FEATURE_FEATURE_OBJECT_GEOMETRY_OBJECT = _descriptor.Descriptor(
  name='geometry_object',
  full_name='Proto.JSON.road_feature.feature_object.geometry_object',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Proto.JSON.road_feature.feature_object.geometry_object.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coordinates', full_name='Proto.JSON.road_feature.feature_object.geometry_object.coordinates', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ROAD_FEATURE_FEATURE_OBJECT_GEOMETRY_OBJECT_COORDINATE_OBJECT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=470,
  serialized_end=644,
)

_ROAD_FEATURE_FEATURE_OBJECT_PROPERTY_OBJECT = _descriptor.Descriptor(
  name='property_object',
  full_name='Proto.JSON.road_feature.feature_object.property_object',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Proto.JSON.road_feature.feature_object.property_object.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Proto.JSON.road_feature.feature_object.property_object.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event', full_name='Proto.JSON.road_feature.feature_object.property_object.event', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='direction', full_name='Proto.JSON.road_feature.feature_object.property_object.direction', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Proto.JSON.road_feature.feature_object.property_object.type', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='Proto.JSON.road_feature.feature_object.property_object.confidence', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bothdirections', full_name='Proto.JSON.road_feature.feature_object.property_object.bothdirections', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='triggerIndex', full_name='Proto.JSON.road_feature.feature_object.property_object.triggerIndex', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='required', full_name='Proto.JSON.road_feature.feature_object.property_object.required', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='featureZoneId', full_name='Proto.JSON.road_feature.feature_object.property_object.featureZoneId', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maxDetectionTime', full_name='Proto.JSON.road_feature.feature_object.property_object.maxDetectionTime', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='detectionUpdateIntervall', full_name='Proto.JSON.road_feature.feature_object.property_object.detectionUpdateIntervall', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maxDistance', full_name='Proto.JSON.road_feature.feature_object.property_object.maxDistance', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='actions', full_name='Proto.JSON.road_feature.feature_object.property_object.actions', index=13,
      number=14, type=11, cpp_type=10, label=3,
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
  serialized_start=647,
  serialized_end=970,
)

_ROAD_FEATURE_FEATURE_OBJECT = _descriptor.Descriptor(
  name='feature_object',
  full_name='Proto.JSON.road_feature.feature_object',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Proto.JSON.road_feature.feature_object.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='geometry', full_name='Proto.JSON.road_feature.feature_object.geometry', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='properties', full_name='Proto.JSON.road_feature.feature_object.properties', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ROAD_FEATURE_FEATURE_OBJECT_GEOMETRY_OBJECT, _ROAD_FEATURE_FEATURE_OBJECT_PROPERTY_OBJECT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=285,
  serialized_end=970,
)

_ROAD_FEATURE = _descriptor.Descriptor(
  name='road_feature',
  full_name='Proto.JSON.road_feature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roadFeature', full_name='Proto.JSON.road_feature.roadFeature', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Proto.JSON.road_feature.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='features', full_name='Proto.JSON.road_feature.features', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ROAD_FEATURE_ROAD_FEATURE_OBJECT, _ROAD_FEATURE_FEATURE_OBJECT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=970,
)

_ROAD_FEATURE_ROAD_FEATURE_OBJECT.containing_type = _ROAD_FEATURE
_ROAD_FEATURE_FEATURE_OBJECT_GEOMETRY_OBJECT_COORDINATE_OBJECT.containing_type = _ROAD_FEATURE_FEATURE_OBJECT_GEOMETRY_OBJECT
_ROAD_FEATURE_FEATURE_OBJECT_GEOMETRY_OBJECT.fields_by_name['coordinates'].message_type = _ROAD_FEATURE_FEATURE_OBJECT_GEOMETRY_OBJECT_COORDINATE_OBJECT
_ROAD_FEATURE_FEATURE_OBJECT_GEOMETRY_OBJECT.containing_type = _ROAD_FEATURE_FEATURE_OBJECT
_ROAD_FEATURE_FEATURE_OBJECT_PROPERTY_OBJECT.fields_by_name['actions'].message_type = actions__pb2._ACTION_OBJECT
_ROAD_FEATURE_FEATURE_OBJECT_PROPERTY_OBJECT.containing_type = _ROAD_FEATURE_FEATURE_OBJECT
_ROAD_FEATURE_FEATURE_OBJECT.fields_by_name['geometry'].message_type = _ROAD_FEATURE_FEATURE_OBJECT_GEOMETRY_OBJECT
_ROAD_FEATURE_FEATURE_OBJECT.fields_by_name['properties'].message_type = _ROAD_FEATURE_FEATURE_OBJECT_PROPERTY_OBJECT
_ROAD_FEATURE_FEATURE_OBJECT.containing_type = _ROAD_FEATURE
_ROAD_FEATURE.fields_by_name['roadFeature'].message_type = _ROAD_FEATURE_ROAD_FEATURE_OBJECT
_ROAD_FEATURE.fields_by_name['features'].message_type = _ROAD_FEATURE_FEATURE_OBJECT
DESCRIPTOR.message_types_by_name['road_feature'] = _ROAD_FEATURE

road_feature = _reflection.GeneratedProtocolMessageType('road_feature', (_message.Message,), dict(

  road_feature_object = _reflection.GeneratedProtocolMessageType('road_feature_object', (_message.Message,), dict(
    DESCRIPTOR = _ROAD_FEATURE_ROAD_FEATURE_OBJECT,
    __module__ = 'road_feature_pb2'
    # @@protoc_insertion_point(class_scope:Proto.JSON.road_feature.road_feature_object)
    ))
  ,

  feature_object = _reflection.GeneratedProtocolMessageType('feature_object', (_message.Message,), dict(

    geometry_object = _reflection.GeneratedProtocolMessageType('geometry_object', (_message.Message,), dict(

      coordinate_object = _reflection.GeneratedProtocolMessageType('coordinate_object', (_message.Message,), dict(
        DESCRIPTOR = _ROAD_FEATURE_FEATURE_OBJECT_GEOMETRY_OBJECT_COORDINATE_OBJECT,
        __module__ = 'road_feature_pb2'
        # @@protoc_insertion_point(class_scope:Proto.JSON.road_feature.feature_object.geometry_object.coordinate_object)
        ))
      ,
      DESCRIPTOR = _ROAD_FEATURE_FEATURE_OBJECT_GEOMETRY_OBJECT,
      __module__ = 'road_feature_pb2'
      # @@protoc_insertion_point(class_scope:Proto.JSON.road_feature.feature_object.geometry_object)
      ))
    ,

    property_object = _reflection.GeneratedProtocolMessageType('property_object', (_message.Message,), dict(
      DESCRIPTOR = _ROAD_FEATURE_FEATURE_OBJECT_PROPERTY_OBJECT,
      __module__ = 'road_feature_pb2'
      # @@protoc_insertion_point(class_scope:Proto.JSON.road_feature.feature_object.property_object)
      ))
    ,
    DESCRIPTOR = _ROAD_FEATURE_FEATURE_OBJECT,
    __module__ = 'road_feature_pb2'
    # @@protoc_insertion_point(class_scope:Proto.JSON.road_feature.feature_object)
    ))
  ,
  DESCRIPTOR = _ROAD_FEATURE,
  __module__ = 'road_feature_pb2'
  # @@protoc_insertion_point(class_scope:Proto.JSON.road_feature)
  ))
_sym_db.RegisterMessage(road_feature)
_sym_db.RegisterMessage(road_feature.road_feature_object)
_sym_db.RegisterMessage(road_feature.feature_object)
_sym_db.RegisterMessage(road_feature.feature_object.geometry_object)
_sym_db.RegisterMessage(road_feature.feature_object.geometry_object.coordinate_object)
_sym_db.RegisterMessage(road_feature.feature_object.property_object)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), b'\n\036net.ktc.miles.model.proto.JSONB\017RoadFeatureJSONH\001')
# @@protoc_insertion_point(module_scope)
