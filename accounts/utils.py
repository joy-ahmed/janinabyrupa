import os

def avatar_upload_path(instance, filename):
    user_id = instance.id

    # generate upload path
    new_filename = f"avatar_{user_id}_{filename}"
    return os.path.join('users/images/avatar', new_filename)