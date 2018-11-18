import os


def get_upload_media_name(instance, filename):
    """
    Generic method to manage model media
    - Use a uuid string to avoid name conflicts
    - Added a 's' to media type to generate a plural folder

    """
    dirname = "media/" + instance.media_type + "s/"
    extension = os.path.splitext(filename)[1]
    return dirname + str(instance.media_key) + extension
