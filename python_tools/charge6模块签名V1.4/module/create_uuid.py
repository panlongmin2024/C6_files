import os
import uuid

import os


def create_uuid_file(file_path):
    random_string = str(uuid.uuid4()).replace('-', '')[:32]
    with open(file_path, 'w') as file:
        file.write(random_string)
    return random_string


def get_file_size(file_path):
    return os.path.getsize(file_path)



