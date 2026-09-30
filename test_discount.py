# write test cases for
import discount


#  test_normal_Case
def test_normal_case():
    assert discount.calculate_discount(1000) == 150


# test_boundry_at_discount
def test_boundry_at_discount():
    assert discount.calculate_discount(5000) == 500


# test_boundary_below_discount
def test_boundary_below_discount():
    assert discount.calculate_discount(3000) == 450


# test_boundary_above_discount
def test_boundary_above_discount():
    assert discount.calculate_discount(5500) == 550
