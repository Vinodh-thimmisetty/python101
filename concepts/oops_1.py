from random import randint


class ISO6346:

    @staticmethod
    def create(owner_code, category, serial_number):
        return owner_code[:3] + category + str(serial_number)[:6].zfill(6) + str(randint(0, 9))


class ShippingContainer:
    HEIGHT_IN_FEET = 8.5
    WIDTH_IN_FEET = 8

    next_serial_number = 123  # class attribute

    @classmethod
    def create_empty(cls, owner_code, length_in_feet, **kwargs):
        return cls(owner_code, length_in_feet, contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_in_feet, contents, **kwargs):
        return cls(owner_code, length_in_feet, contents=list(contents), **kwargs)

    @classmethod
    def _generate_sno(cls):
        result = cls.next_serial_number
        cls.next_serial_number += 1
        return result

    @staticmethod
    def _generate_bic_code(owner_code, serial_number=randint(1, 100000)):
        return ISO6346.create(owner_code=owner_code, category="U", serial_number=serial_number)

    def __init__(self, owner_code, length_in_feet, contents, **kwargs):
        self.owner_code = owner_code
        self.length_in_feet = length_in_feet
        self.contents = contents
        self.serial_number = ShippingContainer._generate_sno()
        self.bic_code = self._generate_bic_code(owner_code, serial_number=self.serial_number)

    @property
    def container_volume_ft3(self):
        return ShippingContainer.HEIGHT_IN_FEET * ShippingContainer.WIDTH_IN_FEET * self.length_in_feet


class RefrigeratorShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_IN_FEET = 100

    def __init__(self, owner_code, length_in_feet, contents, *, celsius, **kwargs):
        super().__init__(owner_code, length_in_feet, contents, **kwargs)
        self.celsius = celsius

    @staticmethod
    def _cel_2_fah(celsius):
        return celsius * (9 / 5) + 32

    @staticmethod
    def _fah_2_cel(fahrenheit):
        return (fahrenheit - 32) * (5 / 9)

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, celsius):
        self._set_celsius(celsius)

    def _set_celsius(self, celsius):
        if celsius > RefrigeratorShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature is Too Hot !!")
        self._celsius = round(celsius, 2)

    @property
    def fahrenheit(self):
        return RefrigeratorShippingContainer._cel_2_fah(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, fahrenheit):
        self.celsius = RefrigeratorShippingContainer._fah_2_cel(fahrenheit)

    @staticmethod
    def _generate_bic_code(owner_code, serial_number=randint(1, 100000)):
        return ISO6346.create(owner_code=owner_code, category="R", serial_number=serial_number)

    @property
    def container_volume_ft3(self):
        return super().container_volume_ft3 - RefrigeratorShippingContainer.FRIDGE_VOLUME_IN_FEET


class HeatedRefrigeratedShippingContainer(RefrigeratorShippingContainer):
    MIN_CELSIUS = -20.0

    def _set_celsius(self, celsius):
        if celsius < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temperature too Cold !!")
        super()._set_celsius(celsius)
