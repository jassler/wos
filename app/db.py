import argparse

from wos.database import init_engine, init_db, db_session
from wos.models import User


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Database Migration Tool'
    )
    parser.add_argument(
        '--db',
        type=str,
        required=True,
        help='Configuration'
    )
    parser.add_argument(
        '--init',
        action='store_true',
        help='Initialize database'
    )
    parser.add_argument(
        '--demo',
        action='store_true',
        help='Preload with demo data'
    )
    args = parser.parse_args()
    init_engine(args.db)
    if args.init:
        init_db()
    if args.demo:
        db_session.add(User('demo@demo.com', 'demo', True, True))
        db_session.commit()
