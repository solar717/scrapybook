#!/usr/bin/env python

from scrapy.utils.project import get_project_settings
from speed.spiders.server import *

if __name__ == "__main__":
    settings = get_project_settings()
    
    SimpleServer(settings.getint('SPEED_PORT', 9312), settings)
    
    reactor.run()
