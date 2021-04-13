from uuid import UUID


def validate_if_uuid(uuid_to_be_tested):
    try:
        UUID(uuid_to_be_tested)
        return True
    except ValueError:
        return False
