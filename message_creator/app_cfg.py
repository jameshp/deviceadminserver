'''helpers for the SPBT protobuf objects

* create default protobuf objects

    the create_<object> functions are used to create empty/default objects. 
    This functions can be called with the arguments *read_from* and *read_as* to initialize the objects from previous serialized (json or binary) protobuf objects
    
    The argument read_from is the file-path to the serialized object, with read_as can be set the serialization format (json|dat). If read_as
    isn't set, the format is parsed from the file-path suffix or set to binary if the suffix isn't json or dat.
    
    >>> # read a json serialized event
    >>> create_event(read_from='c:/path/to/ser.js', read_as='json')

* create custom protobuf objects

    Beside the create_<object> functions, every available SPBT protobuf object has a factory method to create custom objects. 
    This functions can be called with the arguments *write_to*, *write_as* and *write_defaults* to serialize the objects to a file
    
    write_to is the path to the file to write, write_as is the format to write (json|dat). If write_as
    isn't set, the format is parsed from the file-path suffix or set to binary if the suffix isn't json or dat.
    write_defaults can be set to True, to write also the defaults in the json output
    
    >>> # create a custom probe engine
    >>> probe_engine_config(trigger_filter_radius=radius, enable_parallelization=True, write_to='c:\\temp\\engine.cfg', write_as='json')

* Implementation Details/ Extend the factory methods

    Use kwargs in the factory methods to add parameters, see for example probe_engine_config
    The create_<object> functions shall only be used to create empty object or to load previous serialized objects

'''
import probe_engine_config_pb2
import event_pb2
import geo_positions_pb2
import mobile_app_config_pb2
import road_feature_pb2
import spbt_config_pb2
import argparse
import os
import logging
logger = logging.getLogger('SPBT msg creator')

try:
    from google.protobuf.json_format import MessageToJson, Parse
except ImportError:
    logger.warn('unable to load %s. Please install protobuf>=3.0.0b to use the to json functions'
                % 'from google.protobuf.json_format import MessageToJson, Parse')

def _writer_decorator(func):
    '''add the kwarg write_to='path/filename.suffix' to the xxx_cfg functions to serialize the cfg to a file
    the kwarg write_as can be json or dat, if write as is not set, then is parsed from the write to suffix (if is json or dat)
    the default value is dat (if not set in write_as or parsable from the suffix)
    
    write_defaults: only used for output format json, writes also the default values to the json file, default is False
    '''
    def wrapper(*args, **kwargs):
        write_to = kwargs.get('write_to')
        write_as = kwargs.get('write_as')
        write_defaults = kwargs.get('write_defaults', False)
        cg_msg = func(*args, **kwargs)
        if write_to and not write_as:
            suffix = write_to.split('.')[-1]
            write_as = suffix if suffix in ['dat', 'json'] else 'dat'
        
        logger.info('serialize the msg to %s as [Format: %s]' % (write_to, write_as))
        
        if write_to:
            serialize_to_file(cg_msg, write_to, write_as, write_defaults)
        return cg_msg
    return wrapper

def to_json(msg, write_defaults=False):
    '''helper to convert a protobuf object to json.
    '''
    return MessageToJson(msg, write_defaults)

def serialize_to_file(msg, path, format='dat', write_defaults=False):
    '''serialize a msg to a file
    
    :param protobuf msg: the object to serialize
    :param str path: path to the file to write
    :param str format: serialization format, dat (default) or json
    :param bool write_defaults: write also the default values in the json serialization, default is False
    '''
    
    assert format in ['dat', 'json'], '%s is a unknown output format, available options are dat (for binary output) or json (for json output)'
    
    serialized_out = None
    if format == 'dat':
        serialized_out = msg.SerializeToString()
    elif format == 'json':
        serialized_out=MessageToJson(msg, write_defaults)
    if serialized_out:
        with open(path, 'wb') as ser_out_file:
            ser_out_file.write(serialized_out)

def _read_decorator(func):
    def wrapper(*args, **kwargs):
        read_from = kwargs.get('read_from')
        read_as = kwargs.get('read_as')
        msg = func(*args,**kwargs)
        
        if read_from and not read_as:
            suffix = read_from.split('.')[-1]
            read_as = suffix if suffix in ['dat', 'json'] else 'dat'
        
        if read_from:
            deserialize_from_file(msg, read_from, read_as)
        return msg
    return wrapper

