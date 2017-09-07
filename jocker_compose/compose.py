from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def read_compose(filename='jocker-compose.yml'):
    """Read and parse the compose file"""
    # TODO: catch yaml parsing errors, provide a useful message
    return load(open(filename, 'r'), Loader=Loader)


def validate_compose(content):
    """Validate compose content"""
    # TODO: determine validation rules, like flavours or command are required
    return content
