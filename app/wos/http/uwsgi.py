# -*- coding: utf-8 -*-
import sys
import site

site.addsitedir('/usr/share/python/wos/lib/python2.7/site-packages')
sys.path.append('/usr/share/python/wos/lib/python2.7/site-packages')

from wos.http import create_app
application = create_app('/var/lib/wos/wos.ini')

if __name__ == '__main__':
    application.run(
        host='0.0.0.0',
        port=8080
    )