def deserialize_from_file(msg, path, format='dat'):
    '''deserialize a msg from a file
    
    :param protobuf msg: the object to deserialize
    :param str path: path to the file to read
    :param str format: serialization format, dat (default) or json
    
    '''
    assert format in ['dat', 'json'], '%s is a unknown input format, available options are dat (binary) or json'
    
    with open(path, 'rb') as infile:
        data = infile.read()
    if format == 'dat':
        msg.ParseFromString(data)
    elif format == 'json':
        Parse(data, msg)
    return msg

@_read_decorator
def create_event(*args, **kwargs):
    return event_pb2.event_message()

@_writer_decorator
def event(imei="12324345",
          type="AppStarted",
          data={'foo':'bar'},
          seconds=0,
          nanos=0,
          lat=46.111,
          lon=18.123,
          speed=121.23,
          course=12.23,
          elevation=234.12,
          accuracy=0.23,
          **kwargs):
    event= create_event(**kwargs)
    event.event.type = type
    event.event.data.update(data)
    event.device.imei = imei
    event.position.timestamp.seconds = int(seconds)
    event.position.timestamp.nanos = int(nanos)
    event.position.lat = float(lat)
    event.position.lon = float(lon)
    event.position.speed = float(speed)
    event.position.course = float(course)
    event.position.elevation = float(elevation)
    event.position.accuracy = float(accuracy)
    
    
    return event

@_read_decorator
def create_geo_positions(*args, **kwargs):
    return geo_positions_pb2.geo_positions()

@_writer_decorator
def geo_positions(positions=[{
                              'seconds':0,
                              'nanos':0,
                              'lat': 46.121,
                              'lon':18.11,
                              'speed':121.12,
                              'course':34.1,
                              'elevation':123.4,
                              'accuracy':0.25,
                              'is_from_mock':False,
                              'provider':'gps'
                              },],**kwargs):
    cfg = create_geo_positions(**kwargs)
    for position in positions:
        pos = cfg.positions.add()
        pos.timestamp.seconds = int(position['seconds'])
        pos.timestamp.nanos = int(position['nanos'])
        pos.lat = float(position['lat'])
        pos.lon = float(position['lon'])
        pos.speed = float(position['speed'])
        pos.course = float(position['course'])
        pos.elevation = float(position['elevation'])
        pos.accuracy = float(position['accuracy'])
        pos.is_from_mock = bool(position['is_from_mock'])
        pos.provider = position['provider']
    return cfg

@_read_decorator
def create_road_feature(*args, **kwargs):
    return road_feature_pb2.road_feature()

@_writer_decorator
def road_feature(feature_type="FeatureCollection",
                 valid_from="2015-09-23T09:28:19.000Z",
                 algorithm="PoximityBased",
                 features=[{'type':'Feature',
                           'geometry':{
                                       'type':'Poligon', 
                                       'geolocation':[[16.33002501719602, 48.13491618623660], [16.53002501719602, 48.23491618623660]]
                             },
                           'properties':{'tollpoints':[{'id':1, 'name':"Inzersdorf", 'event':"EntranceExit", "direction":0},]}
                           },],
                 **kwargs):
    cfg = create_road_feature(**kwargs)
    cfg.type = feature_type
    cfg.roadFeature.validFrom = valid_from
    cfg.roadFeature.algorithm = algorithm
    
    for feature in features:
        feat = cfg.features.add()
        feat.type = feature['type']
        feat.geometry.type = feature['geometry']['type']
        for coordinates in feature['geometry']['geolocation']:
            coord = feat.geometry.coordinates.add()
            coord.lat = float(coordinates[0])
            coord.lon = float(coordinates[1])

        for tp in feature['properties']['tollpoints']:
          fob = road_feature_pb2.road_feature.feature_object.property_object()
          fob.id = int(tp['id'])
          fob.name = tp['name']
          fob.event = tp['event']
          fob.direction = int(tp['direction'])
          fob.type = int(0)
          fob.confidence = float(0.5)
          fob.bothdirections = int(0)
          fob.triggerIndex = int(1)
          fob.required = bool(True)
          feat.properties.CopyFrom(fob)

    return cfg

@_read_decorator
def create_mobile_app_config(*args, **kwargs):
    return mobile_app_config_pb2.mobile_app_config()

