import unittest

from concepts import oops_1


class ShippingTests(unittest.TestCase):

    def test_is_shipping_container_defined(self):
        self.assertTrue(oops_1.ShippingContainer("TVK", 20, ["food"]))

    def test_serial_number_assignment(self):
        container1 = oops_1.ShippingContainer("TVK", 20, ["food"])
        start_sno = container1.serial_number
        self.assertEqual(start_sno, container1.serial_number)
        container2 = oops_1.ShippingContainer("TVK", 20, ["food"])
        self.assertEqual(start_sno + 1, container2.serial_number)
        self.assertEqual(start_sno + 2, oops_1.ShippingContainer.next_serial_number)

    def test_create_empty_container(self):
        empty_container = oops_1.ShippingContainer.create_empty("TVK", 20)
        self.assertTrue(isinstance(empty_container, oops_1.ShippingContainer))
        self.assertEqual(empty_container.owner_code, "TVK", 20)
        self.assertTrue(len(empty_container.contents) == 0)

    def test_create_container_with_items(self):
        items_container = oops_1.ShippingContainer.create_with_items("TVK", 20, {"fish", "jewels"})
        self.assertTrue(isinstance(items_container, oops_1.ShippingContainer))
        self.assertTrue(isinstance(items_container.contents, list))
        self.assertEqual(items_container.owner_code, "TVK", 20)
        self.assertCountEqual(items_container.contents, ["fish", "jewels"])
        self.assertListEqual(sorted(items_container.contents), sorted(["fish", "jewels"]))

    def test_generate_bic_code(self):
        owner_code = "VINODH_KUMAR_THIMMISETTY"
        c1 = oops_1.ShippingContainer(owner_code=owner_code, length_in_feet=20, contents=["footware", "clothes"])
        bic_code = c1.bic_code
        self.assertEqual(len(bic_code), 11)
        self.assertEqual(bic_code[:3], owner_code[:3])
        self.assertEqual(bic_code[3], "U")

    def test_refrigerator_container_bic_code(self):
        owner_code = "VINODH_KUMAR_THIMMISETTY"
        r1 = oops_1.RefrigeratorShippingContainer.create_with_items(owner_code=owner_code,
                                                                    length_in_feet=20,
                                                                    contents=["fish", "crab"],
                                                                    celsius=2.0)
        self.assertEqual(r1.bic_code[3], "R")

    def test_refrigerator_container_temperature_is_within_range(self):
        self.assertRaises(ValueError,
                          oops_1.RefrigeratorShippingContainer,
                          "VInodh", 20, contents=["fish", "crab"], celsius=10)
        r1 = oops_1.RefrigeratorShippingContainer("VINODH", 20, contents=["fish", "crab"], celsius=3.0)
        self.assertEqual(r1.MAX_CELSIUS, 4.0)
        with self.assertRaises(ValueError):
            r1.celsius = 20

    def test_refrigerator_container_celsius_and_fahrenheit_conversions(self):
        r1 = oops_1.RefrigeratorShippingContainer("VINODH", 20, contents=["fish", "crab"], celsius=3.0)
        self.assertEqual(r1.fahrenheit, round(oops_1.RefrigeratorShippingContainer._cel_2_fah(3.0), 2))
        with self.assertRaises(ValueError):
            r1.fahrenheit = 100
        r1.fahrenheit = -32
        self.assertEqual(r1.celsius, round(oops_1.RefrigeratorShippingContainer._fah_2_cel(-32), 2))

    def test_container_measurements(self):
        c1 = oops_1.ShippingContainer.create_empty("VINODH", 20)
        self.assertEqual(c1.HEIGHT_IN_FEET, 8.5)
        self.assertEqual(c1.WIDTH_IN_FEET, 8)
        self.assertEqual(c1.length_in_feet, 20)
        self.assertEqual(c1.container_volume_ft3, 8.5 * 8 * 20)

        r1 = oops_1.RefrigeratorShippingContainer.create_empty("VINODH", 20, celsius=-10)
        self.assertEqual(r1.HEIGHT_IN_FEET, 8.5)
        self.assertEqual(r1.WIDTH_IN_FEET, 8)
        self.assertEqual(r1.length_in_feet, 20)
        self.assertEqual(r1.container_volume_ft3, (8.5 * 8 * 20) - 100)

    def test_heated_refrigerated_heated_container(self):
        h1 = oops_1.HeatedRefrigeratedShippingContainer.create_empty("VINODH", 20, celsius=-10)
        with self.assertRaises(ValueError):
            h1.celsius = 10
        with self.assertRaises(ValueError):
            h1.celsius = -100


if __name__ == '__main__':
    unittest.main()
