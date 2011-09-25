#! /usr/bin/env python
#
# Voldemort config
#
# @author: Sreejith K
# Created On 19th Sep 2011


import os

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


DEFAULT_CONFIG = {'layout_dir'  : 'layout',
                  'include_dir' : 'include',
                  'posts_dir'   : 'posts',
                  'post_url'    : '%Y/%m/%d',
                  'site_dir'    : '_site'
                }


class Config(object):
    """ Converts a dict to object.
    """
    def __init__(self, dict):
        self.__dict__.update(dict)


def load_config(work_dir, name='settings.yaml'):
    """ Loads the configuration from the working directory. Else loads
    the default config.
    """
    config_file = os.path.join(work_dir, name)
    if os.path.exists(config_file):
        config = Config(load(file(config_file, 'r'), Loader=Loader))
    else:
        config = Config(DEFAULT_CONFIG)
    config.layout_dir = os.path.join(work_dir, config.layout_dir)
    config.include_dir = os.path.join(work_dir, config.include_dir)
    config.posts_dir = os.path.join(work_dir, config.posts_dir)
    config.site_dir = os.path.join(work_dir, config.site_dir)
    return config