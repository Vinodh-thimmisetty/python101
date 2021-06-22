import dataclasses
from enum import Enum
from tokenize import Double

EQUATOR = 0  # latitude
PRIME_MERIDIAN = 0  # longitude
NORTHERN_HEMISPHERE = (EQUATOR, 90)
SOUTHERN_HEMISPHERE = (EQUATOR, -90)
EASTERN_HEMISPHERE = (PRIME_MERIDIAN, 180)
WESTERN_HEMISPHERE = (PRIME_MERIDIAN, -180)


def lat_direction(latitude):
    return Direction.North.value if float(latitude) > EQUATOR else Direction.South.value


def long_direction(longitude):
    return Direction.East.value if float(longitude) > PRIME_MERIDIAN else Direction.West.value


def format_position(latitude, longitude):
    return f"(Latitude={latitude}° {lat_direction(latitude)}," \
           f"Longitude={longitude}° {long_direction(longitude)})"


class Direction(Enum):
    North = "N"
    South = "S"
    East = "E"
    West = "W"


@dataclasses.dataclass(frozen=True, order=True, repr=False)
class GeoPosition:
    latitude: Double
    longitude: Double

    def __post_init__(self):
        if self.latitude and self.longitude and \
                isinstance(self.latitude, (int, float)) and isinstance(self.longitude, (int, float)):
            if not (SOUTHERN_HEMISPHERE[1] <= self.latitude <= NORTHERN_HEMISPHERE[1]):
                raise ValueError(f"Latitude {self.latitude} out of Range !!")
            if not (WESTERN_HEMISPHERE[1] <= self.longitude <= EASTERN_HEMISPHERE[1]):
                raise ValueError(f"Longitude {self.longitude} out of Range !!")
        else:
            raise ValueError(f"Both Latitude/Longitude is required !!")

    def __repr__(self):
        return f"{self.__class__.__name__}" \
               f"{format_position(self.latitude, self.longitude)}"

    def __str__(self):
        return format_position(self.latitude, self.longitude)

    def __format__(self, format_spec):
        number_of_decimals = 2
        prefix, separator, suffix = format_spec.partition(".")
        if separator:
            number_of_decimals = int(suffix)
        lat = format(abs(self.latitude), f".{number_of_decimals}f")
        long = format(abs(self.longitude), f".{number_of_decimals}f")
        return format_position(lat, long)


@dataclasses.dataclass
class Location:
    name: str
    position: GeoPosition

    def __post_init__(self):
        if not self.name or self.position:
            raise ValueError("Name/Position cannot be Empty !!")
