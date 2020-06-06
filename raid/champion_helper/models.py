from django.db import models
from django.db.models import Q, F, Avg

from decimal import Decimal

# Create your models here.

# TODO: figure out how I want the FKs to work,
# and how to limit the relationship between
# factions and allicances

RARITIES = (
        ("c", "Common"),
        ("unc", "Uncommon"),
        ("rare", "Rare"),
        ("epic", "Epic"),
        ("legend", "Legendary"),
    )

TYPES = (
        ("attack", "Attack"),
        ("defense", "Defense"),
        ("hp", "HP"),
        ("support", "Support"),
    )


class Alliance(models.Model):
    """
    Represents an Alliance
    An Alliance has a name, and has up to 4 factions
    """

    ALLIANCES = (
        ("telerians", "Telerians"),
        ("gaellen_pact", "Gaellen Pact"),
        ("corrupted", "The Corrupted"),
        ("nyresan_union", "Nyresan Union"),
    )

    name = models.CharField(max_length=50, choices=ALLIANCES, unique=True)

    def __str__(self):
        return self.get_name_display()


class Faction(models.Model):
    """
    Rerpresents a faction
    A faction has a name, and belongs to 1, and only 1, Alliance
    """

    FACTIONS = (
        ("banner_lords", "Banner Lords"),
        ("high_elves", "High Elves"),
        ("sacred_order", "The Sacred Order"),
        ("barbarians", "Barbarians"),
        ("ogryn_tribes", "Ogryn Tribes"),
        ("lizardmen", "Lizardmen"),
        ("skinwalkers", "Skinwalkers"),
        ("orcs", "Orcs"),
        ("demonspawn", "Demonspawn"),
        ("undead_hordes", "Undead Hordes"),
        ("dark_elves", "Dark Elves"),
        ("knight_revenant", "Knight Revenant"),
        ("dwarves", "Dwarves"),
    )
    name = models.CharField(max_length=50, choices=FACTIONS, unique=True)
    alliance = models.ForeignKey(Alliance, on_delete=models.PROTECT)

    def __str__(self):
        return self.get_name_display()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "alliance"],
                name="unique_faction_alliance_pair"
            ),
        ]


class Affinity(models.Model):
    """
    Represents the Affinity of a Champion
    An Affinity has a name, and may have
    a strength and weakness
    """

    AFFINITIES = (
        ("force", "Force"),
        ("magic", "Magic"),
        ("spirit", "Spirit"),
        ("void", "Void"),
    )
    name = models.CharField(max_length=6, choices=AFFINITIES, unique=True)
    # See docs on [Field.null](https://docs.djangoproject.com/en/3.0/ref/models/fields/#null) to understand why null=True and blank=True are both needed
    strength = models.OneToOneField(
        "Affinity",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="strong_against",
    )
    weakness = models.OneToOneField(
        "Affinity",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="weak_against",
    )

    def __str__(self):
        return self.get_name_display()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=(
                    # Both strength and weakness are null
                    (Q(strength__isnull=True, weakness__isnull=True))
                    |
                    # OR neither are null AND they are not equal
                    (
                        Q(strength__isnull=False, weakness__isnull=False)
                        & ~Q(strength_id=F("weakness"))
                    )
                ),
                name="strength_weakness_are_both_null_or_populated_and_diff",
            ),
            models.UniqueConstraint(
                fields=["strength", "weakness"],
                name="unique_strength_weakness_pair"
            ),
        ]


class Champion(models.Model):
    """
    Represents a Champion from Raid Shadow Legends
    """

    name = models.CharField(max_length=100, unique=True)
    rarity = models.CharField(max_length=6, choices=RARITIES)
    faction = models.ForeignKey(Faction, on_delete=models.PROTECT)
    affinity = models.ForeignKey(Affinity, on_delete=models.PROTECT)
    type = models.CharField(max_length=7, choices=TYPES)

    def avg_rating(self):
        """
        Return the average of a Champion's Ratings rounded to 1 decimal place.
        Have database calculate the average (returned as a
        dictionary), grab the value of the calculated average
        """
        avg = self.rating_set.aggregate(Avg("value")).get("value__avg")
        return avg.quantize(Decimal("1.0"))

    # Other possible fields: skills
    # TODO: If adding number owned, or max power,
    # create new models to allow users to have
    # their own set of champions

    def __str__(self):
        return self.name


class Location(models.Model):
    """
    Represents an in-game location that can be fights occur
    """

    name = models.CharField(max_length=50, unique=True)
    TYPES = (
        ("general", "General"),
        ("dungeons", "Character Dungeons"),
        ("keeps", "Affinity Keeps"),
    )
    type = models.CharField(max_length=8, choices=TYPES)

    def __str__(self):
        """
        Modify self.name before displaying:
        Capitalize the first letter of each word in self.name
        Replace underscores in self.name with spaces
        """
        return " ".join((word.capitalize() for word in self.name.split("_")))

    def save(self, *args, **kwargs):
        """
        Modify self.name before saving:
        Make self.name lowercase
        Replace spaces in self.name with underscores
        """
        if self.name:
            self.name = self.name.lower()
            self.name = self.name.replace(" ", "_")
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["type", "name"]


class Rating(models.Model):
    """
    Represents a rating for a Champion in a specific
    in-game location.
    Ratings range from 0 - 5, with 1 decimal place
    """
    # Generates all the values from 0.0 - 5.0, inclusive,
    # stepping by 0.1
    POSSIBLE_RATINGS = zip(
        (Decimal(x)/10 for x in range(0, 51)),
        (Decimal(x)/10 for x in range(0, 51))
    )

    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    value = models.DecimalField(
        max_digits=2, decimal_places=1, choices=POSSIBLE_RATINGS
    )

    def __str__(self):
        return f"{self.champion}'s rating for {self.location}"

    class Meta:
        ordering = ["location"]
        constraints = [
            models.CheckConstraint(
                check=(
                    Q(
                        # TODO: Might need to use Decimal()
                        value__gte=0.0,
                        value__lte=5.0
                    )
                ),
                name="zero_to_five_rating"
            ),
            models.UniqueConstraint(
                fields=["champion", "location"],
                name="unique_champion_location_pair"
            )
        ]
