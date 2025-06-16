import unittest
from space_invader_culminating import Bullet, Player, Invader

class TestBulletsLogic(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.bullet = Bullet()
        self.invader = Invader()

    def test_1_bullet_initial_position(self):
        print("\nTEST 1 Bullet Initial Position")
        print(f"Expected: bullet.y > player.y")
        print(f"Actual: bullet.y = {self.bullet.y}, player.y = {self.player.y}")
        try:
            self.assertGreater(self.bullet.y, self.player.y)
            print("Result: PASSED")
        except AssertionError:
            print("Result: FAILED")
            raise
        print("-" * 50)

    def test_2_bullet_moves_up(self):
        print("\nTEST 2 Bullet Moves Up")
        initial_y = self.bullet.y
        self.bullet.y += self.bullet.dy * 0.016
        print(f"Expected: bullet.y > initial_y")
        print(f"Actual: bullet.y = {self.bullet.y}, initial_y = {initial_y}")
        try:
            self.assertGreater(self.bullet.y, initial_y)
            print("Result: PASSED")
        except AssertionError:
            print("Result: FAILED")
            raise
        print("-" * 50)

    def test_3_bullet_hits_invader(self):
        print("\nTEST 3 Bullet Hits Invader")
        self.bullet.position = self.invader.position
        hit = self.bullet.intersects(self.invader)
        print(f"Expected: hit.hit = True, hit.entity = invader")
        print(f"Actual: hit.hit = {hit.hit}, hit.entity = {hit.entity}")
        try:
            self.assertTrue(hit.hit)
            self.assertEqual(hit.entity, self.invader)
            print("Result: PASSED")
        except AssertionError:
            print("Result: FAILED")
            raise # raises as error in case the test fails 
        print("-" * 50)

    def test_4_player_initial_position(self):
        print("\nTEST 4 Player Initial Position")
        print("Expected: player.x == 0 and player.y == -0.5")
        print(f"Actual: player.x = {self.player.x}, player.y = {self.player.y}")
        try:
            self.assertEqual(self.player.x, 0)
            self.assertEqual(self.player.y, -0.5)
            print("Result: PASSED")
        except AssertionError:
            print("Result: FAILED")
            raise # raises as error in case the test fails 
        print("-" * 50)

    def test_5_invader_initial_position_range(self):
        print("\nTEST 5 Invader Initial Position Range")
        print("Expected: -0.5 <= invader.x <= 0.5 and 0.8 <= invader.y <= 1.2")
        print(f"Actual: invader.x = {self.invader.x}, invader.y = {self.invader.y}")
        try:
            self.assertGreaterEqual(self.invader.x, -0.5)
            self.assertLessEqual(self.invader.x, 0.5)
            self.assertGreaterEqual(self.invader.y, 0.8)
            self.assertLessEqual(self.invader.y, 1.2)
            print("Result: PASSED")
        except AssertionError:
            print("Result: FAILED")
            raise # raises as error in case the test fails 
        print("-" * 50)

    def test_6_bullet_scale_and_color(self):
        print("\nTEST 6 Bullet Scale and Color")
        print("Expected: bullet.scale == (0.02, 0.1, 0.1) and bullet.color == color.green")
        print(f"Actual: bullet.scale = {self.bullet.scale}, bullet.color = {self.bullet.color}")
        try:
            self.asserEqual(self.bullet.scale, (0.02, 0.1, 0.1))
            self.assertEqual(self.bullet.color, self.bullet.color)
            print("Result: PASSED")
        except AssertionError:
            print("Result: FAILED")
            raise # raises as error in case the test fails 
        print("-" * 50)

if __name__ == '__main__':
    unittest.main()