from unittest import TestCase
import area

class TestShapeArea(TestCase):

    def test_triangle_area(self):
        self.assertEqual(10, area.triangle_area(4,5))

    def test_triangle_area_floating_point(self):
        self.assertAlmostEqual(17.79875, area.triangle_area(7.25, 4.91))

    def test_triangle_negative_height_base_raises_value_exception(self):
        with self.assertRaises(ValueError):
            area.triangle_area(9,-10)

        with self.assertRaises(ValueError):
            area.triangle_area(-9,10)

        with self.assertRaises(ValueError):
            area.triangle_area(-9, -10)

    def test_triangle_area_zeros(self):
        self.assertEqual(0, area.triangle_area(0,0))

        self.assertEqual(0, area.triangle_area(10,0))

        self.assertEqual(0, area.triangle_area(0,4))

class TestShapeAreasCircles(TestCase):

    def test__circle_area(self):
        self.assertAlmostEqual(12.566370614359172, area.circle_area(2))
        
    def test_circle_area_radius_0(self): 
        self.assertAlmostEqual(0, area.circle_area(0))

    def test_circle_area_negative_radius(self):
        with self.assertRaises(ValueError):
            area.circle_area(-3)