@_writer_decorator
def mobile_app_config(log_level=0, 
                      log_enabled=True,
                      
                      simulation_enabled=False,
                      default_simulation_file='',
                      login_user='username',
                      login_pwd='pwd',
                      initial_balance=1,
                      selected_vehicle='AT123',

                      raw_data_collection_enabled = True,                      
                      raw_data_collection_server_type = 0,
                      raw_data_collection_url="http://127.0.0.1:8888/smartphone/v1/positions/raw",
                      raw_data_collection_credentials = 'auth',
                      raw_data_collection_send_interval_sec=10,
                      raw_data_collection_buffering_sec = 1200,

                      probe_data_collection_enabled = False,                      
                      probe_data_collection_server_type = 0,
                      probe_data_collection_url="127.0.0.1:8888",
                      probe_data_collection_credentials = 'auth',
                      probe_data_collection_send_interval_sec=60,
                      probe_data_collection_position_interval_sec=60,
                      probe_data_collection_position_interval_meter=100,
                      probe_data_collection_buffering_sec = 0,

                      virtual_gantry_detection_enabled = True,      
                      virtual_gantry_detection_server_type = 0,
                      virtual_gantry_detection_url="http://127.0.0.1:8888/smartphone/v1/positions/virtualgantry",
                      virtual_gantry_detection_credentials = 'auth',
                      virtual_gantry_detection_buffering_sec = 1200,
                      virtual_gantry_detection_position_interval_sec=1,
                      virtual_gantry_detection_position_interval_meter=10,
                      
                      event_config_enabled=True,
                      event_config_server_type=0,
                      event_config_url="http://127.0.0.1:8888/smartphone/v1/events",
                      event_config_credentials='auth',
                      event_config_buffering_sec=1200,
                      
                      user_config_enabled_automatic_tolling=True,
                      user_config_audio_enabled=True,
                      user_config_visual_enabled=True,
                      
                      configuration_service_server_type=0,
                      configuration_service_url="http://127.0.0.1:8888/smartphone/v1/appconfiguration/versions/LATEST",
                      configuration_service_credentials='auth',
					  configuration_service_update_interval_sec=3600,
                      
                      road_feature_config_server_type=0,               
                      road_feature_config_url="http://127.0.0.1:8888/smartphone/v1/roadfeatures/versions/LATEST",
					  road_feature_config_credentials='auth',
                      road_feature_config_update_interval_sec=3600,

                      trial_config_users='users',
                      trial_config_users_user='359523063970048',
                      trial_config_users_data={'cat':'EURO0', 'country':'AT', 'type':'0', 'lpn':'W-112341A'},
                      
                      **kwargs):

    cfg = create_mobile_app_config(**kwargs)
    cfg.logging_config.level = int(log_level)
    cfg.logging_config.enabled = bool(log_enabled)
    
    cfg.testing_config.simulation_enabled = bool(simulation_enabled)
    cfg.testing_config.default_simulation_file = default_simulation_file
    cfg.testing_config.login_user = login_user
    cfg.testing_config.login_pwd = login_pwd
    cfg.testing_config.initial_balance = int(initial_balance)
    cfg.testing_config.selected_vehicle = selected_vehicle
    cfg.testing_config.default_road_feature.CopyFrom(road_feature(**kwargs))
    
    cfg.raw_data_config.send_interval_sec = int(raw_data_collection_send_interval_sec)
    cfg.raw_data_config.base_config.enabled = bool(raw_data_collection_enabled)
    cfg.raw_data_config.base_config.buffering_sec = int(raw_data_collection_buffering_sec)
    cfg.raw_data_config.base_config.url.credentials = raw_data_collection_credentials
    cfg.raw_data_config.base_config.url.type = int(raw_data_collection_server_type)
    cfg.raw_data_config.base_config.url.url = raw_data_collection_url
    
    cfg.probe_data_config.send_interval_sec = int(probe_data_collection_send_interval_sec)
    cfg.probe_data_config.position_interval_meter = int(probe_data_collection_position_interval_meter)
    cfg.probe_data_config.position_interval_sec = int(probe_data_collection_position_interval_sec)
    cfg.probe_data_config.base_config.enabled = bool(probe_data_collection_enabled)
    cfg.probe_data_config.base_config.buffering_sec = int(probe_data_collection_buffering_sec)
    cfg.probe_data_config.base_config.url.credentials = probe_data_collection_credentials
    cfg.probe_data_config.base_config.url.type = int(probe_data_collection_server_type)
    cfg.probe_data_config.base_config.url.url = probe_data_collection_url
    
    cfg.virtual_gantry_detection_config.position_interval_sec = int(virtual_gantry_detection_position_interval_sec)
    cfg.virtual_gantry_detection_config.position_interval_meter = int(virtual_gantry_detection_position_interval_meter)
    cfg.virtual_gantry_detection_config.base_config.enabled = bool(virtual_gantry_detection_enabled)
    cfg.virtual_gantry_detection_config.base_config.buffering_sec = int(virtual_gantry_detection_buffering_sec)
    cfg.virtual_gantry_detection_config.base_config.url.credentials = virtual_gantry_detection_credentials
    cfg.virtual_gantry_detection_config.base_config.url.type = int(virtual_gantry_detection_server_type)
    cfg.virtual_gantry_detection_config.base_config.url.url = virtual_gantry_detection_url
    
    cfg.event_config.enabled = bool(event_config_enabled)
    cfg.event_config.buffering_sec = int(event_config_buffering_sec)
    cfg.event_config.url.credentials = event_config_credentials
    cfg.event_config.url.type = int(event_config_server_type)
    cfg.event_config.url.url = event_config_url
    
    cfg.user_config.enabled_automatic_tolling = bool(user_config_enabled_automatic_tolling)
    cfg.user_config.notification_config.audio_enabled = bool(user_config_audio_enabled)
    cfg.user_config.notification_config.visual_enabled = bool(user_config_visual_enabled)
    
    cfg.configuration_service_url.update_interval_sec = int(configuration_service_update_interval_sec)
    cfg.configuration_service_url.url.credentials = configuration_service_credentials
    cfg.configuration_service_url.url.type = int(configuration_service_server_type)
    cfg.configuration_service_url.url.url = configuration_service_url
    
    cfg.road_feature_config.update_interval_sec = int(road_feature_config_update_interval_sec)
    cfg.road_feature_config.url.credentials = road_feature_config_credentials
    cfg.road_feature_config.url.type = int(road_feature_config_server_type)
    cfg.road_feature_config.url.url = road_feature_config_url

    cfg.trial_config.accepted_users.name = trial_config_users
    user_data = cfg.trial_config.accepted_users.data.add()
    user_data.name = trial_config_users_user
    user_data.data.update(trial_config_users_data)
    
    #cfg.security_config
    # see mobile_app_conig.proto -> TODO
    
    return cfg

