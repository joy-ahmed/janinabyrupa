import os

def product_image_upload_path(instance, filename):
    image_id = instance.id

    # generate upload path
    new_filename = f"product_image_{image_id}_{filename}"
    return os.path.join('products/images', new_filename)