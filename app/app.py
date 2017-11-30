# -*- coding: utf-8 -*-

import argparse

from wos.http import create_app


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Web Application'
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug mode'
    )
    parser.add_argument(
        '--host',
        type=str,
        default='127.0.0.1',
        help='Host address'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=8081,
        help='Port'
    )
    parser.add_argument(
        '--config',
        required=True,
        help='Configuration'
    )
    args = parser.parse_args()
    app = create_app(args.config)
    app.run(
        debug=args.debug,
        host=args.host,
        port=args.port
    )
