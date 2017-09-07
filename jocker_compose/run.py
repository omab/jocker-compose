import sys
import argparse


def do_build(args):
    print('BUILD:', args)


def do_up(args):
    print('UP:', args)


def do_down(args):
    print('DOWN:', args)


def do_run(args):
    print('RUN:', args)


def do_status(args):
    print('STATUS:', args)


parser = argparse.ArgumentParser(description='Jail composing management tool')
parser.add_argument(
    '--compose-file',
    default='jocker-compose.yml',
    help='specify compose file (default jocker-compose.yml)'
)
subparsers = parser.add_subparsers()

build_parser = subparsers.add_parser(
    'build',
    description='Build jails into flavours'
)
build_parser.add_argument('names', nargs='*', help='jail flavours to build')
build_parser.add_argument('--install', action='store_true',
                          help='install the built jail flavour')
build_parser.set_defaults(func=do_build)

up_parser = subparsers.add_parser(
    'up',
    description='Start one or all the jails'
)
up_parser.add_argument('names', nargs='*', help='jails to start')
up_parser.set_defaults(func=do_up)

down_parser = subparsers.add_parser(
    'down',
    description='Stop one or all the jails'
)
down_parser.add_argument('names', nargs='*', help='jails to stop')
down_parser.set_defaults(func=do_down)

run_parser = subparsers.add_parser(
    'run',
    description='Run a command in the given jails'
)
run_parser.add_argument('names', nargs='+', help='jails to run the command on')
run_parser.add_argument('command', nargs='+', help='command to run')
run_parser.add_argument('args', nargs=argparse.REMAINDER, help='command to run')
run_parser.set_defaults(func=do_run)

status_parser = subparsers.add_parser('status', help='jails status')
status_parser.set_defaults(func=do_status)

if __name__ == '__main__':
    args = parser.parse_args()
    if len(sys.argv) > 1:
        args.func(args)
    else:
        parser.print_help()
