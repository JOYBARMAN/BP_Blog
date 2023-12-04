from django.db.models import TextChoices


class ReactionChoices(TextChoices):
    UNDEFINED = "UNDEFINED", "Undefined"
    LIKE = "LIKE", "Like"
    DISLIKE = "DISLIKE", "Dislike"
    HAHA = "HAHA", "Haha"
    SAD = "SAD", "Sad"
    CUTE = "CUTE", "Cute"
    LOVE = "LOVE", "Love"
