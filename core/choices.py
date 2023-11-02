from django.db.models import TextChoices


class UserType(TextChoices):
    AUTHOR = "AUTHOR", "Author"
    VISITOR = "VISITOR", "Visitor"
    UNDEFINED = "UNDEFINED", "Undefined"