@_read_decorator
def create_spbt_config(*args, **kwargs):
    return spbt_config_pb2.application_config()

@_writer_decorator
def spbt_config(**kwargs):
    '''create a nested SPBT config containing probe_engine_config and mobile_app_config
    '''
    cfg = create_spbt_config(**kwargs)
    kwargs.pop('read_from', None)
    kwargs.pop('write_to', None)
    
    cfg.engine_config.CopyFrom(probe_engine_config(**kwargs))
    cfg.app_config.CopyFrom(mobile_app_config(**kwargs))
    return cfg

@_read_decorator
def create_probe_engine_config(*args, **kwargs):
    return probe_engine_config_pb2.probe_engine_config()

@_writer_decorator
def probe_engine_config(buffer_size=20, 
                     override_buffer_on_new_positions=False,
                     autostart_detection_loop=False, 
                     enable_parallelization=False,
                     filters=['Hot_Spot', 'Normalize'],
                     detection_type = 'Proximity_Based',
                     trigger_filter = 'Radial',
                     trigger_filter_radius = 1000,
                     **kwargs
                     ):
    msg = create_probe_engine_config(**kwargs)
    msg.buffer_size = int(buffer_size)
    msg.override_buffer_on_new_positions = bool(override_buffer_on_new_positions)
    msg.autostart_detection_loop = bool(autostart_detection_loop)
    msg.enable_parallelization = bool(enable_parallelization)

    for filter in filters:
        filter_cfg = msg.filter_config.add()
        filter_cfg.type = probe_engine_config_pb2.filter_config_object.filter_type.Value(filter)


    detect_conf = probe_engine_config_pb2.detection_config_object()
    detect_conf.type = probe_engine_config_pb2.detection_config_object.detection_type.Value(detection_type)
    prox_det_conf = probe_engine_config_pb2.detection_config_object.proximity_config_object()
    detect_conf.proximity_config.CopyFrom(prox_det_conf)
    msg.detection_config.CopyFrom(detect_conf)


    t_map_c_obj = probe_engine_config_pb2.trigger_area_filter_config_object()
    t_map_c_obj.type = probe_engine_config_pb2.trigger_area_filter_config_object.filter_type.Value(trigger_filter)

    t_map_f = probe_engine_config_pb2.trigger_area_filter_config_object.radial_filter_config_object()
    t_map_f.radius = int(trigger_filter_radius)
    t_map_c_obj.radial_filter.CopyFrom(t_map_f)

    t_map_conf = probe_engine_config_pb2.trigger_area_map_config_object()
    t_map_conf.filter_config.CopyFrom(t_map_c_obj)
    msg.trigger_map_config.CopyFrom(t_map_conf)

    return msg



