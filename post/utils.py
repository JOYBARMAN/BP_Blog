"""Custom upload dir for richtext field """


def custom_upload_to(instance, filename):
    model_name = instance.__class__.__name__
    return f"custom_directory/{model_name}/"
