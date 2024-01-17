def get_path_upload_avatar(instance, file):
    """Create path for upload avatar: format media/avatars/<user_id>/<filename>
    """
    return f"avatars/{instance.id}/{file}"

def validate_size_image(file_obj):
    """Validate size user avatar's image
    """
    limit = 2
    if file_obj.size > limit * 1024 * 1024:
        raise ValueError(f"The maximum size of the uploaded image is {limit}MB")