if __name__ == "__main__":
    description = ("Tool to CREATE SPBT ProtoBuf JSON Templates and to CONVERT SPBT ProtoBuf JSON Files to ProtoBuf Binary Files"
                   "\n\n"
                   "Print the subcommand help with:\n"
                   "\t%(prog)s <objectname> CREATE -h [eg. %(prog)s event CREATE -h]\n"
                   "\t%(prog)s <objectname> CONVERT -h [eg. %(prog)s event CONVERT -h]\n"
                   )
    epilog = ("USAGE EXAMPLES:"
              "\n\n"
              "\tCREATE a event json template (named event.json) in the current directory\n"
              "\t\t%(prog)s event CREATE\n"
              "\n"
              "\tCREATE a event json template in c:/temp/my_event.json\n"
              "\t\t%(prog)s event CREATE c:/temp/my_event.json\n"
              "\n"
              "\tCONVERT my_event.json to a ProtoBuf binary File. The File is written to <Current Directory>/my_event.dat\n"
              "\t\t%(prog)s event CONVERT c:/temp/my_event.json\n"
              "\n"
              "\tCONVERT my_event.json to c:/temp/new_event.dat\n"
              "\t\t%(prog)s event CONVERT c:/temp/my_event.json -o c:/temp/new_event.dat\n"
              "\n"
              "\tCONVERT new_event.dat back to json\n"
              "\t\t%(prog)s event CONVERT c:/temp/new_event.dat -o c:/temp/converted_event.js --in-format dat --out-format json\n"
              
              )
    parser = argparse.ArgumentParser(description=description, epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("object", help="the SPBT protobuf object name",
                          choices=['event', 'geo_positions','mobile_app_config', 'probe_engine_config', 'road_feature', 'spbt_config'])
    subparsers = parser.add_subparsers()
    template = subparsers.add_parser("CREATE", help="create json template from a default SPBT protobuf object")
    template.set_defaults(which='create')
    convert = subparsers.add_parser("CONVERT", help="convert a json serialized protobuf object to a binary serialized")
    convert.set_defaults(which='convert')
    
    template.add_argument("output", nargs='?', help="where to write the output json file, default is <curdir>/<object>.json", default=None)
    
    convert.add_argument("input", help="path to the file to parse")
    convert.add_argument("--in-format", dest='inf' ,help="the input serialization format, default is json", default='json', choices=['json', 'dat'])
    convert.add_argument("--out-format", dest='outf' ,help="the output serialization format, default is dat (binary)", default='dat', choices=['json', 'dat'])
    convert.add_argument("-o", "--output", help="path to the output file, default is the same as the input with the --out-format suffix", default=None)
    
    #print convert.parse_args()
    parsed = parser.parse_args()
    if parsed.which == 'create':
        msg = eval('%s()'%parsed.object) # create a template with the defaults defined
        dst = parsed.output if parsed.output else os.path.join(os.path.curdir, '%s.%s' % (parsed.object, 'json'))
        print "Serialize %s to %s" % (parsed.object, dst)
        serialize_to_file(msg, dst, 'json', True)
    if parsed.which == 'convert':
        msg = eval('create_%s'%parsed.object)(read_from=parsed.input, read_as=parsed.inf)
        dst = parsed.output if parsed.output else '%s.%s'%(os.path.splitext(parsed.input)[0], parsed.outf)
        print "Serialize %s to %s" % (parsed.object, dst)
        serialize_to_file(msg, dst, parsed.outf, True)
    
