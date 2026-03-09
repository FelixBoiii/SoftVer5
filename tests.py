import unittest
from curling import *
class TestGenerated(unittest.TestCase):
    
    def test_0(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-1.0950200504862426, 6.944297700598799), 12, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_1(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (7.70767131470665, -2.837857103250963), 5, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_2(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-5.585025290806424, -2.906564333058471), 1, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_3(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(False, (-3.700709036902998, -7.58254205964807), 2, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_4(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-6.848276691325179, -6.59862888393419), 12, False, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_5(self):
        obj_0 = Stone(False, (-0.6668944026363022, -1.8956845397387756), 3, False, False)
        
        var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
        var_2 = obj_0.distance_to_center()                        # Random method 2
        var_3 = obj_0.is_passed_hogline()                         # Random method 3
        var_4 = obj_0.is_in_house()
        var_5 = obj_0.is_out_of_play()
        var_6 = str(obj_0)
            
        
        self.assertEqual(var_1, True)
        self.assertEqual(var_2, 4.900762586075256)
        self.assertEqual(var_3, True)
        self.assertEqual(var_4, False)
        self.assertEqual(var_5, False)
        self.assertEqual(var_6, 'Yellow stone at (-2.17, -4.40), round 3, active')
                
        
    def test_6(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (2.3906341421852186, -3.2718662744390343), -1, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_7(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-3.872174373966679, -5.698078139055024), 8, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_8(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (0.10762151082315974, -2.6301561550692654), 11, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_9(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (5.917157020615591, 6.403400200312497), 7, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_10(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (7.478425458097131, 7.8418843741265345), 10, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_11(self):
        obj_0 = Stone(False, (2.4733262389787853, -0.8852443079864649), 5, True, False)
        
        var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
        var_2 = obj_0.distance_to_center()                        # Random method 2
        var_3 = obj_0.is_passed_hogline()                         # Random method 3
        var_4 = obj_0.is_in_house()
        var_5 = obj_0.is_out_of_play()
        var_6 = str(obj_0)
            
        
        self.assertEqual(var_1, True)
        self.assertEqual(var_2, 3.522391657984578)
        self.assertEqual(var_3, True)
        self.assertEqual(var_4, False)
        self.assertEqual(var_5, False)
        self.assertEqual(var_6, 'Yellow stone at (0.97, -3.39), round 5, active')
                
        
    def test_12(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (5.078366477933519, 0.19355725261157097), 1, False, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_13(self):
        with self.assertRaisesRegex(ValueError, "Cannot calculate distance to center for a burned stone."):
            obj_0 = Stone(False, (-1.1289715703552705, -0.9324070492968968), 5, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_14(self):
        with self.assertRaisesRegex(ValueError, "Cannot calculate distance to center for a burned stone."):
            obj_0 = Stone(False, (0.4019647907282078, -5.471786539002428), 5, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_15(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (5.253082216966979, -2.20343528005459), 3, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_16(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (1.194642482182939, -7.776514139421581), 0, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_17(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-7.563474952671987, -3.5759856095499565), 11, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_18(self):
        obj_0 = Stone(True, (1.645700436653387, 4.066339964501859), 5, True, False)
        
        var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
        var_2 = obj_0.distance_to_center()                        # Random method 2
        var_3 = obj_0.is_passed_hogline()                         # Random method 3
        var_4 = obj_0.is_in_house()
        var_5 = obj_0.is_out_of_play()
        var_6 = str(obj_0)
            
        
        self.assertEqual(var_1, True)
        self.assertEqual(var_2, 1.573101872618767)
        self.assertEqual(var_3, True)
        self.assertEqual(var_4, True)
        self.assertEqual(var_5, False)
        self.assertEqual(var_6, 'Red stone at (0.15, 1.57), round 5, active')
                
        
    def test_19(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (6.219237645115928, -0.4144942879519036), 5, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_20(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-4.428285646166335, -7.637089799957614), 11, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_21(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (2.7419588680713503, 7.365671367538601), 9, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_22(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (0.10353445456259713, -5.2627131915475385), -2, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_23(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (6.902021720436782, -1.9226891676989961), 6, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_24(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-3.727674457490293, 7.122528100285615), 4, False, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_25(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-6.322470148835151, 4.118588214506945), 8, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_26(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(False, (6.688789627921889, 6.621850376856894), 6, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_27(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (3.092116472769858, 3.6689135775165074), 9, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_28(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (3.1444348537758575, -3.5008907860806335), 4, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_29(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-1.3423206307303097, -3.5288118102883015), 12, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_30(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(False, (4.546864903383984, -5.515056535110201), 1, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_31(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-0.9092021666291927, 6.245758937433573), 8, False, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_32(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-2.068601967820655, -7.131451983364034), 2, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_33(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (4.070851323225819, 4.400417404819109), 9, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_34(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (4.957260316673111, 1.1868575625140743), -1, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_35(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-0.3227423362635182, 0.2250604820012061), -2, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_36(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-2.927179249044892, 1.1170181773037076), 11, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_37(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-2.0688086337747755, -4.187594695774623), 3, False, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_38(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-4.906239768276389, -3.761821949523396), 10, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_39(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (3.2618568212833914, 5.0406728302112285), 12, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_40(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-1.5026166939352823, 7.083175075293974), 11, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_41(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-1.819377727361644, 1.229114722763116), 8, False, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_42(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (0.47326152055042137, 4.079860512292436), -2, False, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_43(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (2.7197928232039708, 7.903182245480311), -2, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_44(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (-0.23073322664492757, -6.537437805005103), 9, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_45(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (7.8995170511256525, -6.772959070692952), 4, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_46(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(False, (0.3546112340415064, 5.5670994103057545), 8, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_47(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (2.433441062497902, -4.106215913978955), 5, False, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_48(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-0.16115691763485174, -5.752803198932554), 10, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_49(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-1.6471468983998605, 0.97038411392254), -1, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_50(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (3.95730568937784, -5.722059330573167), 6, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_51(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-2.644332092684298, -7.876064835377505), 12, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_52(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-1.7560635693689477, -5.512929479735412), 11, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_53(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-6.676777766470705, -1.8771394093933242), 1, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_54(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (4.142668231336579, 0.6681726219946196), -2, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_55(self):
        with self.assertRaisesRegex(ValueError, "Cannot calculate distance to center for a burned stone."):
            obj_0 = Stone(True, (-0.5690499194577967, -4.9001645422403275), 2, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_56(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (6.606790184742978, 7.71215736151062), 3, False, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_57(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-5.785019423226281, -2.559479888343496), 3, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_58(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (-3.509034785076116, 4.77926522542657), 2, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_59(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-4.601698275224546, -5.3920207488899585), -2, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_60(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (5.49301180078786, -1.6690891017481615), 0, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_61(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-1.4412818901292326, -7.1118240519748905), 2, False, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_62(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-6.305940370204111, -7.421063891513949), -1, False, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_63(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (-2.5554891942669133, 1.3596519580762383), 3, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_64(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-6.559635505745428, -2.634568826482079), -1, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_65(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-0.13052523525151294, 6.355935852344375), 3, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_66(self):
        with self.assertRaisesRegex(ValueError, "Cannot calculate distance to center for a burned stone."):
            obj_0 = Stone(True, (-1.4686576983135033, 2.8838985126147705), 2, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_67(self):
        with self.assertRaisesRegex(ValueError, "Cannot calculate distance to center for a burned stone."):
            obj_0 = Stone(True, (-1.687212324412533, 0.053554386298715784), 4, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_68(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-4.913013043552192, 3.5421202713500914), 8, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_69(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (-6.713831471295082, -6.242239016392265), 9, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_70(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(False, (0.6314430586714437, 6.063620772232486), 8, False, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_71(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (6.678089334194073, -5.016198467003086), 11, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_72(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (1.3930262807986118, 5.984708391937492), -1, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_73(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-3.0138346410755474, 3.098486924229764), -2, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_74(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (0.15099482534015962, 1.6635715646250429), -2, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_75(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (7.094207582263424, -5.059473105997633), 10, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_76(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (3.8308718258030403, 7.578557091400903), 11, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_77(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-5.890077591966865, 0.34049389710839506), 6, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_78(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (6.756486939557734, 4.423966104987928), 0, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_79(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(False, (0.9161552198431728, 6.024991965489383), 1, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_80(self):
        obj_0 = Stone(True, (0.13672021423866987, -3.038658167366089), 10, False, False)
        
        var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
        var_2 = obj_0.distance_to_center()                        # Random method 2
        var_3 = obj_0.is_passed_hogline()                         # Random method 3
        var_4 = obj_0.is_in_house()
        var_5 = obj_0.is_out_of_play()
        var_6 = str(obj_0)
            
        
        self.assertEqual(var_1, True)
        self.assertEqual(var_2, 5.703969325758734)
        self.assertEqual(var_3, True)
        self.assertEqual(var_4, False)
        self.assertEqual(var_5, False)
        self.assertEqual(var_6, 'Red stone at (-1.36, -5.54), round 10, active')
                
        
    def test_81(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (7.787009312939178, 6.075991210271887), 0, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_82(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (5.0078611753327245, -1.3804183969055046), 12, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_83(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-1.9998783801524276, 0.1709517926570534), 11, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_84(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(False, (-1.7004495370589936, 2.7411089699894635), 10, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_85(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (5.639445721384668, 2.7298173242518473), 5, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_86(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-5.2938700089195265, 7.475602000160521), 10, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_87(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (3.6657469640245655, -3.580390503395641), 12, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_88(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(False, (-7.841745134104876, -1.8179827162922422), 1, False, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_89(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(False, (-4.309232162715595, -4.554396613145618), 7, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_90(self):
        obj_0 = Stone(True, (0.9574305622627435, 0.36973312576458994), 2, False, False)
        
        var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
        var_2 = obj_0.distance_to_center()                        # Random method 2
        var_3 = obj_0.is_passed_hogline()                         # Random method 3
        var_4 = obj_0.is_in_house()
        var_5 = obj_0.is_out_of_play()
        var_6 = str(obj_0)
            
        
        self.assertEqual(var_1, True)
        self.assertEqual(var_2, 2.198276267949783)
        self.assertEqual(var_3, True)
        self.assertEqual(var_4, False)
        self.assertEqual(var_5, False)
        self.assertEqual(var_6, 'Red stone at (-0.54, -2.13), round 2, active')
                
        
    def test_91(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (4.455558698924344, 3.389266809246557), 12, False, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_92(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(False, (-3.4876312286452844, -2.7494279986678105), 1, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_93(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(False, (5.301188213685206, -7.935993725753679), 8, False, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_94(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (3.0077090685299392, -7.887560443673232), 7, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_95(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (6.235524514227222, 5.302542717484441), 0, True, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_96(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-3.601167567779667, 2.4601037167727284), 0, False, False)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_97(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(False, (4.30955565063425, -3.4846722941284796), 8, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_98(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-5.385703128255388, -3.9963988927143443), 6, True, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        
    def test_99(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-5.769776473345921, 0.038103323680529044), 1, False, True)
            
            var_1 = obj_0.move((-1.50, -2.50), 8, True)         # Random method 1
            var_2 = obj_0.distance_to_center()                        # Random method 2
            var_3 = obj_0.is_passed_hogline()                         # Random method 3
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_6 = str(obj_0)
                
        