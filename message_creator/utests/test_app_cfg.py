import unittest
import sys
import os
from google.protobuf.json_format import MessageToJson, Parse
from google.protobuf.message import DecodeError
import random
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
import app_cfg

import tempfile
import shutil
import uuid


class CFGTest(unittest.TestCase):
    
    
    def setUp(self):
        self.testdir = tempfile.mkdtemp()
    def tearDown(self):
        shutil.rmtree(self.testdir)
    
    def _tmpfname(self, suffix='dat'):
        return os.path.join(self.testdir, '%s.%s'%(str(uuid.uuid4()), suffix))
    
    def test_default_read_write(self):
        radius = 123
        p1 = self._tmpfname('bla')
        w = app_cfg.probe_engine_config(trigger_filter_radius=radius, write_to=p1)
        
        # read it as dat
        r = app_cfg.create_probe_engine_config(read_from=p1)
        self.assertEqual(w.trigger_map_config.filter_config.radial_filter.radius,
                         r.trigger_map_config.filter_config.radial_filter.radius)
        self.assertEqual(w.trigger_map_config.filter_config.radial_filter.radius,
                         radius)
        
        
    
    def test_to_json(self):
        p1 = self._tmpfname('json')
        radius = 112
        w = app_cfg.probe_engine_config(trigger_filter_radius=radius, write_to=p1)
        r = app_cfg.create_probe_engine_config(read_from=p1)
        self.assertEqual(w.trigger_map_config.filter_config.radial_filter.radius,
                         r.trigger_map_config.filter_config.radial_filter.radius)
        self.assertEqual(w.trigger_map_config.filter_config.radial_filter.radius,
                         radius)
        
        self.assertRaises(DecodeError, app_cfg.create_probe_engine, read_from=p1, read_as='dat')
    
    def test_setup_from_file(self):
        p1 = self._tmpfname('json')
        radius = 112
        cfg1 = app_cfg.probe_engine_config(trigger_filter_radius=radius, write_to=p1)
        cfg2 = app_cfg.probe_engine_config(read_from=p1, enable_parallelization=True)
        
        # read the second object from the serialized json from object 1, the radius is overwritten
        # by the default value in the function
        self.assertNotEqual(cfg1.trigger_map_config.filter_config.radial_filter.radius,
                            cfg2.trigger_map_config.filter_config.radial_filter.radius)
        self.assertNotEqual(cfg1.enable_parallelization, cfg2.enable_parallelization)
    
    def test_create_spbt_config(self):
        p1 = self._tmpfname()
        radius = random.randint(0,1000)
        cfg1 = app_cfg.spbt_config(trigger_filter_radius=radius, enable_parallelization=True, write_to=p1)
        self.assertEqual(radius, cfg1.engine_config.trigger_map_config.filter_config.radial_filter.radius)
        cfg2 = app_cfg.create_spbt_config(read_from=p1)
        self.assertEqual(radius, cfg2.engine_config.trigger_map_config.filter_config.radial_filter.radius)
