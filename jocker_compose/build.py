def build_flavour(compose, name):
    """Build the given jail flavour"""
    service = compose['services'].get(name)

    if not service:
        raise RuntimeError('Missing service: {name}'.format(name=name))


def build_flavours(compose, names):
    """Build the jail flavours for the given names"""
    return [build_flavour(compose, name) for name in names]
