
import sys
import event_pb2 as __event
import geo_positions_pb2 as __geo_positions
import mobile_app_config_pb2 as __mobile_app_config
import probe_engine_config_pb2 as __probe_engine_config
import road_feature_pb2 as __road_feature
import spbt_config_pb2 as __spbt_config


# writes the message (as serialized binary string) to the file (with file_name)
# message e.g.: my_proto_message.SerializeToString()
# file_name e.g.: "my_proto_message.dat"
def write_message_to_file(file_name, message):
	f = open(file_name, "wb")
	f.write(message)
	f.close()

# read a message (as serialized binary string) from the file (with file_name)
# message e.g.: my_proto_message
# file_name e.g.: "my_proto_message.dat"
def read_message_from_file(file_name, message):
	try:
		f = open(file_name, "rb")
		message.ParseFromString(f.read())
		f.close()
	except IOError:
		print(file_name + ": Could not open file.")


def create_event_message():
	# fill the message here
	msg = __event.event_message()
	## start

	## end
	return msg

def create_geo_positions_message():
	# fill the message here
	msg = __geo_positions.geo_positions()
	## start

	## end
	return msg

def create_road_feature_message():
	# fill the message here
	msg = __road_feature.road_feature()
	## start

	## end
	return msg

def create_mobile_app_config_message():
	# fill the message here
	msg = __mobile_app_config.mobile_app_config()
	## start

	## end
	return msg

def create_probe_engine_config_message():
	# fill the message here
	msg = __probe_engine_config.probe_engine_config()
	## start
	msg.buffer_size = 20
	msg.autostart_detection_loop = False
	msg.enable_parallelization = False

		# add the filter types 
	f_n = msg.filter_config.add()
	f_n.type = __probe_engine_config.filter_config_object.filter_type.Value('Normalize')
	f_h = msg.filter_config.add()
	f_h.type = __probe_engine_config.filter_config_object.filter_type.Value('Hot_Spot')


		# add the detection algorithm config object
	detect_conf = __probe_engine_config.detection_config_object()
	detect_conf.type = __probe_engine_config.detection_config_object.detection_type.Value('Proximity_Based')
	prox_det_conf = __probe_engine_config.detection_config_object.proximity_config_object()
	detect_conf.proximity_config.CopyFrom(prox_det_conf)
	msg.detection_config.CopyFrom(detect_conf)


		# add the trigger area filter config
	t_map_c_obj = __probe_engine_config.trigger_area_filter_config_object()
	t_map_c_obj.type = __probe_engine_config.trigger_area_filter_config_object.filter_type.Value('Radial')

	t_map_f = __probe_engine_config.trigger_area_filter_config_object.radial_filter_config_object()
	t_map_f.radius = 1000
	t_map_c_obj.radial_filter.CopyFrom(t_map_f)

	t_map_conf = __probe_engine_config.trigger_area_map_config_object()
	t_map_conf.filter_config.CopyFrom(t_map_c_obj)
	msg.trigger_map_config.CopyFrom(t_map_conf)

	## end
	return msg

def create_spbt_config_message():
	# fill the message here
	msg = __spbt_config.application_config()
	## start
	msg.engine_config.CopyFrom(create_probe_engine_config_message())
	msg.app_config.CopyFrom(create_mobile_app_config_message())
	## end
	return msg

def main(argv):
	# enable and disable messages here
	write_message_to_file("spbt_conf.dat", create_spbt_config_message().SerializeToString())
	write_message_to_file("event_msg.dat", create_event_message().SerializeToString())
	write_message_to_file("geo_positions.dat", create_geo_positions_message().SerializeToString())
	write_message_to_file("road_feature.dat", create_road_feature_message().SerializeToString())
	write_message_to_file("mobile_app_conf.dat", create_mobile_app_config_message().SerializeToString())
	write_message_to_file("probe_engine_conf.dat", create_probe_engine_config_message().SerializeToString())


if __name__ == "__main__":
	main(sys.argv)