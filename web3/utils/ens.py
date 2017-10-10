

def is_ens_name(value):
    if isinstance(value, bytes):
        value = value.decode('utf-8')
    if not isinstance(value, str):
        return False
    return value.endswith('.eth')
