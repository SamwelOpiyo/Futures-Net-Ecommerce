from django.core.files.base import ContentFile

from celery.utils.log import get_task_logger
import os
from PIL import Image
from io import BytesIO

from catalogue.models import MediaUpload
from futures_net_ecommerce.taskapp.celery import app


logger = get_task_logger(__name__)


def make_thumbnail(media_upload_object):
        """
        Creates thumbnail of media upload
        """
        if not media_upload_object.media_file:
            logger.info("Media File does not exist in this object.")

        try:
            image = Image.open(media_upload_object.media_file)
            image.thumbnail([200, 200], Image.ANTIALIAS)

            thumb_name, thumb_extension = os.path.splitext(media_upload_object.media_file.name)
            thumb_extension = thumb_extension.lower()

            thumb_filename = thumb_name + "_thumb" + thumb_extension

            if thumb_extension in [".jpg", ".jpeg"]:
                FTYPE = "JPEG"
            elif thumb_extension == ".gif":
                FTYPE = "GIF"
            elif thumb_extension == ".png":
                FTYPE = "PNG"
            else:
                return False  # Unrecognized file type

            # Save thumbnail to in-memory file as StringIO
            temp_thumb = BytesIO()
            image.save(temp_thumb, FTYPE)
            temp_thumb.seek(0)

            thumbnail_object = MediaUpload(user=media_upload_object.user)
            logger.info("Created Thumbnail Media Upload Object.")
            thumbnail_object.media_file.save(thumb_filename, ContentFile(temp_thumb.read()))
            thumbnail_object.save()
            media_upload_object.media_upload_thumbnail.add(thumbnail_object)
            logger.info("Added Thumbnail Media Object to Media Upload Object.")
            temp_thumb.close()
            image.close()
        except AttributeError:
            pass
        except OSError:
            pass

        return True


@app.task(name="generate_media_upload_thumbnail_task", bind=True)
def generate_media_upload_thumbnail_task(self, media_upload_object_key):
    media_upload_object = MediaUpload.objects.get(media_key=media_upload_object_key)
    logger.info("Retrieved Media Upload Object:" + str(media_upload_object_key))
    return make_thumbnail(media_upload_object)
