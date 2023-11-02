from django.db.models import TextChoices


class BloodGroups(TextChoices):
    NOT_SET = "NOT_SET", "Not Set"
    A_POSITIVE = "A+"
    A_NEGATIVE = "A-"
    B_POSITIVE = "B+"
    B_NEGATIVE = "B-"
    AB_POSITIVE = "AB+"
    AB_NEGATIVE = "AB-"
    O_POSITIVE = "O+"
    O_NEGATIVE = "O-"


class UserKind(TextChoices):
    ADMIN = "ADMIN", "Admin"
    AUTHOR = "AUTHOR", "Author"
    SUPER_ADMIN = "SUPER_ADMIN", "Super Admin"
    UNDEFINED = "UNDEFINED", "Undefined"


class UserGender(TextChoices):
    FEMALE = "FEMALE", "Female"
    MALE = "MALE", "Male"
    UNKNOWN = "UNKNOWN", "Unknown"
    OTHER = "OTHER", "Other"


class UserStatus(TextChoices):
    ACTIVE = "ACTIVE", "Active"
    DRAFT = "DRAFT", "Draft"
    INACTIVE = "INACTIVE", "Inactive"
    REMOVED = "REMOVED", "Removed"
