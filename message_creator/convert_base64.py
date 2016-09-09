import base64

path = "C:\\ktcsrc\\Projects\\SmartphoneBasedTolling\\SmartToll\\trunk\\Tools\\message_creator\\"
file = "SIT_environment_dietweis_context_v12_80m_mcd_zones_in_both_directions_2016_06_03.dat"
out_name = "SIT_environment_dietweis_context_v12_80m_mcd_zones_in_both_directions_2016_06_03.b64"

b64 = base64.b64encode(open(path + file, 'rb').read())
print b64

f = open(path + out_name, 'w+')
f.write(b64)
f.flush()
f.close()
