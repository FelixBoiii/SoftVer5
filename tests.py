import unittest
from curling import *
class TestGenerated(unittest.TestCase):
    
    def test_0(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        var_1 = obj_2.__str__()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, 'Game with 0 ends')
        
    def test_1(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (-2.9091734083845626, 5.177388046044722), 9, False, True)
            
            var_3 = obj_0.is_guard()
            obj_0.move_out_of_play()
            obj_0.move_out_of_play()
            var_6 = obj_0.is_in_house()
            var_7 = obj_0.is_in_house()
            var_0 = obj_0.__str__()
            var_2 = obj_0.is_in_house()
            var_4 = obj_0.is_out_of_bounds()
        
    def test_2(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
            obj_2 = Game()
            
            var_0 = obj_2.score()
            obj_2.add_end(End(False))
            var_3 = obj_2.score()
            obj_2.add_end(End(True))
        
    def test_3(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (7.929213867915768, -7.841941672147362), 8, False, False)
            
            var_0 = obj_0.move((-2.9690268322808713, -1.039294664625496), 0, True)
        
    def test_4(self):
        obj_2 = Game()
        
        var_3 = obj_2.red_winner()
        obj_2.add_end(End(False))
        var_1 = obj_2.red_winner()
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |    1 | Total\n----|------|------\nRed |    0 |     0\nYel | h  0 |     0\n')
        self.assertEqual(var_1, None)
        self.assertEqual(var_3, None)
        
    def test_5(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_0 = obj_1.done()
            var_2 = obj_1.overlaps_any_stone(Stone(False, (-1.0096483966269503, -4.577542491708748), -2, True, True))
            obj_1.add_stone(Stone(True, (-0.4404636946188578, 6.633452475864273), -2, True, True))
            var_3 = obj_1.drawn()
        
    def test_6(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (-3.2821326186226827, 5.093864543848378), 10, True, True)
            
            var_0 = obj_0.is_passed_hogline()
            obj_0.burn()
        
    def test_7(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_8(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-4.38371907158254, -6.757017521157541), 9, False, False)
            
            var_2 = obj_0.move((3.039923261214396, 0.013721255328642101), 12, True)
            var_1 = obj_0.is_passed_hogline()
            var_5 = obj_0.is_in_house()
            var_0 = obj_0.is_in_house()
            var_4 = obj_0.is_in_house()
            var_8 = obj_0.is_guard()
            var_9 = obj_0.move((3.917574472271111, -7.409567703530323), 8, False)
            obj_0.move_out_of_play()
            var_6 = obj_0.distance_to_center()
            var_7 = obj_0.move((-2.8228621461406487, -6.227757658751775), 2, True)
        
    def test_9(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        var_2 = obj_2.score()
        var_1 = obj_2.score()
        var_4 = obj_2.display_scoreboard()
        var_3 = obj_2.__str__()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, (0, 0))
        self.assertEqual(var_3, 'Game with 0 ends')
        self.assertEqual(var_4, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_10(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-5.25718808998438, 5.165132079404248), 4, True, False)
            
            var_0 = obj_0.is_out_of_bounds()
        
    def test_11(self):
        obj_1 = End(True)
        
        var_6 = obj_1.__str__()
        var_1 = obj_1.overlaps_any_stone(Stone(True, (-4.035734350370431, 2.516603297012086), 3, False, True))
        var_0 = obj_1.done()
        var_4 = obj_1.score()
        var_5 = obj_1.score()
        var_3 = obj_1.done()
        var_2 = obj_1.drawn()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, True)
        self.assertEqual(var_3, False)
        self.assertEqual(var_4, 0)
        self.assertEqual(var_5, 0)
        self.assertEqual(var_6, 'End with Red hammer and 0 stones')
        
    def test_12(self):
        with self.assertRaisesRegex(ValueError, "The first stone must be thrown by the team without the hammer."):
            obj_1 = End(True)
            
            var_3 = obj_1.__str__()
            obj_1.add_stone(Stone(True, (-0.20737511178984214, 7.648544673151605), 3, False, True))
            var_2 = obj_1.red_won()
            var_0 = obj_1.done()
            obj_1.add_stone(Stone(True, (5.315815274614428, -3.5251398418096453), 2, True, True))
        
    def test_13(self):
        obj_1 = End(False)
        
        var_0 = obj_1.done()
        var_1 = obj_1.score()
        var_2 = obj_1.drawn()
        var_3 = obj_1.red_won()
        var_6 = obj_1.__str__()
        var_5 = obj_1.score()
        var_4 = obj_1.drawn()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, 0)
        self.assertEqual(var_2, True)
        self.assertEqual(var_3, None)
        self.assertEqual(var_4, True)
        self.assertEqual(var_5, 0)
        self.assertEqual(var_6, 'End with Yellow hammer and 0 stones')
        
    def test_14(self):
        with self.assertRaisesRegex(ValueError, "The first stone must be thrown by the team without the hammer."):
            obj_1 = End(True)
            
            var_5 = obj_1.drawn()
            obj_1.add_stone(Stone(True, (1.0709440937631491, -7.244614239290135), 5, False, True))
            var_4 = obj_1.done()
            var_2 = obj_1.score()
            obj_1.add_stone(Stone(False, (1.0252055646674076, 0.31753238186650634), 10, False, True))
            obj_1.add_stone(Stone(True, (7.165932169500454, 3.045012308821086), 12, False, True))
        
    def test_15(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        
    def test_16(self):
        obj_2 = Game()
        
        obj_2.add_end(End(True))
        
        
    def test_17(self):
        obj_2 = Game()
        
        var_3 = obj_2.display_scoreboard()
        var_4 = obj_2.red_winner()
        var_1 = obj_2.__str__()
        var_2 = obj_2.display_scoreboard()
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_3, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_4, None)
        
    def test_18(self):
        obj_0 = Stone(True, (-0.2056371499244385, 0.7518327886582288), 6, True, False)
        
        var_2 = obj_0.is_guard()
        var_1 = obj_0.is_guard()
        var_0 = obj_0.is_guard()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, False)
        
    def test_19(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        var_2 = obj_2.score()
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 1 ends')
        self.assertEqual(var_2, (0, 0))
        
    def test_20(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (7.472241924490946, -3.6561235233515283), 11, True, True)
            
            var_0 = obj_0.is_out_of_play()
            var_2 = obj_0.is_in_house()
            var_6 = obj_0.distance_to_center()
            var_5 = obj_0.move((2.6583942143047548, -7.388910054760476), -1, True)
            var_3 = obj_0.is_passed_hogline()
            var_4 = obj_0.move((1.049977825381884, 2.6802537231539922), 7, False)
            var_1 = obj_0.is_in_house()
        
    def test_21(self):
        obj_1 = End(True)
        
        var_3 = obj_1.overlaps_any_stone(Stone(True, (2.2247621166282503, -1.4358142560561724), 10, True, True))
        var_1 = obj_1.overlaps_any_stone(Stone(True, (4.281948619087936, -4.273641173861678), 5, True, True))
        var_2 = obj_1.drawn()
        var_4 = obj_1.__str__()
        var_0 = obj_1.drawn()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, True)
        self.assertEqual(var_3, False)
        self.assertEqual(var_4, 'End with Red hammer and 0 stones')
        
    def test_22(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        
    def test_23(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        
    def test_24(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_25(self):
        obj_2 = Game()
        
        var_1 = obj_2.display_scoreboard()
        var_0 = obj_2.score()
        var_2 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, (0, 0))
        
    def test_26(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-7.9438104518281225, -6.310347854110905), 2, True, False)
            
            var_3 = obj_0.is_out_of_play()
            var_7 = obj_0.is_out_of_bounds()
            var_4 = obj_0.__str__()
            var_9 = obj_0.__str__()
            var_0 = obj_0.__str__()
            var_8 = obj_0.is_guard()
            var_1 = obj_0.move((4.695834428593841, -7.623460619424643), 0, True)
            var_2 = obj_0.is_guard()
            obj_0.move_out_of_play()
            obj_0.burn()
        
    def test_27(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        
        
    def test_28(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_1 = obj_1.overlaps_any_stone(Stone(True, (7.792011347431117, 0.8486801962652688), 4, False, False))
            var_2 = obj_1.score()
            var_0 = obj_1.red_won()
        
    def test_29(self):
        with self.assertRaisesRegex(ValueError, "Stone's hammer status does not match the end's hammer status."):
            obj_1 = End(False)
            
            var_4 = obj_1.done()
            var_2 = obj_1.drawn()
            var_1 = obj_1.overlaps_any_stone(Stone(False, (-0.13992721749676562, 1.8132954338733942), 9, True, True))
            var_0 = obj_1.__str__()
            var_3 = obj_1.score()
            obj_1.add_stone(Stone(True, (-0.009535144868600298, 3.238053289737662), 4, True, True))
            var_6 = obj_1.overlaps_any_stone(Stone(True, (5.96087007745237, 3.650651567026955), 1, False, True))
        
    def test_30(self):
        obj_1 = End(True)
        
        var_0 = obj_1.red_won()
        var_1 = obj_1.drawn()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, True)
        
    def test_31(self):
        obj_2 = Game()
        
        var_2 = obj_2.__str__()
        var_4 = obj_2.display_scoreboard()
        var_3 = obj_2.display_scoreboard()
        var_0 = obj_2.__str__()
        var_1 = obj_2.score()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_4, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_32(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        
    def test_33(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            obj_1.add_stone(Stone(False, (-0.21568055912281991, 5.938905191153891), 10, False, False))
            var_1 = obj_1.done()
            var_2 = obj_1.score()
            obj_1.add_stone(Stone(False, (-0.6105290510984869, 1.494515527251421), 2, False, False))
            obj_1.add_stone(Stone(True, (1.1146307059846539, 5.192980661234397), 2, False, False))
            var_0 = obj_1.red_won()
        
    def test_34(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        obj_2.add_end(End(True))
        var_2 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_2, 'Game with 1 ends')
        
    def test_35(self):
        obj_1 = End(True)
        
        var_0 = obj_1.red_won()
        
        self.assertEqual(var_0, None)
        
    def test_36(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        
    def test_37(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-3.739399985698567, -6.379898249534355), -2, True, True)
            
            obj_0.burn()
            var_0 = obj_0.is_passed_hogline()
        
    def test_38(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-5.925375490338915, -0.33945855515486656), -1, True, False)
            
            var_1 = obj_0.is_guard()
            var_3 = obj_0.is_passed_hogline()
            var_0 = obj_0.move((7.227661716478078, -6.949102007942873), 0, True)
            obj_0.move_out_of_play()
        
    def test_39(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-0.8016083499413025, -3.8466422149879236), -2, True, True)
            
            obj_0.move_out_of_play()
            var_1 = obj_0.__str__()
            var_3 = obj_0.is_out_of_bounds()
            var_0 = obj_0.is_out_of_bounds()
        
    def test_40(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-1.6385695577913424, 5.383408762254824), 12, True, False)
            
            obj_0.move_out_of_play()
            obj_0.move_out_of_play()
            var_2 = obj_0.is_in_house()
        
    def test_41(self):
        obj_1 = End(False)
        
        var_4 = obj_1.drawn()
        var_0 = obj_1.done()
        var_3 = obj_1.red_won()
        var_1 = obj_1.drawn()
        var_2 = obj_1.done()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, True)
        self.assertEqual(var_2, False)
        self.assertEqual(var_3, None)
        self.assertEqual(var_4, True)
        
    def test_42(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        
    def test_43(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_44(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (-0.030490103887355957, 6.348878105358077), 4, False, True)
            
            obj_0.move_out_of_play()
            var_2 = obj_0.is_in_house()
            var_1 = obj_0.__str__()
            obj_0.move_out_of_play()
            var_5 = obj_0.__str__()
            var_4 = obj_0.is_in_house()
            var_3 = obj_0.__str__()
        
    def test_45(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-3.1971791960847664, 4.2961724926777904), 0, False, False)
            
            var_2 = obj_0.is_guard()
            var_3 = obj_0.is_in_house()
            var_0 = obj_0.distance_to_center()
            var_1 = obj_0.is_out_of_play()
            var_4 = obj_0.is_in_house()
        
    def test_46(self):
        with self.assertRaisesRegex(ValueError, "Stone's round does not match the expected round based on the number of stones already placed."):
            obj_1 = End(False)
            
            obj_1.add_stone(Stone(True, (-7.366516568888212, 1.9374550839906846), 3, False, True))
            var_1 = obj_1.drawn()
            var_0 = obj_1.done()
            obj_1.add_stone(Stone(False, (6.97017205873709, -1.343620515321307), 1, False, False))
            var_4 = obj_1.red_won()
        
    def test_47(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-2.1654390686271796, 2.717523593517331), 0, False, True)
            
            obj_0.burn()
        
    def test_48(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_0 = obj_1.done()
            var_6 = obj_1.red_won()
            var_4 = obj_1.done()
            var_5 = obj_1.score()
            var_3 = obj_1.red_won()
            var_1 = obj_1.overlaps_any_stone(Stone(True, (7.719708513579411, 6.614167274779888), -1, True, True))
            var_2 = obj_1.overlaps_any_stone(Stone(True, (-1.7550902527629937, -2.3985768332253947), 5, False, False))
        
    def test_49(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (4.803680687982904, 2.19774205857375), 1, False, False)
            
            var_2 = obj_0.is_out_of_bounds()
            var_3 = obj_0.move((3.2195517699612672, -0.021187452847897248), 12, False)
            var_1 = obj_0.is_in_house()
            var_4 = obj_0.distance_to_center()
            var_0 = obj_0.distance_to_center()
        
    def test_50(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_5 = obj_1.red_won()
            var_3 = obj_1.done()
            var_2 = obj_1.drawn()
            var_0 = obj_1.score()
            var_4 = obj_1.overlaps_any_stone(Stone(False, (3.6002571543181237, -4.966308852757109), -1, False, True))
            var_1 = obj_1.drawn()
        
    def test_51(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (6.16401779071405, -4.494452704546308), 8, True, False)
            
            obj_0.burn()
        
    def test_52(self):
        obj_1 = End(False)
        
        var_4 = obj_1.__str__()
        var_2 = obj_1.drawn()
        var_3 = obj_1.__str__()
        var_6 = obj_1.done()
        var_5 = obj_1.overlaps_any_stone(Stone(False, (-4.266743151994968, 5.510492482706351), 9, True, True))
        var_0 = obj_1.drawn()
        var_1 = obj_1.__str__()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, 'End with Yellow hammer and 0 stones')
        self.assertEqual(var_2, True)
        self.assertEqual(var_3, 'End with Yellow hammer and 0 stones')
        self.assertEqual(var_4, 'End with Yellow hammer and 0 stones')
        self.assertEqual(var_5, False)
        self.assertEqual(var_6, False)
        
    def test_53(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (3.864170756633916, -3.4924517335213263), 12, True, False)
            
            var_3 = obj_0.move((-0.16236509081447004, 3.079839346024139), -2, False)
            obj_0.burn()
            obj_0.move_out_of_play()
            var_5 = obj_0.is_in_house()
            var_4 = obj_0.distance_to_center()
            var_6 = obj_0.is_out_of_play()
            var_7 = obj_0.__str__()
            var_0 = obj_0.is_out_of_play()
            var_1 = obj_0.distance_to_center()
            obj_0.move_out_of_play()
        
    def test_54(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_2 = obj_1.done()
            obj_1.add_stone(Stone(False, (-5.914156033799527, -1.6959033866012572), 9, True, False))
            var_0 = obj_1.done()
            var_3 = obj_1.drawn()
            obj_1.add_stone(Stone(False, (3.1131092182786446, 6.055252637284466), 8, False, False))
        
    def test_55(self):
        obj_2 = Game()
        
        var_2 = obj_2.score()
        var_0 = obj_2.__str__()
        var_1 = obj_2.score()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, (0, 0))
        
    def test_56(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (-7.816350062852614, 2.4784166763151063), 10, True, False)
            
            var_4 = obj_0.is_in_house()
            var_2 = obj_0.distance_to_center()
            var_6 = obj_0.is_out_of_play()
            var_1 = obj_0.move((1.34199827101647, -0.9362919777028402), -1, True)
            var_3 = obj_0.move((1.9544706830296317, 7.001187371996352), 2, True)
            var_0 = obj_0.is_guard()
            var_5 = obj_0.is_in_house()
        
    def test_57(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        var_1 = obj_2.display_scoreboard()
        var_2 = obj_2.__str__()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, 'Game with 0 ends')
        
    def test_58(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_0 = obj_1.red_won()
            var_1 = obj_1.overlaps_any_stone(Stone(True, (-1.6155457414292762, 6.940532893275421), 2, True, False))
        
    def test_59(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        obj_2.add_end(End(True))
        var_1 = obj_2.__str__()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, 'Game with 1 ends')
        
    def test_60(self):
        obj_1 = End(False)
        
        var_1 = obj_1.overlaps_any_stone(Stone(True, (-6.769806980565649, -7.3075769166601106), 4, True, True))
        var_0 = obj_1.score()
        var_2 = obj_1.__str__()
        
        self.assertEqual(var_0, 0)
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, 'End with Yellow hammer and 0 stones')
        
    def test_61(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        
    def test_62(self):
        obj_2 = Game()
        
        var_2 = obj_2.display_scoreboard()
        obj_2.add_end(End(False))
        obj_2.add_end(End(False))
        obj_2.add_end(End(False))
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |    1 |    2 |    3 | Total\n----|------|------|------|------\nRed |    0 |    0 |    0 |     0\nYel | h  0 | h  0 | h  0 |     0\n')
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_63(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_0 = obj_1.red_won()
            var_5 = obj_1.drawn()
            obj_1.add_stone(Stone(True, (5.646598125300033, -4.229483396336036), 11, True, False))
            var_3 = obj_1.done()
            var_1 = obj_1.red_won()
            var_4 = obj_1.drawn()
            var_6 = obj_1.score()
        
    def test_64(self):
        obj_2 = Game()
        
        var_1 = obj_2.score()
        var_2 = obj_2.display_scoreboard()
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_65(self):
        obj_2 = Game()
        
        var_1 = obj_2.__str__()
        var_0 = obj_2.score()
        var_3 = obj_2.display_scoreboard()
        var_2 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, (0, 0))
        self.assertEqual(var_3, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_66(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        obj_2.add_end(End(False))
        var_2 = obj_2.display_scoreboard()
        var_4 = obj_2.score()
        var_3 = obj_2.score()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, 'End |    1 | Total\n----|------|------\nRed |    0 |     0\nYel | h  0 |     0\n')
        self.assertEqual(var_3, (0, 0))
        self.assertEqual(var_4, (0, 0))
        
    def test_67(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        var_1 = obj_2.__str__()
        var_2 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, (0, 0))
        
    def test_68(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (4.136440728919171, 6.941391586672312), 8, False, False)
            
            var_1 = obj_0.is_passed_hogline()
            var_0 = obj_0.distance_to_center()
            var_2 = obj_0.move((3.8718873977575985, 4.182205385403954), 11, True)
        
    def test_69(self):
        obj_2 = Game()
        
        var_2 = obj_2.__str__()
        var_1 = obj_2.display_scoreboard()
        var_0 = obj_2.display_scoreboard()
        obj_2.add_end(End(False))
        var_3 = obj_2.score()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, (0, 0))
        
    def test_70(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-6.066073991616477, 5.518671979311986), 11, True, True)
            
            var_2 = obj_0.move((0.4929193749402625, -7.8243973867955745), 11, True)
            var_4 = obj_0.is_in_house()
            var_0 = obj_0.move((-6.2105553225235255, -7.660413507432009), 8, False)
            obj_0.move_out_of_play()
            var_1 = obj_0.__str__()
        
    def test_71(self):
        obj_2 = Game()
        
        var_1 = obj_2.score()
        var_3 = obj_2.__str__()
        var_0 = obj_2.score()
        var_2 = obj_2.__str__()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, 'Game with 0 ends')
        
    def test_72(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_3 = obj_1.drawn()
            var_5 = obj_1.__str__()
            obj_1.add_stone(Stone(False, (4.419951516299104, 6.798507932523108), 9, False, False))
            var_0 = obj_1.overlaps_any_stone(Stone(True, (1.2627413529652447, -7.4959371871116165), 6, True, True))
            var_4 = obj_1.score()
            var_1 = obj_1.__str__()
            var_2 = obj_1.red_won()
        
    def test_73(self):
        obj_1 = End(True)
        
        var_3 = obj_1.score()
        var_2 = obj_1.red_won()
        var_0 = obj_1.red_won()
        var_1 = obj_1.__str__()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'End with Red hammer and 0 stones')
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, 0)
        
    def test_74(self):
        obj_1 = End(True)
        
        var_0 = obj_1.score()
        
        self.assertEqual(var_0, 0)
        
    def test_75(self):
        obj_1 = End(True)
        
        var_1 = obj_1.done()
        var_2 = obj_1.done()
        var_0 = obj_1.score()
        
        self.assertEqual(var_0, 0)
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, False)
        
    def test_76(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (-5.403637757837613, -6.413203045112139), 5, True, True)
            
            obj_0.move_out_of_play()
            var_1 = obj_0.move((3.8602431210488835, -4.593063553650548), 7, False)
        
    def test_77(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-6.330727131434424, -5.059966235887783), 8, True, False)
            
            var_6 = obj_0.is_out_of_bounds()
            var_4 = obj_0.distance_to_center()
            var_0 = obj_0.move((-3.2368238828591167, -2.1886418229884494), 3, True)
            var_2 = obj_0.move((4.991955043072098, -7.249267342940163), 0, False)
            obj_0.burn()
            var_1 = obj_0.is_out_of_bounds()
            var_5 = obj_0.__str__()
        
    def test_78(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        var_1 = obj_2.__str__()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'Game with 0 ends')
        
    def test_79(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-7.934746685511335, 1.119788231672958), 2, True, False)
            
            var_6 = obj_0.is_out_of_play()
            var_3 = obj_0.distance_to_center()
            var_4 = obj_0.is_in_house()
            var_2 = obj_0.is_guard()
            var_5 = obj_0.is_passed_hogline()
            var_0 = obj_0.is_guard()
            obj_0.burn()
            var_1 = obj_0.is_in_house()
        
    def test_80(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-2.522436646209977, 7.719559138455105), -2, True, True)
            
            var_2 = obj_0.__str__()
            var_4 = obj_0.is_in_house()
            var_8 = obj_0.is_out_of_play()
            var_0 = obj_0.is_passed_hogline()
            var_7 = obj_0.is_guard()
            var_3 = obj_0.move((0.9222647202144962, -6.069635646563388), 11, False)
            obj_0.burn()
            obj_0.burn()
            var_1 = obj_0.is_out_of_play()
            var_6 = obj_0.is_guard()
        
    def test_81(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-4.001359269404658, -0.8771090716097429), 0, True, False)
            
            var_7 = obj_0.is_passed_hogline()
            var_6 = obj_0.distance_to_center()
            var_5 = obj_0.__str__()
            var_2 = obj_0.move((-3.6277969935462924, 7.954746703402854), 5, True)
            obj_0.move_out_of_play()
            var_4 = obj_0.is_guard()
            var_0 = obj_0.is_passed_hogline()
            obj_0.move_out_of_play()
        
    def test_82(self):
        obj_2 = Game()
        
        obj_2.add_end(End(True))
        
        
    def test_83(self):
        obj_2 = Game()
        
        var_1 = obj_2.display_scoreboard()
        var_4 = obj_2.__str__()
        obj_2.add_end(End(False))
        obj_2.add_end(End(False))
        var_2 = obj_2.display_scoreboard()
        
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, 'End |    1 |    2 | Total\n----|------|------|------\nRed |    0 |    0 |     0\nYel | h  0 | h  0 |     0\n')
        self.assertEqual(var_4, 'Game with 0 ends')
        
    def test_84(self):
        with self.assertRaisesRegex(ValueError, "Stone's round does not match the expected round based on the number of stones already placed."):
            obj_1 = End(False)
            
            obj_1.add_stone(Stone(True, (-1.5550301189440692, 1.447999107830828), 2, False, False))
            var_1 = obj_1.score()
            var_2 = obj_1.done()
        
    def test_85(self):
        with self.assertRaisesRegex(ValueError, "The first stone must be thrown by the team without the hammer."):
            obj_1 = End(False)
            
            var_2 = obj_1.done()
            obj_1.add_stone(Stone(False, (4.907509760550861, -5.715764249471301), 7, False, True))
            obj_1.add_stone(Stone(False, (-2.362217849241956, 7.43917427509273), 9, False, True))
            var_1 = obj_1.red_won()
        
    def test_86(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_0 = obj_1.red_won()
            obj_1.add_stone(Stone(False, (4.134686135726751, 1.3823631633874687), 11, True, True))
        
    def test_87(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-1.2073244348735983, -3.349406721714109), 12, True, True)
            
            var_6 = obj_0.is_guard()
            obj_0.burn()
            var_7 = obj_0.is_out_of_play()
            var_4 = obj_0.is_out_of_bounds()
            var_5 = obj_0.is_passed_hogline()
            var_2 = obj_0.is_in_house()
            var_1 = obj_0.distance_to_center()
            var_3 = obj_0.is_in_house()
        
    def test_88(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_3 = obj_1.red_won()
            var_4 = obj_1.overlaps_any_stone(Stone(False, (2.74239221551767, 1.8489526114406836), 2, True, True))
            obj_1.add_stone(Stone(False, (-3.2479809952907264, -4.0709934471364715), 0, True, False))
            var_0 = obj_1.__str__()
            var_1 = obj_1.__str__()
        
    def test_89(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-2.894846415008548, 1.5297597428247407), 2, True, False)
            
            obj_0.move_out_of_play()
            var_0 = obj_0.is_guard()
        
    def test_90(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (4.01560776449873, 0.4195448596091964), 3, False, True)
            
            var_8 = obj_0.is_out_of_bounds()
            var_5 = obj_0.__str__()
            obj_0.burn()
            obj_0.burn()
            var_3 = obj_0.is_out_of_play()
            var_1 = obj_0.is_passed_hogline()
            obj_0.move_out_of_play()
            var_0 = obj_0.is_in_house()
            var_6 = obj_0.is_passed_hogline()
        
    def test_91(self):
        obj_2 = Game()
        
        var_2 = obj_2.display_scoreboard()
        var_1 = obj_2.score()
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_92(self):
        with self.assertRaisesRegex(ValueError, "The first stone must be thrown by the team without the hammer."):
            obj_1 = End(False)
            
            var_6 = obj_1.score()
            var_4 = obj_1.drawn()
            var_3 = obj_1.drawn()
            obj_1.add_stone(Stone(False, (5.8530511769502365, -0.6760366445407691), 3, False, True))
            var_1 = obj_1.drawn()
            var_0 = obj_1.__str__()
            obj_1.add_stone(Stone(True, (-1.7738949598813978, 4.323909095120079), 11, False, False))
        
    def test_93(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_3 = obj_1.done()
            var_0 = obj_1.red_won()
            var_2 = obj_1.drawn()
            var_1 = obj_1.overlaps_any_stone(Stone(True, (5.818367952168117, -6.456957167234426), 7, False, False))
        
    def test_94(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_1 = obj_1.overlaps_any_stone(Stone(False, (4.3635483554187715, -6.4405438304492595), -2, True, False))
            obj_1.add_stone(Stone(True, (5.425726087443902, -2.625643756775723), 1, False, True))
            obj_1.add_stone(Stone(False, (-3.402289240938382, -3.63785194913736), 12, True, False))
            var_3 = obj_1.score()
        
    def test_95(self):
        obj_2 = Game()
        
        obj_2.add_end(End(True))
        var_2 = obj_2.__str__()
        var_0 = obj_2.red_winner()
        var_3 = obj_2.score()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_2, 'Game with 1 ends')
        self.assertEqual(var_3, (0, 0))
        
    def test_96(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (3.2704705152697073, 1.8612158737833813), 7, True, False)
            
            var_0 = obj_0.is_guard()
            obj_0.burn()
            var_9 = obj_0.is_in_house()
            var_7 = obj_0.distance_to_center()
            var_1 = obj_0.is_guard()
            var_8 = obj_0.move((-4.265103538058463, 4.336775838511995), 4, False)
            var_6 = obj_0.distance_to_center()
            var_3 = obj_0.is_out_of_play()
            var_5 = obj_0.distance_to_center()
            obj_0.move_out_of_play()
        
    def test_97(self):
        with self.assertRaisesRegex(ValueError, "Cannot calculate distance to center for a burned stone."):
            obj_0 = Stone(True, (6.043570161866047, -2.1856715672377405), 10, True, True)
            
            var_0 = obj_0.is_out_of_bounds()
            var_1 = obj_0.is_passed_hogline()
            var_7 = obj_0.is_out_of_bounds()
            var_2 = obj_0.distance_to_center()
            var_4 = obj_0.move((6.535984721807619, -1.308757692090511), -2, True)
            var_3 = obj_0.is_in_house()
            var_5 = obj_0.is_passed_hogline()
            var_6 = obj_0.move((3.4244482922275896, 3.544744301207311), -1, True)
        
    def test_98(self):
        obj_1 = End(True)
        
        var_2 = obj_1.red_won()
        var_4 = obj_1.red_won()
        var_0 = obj_1.overlaps_any_stone(Stone(True, (0.4853118861218171, 5.5609292978350275), 5, False, True))
        var_3 = obj_1.done()
        var_1 = obj_1.red_won()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, False)
        self.assertEqual(var_4, None)
        
    def test_99(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        
        
    def test_100(self):
        obj_2 = Game()
        
        var_3 = obj_2.display_scoreboard()
        obj_2.add_end(End(False))
        var_0 = obj_2.score()
        obj_2.add_end(End(False))
        var_2 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_2, 'End |    1 |    2 | Total\n----|------|------|------\nRed |    0 |    0 |     0\nYel | h  0 | h  0 |     0\n')
        self.assertEqual(var_3, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_101(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        
    def test_102(self):
        obj_1 = End(False)
        
        var_0 = obj_1.score()
        
        self.assertEqual(var_0, 0)
        
    def test_103(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_4 = obj_1.overlaps_any_stone(Stone(False, (-7.774934462809725, -4.871442326613147), -1, False, True))
            var_5 = obj_1.done()
            var_2 = obj_1.score()
            var_1 = obj_1.red_won()
            var_0 = obj_1.score()
            var_3 = obj_1.overlaps_any_stone(Stone(False, (4.042180676428313, 6.976256391389667), 2, False, True))
        
    def test_104(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_0, None)
        
    def test_105(self):
        with self.assertRaisesRegex(ValueError, "The first stone must be thrown by the team without the hammer."):
            obj_1 = End(True)
            
            var_2 = obj_1.overlaps_any_stone(Stone(True, (3.5736462180414037, -0.9524883887868132), 4, False, True))
            var_1 = obj_1.done()
            obj_1.add_stone(Stone(True, (-1.7556430218330945, 0.4877004309782187), 1, False, True))
            var_0 = obj_1.done()
            var_4 = obj_1.overlaps_any_stone(Stone(True, (0.6307546565785902, 0.5891319270888022), 4, True, False))
        
    def test_106(self):
        obj_1 = End(True)
        
        var_0 = obj_1.__str__()
        var_2 = obj_1.drawn()
        var_1 = obj_1.score()
        var_5 = obj_1.score()
        var_3 = obj_1.done()
        var_4 = obj_1.red_won()
        
        self.assertEqual(var_0, 'End with Red hammer and 0 stones')
        self.assertEqual(var_1, 0)
        self.assertEqual(var_2, True)
        self.assertEqual(var_3, False)
        self.assertEqual(var_4, None)
        self.assertEqual(var_5, 0)
        
    def test_107(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (0.4280344930580906, 2.8289163722311343), 0, True, True)
            
            var_1 = obj_0.is_in_house()
            var_2 = obj_0.is_guard()
            obj_0.burn()
            var_3 = obj_0.is_passed_hogline()
            obj_0.burn()
        
    def test_108(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-4.351158051458812, 7.374865546391282), 9, False, True)
            
            var_3 = obj_0.__str__()
            var_0 = obj_0.is_guard()
            var_1 = obj_0.move((3.154555794659599, -7.762095863691988), -1, True)
            var_2 = obj_0.is_out_of_bounds()
        
    def test_109(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (6.909083357098709, -6.660806688857541), -2, True, True)
            
            var_2 = obj_0.is_out_of_play()
            var_1 = obj_0.move((-4.339766473266607, 7.2460982807056045), 1, True)
            var_4 = obj_0.is_guard()
            obj_0.burn()
            var_6 = obj_0.is_out_of_bounds()
            obj_0.move_out_of_play()
            obj_0.burn()
        
    def test_110(self):
        obj_1 = End(True)
        
        var_0 = obj_1.red_won()
        var_3 = obj_1.score()
        var_2 = obj_1.score()
        var_1 = obj_1.score()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 0)
        self.assertEqual(var_2, 0)
        self.assertEqual(var_3, 0)
        
    def test_111(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_1 = obj_1.drawn()
            var_0 = obj_1.red_won()
            var_4 = obj_1.__str__()
            var_3 = obj_1.__str__()
            var_2 = obj_1.overlaps_any_stone(Stone(True, (6.801543616351397, 1.548179959501443), 0, True, False))
            var_5 = obj_1.overlaps_any_stone(Stone(False, (-3.8955326302153903, 0.218934587606892), 3, False, True))
        
    def test_112(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_4 = obj_1.overlaps_any_stone(Stone(True, (0.4471229244567638, -6.701313462445993), 12, False, False))
            var_2 = obj_1.done()
            var_1 = obj_1.score()
            var_3 = obj_1.drawn()
            var_0 = obj_1.red_won()
        
    def test_113(self):
        obj_1 = End(False)
        
        var_2 = obj_1.overlaps_any_stone(Stone(True, (-2.3030008090306335, -7.236711835707505), 4, False, True))
        var_3 = obj_1.score()
        var_6 = obj_1.score()
        var_0 = obj_1.score()
        var_4 = obj_1.red_won()
        var_5 = obj_1.__str__()
        var_1 = obj_1.score()
        
        self.assertEqual(var_0, 0)
        self.assertEqual(var_1, 0)
        self.assertEqual(var_2, False)
        self.assertEqual(var_3, 0)
        self.assertEqual(var_4, None)
        self.assertEqual(var_5, 'End with Yellow hammer and 0 stones')
        self.assertEqual(var_6, 0)
        
    def test_114(self):
        obj_1 = End(True)
        
        var_0 = obj_1.drawn()
        
        self.assertEqual(var_0, True)
        
    def test_115(self):
        obj_1 = End(True)
        
        var_1 = obj_1.red_won()
        var_0 = obj_1.overlaps_any_stone(Stone(False, (1.418331535400661, 0.2165735896115546), 8, False, True))
        var_5 = obj_1.done()
        var_4 = obj_1.drawn()
        var_3 = obj_1.drawn()
        var_2 = obj_1.done()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, False)
        self.assertEqual(var_3, True)
        self.assertEqual(var_4, True)
        self.assertEqual(var_5, False)
        
    def test_116(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(False, (0.5777203613974358, 0.6438924692381267), 2, True, False)
            
            var_5 = obj_0.is_in_house()
            var_0 = obj_0.move((-1.9906654357270774, 6.420035491229811), 1, True)
            var_3 = obj_0.move((-0.9526772794245222, -2.476461275252298), 3, True)
            var_2 = obj_0.is_in_house()
            var_1 = obj_0.move((1.984081371368001, 4.282373511506949), 3, False)
            var_4 = obj_0.is_in_house()
            obj_0.burn()
            var_7 = obj_0.is_out_of_play()
            var_6 = obj_0.is_passed_hogline()
        
    def test_117(self):
        obj_2 = Game()
        
        var_2 = obj_2.display_scoreboard()
        var_0 = obj_2.__str__()
        var_1 = obj_2.score()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_118(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (-7.389748280829192, -7.523832441235294), 8, True, False)
            
            obj_0.move_out_of_play()
            var_1 = obj_0.is_passed_hogline()
            var_7 = obj_0.is_out_of_bounds()
            var_5 = obj_0.is_passed_hogline()
            var_6 = obj_0.distance_to_center()
            var_3 = obj_0.is_out_of_play()
            var_4 = obj_0.is_in_house()
            var_2 = obj_0.move((0.06582174754313108, 1.0237375836731974), 3, False)
        
    def test_119(self):
        obj_2 = Game()
        
        var_1 = obj_2.score()
        obj_2.add_end(End(False))
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 1 ends')
        self.assertEqual(var_1, (0, 0))
        
    def test_120(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        var_1 = obj_2.__str__()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, 'Game with 0 ends')
        
    def test_121(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (3.071554279174915, 0.3592189820255989), 9, False, False)
            
            var_2 = obj_0.distance_to_center()
            var_6 = obj_0.distance_to_center()
            var_8 = obj_0.__str__()
            var_1 = obj_0.is_in_house()
            obj_0.burn()
            var_0 = obj_0.move((6.257336292640057, 2.67699517021698), -2, True)
            var_4 = obj_0.move((5.370722570066995, 0.9122569918854229), 0, True)
            var_3 = obj_0.is_out_of_bounds()
            obj_0.move_out_of_play()
        
    def test_122(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_0 = obj_1.overlaps_any_stone(Stone(False, (-5.753260165224912, 6.115760292213768), 5, True, False))
            var_3 = obj_1.__str__()
            var_4 = obj_1.__str__()
            var_2 = obj_1.done()
            var_1 = obj_1.__str__()
        
    def test_123(self):
        obj_1 = End(False)
        
        var_1 = obj_1.red_won()
        var_3 = obj_1.score()
        var_0 = obj_1.score()
        var_2 = obj_1.__str__()
        var_4 = obj_1.red_won()
        
        self.assertEqual(var_0, 0)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 'End with Yellow hammer and 0 stones')
        self.assertEqual(var_3, 0)
        self.assertEqual(var_4, None)
        
    def test_124(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-1.8085135418674643, -0.9959517452637989), 4, True, False)
            
            var_5 = obj_0.is_guard()
            var_3 = obj_0.distance_to_center()
            var_0 = obj_0.is_out_of_bounds()
            var_2 = obj_0.is_out_of_bounds()
            var_6 = obj_0.move((7.393121675515401, -7.478069330338123), 8, True)
            var_4 = obj_0.is_in_house()
            var_1 = obj_0.move((-5.828993902257901, 2.14181126109653), 8, True)
        
    def test_125(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (4.5665571679579156, 3.234964157442997), 12, False, False)
            
            var_5 = obj_0.is_guard()
            obj_0.burn()
            var_3 = obj_0.is_guard()
            obj_0.move_out_of_play()
            var_2 = obj_0.is_out_of_bounds()
            var_7 = obj_0.is_out_of_play()
            obj_0.burn()
            var_0 = obj_0.is_out_of_play()
            var_1 = obj_0.move((-7.503788417093542, -6.5314920522166755), 5, False)
            var_4 = obj_0.distance_to_center()
        
    def test_126(self):
        obj_0 = Stone(True, (-2.0624244391213935, 5.424775194616357), 8, False, False)
        
        var_1 = obj_0.__str__()
        var_6 = obj_0.is_out_of_play()
        var_5 = obj_0.is_guard()
        var_0 = obj_0.distance_to_center()
        var_4 = obj_0.is_passed_hogline()
        var_2 = obj_0.is_out_of_bounds()
        var_3 = obj_0.move((-3.870982235550759, -1.4740436085378406), 9, True)
        
        self.assertEqual(var_0, 5.803600647805648)
        self.assertEqual(var_1, 'Red stone at (-2.06, 5.42), round 8, active')
        self.assertEqual(var_2, False)
        self.assertEqual(var_3, True)
        self.assertEqual(var_4, True)
        self.assertEqual(var_5, True)
        self.assertEqual(var_6, False)
        
    def test_127(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-3.0423838848576796, 4.717880783923345), 3, False, False)
            
            var_9 = obj_0.is_out_of_bounds()
            var_4 = obj_0.is_guard()
            var_6 = obj_0.is_passed_hogline()
            var_5 = obj_0.__str__()
            var_0 = obj_0.__str__()
            var_3 = obj_0.is_in_house()
            var_1 = obj_0.is_guard()
            var_2 = obj_0.is_guard()
            var_8 = obj_0.is_out_of_bounds()
            obj_0.move_out_of_play()
        
    def test_128(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-1.9534536683526387, -4.560054226677748), 0, False, False)
            
            var_3 = obj_0.move((-4.944882760811062, 3.1468585433418745), 12, True)
            var_2 = obj_0.is_out_of_bounds()
            var_4 = obj_0.__str__()
            var_7 = obj_0.is_out_of_bounds()
            var_5 = obj_0.distance_to_center()
            obj_0.burn()
            obj_0.move_out_of_play()
            var_1 = obj_0.move((6.5626779757165945, -2.263465118463298), 4, True)
        
    def test_129(self):
        obj_2 = Game()
        
        var_2 = obj_2.red_winner()
        var_1 = obj_2.score()
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, None)
        
    def test_130(self):
        obj_2 = Game()
        
        var_1 = obj_2.display_scoreboard()
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_131(self):
        obj_2 = Game()
        
        var_2 = obj_2.display_scoreboard()
        var_1 = obj_2.__str__()
        obj_2.add_end(End(True))
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |    1 | Total\n----|------|------\nRed | h  0 |     0\nYel |    0 |     0\n')
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_132(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-5.331402271655998, 3.5556677617158385), 12, True, False)
            
            var_0 = obj_0.is_out_of_bounds()
            var_3 = obj_0.is_guard()
            var_1 = obj_0.move((0.7206605265383352, -4.906650125526717), -2, False)
            var_4 = obj_0.is_in_house()
            var_2 = obj_0.is_out_of_play()
        
    def test_133(self):
        obj_2 = Game()
        
        var_1 = obj_2.red_winner()
        var_0 = obj_2.score()
        var_3 = obj_2.red_winner()
        var_2 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_3, None)
        
    def test_134(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (-3.1469176267748153, 4.691922522425589), 8, False, False)
            
            var_7 = obj_0.move((2.909625108160217, 5.181683115555577), -1, False)
            var_3 = obj_0.move((0.3276566810343944, 6.588728767371608), 3, False)
            var_9 = obj_0.distance_to_center()
            var_4 = obj_0.distance_to_center()
            var_6 = obj_0.is_guard()
            obj_0.burn()
            var_5 = obj_0.is_out_of_play()
            var_2 = obj_0.is_out_of_play()
            var_1 = obj_0.move((-6.251320717649445, 0.21802887632386714), 9, True)
            var_8 = obj_0.distance_to_center()
        
    def test_135(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (7.061205128721662, 2.179478288907184), 7, False, False)
            
            var_1 = obj_0.distance_to_center()
            var_0 = obj_0.__str__()
        
    def test_136(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_0 = obj_1.__str__()
            var_2 = obj_1.done()
            var_1 = obj_1.score()
            var_3 = obj_1.overlaps_any_stone(Stone(False, (-5.460664190945057, -7.845212859527326), 12, True, True))
        
    def test_137(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        var_3 = obj_2.display_scoreboard()
        var_2 = obj_2.display_scoreboard()
        var_1 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_3, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_138(self):
        obj_0 = Stone(False, (1.3114671219152516, 6.93407451726689), 5, False, True)
        
        var_0 = obj_0.is_passed_hogline()
        var_1 = obj_0.is_out_of_bounds()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, False)
        
    def test_139(self):
        obj_0 = Stone(True, (4.946355422565821, -1.5161565844366294), 8, True, True)
        
        var_0 = obj_0.is_out_of_bounds()
        
        self.assertEqual(var_0, False)
        
    def test_140(self):
        obj_1 = End(False)
        
        var_3 = obj_1.overlaps_any_stone(Stone(False, (7.9787648555637105, 4.824240807010357), 9, True, True))
        var_2 = obj_1.score()
        var_0 = obj_1.score()
        var_1 = obj_1.overlaps_any_stone(Stone(True, (1.2811295422371263, 0.8814705444662607), 4, False, False))
        var_4 = obj_1.score()
        
        self.assertEqual(var_0, 0)
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, 0)
        self.assertEqual(var_3, False)
        self.assertEqual(var_4, 0)
        
    def test_141(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (7.2693732824723085, -5.889936520502564), 4, False, True)
            
            obj_0.move_out_of_play()
            var_1 = obj_0.is_out_of_play()
        
    def test_142(self):
        with self.assertRaisesRegex(ValueError, "Stone's round does not match the expected round based on the number of stones already placed."):
            obj_1 = End(True)
            
            var_0 = obj_1.red_won()
            obj_1.add_stone(Stone(False, (0.6538149289434028, -1.917245746758704), 3, True, True))
            var_5 = obj_1.overlaps_any_stone(Stone(False, (1.8723232847237412, -2.357912140531541), 10, True, False))
            var_4 = obj_1.drawn()
            obj_1.add_stone(Stone(False, (-0.19071928213820577, -1.3050754717593218), 9, True, True))
            var_1 = obj_1.overlaps_any_stone(Stone(False, (-3.7795437217914998, -6.406198191837786), 8, False, False))
        
    def test_143(self):
        obj_2 = Game()
        
        var_2 = obj_2.score()
        var_1 = obj_2.red_winner()
        obj_2.add_end(End(True))
        obj_2.add_end(End(True))
        
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, (0, 0))
        
    def test_144(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_2 = obj_1.drawn()
            var_3 = obj_1.drawn()
            obj_1.add_stone(Stone(False, (7.576807823093906, 2.559373213974242), -1, True, True))
            var_4 = obj_1.done()
            var_5 = obj_1.drawn()
            var_1 = obj_1.done()
        
    def test_145(self):
        with self.assertRaisesRegex(ValueError, "Stone's round does not match the expected round based on the number of stones already placed."):
            obj_1 = End(True)
            
            var_3 = obj_1.done()
            var_0 = obj_1.__str__()
            obj_1.add_stone(Stone(False, (7.175257079167666, 5.389229766671466), 8, True, True))
            obj_1.add_stone(Stone(True, (-5.124479592285738, 7.383513492044788), 11, False, True))
            var_2 = obj_1.score()
        
    def test_146(self):
        obj_1 = End(False)
        
        var_0 = obj_1.overlaps_any_stone(Stone(False, (-0.7643382910371592, -3.5150424944500998), 5, False, True))
        var_2 = obj_1.__str__()
        var_1 = obj_1.done()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, 'End with Yellow hammer and 0 stones')
        
    def test_147(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_2 = obj_1.overlaps_any_stone(Stone(True, (-2.374062188820906, 5.7891965802174905), 10, False, False))
            obj_1.add_stone(Stone(True, (7.9319555226448735, 0.3568579646029537), 8, False, False))
            var_3 = obj_1.score()
            var_0 = obj_1.__str__()
        
    def test_148(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-3.9982199018250224, 4.621172534028391), 2, False, True)
            
            var_1 = obj_0.__str__()
            var_0 = obj_0.is_in_house()
            var_3 = obj_0.is_in_house()
            var_2 = obj_0.move((-7.054352682693672, 1.8123202038928028), 2, False)
            var_4 = obj_0.is_in_house()
        
    def test_149(self):
        obj_2 = Game()
        
        var_1 = obj_2.__str__()
        var_0 = obj_2.red_winner()
        var_2 = obj_2.score()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, (0, 0))
        
    def test_150(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-6.952456559559211, 3.17668950928252), -1, True, True)
            
            var_5 = obj_0.is_out_of_play()
            var_6 = obj_0.is_passed_hogline()
            obj_0.move_out_of_play()
            var_3 = obj_0.is_in_house()
            var_7 = obj_0.is_passed_hogline()
            obj_0.burn()
            var_0 = obj_0.move((-3.913662857177334, -5.802061443800174), 4, False)
            var_2 = obj_0.move((4.7246498363644385, -7.912515037284281), 12, True)
        
    def test_151(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (-7.061878804427369, 4.433833760719304), 4, False, True)
            
            var_7 = obj_0.is_out_of_bounds()
            var_2 = obj_0.is_guard()
            var_0 = obj_0.is_guard()
            var_5 = obj_0.is_guard()
            var_3 = obj_0.is_guard()
            obj_0.move_out_of_play()
            var_1 = obj_0.is_in_house()
            var_6 = obj_0.is_guard()
            obj_0.move_out_of_play()
        
    def test_152(self):
        obj_1 = End(False)
        
        var_1 = obj_1.red_won()
        var_0 = obj_1.__str__()
        
        self.assertEqual(var_0, 'End with Yellow hammer and 0 stones')
        self.assertEqual(var_1, None)
        
    def test_153(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_1 = obj_1.overlaps_any_stone(Stone(False, (0.7125452732882476, 2.596621439834685), -2, False, False))
            var_2 = obj_1.score()
            var_3 = obj_1.score()
            obj_1.add_stone(Stone(True, (7.637612347222776, 2.6062499511256796), -2, True, True))
            var_0 = obj_1.done()
        
    def test_154(self):
        obj_0 = Stone(False, (-2.1813600965857276, -1.6574012415093904), 5, True, True)
        
        var_1 = obj_0.is_out_of_bounds()
        var_0 = obj_0.is_in_house()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, False)
        
    def test_155(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_5 = obj_1.drawn()
            var_0 = obj_1.done()
            var_4 = obj_1.__str__()
            var_6 = obj_1.overlaps_any_stone(Stone(True, (-2.196504776901799, 4.925171620568614), 10, True, False))
            var_2 = obj_1.done()
            obj_1.add_stone(Stone(False, (-6.232488820149928, 1.2787852459483808), 5, False, False))
            var_1 = obj_1.red_won()
        
    def test_156(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_4 = obj_1.score()
            var_1 = obj_1.drawn()
            var_2 = obj_1.red_won()
            obj_1.add_stone(Stone(True, (7.073876674420497, -1.9091320977338473), 5, True, False))
            obj_1.add_stone(Stone(False, (-2.8037357358836594, -7.509321744176011), 3, False, True))
        
    def test_157(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-5.440735223814423, -3.4736777810311423), -1, True, True)
            
            obj_0.burn()
        
    def test_158(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-2.5891947858720314, 5.639736960617498), 9, False, False)
            
            var_0 = obj_0.is_guard()
            var_2 = obj_0.is_out_of_play()
            var_1 = obj_0.is_out_of_play()
        
    def test_159(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (3.601974607699299, 5.374549236654486), 5, False, True)
            
            obj_0.move_out_of_play()
            obj_0.burn()
            var_6 = obj_0.distance_to_center()
            var_5 = obj_0.move((-0.6889107555920138, -2.5534041085283725), 12, False)
            obj_0.burn()
            var_2 = obj_0.__str__()
            var_1 = obj_0.is_in_house()
            var_7 = obj_0.distance_to_center()
            var_4 = obj_0.move((-3.6772148062234695, 4.451928322340308), 4, True)
        
    def test_160(self):
        obj_2 = Game()
        
        var_2 = obj_2.red_winner()
        var_0 = obj_2.__str__()
        var_1 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, None)
        
    def test_161(self):
        with self.assertRaisesRegex(ValueError, "Cannot calculate distance to center for a burned stone."):
            obj_0 = Stone(True, (-1.521173649223238, 6.874762622080734), 4, True, True)
            
            var_2 = obj_0.is_passed_hogline()
            var_8 = obj_0.distance_to_center()
            obj_0.burn()
            obj_0.move_out_of_play()
            var_7 = obj_0.is_guard()
            var_3 = obj_0.is_out_of_play()
            obj_0.burn()
            var_5 = obj_0.is_out_of_bounds()
            var_4 = obj_0.is_passed_hogline()
        
    def test_162(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (7.70294013969003, -3.487648046202489), -1, True, False)
            
            var_4 = obj_0.is_guard()
            var_1 = obj_0.move((3.1081188374160273, 1.8007900338011638), 8, False)
            var_3 = obj_0.__str__()
            var_2 = obj_0.is_passed_hogline()
            var_0 = obj_0.is_in_house()
        
    def test_163(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        
    def test_164(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        
    def test_165(self):
        obj_2 = Game()
        
        var_2 = obj_2.display_scoreboard()
        var_0 = obj_2.red_winner()
        var_4 = obj_2.score()
        var_1 = obj_2.display_scoreboard()
        var_3 = obj_2.score()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_3, (0, 0))
        self.assertEqual(var_4, (0, 0))
        
    def test_166(self):
        obj_1 = End(True)
        
        var_3 = obj_1.score()
        var_1 = obj_1.done()
        var_2 = obj_1.score()
        var_0 = obj_1.score()
        
        self.assertEqual(var_0, 0)
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, 0)
        self.assertEqual(var_3, 0)
        
    def test_167(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_4 = obj_1.done()
            obj_1.add_stone(Stone(True, (-1.4503984435051862, -2.950124283796425), 11, False, False))
            var_2 = obj_1.red_won()
            var_0 = obj_1.overlaps_any_stone(Stone(True, (1.3371643645330291, 5.906550440564898), 9, True, False))
            var_5 = obj_1.__str__()
            var_3 = obj_1.red_won()
        
    def test_168(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (4.085920645727876, 5.682453522492892), -2, True, True)
            
            var_2 = obj_0.is_out_of_bounds()
            var_7 = obj_0.is_passed_hogline()
            obj_0.burn()
            var_1 = obj_0.is_out_of_bounds()
            var_0 = obj_0.is_out_of_play()
            var_5 = obj_0.distance_to_center()
            var_3 = obj_0.distance_to_center()
            var_6 = obj_0.is_guard()
        
    def test_169(self):
        obj_1 = End(True)
        
        var_3 = obj_1.__str__()
        var_2 = obj_1.score()
        var_1 = obj_1.red_won()
        var_0 = obj_1.red_won()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 0)
        self.assertEqual(var_3, 'End with Red hammer and 0 stones')
        
    def test_170(self):
        with self.assertRaisesRegex(ValueError, "Stone's hammer status does not match the end's hammer status."):
            obj_1 = End(True)
            
            obj_1.add_stone(Stone(False, (-1.8602438688991771, -6.541497332467747), 7, False, True))
            var_2 = obj_1.__str__()
            var_1 = obj_1.done()
        
    def test_171(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        var_1 = obj_2.score()
        var_2 = obj_2.red_winner()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, None)
        
    def test_172(self):
        obj_2 = Game()
        
        var_3 = obj_2.score()
        var_1 = obj_2.score()
        obj_2.add_end(End(False))
        var_4 = obj_2.__str__()
        var_2 = obj_2.__str__()
        
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'Game with 1 ends')
        self.assertEqual(var_3, (0, 0))
        self.assertEqual(var_4, 'Game with 1 ends')
        
    def test_173(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (-6.397898403835212, -6.032163183693459), 3, True, False)
            
            var_0 = obj_0.is_guard()
            var_2 = obj_0.distance_to_center()
            var_1 = obj_0.is_in_house()
        
    def test_174(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (0.7002028790958494, 3.974577498889756), 11, True, True)
            
            var_8 = obj_0.is_passed_hogline()
            obj_0.burn()
            var_9 = obj_0.is_out_of_bounds()
            obj_0.burn()
            var_4 = obj_0.is_out_of_play()
            var_3 = obj_0.is_passed_hogline()
            var_0 = obj_0.__str__()
            var_2 = obj_0.is_passed_hogline()
            obj_0.move_out_of_play()
            obj_0.burn()
        
    def test_175(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (2.318221030017771, -1.303406228592321), 12, False, False)
            
            var_1 = obj_0.__str__()
            var_2 = obj_0.move((3.9454484191501233, 1.7330851772096771), 1, False)
            var_5 = obj_0.is_out_of_play()
            var_8 = obj_0.distance_to_center()
            var_7 = obj_0.is_out_of_play()
            var_3 = obj_0.is_in_house()
            var_4 = obj_0.is_guard()
            obj_0.burn()
            var_0 = obj_0.is_in_house()
            var_6 = obj_0.__str__()
        
    def test_176(self):
        obj_2 = Game()
        
        var_3 = obj_2.__str__()
        obj_2.add_end(End(False))
        var_2 = obj_2.red_winner()
        obj_2.add_end(End(False))
        var_4 = obj_2.red_winner()
        
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, 'Game with 0 ends')
        self.assertEqual(var_4, None)
        
    def test_177(self):
        obj_2 = Game()
        
        var_1 = obj_2.display_scoreboard()
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_178(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-6.26362359614491, -6.0986747166472774), -1, True, True)
            
            var_0 = obj_0.is_passed_hogline()
        
    def test_179(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (-7.382152612229291, -5.649231635341412), 1, False, True)
            
            obj_0.burn()
            var_4 = obj_0.distance_to_center()
            var_6 = obj_0.is_out_of_bounds()
            var_0 = obj_0.is_out_of_play()
            obj_0.move_out_of_play()
            var_5 = obj_0.is_passed_hogline()
            var_3 = obj_0.move((-1.3380693294522814, -2.146561472155639), -2, True)
        
    def test_180(self):
        obj_1 = End(True)
        
        var_0 = obj_1.drawn()
        var_4 = obj_1.__str__()
        var_3 = obj_1.done()
        var_2 = obj_1.score()
        var_1 = obj_1.drawn()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, True)
        self.assertEqual(var_2, 0)
        self.assertEqual(var_3, False)
        self.assertEqual(var_4, 'End with Red hammer and 0 stones')
        
    def test_181(self):
        obj_1 = End(False)
        
        var_1 = obj_1.score()
        var_2 = obj_1.__str__()
        var_0 = obj_1.red_won()
        var_5 = obj_1.drawn()
        var_3 = obj_1.done()
        var_4 = obj_1.score()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 0)
        self.assertEqual(var_2, 'End with Yellow hammer and 0 stones')
        self.assertEqual(var_3, False)
        self.assertEqual(var_4, 0)
        self.assertEqual(var_5, True)
        
    def test_182(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_0 = obj_1.red_won()
            var_5 = obj_1.__str__()
            var_3 = obj_1.score()
            obj_1.add_stone(Stone(False, (-2.492065761872892, 7.79401701598289), 8, True, False))
            var_2 = obj_1.red_won()
            var_4 = obj_1.drawn()
        
    def test_183(self):
        with self.assertRaisesRegex(ValueError, "Cannot calculate distance to center for a burned stone."):
            obj_0 = Stone(True, (0.2683771237534529, -4.5722093530713295), 8, True, False)
            
            var_0 = obj_0.is_passed_hogline()
            var_1 = obj_0.is_out_of_play()
            var_2 = obj_0.distance_to_center()
            var_5 = obj_0.is_passed_hogline()
            obj_0.move_out_of_play()
            var_6 = obj_0.distance_to_center()
            var_4 = obj_0.is_out_of_bounds()
            var_3 = obj_0.is_passed_hogline()
            var_8 = obj_0.move((-2.756947075622641, 4.182920467197567), 7, False)
        
    def test_184(self):
        obj_0 = Stone(False, (0.041471473503468914, 6.947899960732302), 7, True, True)
        
        var_0 = obj_0.is_passed_hogline()
        
        self.assertEqual(var_0, False)
        
    def test_185(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_186(self):
        obj_2 = Game()
        
        var_1 = obj_2.score()
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, (0, 0))
        
    def test_187(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (4.7843848201424795, -2.4713866814123886), 6, True, False)
            
            obj_0.move_out_of_play()
            var_2 = obj_0.move((4.45733282505544, 4.776739817439321), -2, False)
            obj_0.burn()
            var_5 = obj_0.__str__()
            var_8 = obj_0.is_passed_hogline()
            var_1 = obj_0.is_out_of_bounds()
            var_3 = obj_0.is_guard()
            var_4 = obj_0.__str__()
            var_0 = obj_0.is_in_house()
        
    def test_188(self):
        obj_0 = Stone(True, (2.164168037654921, 5.481975322675545), 5, False, False)
        
        var_0 = obj_0.is_out_of_bounds()
        var_1 = obj_0.is_guard()
        var_4 = obj_0.is_out_of_play()
        var_6 = obj_0.is_out_of_play()
        var_3 = obj_0.is_guard()
        var_2 = obj_0.__str__()
        var_5 = obj_0.distance_to_center()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, True)
        self.assertEqual(var_2, 'Red stone at (2.16, 5.48), round 5, active')
        self.assertEqual(var_3, True)
        self.assertEqual(var_4, False)
        self.assertEqual(var_5, 5.893698052465091)
        self.assertEqual(var_6, False)
        
    def test_189(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_5 = obj_1.score()
            var_3 = obj_1.overlaps_any_stone(Stone(False, (2.8967831119424954, 7.621519269208912), 9, False, True))
            var_1 = obj_1.done()
            var_4 = obj_1.overlaps_any_stone(Stone(True, (2.68360442600207, -1.5004464605985195), 1, True, True))
            var_0 = obj_1.overlaps_any_stone(Stone(False, (-2.3596873637965494, -7.977989751129048), 5, True, False))
            obj_1.add_stone(Stone(False, (4.5978778782920084, 4.007662051573119), 11, True, False))
        
    def test_190(self):
        obj_1 = End(False)
        
        var_1 = obj_1.score()
        var_0 = obj_1.score()
        
        self.assertEqual(var_0, 0)
        self.assertEqual(var_1, 0)
        
    def test_191(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_0 = obj_1.overlaps_any_stone(Stone(True, (-2.3681532043992384, 7.502742566339791), 0, False, True))
        
    def test_192(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        
    def test_193(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_2 = obj_1.red_won()
            var_3 = obj_1.done()
            var_6 = obj_1.done()
            obj_1.add_stone(Stone(False, (7.59319665590407, 1.6963081701670362), 7, False, False))
            obj_1.add_stone(Stone(True, (5.538235401446787, -5.513234863948323), 9, True, False))
            var_0 = obj_1.red_won()
            var_1 = obj_1.overlaps_any_stone(Stone(True, (6.406783764589706, -5.783353124231159), 6, True, True))
        
    def test_194(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-4.203886269752161, 7.913507661980782), 12, True, True)
            
            var_4 = obj_0.is_in_house()
            var_2 = obj_0.is_guard()
            var_3 = obj_0.is_passed_hogline()
            var_0 = obj_0.is_out_of_play()
            var_1 = obj_0.move((0.41570548694291887, -7.8520639167676), -2, False)
            var_5 = obj_0.is_guard()
        
    def test_195(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(False, (-4.956243328772143, -7.454125868997341), 1, False, True)
            
            var_0 = obj_0.is_in_house()
            var_2 = obj_0.is_guard()
            var_1 = obj_0.is_guard()
            var_3 = obj_0.move((5.750912883433436, -6.816213204742443), 10, True)
            var_4 = obj_0.is_guard()
            var_5 = obj_0.__str__()
        
    def test_196(self):
        obj_2 = Game()
        
        var_3 = obj_2.display_scoreboard()
        var_0 = obj_2.red_winner()
        var_2 = obj_2.__str__()
        var_1 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_197(self):
        obj_2 = Game()
        
        var_3 = obj_2.red_winner()
        obj_2.add_end(End(True))
        var_1 = obj_2.score()
        var_2 = obj_2.__str__()
        var_4 = obj_2.score()
        
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'Game with 1 ends')
        self.assertEqual(var_3, None)
        self.assertEqual(var_4, (0, 0))
        
    def test_198(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_199(self):
        with self.assertRaisesRegex(ValueError, "Cannot calculate distance to center for a burned stone."):
            obj_0 = Stone(True, (-3.0225473632732136, 6.911065550034882), 4, False, True)
            
            var_0 = obj_0.distance_to_center()
            var_5 = obj_0.is_in_house()
            obj_0.burn()
            var_1 = obj_0.is_passed_hogline()
            var_3 = obj_0.is_passed_hogline()
            obj_0.burn()
        
    def test_200(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |    1 | Total\n----|------|------\nRed |    0 |     0\nYel | h  0 |     0\n')
        
    def test_201(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_2 = obj_1.red_won()
            obj_1.add_stone(Stone(True, (-6.962384333952603, -1.079572387975622), 10, True, False))
            obj_1.add_stone(Stone(False, (2.895314375723041, -0.4758221548377861), 6, True, False))
            var_0 = obj_1.score()
        
    def test_202(self):
        obj_2 = Game()
        
        var_1 = obj_2.score()
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, (0, 0))
        
    def test_203(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_0 = obj_1.__str__()
            var_3 = obj_1.done()
            var_2 = obj_1.score()
            var_1 = obj_1.drawn()
            obj_1.add_stone(Stone(True, (-5.1409231452410875, 6.092845443073898), 0, False, False))
        
    def test_204(self):
        obj_2 = Game()
        
        var_4 = obj_2.score()
        var_3 = obj_2.red_winner()
        var_2 = obj_2.score()
        var_0 = obj_2.red_winner()
        var_1 = obj_2.__str__()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, (0, 0))
        self.assertEqual(var_3, None)
        self.assertEqual(var_4, (0, 0))
        
    def test_205(self):
        obj_1 = End(True)
        
        var_0 = obj_1.overlaps_any_stone(Stone(True, (-1.525603029152256, 4.428303256222788), 8, False, True))
        var_1 = obj_1.score()
        var_3 = obj_1.score()
        var_2 = obj_1.drawn()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, 0)
        self.assertEqual(var_2, True)
        self.assertEqual(var_3, 0)
        
    def test_206(self):
        obj_1 = End(True)
        
        var_0 = obj_1.__str__()
        var_3 = obj_1.score()
        var_4 = obj_1.__str__()
        var_2 = obj_1.done()
        var_1 = obj_1.done()
        
        self.assertEqual(var_0, 'End with Red hammer and 0 stones')
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, False)
        self.assertEqual(var_3, 0)
        self.assertEqual(var_4, 'End with Red hammer and 0 stones')
        
    def test_207(self):
        obj_2 = Game()
        
        var_2 = obj_2.display_scoreboard()
        var_0 = obj_2.display_scoreboard()
        var_1 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_208(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-6.995287752722058, -0.5100877648768627), 1, True, True)
            
            var_6 = obj_0.__str__()
            var_5 = obj_0.is_passed_hogline()
            var_2 = obj_0.is_out_of_play()
            var_1 = obj_0.move((-7.476315678967339, -1.4229534425003934), 5, True)
            var_3 = obj_0.is_out_of_bounds()
            var_8 = obj_0.is_out_of_play()
            var_4 = obj_0.__str__()
            var_7 = obj_0.distance_to_center()
            obj_0.move_out_of_play()
        
    def test_209(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
            obj_2 = Game()
            
            var_0 = obj_2.display_scoreboard()
            obj_2.add_end(End(True))
            obj_2.add_end(End(False))
        
    def test_210(self):
        obj_2 = Game()
        
        var_2 = obj_2.__str__()
        var_0 = obj_2.display_scoreboard()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, 'Game with 0 ends')
        
    def test_211(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            obj_1.add_stone(Stone(True, (-6.92256645916218, 0.5037343730683883), 2, True, False))
            var_1 = obj_1.drawn()
        
    def test_212(self):
        obj_2 = Game()
        
        obj_2.add_end(End(True))
        var_2 = obj_2.red_winner()
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_2, None)
        
    def test_213(self):
        obj_1 = End(True)
        
        var_0 = obj_1.done()
        var_1 = obj_1.red_won()
        var_2 = obj_1.__str__()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 'End with Red hammer and 0 stones')
        
    def test_214(self):
        obj_2 = Game()
        
        var_2 = obj_2.display_scoreboard()
        var_3 = obj_2.red_winner()
        obj_2.add_end(End(False))
        var_1 = obj_2.score()
        
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_3, None)
        
    def test_215(self):
        obj_1 = End(True)
        
        var_3 = obj_1.overlaps_any_stone(Stone(True, (4.467687801598762, -6.2536693331166955), 9, False, True))
        var_2 = obj_1.done()
        var_1 = obj_1.overlaps_any_stone(Stone(False, (2.347263838061142, 2.899288825829961), 1, False, True))
        var_4 = obj_1.score()
        var_0 = obj_1.score()
        
        self.assertEqual(var_0, 0)
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, False)
        self.assertEqual(var_3, False)
        self.assertEqual(var_4, 0)
        
    def test_216(self):
        obj_2 = Game()
        
        var_2 = obj_2.red_winner()
        var_1 = obj_2.__str__()
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, None)
        
    def test_217(self):
        obj_2 = Game()
        
        var_2 = obj_2.display_scoreboard()
        var_1 = obj_2.__str__()
        obj_2.add_end(End(False))
        var_3 = obj_2.red_winner()
        
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_3, None)
        
    def test_218(self):
        with self.assertRaisesRegex(ValueError, "The first stone must be thrown by the team without the hammer."):
            obj_1 = End(False)
            
            var_4 = obj_1.drawn()
            var_2 = obj_1.score()
            obj_1.add_stone(Stone(False, (3.700703430274416, 7.520395434750341), 2, True, True))
            obj_1.add_stone(Stone(False, (-4.151996057401153, -5.319194096554478), 4, False, True))
            var_0 = obj_1.red_won()
        
    def test_219(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_0 = obj_1.red_won()
            obj_1.add_stone(Stone(False, (0.49158848011578726, -1.2227169821018027), 0, False, True))
            var_3 = obj_1.done()
            var_2 = obj_1.drawn()
        
    def test_220(self):
        obj_1 = End(False)
        
        var_3 = obj_1.__str__()
        var_6 = obj_1.overlaps_any_stone(Stone(True, (0.12737467512794964, 5.284568357257783), 8, True, True))
        var_1 = obj_1.drawn()
        var_5 = obj_1.drawn()
        var_4 = obj_1.red_won()
        var_2 = obj_1.__str__()
        var_0 = obj_1.score()
        
        self.assertEqual(var_0, 0)
        self.assertEqual(var_1, True)
        self.assertEqual(var_2, 'End with Yellow hammer and 0 stones')
        self.assertEqual(var_3, 'End with Yellow hammer and 0 stones')
        self.assertEqual(var_4, None)
        self.assertEqual(var_5, True)
        self.assertEqual(var_6, False)
        
    def test_221(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        var_2 = obj_2.display_scoreboard()
        var_1 = obj_2.red_winner()
        var_3 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_3, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_222(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        var_2 = obj_2.__str__()
        var_1 = obj_2.red_winner()
        var_3 = obj_2.score()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, (0, 0))
        
    def test_223(self):
        obj_2 = Game()
        
        var_2 = obj_2.__str__()
        obj_2.add_end(End(False))
        var_1 = obj_2.score()
        
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'Game with 0 ends')
        
    def test_224(self):
        with self.assertRaisesRegex(ValueError, "Stone's hammer status does not match the end's hammer status."):
            obj_1 = End(True)
            
            var_4 = obj_1.__str__()
            var_2 = obj_1.__str__()
            var_5 = obj_1.__str__()
            var_0 = obj_1.drawn()
            obj_1.add_stone(Stone(False, (-7.619768485308828, 0.5043367069697045), 3, False, True))
            var_3 = obj_1.__str__()
        
    def test_225(self):
        obj_1 = End(True)
        
        var_5 = obj_1.drawn()
        var_4 = obj_1.score()
        var_1 = obj_1.score()
        var_2 = obj_1.done()
        var_0 = obj_1.done()
        var_3 = obj_1.drawn()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, 0)
        self.assertEqual(var_2, False)
        self.assertEqual(var_3, True)
        self.assertEqual(var_4, 0)
        self.assertEqual(var_5, True)
        
    def test_226(self):
        with self.assertRaisesRegex(ValueError, "Cannot calculate distance to center for a burned stone."):
            obj_0 = Stone(False, (-3.8724291038761223, -4.435189206139206), 1, False, True)
            
            var_0 = obj_0.is_in_house()
            var_1 = obj_0.__str__()
            var_2 = obj_0.distance_to_center()
        
    def test_227(self):
        obj_2 = Game()
        
        var_2 = obj_2.red_winner()
        var_0 = obj_2.display_scoreboard()
        var_1 = obj_2.score()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, None)
        
    def test_228(self):
        obj_2 = Game()
        
        var_2 = obj_2.display_scoreboard()
        obj_2.add_end(End(True))
        var_1 = obj_2.red_winner()
        
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_229(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (5.678346892585015, -5.782834849624548), 1, False, False)
            
            var_9 = obj_0.move((-1.6275715267295414, -3.7721144263428084), 12, True)
            var_7 = obj_0.__str__()
            var_4 = obj_0.is_out_of_play()
            var_1 = obj_0.is_in_house()
            var_8 = obj_0.is_passed_hogline()
            var_5 = obj_0.is_out_of_play()
            var_0 = obj_0.is_guard()
            var_3 = obj_0.is_guard()
            var_2 = obj_0.move((6.716085080637768, -5.823035748846479), 4, False)
            obj_0.burn()
        
    def test_230(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (1.3367373127770836, 3.037600323025085), 11, False, False)
            
            obj_0.burn()
            obj_0.burn()
        
    def test_231(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (6.900293800797492, 7.314119861682489), 4, True, False)
            
            var_1 = obj_0.is_out_of_bounds()
            var_0 = obj_0.__str__()
        
    def test_232(self):
        obj_1 = End(True)
        
        var_0 = obj_1.done()
        var_1 = obj_1.red_won()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, None)
        
    def test_233(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            obj_1.add_stone(Stone(False, (-5.185410764404711, 5.86026329354846), 9, True, False))
            obj_1.add_stone(Stone(True, (1.6604477891090212, -1.0772528036486744), 9, False, False))
            var_2 = obj_1.red_won()
            var_3 = obj_1.__str__()
            var_1 = obj_1.done()
        
    def test_234(self):
        obj_2 = Game()
        
        var_2 = obj_2.red_winner()
        var_3 = obj_2.score()
        var_1 = obj_2.red_winner()
        obj_2.add_end(End(False))
        
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, (0, 0))
        
    def test_235(self):
        with self.assertRaisesRegex(ValueError, "Stone's hammer status does not match the end's hammer status."):
            obj_1 = End(False)
            
            obj_1.add_stone(Stone(True, (-7.1106019514382695, -2.2485252537369824), 8, True, True))
            obj_1.add_stone(Stone(False, (2.2751513084294874, -4.550940932747981), 9, False, True))
        
    def test_236(self):
        obj_2 = Game()
        
        var_2 = obj_2.__str__()
        var_1 = obj_2.score()
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'Game with 0 ends')
        
    def test_237(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        var_1 = obj_2.score()
        obj_2.add_end(End(True))
        var_3 = obj_2.red_winner()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_3, None)
        
    def test_238(self):
        with self.assertRaisesRegex(ValueError, "Stone's round does not match the expected round based on the number of stones already placed."):
            obj_1 = End(True)
            
            obj_1.add_stone(Stone(False, (5.712019429274761, 6.180545446904205), 9, True, True))
            var_0 = obj_1.done()
            var_5 = obj_1.drawn()
            var_4 = obj_1.score()
            var_1 = obj_1.__str__()
            var_6 = obj_1.red_won()
            obj_1.add_stone(Stone(True, (3.408134269059371, 1.5374995105914575), 10, False, True))
        
    def test_239(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_0 = obj_1.score()
            obj_1.add_stone(Stone(True, (6.416436431255873, 1.9989692967239332), -1, True, False))
        
    def test_240(self):
        obj_2 = Game()
        
        obj_2.add_end(End(True))
        var_0 = obj_2.__str__()
        var_2 = obj_2.__str__()
        var_3 = obj_2.red_winner()
        
        self.assertEqual(var_0, 'Game with 1 ends')
        self.assertEqual(var_2, 'Game with 1 ends')
        self.assertEqual(var_3, None)
        
    def test_241(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (-0.570269004837602, 5.253208170284196), 1, False, True)
            
            obj_0.burn()
            var_2 = obj_0.is_out_of_play()
            var_4 = obj_0.is_out_of_bounds()
            var_5 = obj_0.move((0.4387161583667236, -4.935366109275462), 2, True)
            var_0 = obj_0.is_out_of_play()
            var_1 = obj_0.is_in_house()
            var_3 = obj_0.is_guard()
        
    def test_242(self):
        obj_1 = End(True)
        
        var_1 = obj_1.__str__()
        var_0 = obj_1.red_won()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'End with Red hammer and 0 stones')
        
    def test_243(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        
    def test_244(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (7.084746277229916, -0.043307630057041635), 10, True, False)
            
            var_0 = obj_0.is_out_of_play()
            var_1 = obj_0.is_in_house()
        
    def test_245(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-2.886357424854692, 0.04689685787671394), 2, False, False)
            
            var_4 = obj_0.distance_to_center()
            var_1 = obj_0.is_passed_hogline()
            var_3 = obj_0.is_out_of_play()
            var_5 = obj_0.move((6.991098606393214, 5.404699920486369), 6, False)
            var_6 = obj_0.__str__()
            var_7 = obj_0.is_out_of_play()
            var_0 = obj_0.__str__()
            obj_0.burn()
        
    def test_246(self):
        obj_1 = End(False)
        
        var_0 = obj_1.red_won()
        var_1 = obj_1.drawn()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, True)
        
    def test_247(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        
        
    def test_248(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (7.48911725705937, 4.31825952923905), 10, False, True)
            
            obj_0.move_out_of_play()
            var_0 = obj_0.is_out_of_play()
            var_1 = obj_0.move((-6.156893658250846, -3.05330338373124), 11, False)
        
    def test_249(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (5.823081173030907, -1.8345762367814462), -2, False, True)
            
            var_0 = obj_0.is_passed_hogline()
            var_1 = obj_0.distance_to_center()
        
    def test_250(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        
    def test_251(self):
        obj_2 = Game()
        
        obj_2.add_end(End(True))
        var_2 = obj_2.__str__()
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_2, 'Game with 1 ends')
        
    def test_252(self):
        obj_1 = End(True)
        
        var_0 = obj_1.overlaps_any_stone(Stone(False, (-0.43853197820213374, -7.287986397588538), 10, True, True))
        
        self.assertEqual(var_0, False)
        
    def test_253(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_0 = obj_1.overlaps_any_stone(Stone(False, (6.804014672168208, 0.4428099247265447), 2, True, True))
            obj_1.add_stone(Stone(True, (-3.4237316543808127, 6.7038465055196), 2, False, False))
        
    def test_254(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-5.56988196053679, -4.102847216750829), 10, False, False)
            
            var_3 = obj_0.is_out_of_bounds()
            obj_0.move_out_of_play()
            var_1 = obj_0.is_passed_hogline()
            obj_0.move_out_of_play()
            var_4 = obj_0.is_out_of_bounds()
            var_2 = obj_0.is_out_of_play()
            var_8 = obj_0.is_out_of_bounds()
            var_6 = obj_0.__str__()
            var_7 = obj_0.distance_to_center()
        
    def test_255(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_1 = obj_1.overlaps_any_stone(Stone(False, (2.5590346514170914, -1.9065427065789997), 8, True, False))
            var_0 = obj_1.score()
        
    def test_256(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (7.418717496283273, 1.6650175516833468), 0, False, False)
            
            var_2 = obj_0.is_guard()
            obj_0.burn()
            var_4 = obj_0.distance_to_center()
            obj_0.burn()
            var_1 = obj_0.move((-2.5845939282929127, 6.634298205469197), 9, True)
            var_0 = obj_0.is_out_of_play()
        
    def test_257(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (4.0361993895170265, -1.2887361635219836), 3, False, True)
            
            var_2 = obj_0.is_out_of_bounds()
            obj_0.burn()
            var_0 = obj_0.__str__()
            obj_0.move_out_of_play()
        
    def test_258(self):
        obj_2 = Game()
        
        var_3 = obj_2.score()
        var_1 = obj_2.red_winner()
        obj_2.add_end(End(True))
        var_2 = obj_2.score()
        
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, (0, 0))
        self.assertEqual(var_3, (0, 0))
        
    def test_259(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-5.0142735136937056, -7.4161629964954425), 6, True, False)
            
            obj_0.burn()
            var_1 = obj_0.__str__()
            var_2 = obj_0.is_in_house()
        
    def test_260(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_0 = obj_1.__str__()
            var_4 = obj_1.done()
            var_3 = obj_1.overlaps_any_stone(Stone(False, (-4.721519776634189, 1.0517857428483417), 8, False, False))
            obj_1.add_stone(Stone(True, (2.3434527050722735, -3.907566076402997), 7, False, True))
            var_5 = obj_1.__str__()
            var_2 = obj_1.overlaps_any_stone(Stone(False, (6.840682699575407, -6.335135660456881), 4, False, False))
        
    def test_261(self):
        with self.assertRaisesRegex(ValueError, "Stone's round does not match the expected round based on the number of stones already placed."):
            obj_1 = End(True)
            
            var_0 = obj_1.red_won()
            var_3 = obj_1.done()
            var_2 = obj_1.red_won()
            var_4 = obj_1.drawn()
            obj_1.add_stone(Stone(False, (5.643666062210718, 3.1861472290625965), 10, True, True))
            var_5 = obj_1.drawn()
        
    def test_262(self):
        obj_1 = End(False)
        
        var_0 = obj_1.score()
        
        self.assertEqual(var_0, 0)
        
    def test_263(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_2 = obj_1.__str__()
            obj_1.add_stone(Stone(True, (2.2676185553195687, 7.086166651340889), 10, False, False))
            var_1 = obj_1.overlaps_any_stone(Stone(True, (-3.5562845467875572, -6.574580966229602), 12, True, False))
            var_4 = obj_1.done()
            var_0 = obj_1.red_won()
        
    def test_264(self):
        obj_2 = Game()
        
        var_1 = obj_2.__str__()
        var_2 = obj_2.display_scoreboard()
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_265(self):
        obj_2 = Game()
        
        obj_2.add_end(End(True))
        var_1 = obj_2.display_scoreboard()
        
        self.assertEqual(var_1, 'End |    1 | Total\n----|------|------\nRed | h  0 |     0\nYel |    0 |     0\n')
        
    def test_266(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-7.125568661384497, 2.291634219581322), -1, True, True)
            
            obj_0.move_out_of_play()
            var_0 = obj_0.is_out_of_play()
            var_2 = obj_0.is_passed_hogline()
        
    def test_267(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-5.383184813988239, 3.9509967351576556), 3, False, False)
            
            var_0 = obj_0.__str__()
        
    def test_268(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        
    def test_269(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_2 = obj_1.done()
            var_0 = obj_1.red_won()
            var_1 = obj_1.overlaps_any_stone(Stone(True, (-3.717676606834205, 2.131225090136777), 10, True, False))
        
    def test_270(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (-0.06931556915712456, -4.828375970266054), 9, False, False)
            
            var_2 = obj_0.is_in_house()
            var_0 = obj_0.__str__()
            var_5 = obj_0.move((7.599007238651385, -0.926933111278915), 3, True)
            obj_0.burn()
            var_3 = obj_0.is_passed_hogline()
            var_1 = obj_0.move((-6.9932699691002895, 0.5454141224636277), 6, True)
        
    def test_271(self):
        obj_0 = Stone(False, (0.426377511779787, 2.4043161172782206), 5, True, False)
        
        var_0 = obj_0.is_passed_hogline()
        var_7 = obj_0.move((-2.0208104766186743, 0.11260581190220265), 1, True)
        var_5 = obj_0.distance_to_center()
        var_1 = obj_0.is_guard()
        var_3 = obj_0.is_in_house()
        var_2 = obj_0.is_out_of_play()
        obj_0.burn()
        var_6 = obj_0.is_out_of_play()
        var_8 = obj_0.__str__()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, True)
        self.assertEqual(var_2, False)
        self.assertEqual(var_3, False)
        self.assertEqual(var_5, 2.9794483511137138)
        self.assertEqual(var_6, True)
        self.assertEqual(var_7, True)
        self.assertEqual(var_8, 'Yellow stone at (2.50, 5.49), round 5, burned')
        
    def test_272(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
            obj_2 = Game()
            
            var_3 = obj_2.red_winner()
            var_1 = obj_2.score()
            obj_2.add_end(End(False))
            var_4 = obj_2.display_scoreboard()
            obj_2.add_end(End(True))
        
    def test_273(self):
        obj_1 = End(True)
        
        var_0 = obj_1.score()
        
        self.assertEqual(var_0, 0)
        
    def test_274(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        var_2 = obj_2.red_winner()
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_2, None)
        
    def test_275(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_3 = obj_1.red_won()
            var_1 = obj_1.__str__()
            var_2 = obj_1.overlaps_any_stone(Stone(False, (-5.289210624520802, 7.822863935854485), 12, False, True))
            var_0 = obj_1.__str__()
            var_5 = obj_1.__str__()
            var_4 = obj_1.overlaps_any_stone(Stone(False, (2.1603039535979978, 2.9308906333454434), 10, False, False))
        
    def test_276(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        
        
    def test_277(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (3.7731045815837128, 3.755000462017076), 9, False, False)
            
            var_8 = obj_0.is_out_of_bounds()
            var_2 = obj_0.is_out_of_bounds()
            var_1 = obj_0.is_out_of_play()
            obj_0.burn()
            var_7 = obj_0.is_in_house()
            var_0 = obj_0.is_passed_hogline()
            var_9 = obj_0.__str__()
            var_5 = obj_0.is_out_of_play()
            obj_0.move_out_of_play()
            var_6 = obj_0.move((7.166443907059014, -1.2964429585169075), 4, False)
        
    def test_278(self):
        obj_1 = End(False)
        
        var_0 = obj_1.drawn()
        
        self.assertEqual(var_0, True)
        
    def test_279(self):
        obj_2 = Game()
        
        obj_2.add_end(End(True))
        obj_2.add_end(End(True))
        
        
    def test_280(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_1 = obj_1.drawn()
            var_0 = obj_1.done()
            var_3 = obj_1.drawn()
            var_2 = obj_1.overlaps_any_stone(Stone(False, (-3.9761257362231763, -1.0367095718749706), 9, True, False))
            var_4 = obj_1.done()
            var_5 = obj_1.overlaps_any_stone(Stone(False, (-5.720985760392548, -5.649604969728735), -1, False, True))
        
    def test_281(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
            obj_2 = Game()
            
            obj_2.add_end(End(True))
            obj_2.add_end(End(False))
            var_0 = obj_2.display_scoreboard()
        
    def test_282(self):
        with self.assertRaisesRegex(ValueError, "Stone's round does not match the expected round based on the number of stones already placed."):
            obj_1 = End(True)
            
            obj_1.add_stone(Stone(False, (-3.301459360944996, -6.537183292381201), 2, True, True))
            var_2 = obj_1.__str__()
            var_3 = obj_1.__str__()
            var_0 = obj_1.score()
        
    def test_283(self):
        with self.assertRaisesRegex(ValueError, "Cannot calculate distance to center for a burned stone."):
            obj_0 = Stone(False, (2.1761849154645745, -0.2718602159714365), 4, False, False)
            
            var_0 = obj_0.is_out_of_play()
            var_4 = obj_0.is_passed_hogline()
            var_6 = obj_0.is_out_of_bounds()
            obj_0.burn()
            var_3 = obj_0.distance_to_center()
            var_1 = obj_0.is_out_of_play()
            var_2 = obj_0.is_guard()
        
    def test_284(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (3.4240349803181456, -2.1061155113942878), 1, True, False)
            
            var_0 = obj_0.distance_to_center()
        
    def test_285(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (-2.148717313952126, -1.3053340773019677), 2, True, False)
            
            var_6 = obj_0.move((-0.12021255282932408, 3.9775191365877056), 9, False)
            var_4 = obj_0.move((-1.7026989382528424, 7.5749257603592), 10, True)
            obj_0.burn()
            var_3 = obj_0.is_out_of_bounds()
            obj_0.burn()
            var_7 = obj_0.distance_to_center()
            var_2 = obj_0.is_guard()
            var_1 = obj_0.is_in_house()
        
    def test_286(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            obj_1.add_stone(Stone(True, (2.023369689800182, -6.922616574898097), 1, True, False))
            var_0 = obj_1.red_won()
            var_4 = obj_1.done()
            obj_1.add_stone(Stone(True, (-4.69859692737394, 0.4374567274159382), 4, False, True))
            var_2 = obj_1.red_won()
        
    def test_287(self):
        obj_2 = Game()
        
        obj_2.add_end(End(True))
        
        
    def test_288(self):
        obj_1 = End(False)
        
        var_5 = obj_1.score()
        var_2 = obj_1.red_won()
        var_1 = obj_1.red_won()
        var_4 = obj_1.__str__()
        var_0 = obj_1.done()
        var_3 = obj_1.red_won()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, None)
        self.assertEqual(var_4, 'End with Yellow hammer and 0 stones')
        self.assertEqual(var_5, 0)
        
    def test_289(self):
        obj_2 = Game()
        
        var_1 = obj_2.display_scoreboard()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_290(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_3 = obj_1.done()
            obj_1.add_stone(Stone(True, (1.6933206505636313, -1.6795791571124337), 11, True, True))
            obj_1.add_stone(Stone(False, (-7.775038809727468, 0.8083874391680528), 6, True, True))
            var_4 = obj_1.__str__()
            var_0 = obj_1.red_won()
            var_1 = obj_1.done()
            var_6 = obj_1.drawn()
        
    def test_291(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_0 = obj_1.__str__()
            obj_1.add_stone(Stone(False, (3.703179405186619, -0.26676061672319307), 2, False, False))
            var_2 = obj_1.done()
        
    def test_292(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_2 = obj_1.drawn()
            obj_1.add_stone(Stone(True, (-3.143757477282101, -0.08518409337429489), 4, False, False))
            var_3 = obj_1.red_won()
            var_1 = obj_1.overlaps_any_stone(Stone(True, (-1.7840361407170882, 4.13395834568294), 10, False, False))
            obj_1.add_stone(Stone(True, (1.4495886613575006, 4.1849793156661175), 9, True, True))
        
    def test_293(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (0.10226824169487259, -7.629815296682272), 9, True, False)
            
            var_5 = obj_0.is_out_of_play()
            obj_0.burn()
            var_0 = obj_0.move((1.2855529511921144, 4.567015559370494), -2, True)
            var_4 = obj_0.is_in_house()
            var_3 = obj_0.is_in_house()
            var_2 = obj_0.__str__()
            obj_0.burn()
            obj_0.move_out_of_play()
        
    def test_294(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-6.312658757668583, -7.728301382423174), -1, True, True)
            
            var_3 = obj_0.distance_to_center()
            var_2 = obj_0.distance_to_center()
            var_1 = obj_0.is_passed_hogline()
            var_0 = obj_0.is_guard()
        
    def test_295(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_1 = obj_1.__str__()
            var_2 = obj_1.score()
            var_0 = obj_1.overlaps_any_stone(Stone(False, (5.321748697885585, 4.657808572679251), -1, True, False))
            var_5 = obj_1.__str__()
            var_3 = obj_1.done()
            var_6 = obj_1.__str__()
            var_4 = obj_1.score()
        
    def test_296(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_0 = obj_1.red_won()
            var_3 = obj_1.done()
            var_1 = obj_1.score()
            var_5 = obj_1.overlaps_any_stone(Stone(False, (-4.825171632642274, 4.959821718411279), 9, True, False))
            obj_1.add_stone(Stone(False, (3.64335302586632, 3.5514722336399185), 5, False, True))
            var_2 = obj_1.red_won()
            var_6 = obj_1.__str__()
        
    def test_297(self):
        with self.assertRaisesRegex(ValueError, "Cannot calculate distance to center for a burned stone."):
            obj_0 = Stone(False, (-1.9306775232084945, -4.478439724903927), 1, True, True)
            
            var_3 = obj_0.distance_to_center()
            var_4 = obj_0.is_in_house()
            var_0 = obj_0.is_out_of_bounds()
            var_2 = obj_0.is_out_of_bounds()
            obj_0.move_out_of_play()
            obj_0.burn()
        
    def test_298(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (0.07976681868783864, -0.600370806320198), 3, False, True)
            
            var_3 = obj_0.is_in_house()
            obj_0.burn()
            var_2 = obj_0.is_out_of_play()
            var_5 = obj_0.is_passed_hogline()
            var_6 = obj_0.is_guard()
            var_1 = obj_0.distance_to_center()
            obj_0.burn()
        
    def test_299(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (-5.922208570584296, -0.8973811531103699), 2, False, True)
            
            var_7 = obj_0.is_passed_hogline()
            var_4 = obj_0.__str__()
            obj_0.move_out_of_play()
            var_6 = obj_0.is_passed_hogline()
            var_1 = obj_0.move((-6.948829877194838, -1.1508489720656705), 6, False)
            obj_0.burn()
            var_5 = obj_0.is_out_of_bounds()
            var_0 = obj_0.is_passed_hogline()
        
    def test_300(self):
        obj_1 = End(False)
        
        var_1 = obj_1.red_won()
        var_0 = obj_1.score()
        
        self.assertEqual(var_0, 0)
        self.assertEqual(var_1, None)
        
    def test_301(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        var_1 = obj_2.red_winner()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, None)
        
    def test_302(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-2.7747399286703676, -0.7992468158937811), -1, False, True)
            
            var_0 = obj_0.move((7.186295397839574, 7.814186481851202), 10, True)
            var_2 = obj_0.move((-7.651162753609583, -1.213904586305901), 11, True)
            var_1 = obj_0.distance_to_center()
            var_6 = obj_0.move((4.317980933123749, 1.7610589858239614), 12, False)
            var_5 = obj_0.is_out_of_bounds()
            var_3 = obj_0.move((-2.5188618149474973, -5.6449035167826125), 12, False)
            var_4 = obj_0.is_out_of_bounds()
        
    def test_303(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (5.6190691201049905, -0.5568550358039257), 0, False, True)
            
            var_2 = obj_0.is_out_of_bounds()
            var_4 = obj_0.__str__()
            var_5 = obj_0.move((5.704416739937191, 4.327812571522703), -1, False)
            obj_0.burn()
            var_1 = obj_0.is_passed_hogline()
            var_0 = obj_0.is_out_of_bounds()
            var_7 = obj_0.__str__()
            var_6 = obj_0.is_in_house()
        
    def test_304(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
            obj_2 = Game()
            
            obj_2.add_end(End(True))
            obj_2.add_end(End(False))
        
    def test_305(self):
        obj_1 = End(True)
        
        var_0 = obj_1.done()
        
        self.assertEqual(var_0, False)
        
    def test_306(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (-3.625312109407904, 5.570489918457545), 9, True, False)
            
            var_3 = obj_0.is_in_house()
            var_0 = obj_0.is_out_of_play()
            var_2 = obj_0.is_out_of_play()
            var_1 = obj_0.__str__()
        
    def test_307(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (2.6921094481778116, -3.81226820597481), 10, False, False)
            
            var_3 = obj_0.is_out_of_bounds()
            var_4 = obj_0.__str__()
            var_2 = obj_0.__str__()
            var_0 = obj_0.__str__()
            obj_0.burn()
        
    def test_308(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        obj_2.add_end(End(False))
        var_0 = obj_2.score()
        var_4 = obj_2.score()
        var_3 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_3, 'End |    1 |    2 | Total\n----|------|------|------\nRed |    0 |    0 |     0\nYel | h  0 | h  0 |     0\n')
        self.assertEqual(var_4, (0, 0))
        
    def test_309(self):
        obj_2 = Game()
        
        var_2 = obj_2.__str__()
        obj_2.add_end(End(False))
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_2, 'Game with 0 ends')
        
    def test_310(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            obj_1.add_stone(Stone(False, (-6.290905246102078, 5.420348600772543), -1, False, True))
            var_2 = obj_1.drawn()
            var_0 = obj_1.done()
            obj_1.add_stone(Stone(True, (6.734443604585239, -0.6662091482464252), 10, False, True))
            var_4 = obj_1.overlaps_any_stone(Stone(False, (-5.232855191584843, 1.8711645297329635), 7, True, True))
            obj_1.add_stone(Stone(True, (4.997425876850844, 6.8324083293129885), 1, False, False))
        
    def test_311(self):
        obj_1 = End(True)
        
        var_4 = obj_1.red_won()
        var_1 = obj_1.__str__()
        var_0 = obj_1.done()
        var_3 = obj_1.__str__()
        var_2 = obj_1.__str__()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, 'End with Red hammer and 0 stones')
        self.assertEqual(var_2, 'End with Red hammer and 0 stones')
        self.assertEqual(var_3, 'End with Red hammer and 0 stones')
        self.assertEqual(var_4, None)
        
    def test_312(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (-3.6124931552655895, 7.595676748349247), 1, True, True)
            
            obj_0.burn()
            var_1 = obj_0.is_guard()
        
    def test_313(self):
        with self.assertRaisesRegex(ValueError, "The first stone must be thrown by the team without the hammer."):
            obj_1 = End(False)
            
            var_4 = obj_1.__str__()
            var_1 = obj_1.drawn()
            var_0 = obj_1.red_won()
            var_3 = obj_1.drawn()
            obj_1.add_stone(Stone(False, (2.354456185513378, -0.7476437498444639), 9, False, True))
        
    def test_314(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        
    def test_315(self):
        obj_2 = Game()
        
        var_1 = obj_2.__str__()
        var_2 = obj_2.display_scoreboard()
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_316(self):
        obj_2 = Game()
        
        var_2 = obj_2.score()
        var_0 = obj_2.__str__()
        var_1 = obj_2.red_winner()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, (0, 0))
        
    def test_317(self):
        obj_1 = End(True)
        
        var_2 = obj_1.__str__()
        var_0 = obj_1.overlaps_any_stone(Stone(False, (-7.000933479695675, 1.0031650067184508), 7, False, True))
        var_1 = obj_1.score()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, 0)
        self.assertEqual(var_2, 'End with Red hammer and 0 stones')
        
    def test_318(self):
        obj_1 = End(False)
        
        var_1 = obj_1.__str__()
        var_0 = obj_1.__str__()
        
        self.assertEqual(var_0, 'End with Yellow hammer and 0 stones')
        self.assertEqual(var_1, 'End with Yellow hammer and 0 stones')
        
    def test_319(self):
        obj_0 = Stone(False, (-7.528398823924547, 4.708820401076528), 4, True, True)
        
        var_0 = obj_0.is_passed_hogline()
        var_2 = obj_0.is_out_of_bounds()
        var_1 = obj_0.is_out_of_bounds()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, False)
        
    def test_320(self):
        obj_2 = Game()
        
        var_2 = obj_2.red_winner()
        var_0 = obj_2.__str__()
        var_1 = obj_2.display_scoreboard()
        var_3 = obj_2.score()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, (0, 0))
        
    def test_321(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_5 = obj_1.done()
            var_4 = obj_1.red_won()
            var_3 = obj_1.red_won()
            var_2 = obj_1.__str__()
            var_1 = obj_1.overlaps_any_stone(Stone(False, (2.3770863661263117, -3.573820091539382), 11, True, False))
            var_0 = obj_1.drawn()
        
    def test_322(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        obj_2.add_end(End(False))
        
        self.assertEqual(var_0, None)
        
    def test_323(self):
        obj_1 = End(True)
        
        var_0 = obj_1.__str__()
        
        self.assertEqual(var_0, 'End with Red hammer and 0 stones')
        
    def test_324(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            obj_1.add_stone(Stone(True, (-5.750758050847956, 1.3796215005560821), -2, False, False))
            obj_1.add_stone(Stone(True, (-6.129650088959464, 2.95279393175948), 4, False, False))
            var_2 = obj_1.red_won()
            obj_1.add_stone(Stone(False, (6.180232374378173, -7.052814158043395), 1, False, True))
        
    def test_325(self):
        with self.assertRaisesRegex(ValueError, "Cannot calculate distance to center for a burned stone."):
            obj_0 = Stone(False, (6.309032831594996, -3.2406795134515924), 5, True, True)
            
            var_0 = obj_0.is_guard()
            var_1 = obj_0.is_out_of_play()
            var_2 = obj_0.distance_to_center()
        
    def test_326(self):
        obj_2 = Game()
        
        var_1 = obj_2.display_scoreboard()
        var_4 = obj_2.score()
        var_0 = obj_2.__str__()
        var_2 = obj_2.red_winner()
        var_3 = obj_2.score()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, (0, 0))
        self.assertEqual(var_4, (0, 0))
        
    def test_327(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (7.998208857215181, -0.2047029058153207), 12, True, True)
            
            var_1 = obj_0.distance_to_center()
            var_2 = obj_0.distance_to_center()
            var_0 = obj_0.is_out_of_bounds()
            var_5 = obj_0.distance_to_center()
            var_3 = obj_0.is_in_house()
            var_7 = obj_0.distance_to_center()
            var_6 = obj_0.is_out_of_bounds()
            var_4 = obj_0.is_out_of_play()
        
    def test_328(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        var_1 = obj_2.score()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, (0, 0))
        
    def test_329(self):
        obj_0 = Stone(True, (1.2678451948781362, -1.3092694992403668), 5, True, True)
        
        var_0 = obj_0.is_in_house()
        
        self.assertEqual(var_0, False)
        
    def test_330(self):
        obj_0 = Stone(False, (-2.730998892149554, -7.467816663898626), 7, False, True)
        
        var_0 = obj_0.is_passed_hogline()
        
        self.assertEqual(var_0, False)
        
    def test_331(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (7.914735367237302, 5.0135194151130555), 1, False, True)
            
            var_3 = obj_0.is_out_of_play()
            obj_0.move_out_of_play()
            var_6 = obj_0.is_out_of_play()
            obj_0.burn()
            var_2 = obj_0.is_out_of_bounds()
            var_4 = obj_0.is_out_of_play()
            obj_0.burn()
            var_1 = obj_0.is_in_house()
        
    def test_332(self):
        obj_0 = Stone(True, (-7.919129602546391, -6.972443197677297), 9, True, True)
        
        var_0 = obj_0.is_out_of_bounds()
        
        self.assertEqual(var_0, False)
        
    def test_333(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (-7.963569259142224, -3.582342139389292), 6, False, False)
            
            var_5 = obj_0.is_passed_hogline()
            var_6 = obj_0.distance_to_center()
            obj_0.burn()
            var_1 = obj_0.distance_to_center()
            obj_0.move_out_of_play()
            var_4 = obj_0.move((4.797690177052182, 2.096378112878714), 11, True)
            var_3 = obj_0.is_out_of_bounds()
        
    def test_334(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_4 = obj_1.done()
            var_1 = obj_1.drawn()
            var_5 = obj_1.done()
            var_6 = obj_1.overlaps_any_stone(Stone(True, (-1.5003783451722263, -0.027874525105673342), 6, False, False))
            var_2 = obj_1.drawn()
            var_3 = obj_1.overlaps_any_stone(Stone(True, (-5.550935135374633, 1.7497512804361879), 3, True, False))
            var_0 = obj_1.overlaps_any_stone(Stone(False, (3.246006920999694, 1.1000684341966238), 12, True, False))
        
    def test_335(self):
        obj_1 = End(True)
        
        var_1 = obj_1.__str__()
        var_2 = obj_1.score()
        var_0 = obj_1.__str__()
        
        self.assertEqual(var_0, 'End with Red hammer and 0 stones')
        self.assertEqual(var_1, 'End with Red hammer and 0 stones')
        self.assertEqual(var_2, 0)
        
    def test_336(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (6.447141378776662, 0.8646439492869558), 10, True, False)
            
            var_0 = obj_0.distance_to_center()
            var_1 = obj_0.is_guard()
        
    def test_337(self):
        with self.assertRaisesRegex(ValueError, "The first stone must be thrown by the team without the hammer."):
            obj_1 = End(True)
            
            obj_1.add_stone(Stone(True, (0.7294682573715292, -2.021773648652065), 2, True, True))
            var_2 = obj_1.__str__()
            var_0 = obj_1.overlaps_any_stone(Stone(False, (0.027708217065848473, 7.1136633018797255), 3, True, False))
        
    def test_338(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (7.152009191620374, 0.2377697817922506), 12, True, False)
            
            obj_0.burn()
            var_3 = obj_0.move((-1.154185477433522, -3.5344327279973644), 6, True)
            obj_0.burn()
            var_1 = obj_0.is_guard()
        
    def test_339(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (7.4943424672997985, 2.1186484089029296), 11, False, True)
            
            var_1 = obj_0.is_out_of_play()
            obj_0.burn()
        
    def test_340(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (0.2678952363833549, 4.307749888019959), -2, True, True)
            
            var_2 = obj_0.is_guard()
            var_3 = obj_0.is_guard()
            var_1 = obj_0.is_in_house()
            var_4 = obj_0.is_guard()
            var_0 = obj_0.__str__()
        
    def test_341(self):
        obj_2 = Game()
        
        var_2 = obj_2.display_scoreboard()
        obj_2.add_end(End(True))
        var_1 = obj_2.display_scoreboard()
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |    1 | Total\n----|------|------\nRed | h  0 |     0\nYel |    0 |     0\n')
        self.assertEqual(var_1, 'End |    1 | Total\n----|------|------\nRed | h  0 |     0\nYel |    0 |     0\n')
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_342(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_5 = obj_1.red_won()
            var_6 = obj_1.overlaps_any_stone(Stone(False, (6.3042495508834016, -7.369528572244974), -1, True, True))
            var_1 = obj_1.score()
            var_0 = obj_1.red_won()
            var_2 = obj_1.overlaps_any_stone(Stone(False, (-0.7118624073436415, 0.9392605709037838), 12, True, False))
            var_4 = obj_1.red_won()
            var_3 = obj_1.red_won()
        
    def test_343(self):
        with self.assertRaisesRegex(ValueError, "The first stone must be thrown by the team without the hammer."):
            obj_1 = End(False)
            
            var_1 = obj_1.red_won()
            var_4 = obj_1.score()
            var_0 = obj_1.__str__()
            var_3 = obj_1.done()
            obj_1.add_stone(Stone(False, (4.885121007178258, -3.7116801198774407), 8, True, True))
        
    def test_344(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (-7.079318300526355, -6.00634791567202), 5, False, True)
            
            var_6 = obj_0.is_passed_hogline()
            obj_0.move_out_of_play()
            var_0 = obj_0.move((2.26237192690221, 2.2180700957032755), 2, True)
            obj_0.move_out_of_play()
            var_5 = obj_0.move((7.37402518126931, 0.19563353360221036), 1, True)
            var_1 = obj_0.is_passed_hogline()
            var_2 = obj_0.is_guard()
            var_7 = obj_0.is_out_of_bounds()
        
    def test_345(self):
        obj_1 = End(False)
        
        var_5 = obj_1.done()
        var_2 = obj_1.red_won()
        var_0 = obj_1.red_won()
        var_1 = obj_1.__str__()
        var_3 = obj_1.score()
        var_6 = obj_1.drawn()
        var_4 = obj_1.__str__()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'End with Yellow hammer and 0 stones')
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, 0)
        self.assertEqual(var_4, 'End with Yellow hammer and 0 stones')
        self.assertEqual(var_5, False)
        self.assertEqual(var_6, True)
        
    def test_346(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        var_1 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, 'Game with 0 ends')
        
    def test_347(self):
        obj_2 = Game()
        
        obj_2.add_end(End(True))
        
        
    def test_348(self):
        obj_1 = End(False)
        
        var_2 = obj_1.done()
        var_0 = obj_1.drawn()
        var_1 = obj_1.drawn()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, True)
        self.assertEqual(var_2, False)
        
    def test_349(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-0.38791800170649005, 0.7972038426218901), 12, False, False)
            
            var_0 = obj_0.move((-5.506953175885537, 5.2074454005962885), 3, True)
        
    def test_350(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (4.086766684442132, 2.4853839890510354), 6, True, False)
            
            var_4 = obj_0.distance_to_center()
            obj_0.burn()
            var_3 = obj_0.distance_to_center()
            var_0 = obj_0.distance_to_center()
            obj_0.move_out_of_play()
            var_5 = obj_0.distance_to_center()
        
    def test_351(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        
        
    def test_352(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_353(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (-5.908024516018875, 3.039353839887376), 6, True, True)
            
            obj_0.move_out_of_play()
            var_1 = obj_0.move((0.02654323135784864, 4.072281250485117), 3, True)
            var_2 = obj_0.distance_to_center()
        
    def test_354(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-7.186240516973019, 6.372648861825505), 1, True, False)
            
            var_3 = obj_0.is_in_house()
            var_1 = obj_0.is_in_house()
            obj_0.burn()
            var_4 = obj_0.distance_to_center()
            var_2 = obj_0.is_in_house()
        
    def test_355(self):
        obj_2 = Game()
        
        var_2 = obj_2.red_winner()
        var_0 = obj_2.red_winner()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_2, None)
        
    def test_356(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (-0.5378997554203266, 7.40983027392749), 9, False, False)
            
            var_3 = obj_0.is_out_of_play()
            var_2 = obj_0.move((5.456589440657927, -0.33942093192647427), 4, True)
            obj_0.move_out_of_play()
            obj_0.move_out_of_play()
        
    def test_357(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_2 = obj_1.done()
            var_0 = obj_1.red_won()
            var_3 = obj_1.drawn()
            var_1 = obj_1.score()
            var_5 = obj_1.red_won()
            obj_1.add_stone(Stone(False, (-5.133632628049515, 2.5606325040154037), -1, False, False))
            obj_1.add_stone(Stone(False, (0.7666697156167555, 4.910554961201507), 3, True, False))
        
    def test_358(self):
        obj_2 = Game()
        
        obj_2.add_end(End(True))
        
        
    def test_359(self):
        obj_2 = Game()
        
        var_2 = obj_2.display_scoreboard()
        var_4 = obj_2.display_scoreboard()
        var_0 = obj_2.display_scoreboard()
        var_3 = obj_2.red_winner()
        obj_2.add_end(End(False))
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_3, None)
        self.assertEqual(var_4, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_360(self):
        obj_1 = End(False)
        
        var_4 = obj_1.red_won()
        var_1 = obj_1.score()
        var_0 = obj_1.drawn()
        var_3 = obj_1.score()
        var_2 = obj_1.drawn()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, 0)
        self.assertEqual(var_2, True)
        self.assertEqual(var_3, 0)
        self.assertEqual(var_4, None)
        
    def test_361(self):
        obj_2 = Game()
        
        var_2 = obj_2.red_winner()
        var_1 = obj_2.__str__()
        var_0 = obj_2.score()
        var_3 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_362(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        var_1 = obj_2.red_winner()
        var_4 = obj_2.__str__()
        var_3 = obj_2.score()
        var_2 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, (0, 0))
        self.assertEqual(var_4, 'Game with 0 ends')
        
    def test_363(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (6.691494423705711, 6.391790033858591), 10, False, False)
            
            var_5 = obj_0.is_guard()
            var_6 = obj_0.distance_to_center()
            obj_0.burn()
            var_1 = obj_0.is_guard()
            var_7 = obj_0.move((-7.963295623761857, 0.7151547368537567), 7, True)
            var_0 = obj_0.move((5.721641828413581, -4.3299506164478405), 4, False)
            var_8 = obj_0.is_passed_hogline()
            var_2 = obj_0.distance_to_center()
            var_4 = obj_0.distance_to_center()
            var_3 = obj_0.distance_to_center()
        
    def test_364(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
            obj_2 = Game()
            
            var_4 = obj_2.display_scoreboard()
            var_1 = obj_2.score()
            obj_2.add_end(End(True))
            var_2 = obj_2.red_winner()
            obj_2.add_end(End(False))
        
    def test_365(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
            obj_2 = Game()
            
            obj_2.add_end(End(False))
            var_2 = obj_2.display_scoreboard()
            obj_2.add_end(End(True))
            var_3 = obj_2.score()
        
    def test_366(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_3 = obj_1.score()
            obj_1.add_stone(Stone(True, (-2.692867793802506, 6.773631295083053), 3, False, False))
            var_2 = obj_1.__str__()
            obj_1.add_stone(Stone(False, (3.598842904683101, -4.605066138705222), 5, True, True))
            var_4 = obj_1.__str__()
            var_6 = obj_1.red_won()
            var_5 = obj_1.done()
        
    def test_367(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            obj_1.add_stone(Stone(False, (3.605271904030202, -6.893554320906977), -1, True, True))
        
    def test_368(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        var_1 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, None)
        
    def test_369(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-2.7163467633580733, 5.727237571626274), 12, False, False)
            
            var_3 = obj_0.is_passed_hogline()
            var_2 = obj_0.distance_to_center()
            obj_0.move_out_of_play()
            var_0 = obj_0.move((3.2198219876218506, 7.203644610993068), 3, False)
        
    def test_370(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (3.341765503681316, 4.630202655290066), -2, False, False)
            
            var_0 = obj_0.is_guard()
            var_1 = obj_0.distance_to_center()
            var_3 = obj_0.__str__()
            var_2 = obj_0.is_guard()
        
    def test_371(self):
        obj_1 = End(True)
        
        var_0 = obj_1.red_won()
        
        self.assertEqual(var_0, None)
        
    def test_372(self):
        obj_2 = Game()
        
        var_1 = obj_2.__str__()
        var_2 = obj_2.__str__()
        obj_2.add_end(End(False))
        
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, 'Game with 0 ends')
        
    def test_373(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_2 = obj_1.overlaps_any_stone(Stone(False, (-5.215380962803643, -1.113167297518876), 0, True, False))
            var_1 = obj_1.score()
            var_0 = obj_1.score()
        
    def test_374(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        var_1 = obj_2.red_winner()
        var_2 = obj_2.score()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, (0, 0))
        
    def test_375(self):
        obj_2 = Game()
        
        var_3 = obj_2.red_winner()
        var_2 = obj_2.__str__()
        var_0 = obj_2.red_winner()
        obj_2.add_end(End(False))
        var_4 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, None)
        self.assertEqual(var_4, 'End |    1 | Total\n----|------|------\nRed |    0 |     0\nYel | h  0 |     0\n')
        
    def test_376(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (7.420544168170798, -1.641494457408232), 9, False, False)
            
            var_2 = obj_0.is_out_of_play()
            var_4 = obj_0.is_in_house()
            var_5 = obj_0.is_in_house()
            var_0 = obj_0.is_out_of_bounds()
            var_7 = obj_0.move((-1.44990695792084, -3.4258728766650357), 12, False)
            obj_0.burn()
            var_6 = obj_0.is_passed_hogline()
            var_1 = obj_0.is_out_of_bounds()
        
    def test_377(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_0 = obj_1.score()
            var_1 = obj_1.__str__()
            var_4 = obj_1.score()
            var_6 = obj_1.overlaps_any_stone(Stone(True, (-6.885895043330976, -7.704679568263174), 3, False, True))
            var_3 = obj_1.overlaps_any_stone(Stone(False, (-3.789776182031469, -1.232734217272025), 6, True, False))
            var_5 = obj_1.red_won()
            var_2 = obj_1.red_won()
        
    def test_378(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-4.63714778175717, -4.015574373941895), -2, True, True)
            
            var_0 = obj_0.is_guard()
        
    def test_379(self):
        obj_1 = End(True)
        
        var_0 = obj_1.__str__()
        
        self.assertEqual(var_0, 'End with Red hammer and 0 stones')
        
    def test_380(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_0 = obj_1.__str__()
            var_4 = obj_1.drawn()
            var_1 = obj_1.__str__()
            var_2 = obj_1.done()
            obj_1.add_stone(Stone(True, (0.0323946934233188, 1.3680647570245679), -1, True, True))
        
    def test_381(self):
        obj_2 = Game()
        
        var_2 = obj_2.__str__()
        var_1 = obj_2.display_scoreboard()
        var_4 = obj_2.red_winner()
        var_0 = obj_2.score()
        var_3 = obj_2.__str__()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, 'Game with 0 ends')
        self.assertEqual(var_4, None)
        
    def test_382(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            obj_1.add_stone(Stone(False, (-1.4860333881556596, 7.562775363365848), 5, True, False))
            var_0 = obj_1.drawn()
        
    def test_383(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (0.28084588647969966, 0.900407660171135), 11, True, True)
            
            var_4 = obj_0.move((-6.952845554594456, -3.0597561766540515), 5, False)
            var_0 = obj_0.move((-0.30659109093841685, -4.540976491997105), 6, True)
            obj_0.burn()
            var_2 = obj_0.distance_to_center()
            var_3 = obj_0.is_out_of_play()
        
    def test_384(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-6.849789702824593, -3.233523154120091), 1, True, True)
            
            var_2 = obj_0.is_in_house()
            var_0 = obj_0.move((-7.443049704698947, -7.412412801307038), 5, True)
            var_1 = obj_0.is_out_of_play()
        
    def test_385(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        var_1 = obj_2.score()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, (0, 0))
        
    def test_386(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-6.874642645721488, -2.3324871526045214), -1, True, True)
            
            var_1 = obj_0.__str__()
            var_2 = obj_0.is_in_house()
            var_3 = obj_0.distance_to_center()
            var_0 = obj_0.is_in_house()
        
    def test_387(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        
    def test_388(self):
        obj_1 = End(True)
        
        var_1 = obj_1.__str__()
        var_0 = obj_1.done()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, 'End with Red hammer and 0 stones')
        
    def test_389(self):
        obj_1 = End(False)
        
        var_0 = obj_1.done()
        
        self.assertEqual(var_0, False)
        
    def test_390(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(False, (-0.4688588929922215, -2.841333991316718), 1, True, False)
            
            var_1 = obj_0.distance_to_center()
            obj_0.burn()
            var_6 = obj_0.is_in_house()
            var_5 = obj_0.move((3.685117570033702, 5.35319883972814), 1, True)
            var_0 = obj_0.is_out_of_bounds()
            obj_0.move_out_of_play()
            var_2 = obj_0.is_guard()
            var_7 = obj_0.is_in_house()
        
    def test_391(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_1 = obj_1.red_won()
            obj_1.add_stone(Stone(False, (5.22788597430975, -2.6011619868966385), 2, False, False))
            var_3 = obj_1.drawn()
            var_4 = obj_1.overlaps_any_stone(Stone(False, (-3.7290142082587927, -5.569741978477023), 2, True, False))
            var_6 = obj_1.done()
            var_5 = obj_1.overlaps_any_stone(Stone(True, (7.14254195895289, 5.281068431018284), 1, False, False))
            var_0 = obj_1.__str__()
        
    def test_392(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        var_1 = obj_2.__str__()
        var_2 = obj_2.score()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, (0, 0))
        
    def test_393(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_394(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
            obj_2 = Game()
            
            obj_2.add_end(End(False))
            obj_2.add_end(End(True))
            var_3 = obj_2.red_winner()
            var_2 = obj_2.red_winner()
            obj_2.add_end(End(True))
        
    def test_395(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        
        
    def test_396(self):
        obj_2 = Game()
        
        var_2 = obj_2.__str__()
        var_1 = obj_2.red_winner()
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 'Game with 0 ends')
        
    def test_397(self):
        obj_1 = End(True)
        
        var_1 = obj_1.__str__()
        var_0 = obj_1.score()
        var_2 = obj_1.__str__()
        var_4 = obj_1.done()
        var_3 = obj_1.score()
        
        self.assertEqual(var_0, 0)
        self.assertEqual(var_1, 'End with Red hammer and 0 stones')
        self.assertEqual(var_2, 'End with Red hammer and 0 stones')
        self.assertEqual(var_3, 0)
        self.assertEqual(var_4, False)
        
    def test_398(self):
        with self.assertRaisesRegex(ValueError, "The first stone must be thrown by the team without the hammer."):
            obj_1 = End(True)
            
            var_1 = obj_1.drawn()
            var_3 = obj_1.__str__()
            obj_1.add_stone(Stone(True, (3.9084323815228803, 2.2425331784078626), 8, False, True))
            var_2 = obj_1.drawn()
        
    def test_399(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_0 = obj_1.overlaps_any_stone(Stone(False, (7.770431605422255, -4.132156709290392), 8, False, False))
        
    def test_400(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-0.2872240969308777, -2.334188949365746), -1, True, True)
            
            var_7 = obj_0.is_passed_hogline()
            var_4 = obj_0.is_out_of_bounds()
            var_5 = obj_0.move((6.837894242667447, -5.083127103926824), 1, True)
            var_9 = obj_0.distance_to_center()
            var_3 = obj_0.is_in_house()
            var_6 = obj_0.is_in_house()
            var_0 = obj_0.distance_to_center()
            obj_0.move_out_of_play()
            var_8 = obj_0.__str__()
            var_2 = obj_0.is_passed_hogline()
        
    def test_401(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        
    def test_402(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-1.5934473265561575, -5.664379573635436), -1, False, False)
            
            var_2 = obj_0.is_guard()
            var_0 = obj_0.is_in_house()
            obj_0.burn()
            var_3 = obj_0.is_out_of_bounds()
            var_7 = obj_0.is_passed_hogline()
            var_4 = obj_0.is_guard()
            var_1 = obj_0.__str__()
            var_5 = obj_0.move((-3.9465617837675104, -3.6686402889889376), 1, False)
        
    def test_403(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-3.737774016857486, 4.640791611661614), 6, False, False)
            
            var_1 = obj_0.is_out_of_bounds()
            var_2 = obj_0.move((-0.5783413142547325, 1.6435304611237846), 8, True)
            obj_0.move_out_of_play()
        
    def test_404(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-7.361618462433084, 4.952110246244995), 12, False, True)
            
            var_4 = obj_0.__str__()
            var_0 = obj_0.move((3.9864629913433998, 7.2743335648068115), 1, True)
            var_3 = obj_0.is_out_of_play()
            obj_0.move_out_of_play()
            var_1 = obj_0.move((-4.346790219768666, -5.207516299910845), 7, False)
        
    def test_405(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_4 = obj_1.drawn()
            var_1 = obj_1.score()
            var_3 = obj_1.done()
            var_0 = obj_1.drawn()
            obj_1.add_stone(Stone(True, (-0.6456089462948924, 0.332769067581312), -1, False, False))
        
    def test_406(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_1 = obj_1.drawn()
            var_0 = obj_1.overlaps_any_stone(Stone(True, (-5.796831650340563, -2.503188630820521), 11, True, True))
        
    def test_407(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_2 = obj_1.red_won()
            var_1 = obj_1.__str__()
            obj_1.add_stone(Stone(False, (5.520071442588302, 5.4990376565215), -1, False, True))
        
    def test_408(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-7.312890664651693, 5.188491974380462), 7, False, True)
            
            var_2 = obj_0.__str__()
            var_0 = obj_0.move((-2.2193333806532625, 6.7261402296803645), 12, False)
            var_3 = obj_0.is_in_house()
            obj_0.move_out_of_play()
            var_4 = obj_0.distance_to_center()
        
    def test_409(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_0 = obj_1.drawn()
            obj_1.add_stone(Stone(True, (4.469270146846927, -0.5265958195760696), 3, False, False))
            var_5 = obj_1.score()
            var_1 = obj_1.red_won()
            var_3 = obj_1.__str__()
            var_4 = obj_1.done()
        
    def test_410(self):
        obj_2 = Game()
        
        obj_2.add_end(End(True))
        var_2 = obj_2.red_winner()
        var_4 = obj_2.score()
        var_1 = obj_2.red_winner()
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, None)
        self.assertEqual(var_4, (0, 0))
        
    def test_411(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_1 = obj_1.overlaps_any_stone(Stone(True, (1.0304470885599741, 2.615779718094714), 12, False, True))
            obj_1.add_stone(Stone(False, (-4.337622990639963, -3.3776507585669364), 11, True, False))
            var_0 = obj_1.drawn()
            var_3 = obj_1.done()
        
    def test_412(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            obj_1.add_stone(Stone(True, (-2.9740907956597287, -2.2598135511749113), 4, False, False))
            var_2 = obj_1.score()
            var_0 = obj_1.drawn()
        
    def test_413(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        var_1 = obj_2.display_scoreboard()
        var_2 = obj_2.score()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, (0, 0))
        
    def test_414(self):
        obj_1 = End(False)
        
        var_0 = obj_1.drawn()
        var_1 = obj_1.drawn()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, True)
        
    def test_415(self):
        obj_2 = Game()
        
        var_4 = obj_2.display_scoreboard()
        var_0 = obj_2.score()
        var_2 = obj_2.display_scoreboard()
        var_3 = obj_2.score()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_3, (0, 0))
        self.assertEqual(var_4, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_416(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        var_3 = obj_2.display_scoreboard()
        var_1 = obj_2.score()
        var_2 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_417(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (5.82532756803835, -0.24202651456190338), 2, False, False)
            
            var_8 = obj_0.move((5.545875004591016, 0.5935276726327885), 12, False)
            var_1 = obj_0.is_out_of_bounds()
            var_6 = obj_0.is_out_of_bounds()
            obj_0.burn()
            obj_0.move_out_of_play()
            var_7 = obj_0.is_out_of_bounds()
            var_5 = obj_0.is_guard()
            var_4 = obj_0.is_out_of_bounds()
            obj_0.move_out_of_play()
        
    def test_418(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_4 = obj_1.overlaps_any_stone(Stone(False, (-7.147461506954409, -7.063344941980439), 7, False, False))
            obj_1.add_stone(Stone(True, (6.569697848330673, 2.5649236574694765), 10, False, True))
            var_1 = obj_1.overlaps_any_stone(Stone(False, (7.078777945638167, -7.338954451075148), -2, False, False))
            obj_1.add_stone(Stone(False, (-1.7874299685142798, -4.5840375983653825), 4, True, False))
            obj_1.add_stone(Stone(False, (5.150336327899513, 3.8621295135552334), 4, True, False))
            var_3 = obj_1.done()
            var_6 = obj_1.score()
        
    def test_419(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-7.078609544009252, -4.361041664551127), 12, True, True)
            
            var_0 = obj_0.is_in_house()
            var_1 = obj_0.is_guard()
            var_2 = obj_0.__str__()
        
    def test_420(self):
        with self.assertRaisesRegex(ValueError, "The first stone must be thrown by the team without the hammer."):
            obj_1 = End(True)
            
            var_1 = obj_1.done()
            obj_1.add_stone(Stone(True, (7.081788796590617, 5.46425191449322), 6, False, True))
            var_3 = obj_1.__str__()
            var_2 = obj_1.score()
            obj_1.add_stone(Stone(True, (6.096974452718305, 2.9736053678047494), 5, True, True))
            obj_1.add_stone(Stone(True, (0.9825754680390411, -1.795011018054442), 3, False, False))
            obj_1.add_stone(Stone(True, (7.2149109771511295, 4.290862972282374), 2, True, False))
        
    def test_421(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        
    def test_422(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(False, (-5.531397038433916, 3.5720622368582653), 2, True, True)
            
            var_2 = obj_0.move((-5.038561876695885, -1.5260508640439863), 12, False)
            var_0 = obj_0.is_out_of_bounds()
            obj_0.move_out_of_play()
        
    def test_423(self):
        obj_2 = Game()
        
        obj_2.add_end(End(True))
        var_1 = obj_2.display_scoreboard()
        
        self.assertEqual(var_1, 'End |    1 | Total\n----|------|------\nRed | h  0 |     0\nYel |    0 |     0\n')
        
    def test_424(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        
    def test_425(self):
        obj_2 = Game()
        
        var_2 = obj_2.__str__()
        var_1 = obj_2.display_scoreboard()
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, 'Game with 0 ends')
        
    def test_426(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
            obj_2 = Game()
            
            obj_2.add_end(End(False))
            var_2 = obj_2.__str__()
            var_1 = obj_2.score()
            obj_2.add_end(End(True))
            var_3 = obj_2.red_winner()
        
    def test_427(self):
        obj_1 = End(True)
        
        var_0 = obj_1.red_won()
        
        self.assertEqual(var_0, None)
        
    def test_428(self):
        obj_2 = Game()
        
        var_2 = obj_2.score()
        var_1 = obj_2.red_winner()
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, (0, 0))
        
    def test_429(self):
        obj_1 = End(False)
        
        var_0 = obj_1.__str__()
        var_1 = obj_1.red_won()
        
        self.assertEqual(var_0, 'End with Yellow hammer and 0 stones')
        self.assertEqual(var_1, None)
        
    def test_430(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (2.989241987645567, -3.4555581317613075), 6, False, False)
            
            var_0 = obj_0.distance_to_center()
            var_1 = obj_0.is_out_of_bounds()
        
    def test_431(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            obj_1.add_stone(Stone(True, (6.915545422437578, 0.8389850550764972), 2, False, False))
            var_4 = obj_1.overlaps_any_stone(Stone(False, (2.8729104652475126, 7.270056857677677), 10, True, False))
            var_3 = obj_1.score()
            var_5 = obj_1.drawn()
            var_2 = obj_1.score()
            var_0 = obj_1.overlaps_any_stone(Stone(True, (0.8071398212819165, -6.154965674981563), 3, False, True))
        
    def test_432(self):
        obj_2 = Game()
        
        var_3 = obj_2.red_winner()
        var_1 = obj_2.__str__()
        var_2 = obj_2.__str__()
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, None)
        
    def test_433(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        var_1 = obj_2.display_scoreboard()
        var_3 = obj_2.score()
        var_2 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_3, (0, 0))
        
    def test_434(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        var_1 = obj_2.display_scoreboard()
        var_2 = obj_2.score()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, (0, 0))
        
    def test_435(self):
        obj_2 = Game()
        
        var_2 = obj_2.display_scoreboard()
        var_1 = obj_2.red_winner()
        var_3 = obj_2.red_winner()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_3, None)
        
    def test_436(self):
        obj_0 = Stone(False, (-0.1512413766256202, -1.6461507917757956), 7, True, True)
        
        var_0 = obj_0.is_out_of_bounds()
        
        self.assertEqual(var_0, False)
        
    def test_437(self):
        obj_0 = Stone(False, (2.683522104068997, -6.87623543045102), 5, False, True)
        
        var_0 = obj_0.is_passed_hogline()
        
        self.assertEqual(var_0, False)
        
    def test_438(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-0.941634110807005, -1.1490616527636508), -2, False, False)
            
            var_0 = obj_0.distance_to_center()
            obj_0.move_out_of_play()
            var_1 = obj_0.__str__()
        
    def test_439(self):
        obj_0 = Stone(False, (0.07897143538240137, -4.912974924021848), 1, False, False)
        
        var_0 = obj_0.is_out_of_bounds()
        
        self.assertEqual(var_0, False)
        
    def test_440(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-7.630247798152734, 7.073887289105052), 12, False, True)
            
            obj_0.move_out_of_play()
            var_2 = obj_0.is_passed_hogline()
            obj_0.burn()
            var_4 = obj_0.move((-6.2108210219586315, -3.8187010841185796), 7, False)
            var_1 = obj_0.move((0.38051056513349124, -5.935729300663295), 9, True)
            var_5 = obj_0.is_out_of_bounds()
            var_3 = obj_0.distance_to_center()
        
    def test_441(self):
        obj_1 = End(False)
        
        var_1 = obj_1.done()
        var_0 = obj_1.drawn()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, False)
        
    def test_442(self):
        obj_2 = Game()
        
        var_1 = obj_2.display_scoreboard()
        var_3 = obj_2.__str__()
        var_2 = obj_2.__str__()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, 'Game with 0 ends')
        
    def test_443(self):
        obj_1 = End(False)
        
        var_0 = obj_1.score()
        
        self.assertEqual(var_0, 0)
        
    def test_444(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        
    def test_445(self):
        obj_2 = Game()
        
        var_2 = obj_2.score()
        var_0 = obj_2.score()
        var_1 = obj_2.display_scoreboard()
        var_3 = obj_2.red_winner()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, (0, 0))
        self.assertEqual(var_3, None)
        
    def test_446(self):
        obj_2 = Game()
        
        var_1 = obj_2.display_scoreboard()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_447(self):
        obj_2 = Game()
        
        var_2 = obj_2.red_winner()
        var_0 = obj_2.score()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_2, None)
        
    def test_448(self):
        obj_2 = Game()
        
        var_1 = obj_2.red_winner()
        var_0 = obj_2.score()
        var_2 = obj_2.red_winner()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, None)
        
    def test_449(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (4.88339155108882, -5.8978971070181085), 9, True, False)
            
            var_5 = obj_0.is_passed_hogline()
            var_4 = obj_0.is_passed_hogline()
            var_6 = obj_0.is_out_of_bounds()
            var_2 = obj_0.is_in_house()
            var_8 = obj_0.is_out_of_play()
            var_3 = obj_0.is_out_of_play()
            var_7 = obj_0.is_guard()
            obj_0.move_out_of_play()
            obj_0.move_out_of_play()
        
    def test_450(self):
        obj_2 = Game()
        
        var_1 = obj_2.red_winner()
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, None)
        
    def test_451(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_2 = obj_1.score()
            var_1 = obj_1.overlaps_any_stone(Stone(False, (-7.564589175772008, 2.7356479185641174), 6, True, False))
            var_5 = obj_1.score()
            var_6 = obj_1.overlaps_any_stone(Stone(False, (-7.886504209350305, 6.221820208141018), -1, True, True))
            var_4 = obj_1.drawn()
            var_3 = obj_1.red_won()
            var_0 = obj_1.score()
        
    def test_452(self):
        obj_1 = End(True)
        
        var_1 = obj_1.red_won()
        var_0 = obj_1.red_won()
        var_5 = obj_1.score()
        var_3 = obj_1.score()
        var_2 = obj_1.red_won()
        var_4 = obj_1.done()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, 0)
        self.assertEqual(var_4, False)
        self.assertEqual(var_5, 0)
        
    def test_453(self):
        obj_1 = End(False)
        
        var_0 = obj_1.done()
        
        self.assertEqual(var_0, False)
        
    def test_454(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-6.7285425773226315, 3.0486987968532), -1, False, True)
            
            var_1 = obj_0.is_guard()
            var_0 = obj_0.distance_to_center()
        
    def test_455(self):
        obj_2 = Game()
        
        var_2 = obj_2.__str__()
        obj_2.add_end(End(False))
        var_4 = obj_2.red_winner()
        var_1 = obj_2.display_scoreboard()
        var_3 = obj_2.__str__()
        
        self.assertEqual(var_1, 'End |    1 | Total\n----|------|------\nRed |    0 |     0\nYel | h  0 |     0\n')
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, 'Game with 1 ends')
        self.assertEqual(var_4, None)
        
    def test_456(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (4.70351088763892, 6.624303992433811), 12, True, True)
            
            var_3 = obj_0.is_in_house()
            var_4 = obj_0.is_in_house()
            var_0 = obj_0.is_passed_hogline()
            var_1 = obj_0.__str__()
            var_5 = obj_0.is_out_of_play()
            var_2 = obj_0.__str__()
        
    def test_457(self):
        obj_2 = Game()
        
        var_3 = obj_2.red_winner()
        var_1 = obj_2.red_winner()
        var_4 = obj_2.display_scoreboard()
        var_0 = obj_2.score()
        var_2 = obj_2.red_winner()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, None)
        self.assertEqual(var_4, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_458(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (-5.695033463938772, 3.9834287884120876), 10, False, False)
            
            obj_0.move_out_of_play()
            var_6 = obj_0.__str__()
            var_3 = obj_0.__str__()
            var_4 = obj_0.move((-0.7326340607112378, 0.594717711546485), 10, False)
            var_2 = obj_0.__str__()
            var_0 = obj_0.is_out_of_bounds()
            var_1 = obj_0.is_out_of_bounds()
        
    def test_459(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_4 = obj_1.__str__()
            var_2 = obj_1.overlaps_any_stone(Stone(False, (-0.4327478800601341, -6.127229255211063), 9, False, False))
            var_5 = obj_1.overlaps_any_stone(Stone(True, (6.211465670581488, 1.21030898991531), -2, False, True))
            var_1 = obj_1.__str__()
            var_3 = obj_1.score()
            obj_1.add_stone(Stone(False, (0.3808138925167537, 0.7341929681024268), -2, True, True))
            var_6 = obj_1.red_won()
        
    def test_460(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (-2.9728138985348895, 0.7777023006759105), 10, False, True)
            
            obj_0.move_out_of_play()
            var_2 = obj_0.is_in_house()
            obj_0.move_out_of_play()
        
    def test_461(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        
    def test_462(self):
        obj_1 = End(False)
        
        var_1 = obj_1.done()
        var_3 = obj_1.drawn()
        var_0 = obj_1.red_won()
        var_2 = obj_1.red_won()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, True)
        
    def test_463(self):
        obj_2 = Game()
        
        var_2 = obj_2.score()
        var_0 = obj_2.display_scoreboard()
        var_1 = obj_2.score()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, (0, 0))
        
    def test_464(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_5 = obj_1.__str__()
            obj_1.add_stone(Stone(True, (2.7373241675013045, -0.31322523086358167), 4, False, False))
            var_6 = obj_1.drawn()
            var_1 = obj_1.__str__()
            var_2 = obj_1.drawn()
            var_4 = obj_1.overlaps_any_stone(Stone(True, (7.593910515150549, -6.493330584727758), 10, False, False))
            var_0 = obj_1.__str__()
        
    def test_465(self):
        obj_1 = End(False)
        
        var_2 = obj_1.red_won()
        var_0 = obj_1.__str__()
        var_1 = obj_1.done()
        
        self.assertEqual(var_0, 'End with Yellow hammer and 0 stones')
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, None)
        
    def test_466(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (-6.9622164272510165, 7.676277056977312), 6, True, True)
            
            var_4 = obj_0.is_passed_hogline()
            var_3 = obj_0.is_passed_hogline()
            var_2 = obj_0.is_out_of_bounds()
            var_5 = obj_0.is_passed_hogline()
            var_0 = obj_0.is_in_house()
            obj_0.burn()
        
    def test_467(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        obj_2.add_end(End(True))
        var_3 = obj_2.__str__()
        var_2 = obj_2.display_scoreboard()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_2, 'End |    1 | Total\n----|------|------\nRed | h  0 |     0\nYel |    0 |     0\n')
        self.assertEqual(var_3, 'Game with 1 ends')
        
    def test_468(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (0.14381702170158484, -1.5157375528584183), 5, True, False)
            
            var_4 = obj_0.move((7.654891226283947, -1.45023017619285), 5, False)
            obj_0.move_out_of_play()
            var_3 = obj_0.is_out_of_play()
            obj_0.move_out_of_play()
            var_2 = obj_0.move((-6.7155811349438395, -2.767260897684274), 10, True)
            var_5 = obj_0.is_passed_hogline()
        
    def test_469(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_470(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-6.204768406550338, -5.47012732906644), 6, True, False)
            
            var_5 = obj_0.distance_to_center()
            var_4 = obj_0.move((-4.135366515481481, 3.5346063824159657), 2, False)
            obj_0.burn()
            var_2 = obj_0.is_guard()
            var_3 = obj_0.move((-2.878958197418367, 3.1271930607195095), 0, False)
            var_1 = obj_0.move((-5.218757291277338, -5.896099046081876), 2, True)
        
    def test_471(self):
        obj_0 = Stone(True, (2.3722106129592895, -3.6426090001716993), 1, True, True)
        
        var_1 = obj_0.is_guard()
        var_2 = obj_0.is_passed_hogline()
        var_0 = obj_0.__str__()
        
        self.assertEqual(var_0, 'Red stone at (-2.50, 5.49), round 1, burned')
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, False)
        
    def test_472(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        var_1 = obj_2.score()
        obj_2.add_end(End(True))
        var_3 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_3, (0, 0))
        
    def test_473(self):
        obj_1 = End(False)
        
        var_0 = obj_1.done()
        
        self.assertEqual(var_0, False)
        
    def test_474(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_475(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_1 = obj_1.overlaps_any_stone(Stone(True, (-2.937191311069693, 7.037996285986917), 8, False, False))
            var_2 = obj_1.drawn()
            var_0 = obj_1.overlaps_any_stone(Stone(True, (0.4725663975219412, 2.5735701584881348), 4, False, True))
        
    def test_476(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            obj_1.add_stone(Stone(False, (4.461913858402646, -7.9381767072980125), 10, True, False))
            var_0 = obj_1.overlaps_any_stone(Stone(False, (5.799392439460091, -4.164304378427856), 0, False, False))
            var_2 = obj_1.drawn()
        
    def test_477(self):
        obj_1 = End(True)
        
        var_0 = obj_1.done()
        
        self.assertEqual(var_0, False)
        
    def test_478(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (5.928498678680242, -6.209104582568527), 0, True, False)
            
            var_7 = obj_0.is_out_of_play()
            var_3 = obj_0.move((4.914905274203919, 0.513753409204174), 1, False)
            var_6 = obj_0.is_out_of_play()
            obj_0.burn()
            var_0 = obj_0.is_out_of_play()
            var_2 = obj_0.__str__()
            obj_0.burn()
            var_4 = obj_0.is_in_house()
            var_8 = obj_0.distance_to_center()
            var_9 = obj_0.is_out_of_play()
        
    def test_479(self):
        obj_2 = Game()
        
        var_2 = obj_2.red_winner()
        var_1 = obj_2.display_scoreboard()
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, None)
        
    def test_480(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        var_2 = obj_2.score()
        var_1 = obj_2.score()
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, (0, 0))
        
    def test_481(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-6.230918492660564, -3.744761792514373), 12, True, True)
            
            var_0 = obj_0.distance_to_center()
            var_1 = obj_0.move((-1.8302853104222248, 1.8501513578324236), 5, True)
        
    def test_482(self):
        obj_2 = Game()
        
        var_3 = obj_2.red_winner()
        var_0 = obj_2.__str__()
        var_1 = obj_2.score()
        obj_2.add_end(End(False))
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_3, None)
        
    def test_483(self):
        with self.assertRaisesRegex(ValueError, "Stone's round does not match the expected round based on the number of stones already placed."):
            obj_1 = End(False)
            
            var_4 = obj_1.score()
            var_2 = obj_1.done()
            var_3 = obj_1.overlaps_any_stone(Stone(True, (-4.347860932778712, 4.337617732747951), 6, True, True))
            obj_1.add_stone(Stone(True, (-4.0801390823055375, 6.307422177532679), 3, False, True))
            obj_1.add_stone(Stone(False, (7.134680950944295, 5.439172030605613), 11, False, True))
        
    def test_484(self):
        obj_0 = Stone(False, (-4.539529544482168, -2.493829309845168), 10, False, True)
        
        var_0 = obj_0.is_out_of_play()
        var_1 = obj_0.is_in_house()
        var_2 = obj_0.is_guard()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, False)
        
    def test_485(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (2.62794955130075, 5.724344814631131), 6, False, False)
            
            obj_0.burn()
            var_2 = obj_0.is_in_house()
            var_5 = obj_0.is_guard()
            var_3 = obj_0.__str__()
            obj_0.move_out_of_play()
            var_0 = obj_0.is_out_of_play()
            var_4 = obj_0.move((6.9954235392098525, -7.766729704248103), -2, True)
            var_8 = obj_0.is_out_of_bounds()
            var_1 = obj_0.is_passed_hogline()
        
    def test_486(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-6.816055394941234, -1.4804268241338185), -2, False, False)
            
            var_1 = obj_0.is_guard()
            obj_0.burn()
            var_6 = obj_0.is_out_of_bounds()
            var_4 = obj_0.__str__()
            var_3 = obj_0.is_passed_hogline()
            var_5 = obj_0.__str__()
            var_0 = obj_0.is_in_house()
        
    def test_487(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_1 = obj_1.done()
            var_2 = obj_1.red_won()
            var_0 = obj_1.drawn()
            obj_1.add_stone(Stone(False, (-0.3249070179262823, -5.7055200379911994), -1, True, True))
        
    def test_488(self):
        obj_1 = End(False)
        
        var_3 = obj_1.drawn()
        var_1 = obj_1.red_won()
        var_0 = obj_1.drawn()
        var_2 = obj_1.done()
        var_4 = obj_1.score()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, False)
        self.assertEqual(var_3, True)
        self.assertEqual(var_4, 0)
        
    def test_489(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (1.7286766490029528, -5.837379507807572), 9, False, False)
            
            obj_0.burn()
            var_2 = obj_0.is_guard()
            var_4 = obj_0.is_passed_hogline()
            var_5 = obj_0.is_in_house()
            obj_0.burn()
            var_1 = obj_0.is_guard()
        
    def test_490(self):
        with self.assertRaisesRegex(ValueError, "Stone's hammer status does not match the end's hammer status."):
            obj_1 = End(True)
            
            obj_1.add_stone(Stone(False, (3.6943784627617635, 4.566068563441295), 2, False, True))
            var_0 = obj_1.overlaps_any_stone(Stone(True, (3.609675977339924, -2.8877650208465973), 4, False, True))
            var_5 = obj_1.red_won()
            var_1 = obj_1.overlaps_any_stone(Stone(False, (4.647729681621312, -1.625032306634166), 7, False, True))
            var_2 = obj_1.drawn()
            var_3 = obj_1.drawn()
        
    def test_491(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        
    def test_492(self):
        obj_1 = End(False)
        
        var_0 = obj_1.drawn()
        var_1 = obj_1.done()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, False)
        
    def test_493(self):
        obj_2 = Game()
        
        var_1 = obj_2.red_winner()
        var_2 = obj_2.display_scoreboard()
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_494(self):
        with self.assertRaisesRegex(ValueError, "The first stone must be thrown by the team without the hammer."):
            obj_1 = End(False)
            
            obj_1.add_stone(Stone(False, (-0.05885104540768182, -5.00813171343232), 3, False, False))
            var_0 = obj_1.overlaps_any_stone(Stone(True, (6.7910539344896055, 3.726644956933299), 9, False, False))
            var_1 = obj_1.drawn()
            var_5 = obj_1.drawn()
            var_2 = obj_1.overlaps_any_stone(Stone(True, (-1.8828016381942767, -1.1128209487208345), 1, False, True))
            var_6 = obj_1.drawn()
            var_3 = obj_1.drawn()
        
    def test_495(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-3.6566894146974462, -7.481101032993125), 11, False, False)
            
            obj_0.move_out_of_play()
            var_0 = obj_0.is_passed_hogline()
            var_6 = obj_0.distance_to_center()
            obj_0.burn()
            var_2 = obj_0.distance_to_center()
            obj_0.burn()
            var_7 = obj_0.is_passed_hogline()
            var_3 = obj_0.is_passed_hogline()
        
    def test_496(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_1 = obj_1.score()
            var_2 = obj_1.__str__()
            obj_1.add_stone(Stone(False, (-6.51858605550898, 4.697645858136603), -2, True, True))
        
    def test_497(self):
        obj_2 = Game()
        
        var_1 = obj_2.display_scoreboard()
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_498(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (2.433343311245391, -6.416121520478004), 11, True, False)
            
            obj_0.move_out_of_play()
        
    def test_499(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (3.5977788093930165, -0.23235897970581476), 0, False, False)
            
            var_7 = obj_0.move((-2.318472262974282, -1.7480141938719367), 9, False)
            var_8 = obj_0.is_in_house()
            var_4 = obj_0.move((7.406204156347766, -4.448456341410045), 3, True)
            var_3 = obj_0.move((-5.007284811674026, -5.427610343525698), -1, True)
            var_5 = obj_0.is_out_of_play()
            var_6 = obj_0.__str__()
            obj_0.move_out_of_play()
            var_0 = obj_0.__str__()
            var_2 = obj_0.is_out_of_bounds()
        
    def test_500(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            obj_1.add_stone(Stone(False, (-5.018464703136901, 5.68804770043362), 5, False, False))
            var_2 = obj_1.done()
            var_5 = obj_1.drawn()
            var_6 = obj_1.done()
            var_0 = obj_1.red_won()
            var_4 = obj_1.red_won()
            var_3 = obj_1.score()
        
    def test_501(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        
    def test_502(self):
        obj_0 = Stone(True, (7.938248591074917, 3.572650563499842), 8, True, True)
        
        var_0 = obj_0.is_out_of_bounds()
        
        self.assertEqual(var_0, False)
        
    def test_503(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (1.1104830100105119, -7.629975917549256), 10, True, True)
            
            var_4 = obj_0.move((2.2447410013112954, 6.997481087617594), 1, True)
            var_8 = obj_0.distance_to_center()
            obj_0.burn()
            var_9 = obj_0.__str__()
            var_1 = obj_0.is_passed_hogline()
            var_6 = obj_0.is_out_of_bounds()
            var_0 = obj_0.is_passed_hogline()
            var_2 = obj_0.is_guard()
            var_7 = obj_0.is_passed_hogline()
            var_3 = obj_0.is_out_of_play()
        
    def test_504(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_2 = obj_1.done()
            var_3 = obj_1.score()
            var_1 = obj_1.drawn()
            var_0 = obj_1.overlaps_any_stone(Stone(False, (-4.320798674805445, 0.7552553414076559), 10, True, False))
        
    def test_505(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        var_4 = obj_2.display_scoreboard()
        var_3 = obj_2.display_scoreboard()
        var_1 = obj_2.score()
        var_2 = obj_2.__str__()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_4, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_506(self):
        obj_1 = End(False)
        
        var_0 = obj_1.__str__()
        
        self.assertEqual(var_0, 'End with Yellow hammer and 0 stones')
        
    def test_507(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        var_1 = obj_2.score()
        var_2 = obj_2.__str__()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'Game with 0 ends')
        
    def test_508(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            obj_1.add_stone(Stone(False, (-2.564830340274865, -1.1946171866875943), -2, True, False))
            var_3 = obj_1.drawn()
            var_4 = obj_1.drawn()
            var_2 = obj_1.drawn()
            obj_1.add_stone(Stone(False, (4.957620964637904, 3.40261177077336), 10, True, True))
            obj_1.add_stone(Stone(False, (-2.7279842756202513, 5.055638731094232), 4, True, True))
            var_1 = obj_1.overlaps_any_stone(Stone(True, (-4.383478484008842, 4.633444907262838), -1, True, True))
        
    def test_509(self):
        obj_1 = End(True)
        
        var_2 = obj_1.red_won()
        var_3 = obj_1.drawn()
        var_1 = obj_1.overlaps_any_stone(Stone(False, (-2.2035881252297376, 6.477082253429138), 7, False, True))
        var_0 = obj_1.done()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, True)
        
    def test_510(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_3 = obj_1.done()
            var_0 = obj_1.__str__()
            obj_1.add_stone(Stone(False, (-5.708481215854036, -5.37710537698171), 0, False, False))
            obj_1.add_stone(Stone(False, (4.671063426002872, 2.5064883651200294), 1, False, True))
            var_1 = obj_1.score()
        
    def test_511(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        
    def test_512(self):
        obj_2 = Game()
        
        var_1 = obj_2.display_scoreboard()
        obj_2.add_end(End(True))
        obj_2.add_end(End(True))
        
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_513(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        var_1 = obj_2.score()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, (0, 0))
        
    def test_514(self):
        obj_0 = Stone(True, (-1.2637007053450464, 3.136988874054092), 2, True, False)
        
        var_4 = obj_0.is_out_of_bounds()
        var_1 = obj_0.is_guard()
        var_0 = obj_0.distance_to_center()
        obj_0.burn()
        var_3 = obj_0.is_in_house()
        
        self.assertEqual(var_0, 3.381957815915025)
        self.assertEqual(var_1, True)
        self.assertEqual(var_3, False)
        self.assertEqual(var_4, False)
        
    def test_515(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        var_1 = obj_2.__str__()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'Game with 0 ends')
        
    def test_516(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
            obj_2 = Game()
            
            obj_2.add_end(End(True))
            obj_2.add_end(End(False))
            obj_2.add_end(End(True))
        
    def test_517(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_1 = obj_1.overlaps_any_stone(Stone(False, (4.798082039548538, -3.7083918638387914), 0, True, True))
            obj_1.add_stone(Stone(False, (1.0351473008135201, -5.854568168279968), 1, False, False))
            var_4 = obj_1.red_won()
            obj_1.add_stone(Stone(False, (6.480284893531472, -7.5969283331618165), 11, False, False))
            var_5 = obj_1.drawn()
            var_3 = obj_1.__str__()
            var_6 = obj_1.__str__()
        
    def test_518(self):
        obj_0 = Stone(False, (-2.1578183045855024, -4.385918581424395), 10, False, False)
        
        obj_0.burn()
        var_1 = obj_0.is_out_of_play()
        var_5 = obj_0.is_passed_hogline()
        var_4 = obj_0.is_out_of_play()
        var_2 = obj_0.is_passed_hogline()
        var_0 = obj_0.is_out_of_play()
        var_3 = obj_0.is_out_of_bounds()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, True)
        self.assertEqual(var_2, False)
        self.assertEqual(var_3, False)
        self.assertEqual(var_4, True)
        self.assertEqual(var_5, False)
        
    def test_519(self):
        with self.assertRaisesRegex(ValueError, "The first stone must be thrown by the team without the hammer."):
            obj_1 = End(False)
            
            var_2 = obj_1.done()
            obj_1.add_stone(Stone(False, (-6.349602155041936, 3.515847497092931), 6, False, True))
            var_0 = obj_1.__str__()
        
    def test_520(self):
        obj_2 = Game()
        
        var_3 = obj_2.red_winner()
        var_1 = obj_2.score()
        obj_2.add_end(End(False))
        var_0 = obj_2.display_scoreboard()
        var_2 = obj_2.red_winner()
        
        self.assertEqual(var_0, 'End |    1 | Total\n----|------|------\nRed |    0 |     0\nYel | h  0 |     0\n')
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, None)
        
    def test_521(self):
        obj_1 = End(False)
        
        var_1 = obj_1.done()
        var_0 = obj_1.red_won()
        var_2 = obj_1.drawn()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, True)
        
    def test_522(self):
        obj_1 = End(False)
        
        var_0 = obj_1.overlaps_any_stone(Stone(False, (6.678445823652229, 4.4700022717768135), 2, False, True))
        
        self.assertEqual(var_0, False)
        
    def test_523(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (-3.2865474644512354, 0.3304208033952243), 3, True, True)
            
            obj_0.move_out_of_play()
        
    def test_524(self):
        obj_2 = Game()
        
        var_1 = obj_2.__str__()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_1, 'Game with 0 ends')
        
    def test_525(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_0 = obj_1.overlaps_any_stone(Stone(False, (7.581202140848939, -2.3014592041500865), -2, True, True))
        
    def test_526(self):
        obj_2 = Game()
        
        var_1 = obj_2.red_winner()
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, None)
        
    def test_527(self):
        with self.assertRaisesRegex(ValueError, "The first stone must be thrown by the team without the hammer."):
            obj_1 = End(False)
            
            var_3 = obj_1.score()
            var_2 = obj_1.__str__()
            var_6 = obj_1.done()
            var_4 = obj_1.done()
            obj_1.add_stone(Stone(False, (-5.339732455074563, 7.320839451905677), 7, False, True))
            var_5 = obj_1.drawn()
            var_1 = obj_1.drawn()
        
    def test_528(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        var_0 = obj_2.score()
        obj_2.add_end(End(False))
        obj_2.add_end(End(False))
        
        self.assertEqual(var_0, (0, 0))
        
    def test_529(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-4.2264186912289485, -1.6902489500456586), 11, False, True)
            
            var_1 = obj_0.__str__()
            var_5 = obj_0.distance_to_center()
            var_3 = obj_0.is_in_house()
            var_2 = obj_0.move((-1.2518850941170996, 2.7307743897286905), 12, True)
            var_0 = obj_0.is_in_house()
            var_4 = obj_0.is_out_of_bounds()
        
    def test_530(self):
        obj_2 = Game()
        
        var_1 = obj_2.display_scoreboard()
        var_0 = obj_2.score()
        var_2 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, (0, 0))
        
    def test_531(self):
        obj_1 = End(True)
        
        var_2 = obj_1.score()
        var_1 = obj_1.done()
        var_3 = obj_1.score()
        var_0 = obj_1.done()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, 0)
        self.assertEqual(var_3, 0)
        
    def test_532(self):
        with self.assertRaisesRegex(ValueError, "Cannot calculate distance to center for a burned stone."):
            obj_0 = Stone(False, (-0.13844142963359118, 4.3294804457895495), 7, True, False)
            
            obj_0.burn()
            var_0 = obj_0.is_out_of_bounds()
            var_4 = obj_0.distance_to_center()
            obj_0.burn()
            var_3 = obj_0.is_guard()
        
    def test_533(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        
    def test_534(self):
        obj_2 = Game()
        
        var_1 = obj_2.__str__()
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, 'Game with 0 ends')
        
    def test_535(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (5.974729958573816, 0.9249653457219154), 10, True, False)
            
            var_4 = obj_0.distance_to_center()
            var_0 = obj_0.distance_to_center()
            var_1 = obj_0.is_guard()
            var_2 = obj_0.is_out_of_bounds()
            var_3 = obj_0.is_guard()
        
    def test_536(self):
        obj_0 = Stone(True, (4.407781886541107, 3.2876894254508393), 9, False, True)
        
        var_1 = obj_0.is_out_of_bounds()
        var_0 = obj_0.__str__()
        
        self.assertEqual(var_0, 'Red stone at (-2.50, 5.49), round 9, burned')
        self.assertEqual(var_1, False)
        
    def test_537(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        
    def test_538(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        
    def test_539(self):
        obj_1 = End(False)
        
        var_1 = obj_1.drawn()
        var_0 = obj_1.drawn()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, True)
        
    def test_540(self):
        obj_1 = End(False)
        
        var_1 = obj_1.drawn()
        var_0 = obj_1.score()
        var_2 = obj_1.drawn()
        
        self.assertEqual(var_0, 0)
        self.assertEqual(var_1, True)
        self.assertEqual(var_2, True)
        
    def test_541(self):
        obj_1 = End(False)
        
        var_2 = obj_1.overlaps_any_stone(Stone(False, (-1.2606997008698322, 0.07461737726778495), 1, True, True))
        var_1 = obj_1.red_won()
        var_0 = obj_1.score()
        
        self.assertEqual(var_0, 0)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, False)
        
    def test_542(self):
        obj_2 = Game()
        
        var_1 = obj_2.__str__()
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'Game with 0 ends')
        
    def test_543(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_0 = obj_1.drawn()
            var_3 = obj_1.overlaps_any_stone(Stone(False, (-6.394510007470826, -3.7727691070400393), -2, True, False))
            var_1 = obj_1.__str__()
            var_5 = obj_1.overlaps_any_stone(Stone(True, (-0.3968261385984988, -6.236340803138848), 5, False, True))
            var_4 = obj_1.drawn()
            var_6 = obj_1.__str__()
            var_2 = obj_1.done()
        
    def test_544(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        
    def test_545(self):
        with self.assertRaisesRegex(ValueError, "The first stone must be thrown by the team without the hammer."):
            obj_1 = End(True)
            
            var_6 = obj_1.done()
            obj_1.add_stone(Stone(True, (2.464561694788241, 6.825683349474991), 7, True, True))
            var_0 = obj_1.done()
            var_4 = obj_1.__str__()
            var_3 = obj_1.done()
            var_5 = obj_1.red_won()
            var_1 = obj_1.overlaps_any_stone(Stone(False, (1.3577618009456334, -6.902324538167441), 11, False, False))
        
    def test_546(self):
        obj_2 = Game()
        
        var_1 = obj_2.__str__()
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, 'Game with 0 ends')
        
    def test_547(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-7.78905480040833, -0.07678054646483012), 6, True, False)
            
            obj_0.move_out_of_play()
            obj_0.burn()
            var_6 = obj_0.__str__()
            var_7 = obj_0.is_out_of_bounds()
            var_2 = obj_0.is_out_of_bounds()
            var_1 = obj_0.is_guard()
            obj_0.move_out_of_play()
            obj_0.move_out_of_play()
        
    def test_548(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (6.006520177059029, 1.7436814735658341), 3, False, True)
            
            var_0 = obj_0.is_in_house()
            obj_0.move_out_of_play()
        
    def test_549(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_1 = obj_1.__str__()
            var_0 = obj_1.__str__()
            var_5 = obj_1.overlaps_any_stone(Stone(False, (6.558352061881392, 4.429159745586373), -2, True, False))
            var_2 = obj_1.overlaps_any_stone(Stone(True, (5.94374475807755, -5.921687574770189), 4, True, False))
            var_3 = obj_1.done()
            obj_1.add_stone(Stone(False, (2.221509509646962, -3.784519426628316), 5, True, False))
        
    def test_550(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-2.899118793566757, -7.818979343100864), -1, True, False)
            
            var_5 = obj_0.is_in_house()
            obj_0.burn()
            obj_0.move_out_of_play()
            var_3 = obj_0.is_out_of_play()
            var_1 = obj_0.__str__()
            var_0 = obj_0.is_in_house()
            var_7 = obj_0.move((-4.786345728460377, -4.500929116253953), 4, True)
            var_2 = obj_0.is_passed_hogline()
        
    def test_551(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_0 = obj_1.drawn()
            var_2 = obj_1.overlaps_any_stone(Stone(True, (-4.016986790606149, -5.833322935253655), 7, False, False))
            var_3 = obj_1.done()
            var_6 = obj_1.overlaps_any_stone(Stone(True, (-0.7334338475348989, 4.987163105381688), 6, False, False))
            var_1 = obj_1.drawn()
            var_5 = obj_1.drawn()
            var_4 = obj_1.overlaps_any_stone(Stone(True, (5.551878823250037, 2.292941206510257), 1, True, True))
        
    def test_552(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (5.98394939340918, -5.0667730750105235), 0, True, True)
            
            var_3 = obj_0.is_in_house()
            var_0 = obj_0.move((-1.9050784998793677, -7.114803830427352), 1, True)
            var_2 = obj_0.is_in_house()
            var_1 = obj_0.is_in_house()
            var_4 = obj_0.move((5.243815892496608, -4.637539961989905), 10, True)
        
    def test_553(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (0.47785878065625376, 3.7157764634791253), 11, False, True)
            
            var_1 = obj_0.distance_to_center()
            var_0 = obj_0.move((-1.5833398758504682, 5.344801401865929), -2, False)
            var_2 = obj_0.is_out_of_play()
        
    def test_554(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_1 = obj_1.overlaps_any_stone(Stone(False, (-0.38218084038123123, 1.8427330488066644), 12, True, False))
            var_0 = obj_1.score()
        
    def test_555(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-4.210496182687088, 4.809274684326178), -2, True, False)
            
            var_0 = obj_0.is_passed_hogline()
            var_3 = obj_0.distance_to_center()
            var_7 = obj_0.__str__()
            var_4 = obj_0.is_in_house()
            obj_0.move_out_of_play()
            var_2 = obj_0.is_passed_hogline()
            var_1 = obj_0.is_in_house()
            var_6 = obj_0.is_in_house()
        
    def test_556(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (-1.9633421621861107, 5.410724040550997), 5, True, True)
            
            var_0 = obj_0.is_passed_hogline()
            var_1 = obj_0.is_passed_hogline()
            obj_0.move_out_of_play()
            var_6 = obj_0.is_out_of_bounds()
            var_8 = obj_0.is_in_house()
            var_7 = obj_0.is_out_of_play()
            var_4 = obj_0.move((-2.2071200039660415, -1.8164768760936614), -2, False)
            var_5 = obj_0.is_out_of_bounds()
            obj_0.burn()
        
    def test_557(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        var_3 = obj_2.red_winner()
        var_2 = obj_2.display_scoreboard()
        var_1 = obj_2.score()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_3, None)
        
    def test_558(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        
    def test_559(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_560(self):
        with self.assertRaisesRegex(ValueError, "Stone's hammer status does not match the end's hammer status."):
            obj_1 = End(True)
            
            var_4 = obj_1.drawn()
            obj_1.add_stone(Stone(False, (-0.009146038394197475, 1.484617236392019), 4, False, False))
            var_5 = obj_1.drawn()
            obj_1.add_stone(Stone(True, (-2.5150303261150917, 3.115856198793683), 6, False, True))
            var_6 = obj_1.drawn()
            var_3 = obj_1.__str__()
            var_0 = obj_1.overlaps_any_stone(Stone(False, (-5.042901322471975, 1.376275698643143), 11, False, False))
        
    def test_561(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        
    def test_562(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_3 = obj_1.overlaps_any_stone(Stone(False, (-1.13516666221566, -1.139208374824765), 4, True, True))
            var_4 = obj_1.done()
            obj_1.add_stone(Stone(True, (4.082398562086867, -2.3497264090884418), 2, True, False))
            var_6 = obj_1.overlaps_any_stone(Stone(False, (3.6433548925707253, -0.517448199040734), -1, False, False))
            obj_1.add_stone(Stone(False, (-0.718114200902793, -5.247128750817797), 1, True, True))
            var_5 = obj_1.drawn()
            var_1 = obj_1.overlaps_any_stone(Stone(True, (7.762921383756025, -7.119232855039838), 9, True, False))
        
    def test_563(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-4.234284963100894, 1.8828197179556696), 7, True, False)
            
            var_0 = obj_0.__str__()
            obj_0.burn()
            var_1 = obj_0.is_in_house()
        
    def test_564(self):
        obj_0 = Stone(True, (5.016631629306103, -3.2288039485484), 8, True, True)
        
        var_0 = obj_0.is_guard()
        var_1 = obj_0.__str__()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, 'Red stone at (-2.50, 5.49), round 8, burned')
        
    def test_565(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_2 = obj_1.score()
            var_0 = obj_1.drawn()
            var_1 = obj_1.overlaps_any_stone(Stone(False, (4.228249201094691, 4.078685519750152), 3, False, False))
            var_3 = obj_1.drawn()
        
    def test_566(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_567(self):
        with self.assertRaisesRegex(ValueError, "The first stone must be thrown by the team without the hammer."):
            obj_1 = End(True)
            
            var_4 = obj_1.score()
            obj_1.add_stone(Stone(True, (3.6483658835202526, 0.21994560647246253), 4, True, True))
            obj_1.add_stone(Stone(False, (0.6482848447418057, -6.523699000314485), 11, True, False))
            var_5 = obj_1.done()
            var_3 = obj_1.__str__()
            var_2 = obj_1.drawn()
        
    def test_568(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_0 = obj_1.score()
            obj_1.add_stone(Stone(True, (-0.8323917485406707, -6.2474134416271365), 11, False, True))
        
    def test_569(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_2 = obj_1.done()
            var_0 = obj_1.overlaps_any_stone(Stone(False, (-2.329608668084619, 1.2762793852254841), 12, False, False))
            var_1 = obj_1.done()
        
    def test_570(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_1 = obj_1.red_won()
            var_3 = obj_1.overlaps_any_stone(Stone(True, (-5.546910752133561, -1.79588595768133), -1, False, False))
            var_0 = obj_1.overlaps_any_stone(Stone(True, (2.3562052655469206, -5.626733635235594), 12, True, True))
            var_2 = obj_1.overlaps_any_stone(Stone(True, (5.565140788929666, -4.588014642931883), 2, False, True))
            var_4 = obj_1.__str__()
        
    def test_571(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_0 = obj_1.score()
            obj_1.add_stone(Stone(False, (-5.969830891319523, 7.331436175647308), 6, True, False))
            var_3 = obj_1.__str__()
            var_1 = obj_1.red_won()
            var_4 = obj_1.done()
            var_2 = obj_1.overlaps_any_stone(Stone(True, (-3.5538452523038924, 0.13016893250030215), 6, True, True))
        
    def test_572(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (2.7535229481115344, 3.245424910566184), 3, False, False)
            
            var_5 = obj_0.is_in_house()
            var_1 = obj_0.__str__()
            obj_0.move_out_of_play()
            var_4 = obj_0.distance_to_center()
            var_3 = obj_0.is_in_house()
            var_2 = obj_0.is_out_of_play()
        
    def test_573(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (7.942748072651991, -5.568562164293416), 0, True, True)
            
            var_8 = obj_0.__str__()
            var_9 = obj_0.is_guard()
            var_7 = obj_0.is_in_house()
            obj_0.burn()
            var_2 = obj_0.move((2.303770059173731, 6.90978155569187), 11, True)
            obj_0.burn()
            var_5 = obj_0.is_passed_hogline()
            var_0 = obj_0.is_guard()
            var_4 = obj_0.is_passed_hogline()
            var_6 = obj_0.distance_to_center()
        
    def test_574(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_1 = obj_1.overlaps_any_stone(Stone(False, (-0.5933948692347997, 4.22583732564091), 12, True, False))
            var_0 = obj_1.red_won()
        
    def test_575(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        var_3 = obj_2.display_scoreboard()
        obj_2.add_end(End(True))
        var_2 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_2, 'End |    1 | Total\n----|------|------\nRed | h  0 |     0\nYel |    0 |     0\n')
        self.assertEqual(var_3, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_576(self):
        obj_1 = End(True)
        
        var_0 = obj_1.drawn()
        
        self.assertEqual(var_0, True)
        
    def test_577(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_0 = obj_1.drawn()
            obj_1.add_stone(Stone(True, (-3.317083580226292, 0.25758283239666646), 11, False, True))
            var_2 = obj_1.drawn()
            obj_1.add_stone(Stone(False, (4.663247555963618, -6.3177355345003985), 12, False, False))
            var_4 = obj_1.overlaps_any_stone(Stone(False, (4.967441254335416, 4.15710110779443), 12, False, False))
        
    def test_578(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            obj_1.add_stone(Stone(True, (-7.988329889332277, -0.41573433587282693), -1, True, True))
            var_1 = obj_1.overlaps_any_stone(Stone(True, (-0.17554841517412, 3.3997883609993576), 0, True, True))
            obj_1.add_stone(Stone(False, (-6.475119721369985, 7.38609205455713), 3, False, True))
            var_0 = obj_1.__str__()
            var_4 = obj_1.drawn()
        
    def test_579(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(False, (-3.3067574393723174, 0.863808645619045), 5, True, True)
            
            var_1 = obj_0.move((-1.9530060771261386, -5.3021363770599095), 12, True)
            var_3 = obj_0.is_in_house()
            var_0 = obj_0.__str__()
            var_8 = obj_0.is_in_house()
            var_2 = obj_0.__str__()
            var_5 = obj_0.distance_to_center()
            var_7 = obj_0.is_passed_hogline()
            obj_0.burn()
            var_9 = obj_0.distance_to_center()
            obj_0.burn()
        
    def test_580(self):
        obj_2 = Game()
        
        var_1 = obj_2.display_scoreboard()
        var_2 = obj_2.__str__()
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, 'Game with 0 ends')
        
    def test_581(self):
        obj_1 = End(False)
        
        var_1 = obj_1.score()
        var_2 = obj_1.red_won()
        var_0 = obj_1.red_won()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 0)
        self.assertEqual(var_2, None)
        
    def test_582(self):
        obj_2 = Game()
        
        var_1 = obj_2.display_scoreboard()
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_583(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        var_1 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_584(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(False, (4.947634571551481, -7.360892235693408), 8, False, True)
            
            var_6 = obj_0.is_out_of_play()
            var_2 = obj_0.is_out_of_bounds()
            var_1 = obj_0.move((7.6407137338054145, -3.6983743217705953), 10, True)
            var_3 = obj_0.move((-6.741210899422988, -5.7840835382509255), -1, False)
            var_0 = obj_0.is_guard()
            obj_0.burn()
            var_5 = obj_0.distance_to_center()
        
    def test_585(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_6 = obj_1.red_won()
            var_2 = obj_1.score()
            obj_1.add_stone(Stone(True, (0.25976487852635444, -3.9831089826535155), 12, True, False))
            var_5 = obj_1.done()
            var_0 = obj_1.score()
            var_1 = obj_1.red_won()
            var_3 = obj_1.red_won()
        
    def test_586(self):
        with self.assertRaisesRegex(ValueError, "Stone's round does not match the expected round based on the number of stones already placed."):
            obj_1 = End(True)
            
            var_6 = obj_1.overlaps_any_stone(Stone(False, (-0.9120798055432022, 2.763633492622164), 9, False, True))
            obj_1.add_stone(Stone(False, (4.63024362796272, 7.209813648153405), 5, True, True))
            var_2 = obj_1.drawn()
            var_3 = obj_1.__str__()
            var_4 = obj_1.done()
            obj_1.add_stone(Stone(True, (-2.8570637940555983, -4.893903167304371), 4, True, False))
            var_1 = obj_1.drawn()
        
    def test_587(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(False, (-7.071051786401021, 3.8405428902924967), 10, True, True)
            
            var_0 = obj_0.is_out_of_play()
            var_2 = obj_0.__str__()
            var_3 = obj_0.__str__()
            var_7 = obj_0.is_out_of_play()
            var_1 = obj_0.move((1.2913743248774896, -6.78767357702066), 3, False)
            var_8 = obj_0.__str__()
            obj_0.burn()
            var_5 = obj_0.is_guard()
            var_6 = obj_0.is_passed_hogline()
        
    def test_588(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-6.683284914724922, 3.4917413493532568), -2, True, False)
            
            obj_0.move_out_of_play()
            var_1 = obj_0.distance_to_center()
            var_3 = obj_0.is_in_house()
            var_2 = obj_0.is_out_of_bounds()
        
    def test_589(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-3.082054772634459, -1.779135968407969), 11, False, True)
            
            var_5 = obj_0.is_passed_hogline()
            var_3 = obj_0.is_in_house()
            var_6 = obj_0.is_out_of_bounds()
            obj_0.move_out_of_play()
            var_4 = obj_0.move((4.6203081922062506, 7.630070540750271), 11, True)
            obj_0.burn()
            var_0 = obj_0.is_passed_hogline()
        
    def test_590(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_0 = obj_1.overlaps_any_stone(Stone(False, (-2.4547699044463602, 0.799419865271414), 12, False, True))
            var_1 = obj_1.drawn()
            obj_1.add_stone(Stone(False, (7.93833903147169, -6.149583396895215), 11, True, True))
        
    def test_591(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        var_1 = obj_2.red_winner()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, None)
        
    def test_592(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-3.137935591060133, -5.802224830123233), 1, True, False)
            
            var_6 = obj_0.is_in_house()
            obj_0.burn()
            var_5 = obj_0.is_passed_hogline()
            var_0 = obj_0.is_guard()
            var_1 = obj_0.is_passed_hogline()
            var_4 = obj_0.is_in_house()
            var_2 = obj_0.distance_to_center()
        
    def test_593(self):
        obj_1 = End(False)
        
        var_0 = obj_1.done()
        
        self.assertEqual(var_0, False)
        
    def test_594(self):
        obj_2 = Game()
        
        obj_2.add_end(End(True))
        
        
    def test_595(self):
        obj_0 = Stone(True, (5.7928548556529265, 2.0589805089733098), 7, False, True)
        
        var_0 = obj_0.is_guard()
        
        self.assertEqual(var_0, False)
        
    def test_596(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (-2.1371556807487444, 4.844853184287439), 2, True, True)
            
            obj_0.burn()
            obj_0.move_out_of_play()
            var_3 = obj_0.is_in_house()
            var_5 = obj_0.is_in_house()
            var_2 = obj_0.__str__()
            var_4 = obj_0.is_passed_hogline()
            var_6 = obj_0.__str__()
            var_1 = obj_0.is_guard()
            var_8 = obj_0.is_guard()
        
    def test_597(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-6.23846809937587, -4.400271147909896), -1, False, False)
            
            var_3 = obj_0.is_passed_hogline()
            obj_0.burn()
            var_0 = obj_0.is_passed_hogline()
            obj_0.move_out_of_play()
            var_4 = obj_0.__str__()
            var_1 = obj_0.__str__()
        
    def test_598(self):
        with self.assertRaisesRegex(ValueError, "Cannot calculate distance to center for a burned stone."):
            obj_0 = Stone(True, (-2.29647577509442, 6.7942017686474205), 2, False, True)
            
            var_6 = obj_0.distance_to_center()
            var_0 = obj_0.is_guard()
            var_7 = obj_0.__str__()
            var_9 = obj_0.is_out_of_bounds()
            var_4 = obj_0.is_in_house()
            obj_0.move_out_of_play()
            var_8 = obj_0.is_guard()
            var_1 = obj_0.is_in_house()
            var_3 = obj_0.distance_to_center()
            var_2 = obj_0.distance_to_center()
        
    def test_599(self):
        obj_2 = Game()
        
        var_3 = obj_2.display_scoreboard()
        var_2 = obj_2.__str__()
        var_0 = obj_2.red_winner()
        var_1 = obj_2.score()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_600(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_0 = obj_1.overlaps_any_stone(Stone(False, (-1.6894321798866692, 5.902715599958148), 4, False, False))
            obj_1.add_stone(Stone(True, (3.1564271976913094, 5.5117310392450705), 8, False, True))
            obj_1.add_stone(Stone(True, (-0.5707003458268769, 5.781303230783768), 11, False, True))
            var_5 = obj_1.overlaps_any_stone(Stone(True, (1.3296327297040378, 1.9216946807247997), 4, True, False))
            var_2 = obj_1.done()
            var_4 = obj_1.red_won()
            var_1 = obj_1.done()
        
    def test_601(self):
        obj_1 = End(True)
        
        var_0 = obj_1.red_won()
        
        self.assertEqual(var_0, None)
        
    def test_602(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        
    def test_603(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        var_1 = obj_2.__str__()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, 'Game with 0 ends')
        
    def test_604(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_5 = obj_1.drawn()
            obj_1.add_stone(Stone(False, (-7.397070619392242, -6.5464687396374455), -2, True, False))
            var_3 = obj_1.red_won()
            obj_1.add_stone(Stone(True, (0.6881374899318189, -0.15450469405626954), 12, False, True))
            var_2 = obj_1.done()
            var_4 = obj_1.__str__()
        
    def test_605(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        var_1 = obj_2.score()
        var_2 = obj_2.red_winner()
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |    1 | Total\n----|------|------\nRed |    0 |     0\nYel | h  0 |     0\n')
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, None)
        
    def test_606(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (7.681559574265384, 3.564975898309209), 11, False, True)
            
            var_2 = obj_0.is_passed_hogline()
            var_3 = obj_0.distance_to_center()
            var_4 = obj_0.is_out_of_bounds()
            var_1 = obj_0.is_guard()
            obj_0.burn()
        
    def test_607(self):
        obj_1 = End(False)
        
        var_0 = obj_1.red_won()
        
        self.assertEqual(var_0, None)
        
    def test_608(self):
        obj_2 = Game()
        
        var_1 = obj_2.score()
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, (0, 0))
        
    def test_609(self):
        obj_2 = Game()
        
        obj_2.add_end(End(True))
        var_1 = obj_2.__str__()
        var_3 = obj_2.__str__()
        var_0 = obj_2.__str__()
        var_4 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 1 ends')
        self.assertEqual(var_1, 'Game with 1 ends')
        self.assertEqual(var_3, 'Game with 1 ends')
        self.assertEqual(var_4, 'Game with 1 ends')
        
    def test_610(self):
        obj_1 = End(False)
        
        var_1 = obj_1.score()
        var_0 = obj_1.red_won()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 0)
        
    def test_611(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_1 = obj_1.overlaps_any_stone(Stone(False, (-1.7745846774635297, 0.9656152365208257), 5, False, False))
            var_0 = obj_1.drawn()
            obj_1.add_stone(Stone(False, (4.801713386059575, -0.33474556493558083), 1, True, False))
            var_2 = obj_1.score()
            var_5 = obj_1.drawn()
            var_4 = obj_1.done()
        
    def test_612(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        var_1 = obj_2.score()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, (0, 0))
        
    def test_613(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_0 = obj_1.red_won()
            var_2 = obj_1.red_won()
            var_1 = obj_1.overlaps_any_stone(Stone(False, (5.072579669350283, 7.569916773041255), 2, False, False))
        
    def test_614(self):
        obj_2 = Game()
        
        var_1 = obj_2.red_winner()
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, None)
        
    def test_615(self):
        obj_1 = End(False)
        
        var_1 = obj_1.red_won()
        var_2 = obj_1.red_won()
        var_0 = obj_1.overlaps_any_stone(Stone(False, (3.734760926075875, 3.575150673269519), 1, False, True))
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, None)
        
    def test_616(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-2.2197822759604904, -7.195597749788247), 0, True, True)
            
            obj_0.move_out_of_play()
            obj_0.burn()
            var_5 = obj_0.is_in_house()
            var_0 = obj_0.is_guard()
            var_2 = obj_0.is_guard()
            var_3 = obj_0.is_out_of_play()
        
    def test_617(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (2.444151393461251, -4.035992115173125), 2, False, False)
            
            var_2 = obj_0.is_guard()
            var_4 = obj_0.move((3.0047905466753573, 1.9208047369021504), 4, True)
            obj_0.move_out_of_play()
            obj_0.burn()
            var_0 = obj_0.is_guard()
            var_5 = obj_0.is_guard()
        
    def test_618(self):
        with self.assertRaisesRegex(ValueError, "Stone's round does not match the expected round based on the number of stones already placed."):
            obj_1 = End(False)
            
            var_1 = obj_1.score()
            var_2 = obj_1.drawn()
            obj_1.add_stone(Stone(True, (2.463663894367542, 4.990537941514379), 2, False, False))
        
    def test_619(self):
        with self.assertRaisesRegex(ValueError, "Cannot calculate distance to center for a burned stone."):
            obj_0 = Stone(True, (-4.984702978716607, 2.1773721715509087), 9, False, True)
            
            var_1 = obj_0.distance_to_center()
            obj_0.move_out_of_play()
            var_6 = obj_0.distance_to_center()
            obj_0.move_out_of_play()
            obj_0.burn()
            var_9 = obj_0.is_guard()
            obj_0.move_out_of_play()
            obj_0.burn()
            obj_0.move_out_of_play()
            var_0 = obj_0.is_out_of_bounds()
        
    def test_620(self):
        obj_1 = End(True)
        
        var_0 = obj_1.drawn()
        var_1 = obj_1.red_won()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, None)
        
    def test_621(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_3 = obj_1.__str__()
            var_0 = obj_1.score()
            var_4 = obj_1.drawn()
            var_6 = obj_1.__str__()
            var_2 = obj_1.score()
            var_5 = obj_1.overlaps_any_stone(Stone(False, (-3.161423155352594, 3.243614675589926), 4, True, False))
            obj_1.add_stone(Stone(True, (6.193325920313816, -4.05725816125479), 10, True, True))
        
    def test_622(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        
    def test_623(self):
        obj_2 = Game()
        
        var_1 = obj_2.display_scoreboard()
        var_2 = obj_2.display_scoreboard()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_624(self):
        obj_2 = Game()
        
        var_1 = obj_2.red_winner()
        var_2 = obj_2.score()
        var_0 = obj_2.red_winner()
        var_3 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, (0, 0))
        self.assertEqual(var_3, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_625(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (2.4139443870445803, -3.445939313583901), -2, True, False)
            
            var_3 = obj_0.is_passed_hogline()
            var_4 = obj_0.move((2.2183911735301223, -1.5627375296344823), 1, False)
            var_1 = obj_0.__str__()
            var_2 = obj_0.is_guard()
            var_0 = obj_0.is_passed_hogline()
        
    def test_626(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (3.803753072350684, 0.9656606542859993), 0, False, False)
            
            var_6 = obj_0.is_in_house()
            var_4 = obj_0.is_guard()
            var_7 = obj_0.__str__()
            var_3 = obj_0.is_out_of_play()
            var_5 = obj_0.__str__()
            obj_0.move_out_of_play()
            var_1 = obj_0.is_passed_hogline()
            var_0 = obj_0.distance_to_center()
        
    def test_627(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        var_1 = obj_2.red_winner()
        obj_2.add_end(End(False))
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, None)
        
    def test_628(self):
        obj_2 = Game()
        
        var_3 = obj_2.__str__()
        var_4 = obj_2.score()
        var_2 = obj_2.red_winner()
        var_1 = obj_2.__str__()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, 'Game with 0 ends')
        self.assertEqual(var_4, (0, 0))
        
    def test_629(self):
        with self.assertRaisesRegex(ValueError, "Stone's hammer status does not match the end's hammer status."):
            obj_1 = End(True)
            
            obj_1.add_stone(Stone(False, (-3.1886138631809864, -5.133727805361525), 4, False, True))
        
    def test_630(self):
        obj_1 = End(False)
        
        var_0 = obj_1.drawn()
        var_2 = obj_1.red_won()
        var_1 = obj_1.__str__()
        var_4 = obj_1.__str__()
        var_3 = obj_1.red_won()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, 'End with Yellow hammer and 0 stones')
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, None)
        self.assertEqual(var_4, 'End with Yellow hammer and 0 stones')
        
    def test_631(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (0.6464573902420625, 3.942102567289542), 12, True, True)
            
            obj_0.move_out_of_play()
            obj_0.burn()
            var_2 = obj_0.move((-2.833105194738298, -5.4375087557617245), -2, True)
            var_1 = obj_0.__str__()
        
    def test_632(self):
        obj_0 = Stone(True, (-0.5123816250260997, -6.142901596048427), 8, True, False)
        
        var_0 = obj_0.__str__()
        
        self.assertEqual(var_0, 'Red stone at (-0.51, -6.14), round 8, active')
        
    def test_633(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-6.691665344205791, 0.1662874172468083), 0, True, False)
            
            var_8 = obj_0.is_guard()
            obj_0.burn()
            var_6 = obj_0.is_guard()
            obj_0.move_out_of_play()
            var_1 = obj_0.is_in_house()
            var_4 = obj_0.is_guard()
            var_2 = obj_0.is_guard()
            obj_0.burn()
            var_0 = obj_0.is_in_house()
        
    def test_634(self):
        with self.assertRaisesRegex(ValueError, "Stone's round does not match the expected round based on the number of stones already placed."):
            obj_1 = End(False)
            
            var_0 = obj_1.overlaps_any_stone(Stone(True, (-3.2805935546623655, 7.317062492947899), 9, False, True))
            obj_1.add_stone(Stone(True, (-1.4850370676995848, -3.4759219225487055), 8, False, False))
        
    def test_635(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_1 = obj_1.overlaps_any_stone(Stone(False, (4.734737599413922, 5.171709889370737), -2, True, True))
            var_0 = obj_1.score()
        
    def test_636(self):
        obj_2 = Game()
        
        var_1 = obj_2.score()
        var_0 = obj_2.score()
        obj_2.add_end(End(True))
        var_2 = obj_2.__str__()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'Game with 1 ends')
        
    def test_637(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (7.44371502623868, -0.5748830751974783), 0, False, False)
            
            var_5 = obj_0.is_guard()
            obj_0.burn()
            var_0 = obj_0.is_out_of_bounds()
            var_4 = obj_0.is_passed_hogline()
            var_2 = obj_0.__str__()
            var_1 = obj_0.is_out_of_play()
            var_7 = obj_0.is_in_house()
            var_3 = obj_0.is_passed_hogline()
        
    def test_638(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (-5.1748759317318065, 2.669283411689525), 6, False, True)
            
            var_8 = obj_0.is_in_house()
            obj_0.burn()
            var_0 = obj_0.move((3.5985336197926685, -4.053860124980428), 1, True)
            var_2 = obj_0.distance_to_center()
            var_7 = obj_0.__str__()
            var_3 = obj_0.is_passed_hogline()
            var_6 = obj_0.is_guard()
            var_5 = obj_0.__str__()
            var_4 = obj_0.is_guard()
        
    def test_639(self):
        obj_2 = Game()
        
        var_3 = obj_2.display_scoreboard()
        var_2 = obj_2.score()
        var_0 = obj_2.__str__()
        var_4 = obj_2.red_winner()
        var_1 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, (0, 0))
        self.assertEqual(var_3, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_4, None)
        
    def test_640(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (1.2142780080325917, 7.806351619984751), 5, False, False)
            
            var_0 = obj_0.is_guard()
            obj_0.move_out_of_play()
            var_5 = obj_0.is_passed_hogline()
            var_1 = obj_0.is_out_of_play()
            var_3 = obj_0.is_in_house()
            var_2 = obj_0.is_guard()
        
    def test_641(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            obj_1.add_stone(Stone(False, (-4.717889286353142, -3.3445102912110816), 12, False, False))
            obj_1.add_stone(Stone(False, (-4.5859190392585365, 7.845272598284744), 5, True, True))
        
    def test_642(self):
        obj_1 = End(True)
        
        var_1 = obj_1.__str__()
        var_6 = obj_1.drawn()
        var_2 = obj_1.red_won()
        var_0 = obj_1.red_won()
        var_4 = obj_1.score()
        var_5 = obj_1.__str__()
        var_3 = obj_1.drawn()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'End with Red hammer and 0 stones')
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, True)
        self.assertEqual(var_4, 0)
        self.assertEqual(var_5, 'End with Red hammer and 0 stones')
        self.assertEqual(var_6, True)
        
    def test_643(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (-1.5202631644945725, -5.941602787197375), 2, True, True)
            
            obj_0.burn()
            var_3 = obj_0.is_in_house()
            var_4 = obj_0.is_guard()
            var_0 = obj_0.distance_to_center()
            var_2 = obj_0.__str__()
        
    def test_644(self):
        obj_1 = End(False)
        
        var_0 = obj_1.red_won()
        var_2 = obj_1.red_won()
        var_1 = obj_1.__str__()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'End with Yellow hammer and 0 stones')
        self.assertEqual(var_2, None)
        
    def test_645(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        
    def test_646(self):
        obj_2 = Game()
        
        var_4 = obj_2.__str__()
        var_1 = obj_2.display_scoreboard()
        var_2 = obj_2.score()
        var_3 = obj_2.__str__()
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, (0, 0))
        self.assertEqual(var_3, 'Game with 0 ends')
        self.assertEqual(var_4, 'Game with 0 ends')
        
    def test_647(self):
        obj_2 = Game()
        
        var_2 = obj_2.__str__()
        obj_2.add_end(End(False))
        var_0 = obj_2.score()
        var_3 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, 'End |    1 | Total\n----|------|------\nRed |    0 |     0\nYel | h  0 |     0\n')
        
    def test_648(self):
        obj_2 = Game()
        
        var_2 = obj_2.score()
        var_3 = obj_2.score()
        var_0 = obj_2.__str__()
        var_1 = obj_2.__str__()
        var_4 = obj_2.score()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, (0, 0))
        self.assertEqual(var_3, (0, 0))
        self.assertEqual(var_4, (0, 0))
        
    def test_649(self):
        obj_2 = Game()
        
        var_2 = obj_2.red_winner()
        obj_2.add_end(End(False))
        var_0 = obj_2.__str__()
        var_3 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 1 ends')
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, 'Game with 1 ends')
        
    def test_650(self):
        obj_2 = Game()
        
        var_1 = obj_2.__str__()
        var_0 = obj_2.red_winner()
        var_2 = obj_2.score()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, (0, 0))
        
    def test_651(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (-0.8020592236846156, -1.2629498960693457), 4, True, True)
            
            obj_0.move_out_of_play()
            var_2 = obj_0.is_passed_hogline()
            var_0 = obj_0.move((7.544173607977623, 4.4592173220172295), -1, True)
            var_3 = obj_0.is_guard()
        
    def test_652(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (3.631679431345031, -7.164554076808143), 10, False, False)
            
            var_3 = obj_0.distance_to_center()
            var_4 = obj_0.move((-3.5569944011473336, 3.9597262347593496), 10, True)
            var_2 = obj_0.is_out_of_play()
            var_0 = obj_0.move((5.196025687420478, -1.0822080131137373), -2, False)
            var_1 = obj_0.__str__()
        
    def test_653(self):
        obj_1 = End(True)
        
        var_3 = obj_1.score()
        var_2 = obj_1.red_won()
        var_5 = obj_1.score()
        var_4 = obj_1.red_won()
        var_1 = obj_1.red_won()
        var_0 = obj_1.drawn()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, 0)
        self.assertEqual(var_4, None)
        self.assertEqual(var_5, 0)
        
    def test_654(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_0 = obj_1.__str__()
            var_1 = obj_1.overlaps_any_stone(Stone(False, (7.5992194438952865, -1.2176475907507154), -2, True, True))
        
    def test_655(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (5.717776697235562, -2.812128350057634), -2, True, False)
            
            var_2 = obj_0.__str__()
            obj_0.burn()
            var_4 = obj_0.is_out_of_play()
            var_6 = obj_0.__str__()
            var_7 = obj_0.move((0.6307351357643185, 6.325349955105564), 12, False)
            var_8 = obj_0.is_guard()
            var_1 = obj_0.is_out_of_bounds()
            var_5 = obj_0.__str__()
            obj_0.move_out_of_play()
        
    def test_656(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            obj_1.add_stone(Stone(True, (-5.271870446451548, -0.6700162063530293), -2, False, False))
        
    def test_657(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-5.5487232384889165, 3.052964204391033), 12, True, True)
            
            obj_0.burn()
            obj_0.move_out_of_play()
            var_0 = obj_0.is_out_of_bounds()
            var_1 = obj_0.is_out_of_play()
        
    def test_658(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (-6.8563826991444845, 7.651924552054211), 8, True, False)
            
            obj_0.burn()
            var_6 = obj_0.is_out_of_play()
            obj_0.burn()
            var_8 = obj_0.is_passed_hogline()
            var_5 = obj_0.is_out_of_play()
            var_1 = obj_0.move((7.026436203713686, 3.2930454816681802), -2, True)
            var_2 = obj_0.is_out_of_play()
            var_4 = obj_0.__str__()
            var_3 = obj_0.is_out_of_play()
        
    def test_659(self):
        obj_2 = Game()
        
        var_3 = obj_2.score()
        var_2 = obj_2.red_winner()
        var_1 = obj_2.red_winner()
        obj_2.add_end(End(False))
        
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, (0, 0))
        
    def test_660(self):
        obj_2 = Game()
        
        var_1 = obj_2.red_winner()
        obj_2.add_end(End(True))
        var_3 = obj_2.score()
        var_2 = obj_2.score()
        
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, (0, 0))
        self.assertEqual(var_3, (0, 0))
        
    def test_661(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_662(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_3 = obj_1.score()
            var_1 = obj_1.__str__()
            var_2 = obj_1.__str__()
            obj_1.add_stone(Stone(True, (3.374698756126783, -7.113045077759255), 8, True, False))
        
    def test_663(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (4.97176182081758, -5.996444450737346), 9, False, True)
            
            var_0 = obj_0.move((7.922556486600515, 3.7264674309078494), -2, False)
            var_2 = obj_0.move((6.368836814907002, -0.8040337602352068), -1, False)
            var_1 = obj_0.is_passed_hogline()
            var_3 = obj_0.move((6.907842689953071, 4.219273166239624), 3, True)
        
    def test_664(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (0.713696894044574, 3.900531587185906), 9, True, False)
            
            var_2 = obj_0.is_out_of_bounds()
            obj_0.burn()
            var_4 = obj_0.is_guard()
            var_1 = obj_0.is_out_of_play()
            var_5 = obj_0.is_in_house()
            obj_0.move_out_of_play()
        
    def test_665(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-4.318488283471847, -7.159397605441944), 9, False, False)
            
            var_1 = obj_0.move((-3.476698910269455, 7.736181114573117), 10, True)
            var_0 = obj_0.is_in_house()
            var_2 = obj_0.is_out_of_play()
        
    def test_666(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
            obj_2 = Game()
            
            var_0 = obj_2.display_scoreboard()
            obj_2.add_end(End(True))
            var_4 = obj_2.score()
            obj_2.add_end(End(False))
            var_2 = obj_2.score()
        
    def test_667(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        var_3 = obj_2.score()
        var_2 = obj_2.score()
        var_1 = obj_2.score()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, (0, 0))
        self.assertEqual(var_3, (0, 0))
        
    def test_668(self):
        obj_2 = Game()
        
        var_1 = obj_2.score()
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, (0, 0))
        
    def test_669(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            obj_1.add_stone(Stone(False, (7.609124148006849, -0.6949787536203402), 2, True, False))
            var_0 = obj_1.red_won()
        
    def test_670(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (2.219854438508637, 0.19598129852271917), 12, True, True)
            
            var_2 = obj_0.is_out_of_bounds()
            var_5 = obj_0.move((5.269479232500112, 2.4639390436622364), 0, True)
            var_6 = obj_0.is_guard()
            var_1 = obj_0.is_in_house()
            obj_0.move_out_of_play()
            var_8 = obj_0.is_in_house()
            var_0 = obj_0.is_passed_hogline()
            var_7 = obj_0.is_passed_hogline()
            var_4 = obj_0.is_out_of_bounds()
        
    def test_671(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (5.65203338806775, 5.0408243499864795), 11, True, False)
            
            var_0 = obj_0.is_guard()
        
    def test_672(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-5.276951855471445, -7.678890681952009), 8, False, True)
            
            var_7 = obj_0.move((7.979667199108105, 7.205348211044692), 1, True)
            var_5 = obj_0.is_out_of_bounds()
            var_6 = obj_0.is_out_of_bounds()
            var_4 = obj_0.__str__()
            var_0 = obj_0.is_out_of_play()
            obj_0.move_out_of_play()
            var_1 = obj_0.__str__()
            var_2 = obj_0.is_in_house()
        
    def test_673(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            obj_1.add_stone(Stone(True, (5.184697786360347, -1.1356689914325777), -2, False, True))
            var_3 = obj_1.red_won()
            var_2 = obj_1.__str__()
            var_1 = obj_1.done()
        
    def test_674(self):
        obj_2 = Game()
        
        var_3 = obj_2.score()
        var_1 = obj_2.__str__()
        var_2 = obj_2.display_scoreboard()
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_3, (0, 0))
        
    def test_675(self):
        obj_2 = Game()
        
        var_1 = obj_2.__str__()
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, 'Game with 0 ends')
        
    def test_676(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-0.3595804225354726, -5.563430613067773), -2, False, False)
            
            var_3 = obj_0.move((-4.002981215164606, 5.0671467083645325), 7, False)
            var_1 = obj_0.distance_to_center()
            obj_0.burn()
            var_2 = obj_0.is_out_of_play()
        
    def test_677(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        
    def test_678(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        var_3 = obj_2.score()
        var_2 = obj_2.score()
        var_4 = obj_2.__str__()
        var_1 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, (0, 0))
        self.assertEqual(var_3, (0, 0))
        self.assertEqual(var_4, 'Game with 0 ends')
        
    def test_679(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        var_1 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, None)
        
    def test_680(self):
        obj_0 = Stone(True, (-2.6466699123024, 7.856851434643627), 6, True, True)
        
        var_0 = obj_0.is_out_of_bounds()
        var_1 = obj_0.is_passed_hogline()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, False)
        
    def test_681(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        var_1 = obj_2.red_winner()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, None)
        
    def test_682(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_0 = obj_1.score()
            var_4 = obj_1.score()
            var_5 = obj_1.__str__()
            var_3 = obj_1.overlaps_any_stone(Stone(True, (-3.0150965156154896, 2.6913236721064138), -2, False, False))
            var_2 = obj_1.drawn()
            var_1 = obj_1.score()
        
    def test_683(self):
        obj_2 = Game()
        
        obj_2.add_end(End(True))
        var_1 = obj_2.red_winner()
        
        self.assertEqual(var_1, None)
        
    def test_684(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
            obj_2 = Game()
            
            obj_2.add_end(End(False))
            obj_2.add_end(End(True))
        
    def test_685(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_5 = obj_1.overlaps_any_stone(Stone(True, (0.08021603412506906, -7.011994987179101), 11, False, False))
            var_6 = obj_1.drawn()
            var_2 = obj_1.score()
            obj_1.add_stone(Stone(True, (5.273596226678231, -4.106882447770895), 2, False, True))
            obj_1.add_stone(Stone(True, (-4.42829832095075, 3.8514857999853636), 10, False, True))
            var_4 = obj_1.drawn()
            var_0 = obj_1.done()
        
    def test_686(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (-4.407783805984549, 7.964020537781904), 8, False, True)
            
            var_0 = obj_0.__str__()
            obj_0.burn()
        
    def test_687(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-4.422505328896154, 6.54839327546401), 11, True, True)
            
            var_0 = obj_0.distance_to_center()
            var_8 = obj_0.distance_to_center()
            var_7 = obj_0.is_passed_hogline()
            var_2 = obj_0.move((-6.561482342838216, 1.2981978591053647), -1, False)
            var_3 = obj_0.__str__()
            obj_0.move_out_of_play()
            var_6 = obj_0.distance_to_center()
            var_5 = obj_0.is_out_of_play()
            var_1 = obj_0.is_in_house()
        
    def test_688(self):
        with self.assertRaisesRegex(ValueError, "Stone's hammer status does not match the end's hammer status."):
            obj_1 = End(False)
            
            obj_1.add_stone(Stone(True, (-0.2605815530625115, 3.612611864681371), 9, True, False))
            var_1 = obj_1.score()
        
    def test_689(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-2.7648652778536036, 0.3760446655052334), 5, False, False)
            
            obj_0.move_out_of_play()
        
    def test_690(self):
        obj_2 = Game()
        
        var_3 = obj_2.red_winner()
        var_1 = obj_2.display_scoreboard()
        var_2 = obj_2.__str__()
        obj_2.add_end(End(False))
        obj_2.add_end(End(False))
        
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, None)
        
    def test_691(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (4.191336676261281, 6.51791111516142), 11, False, False)
            
            var_1 = obj_0.is_guard()
            var_0 = obj_0.is_in_house()
            var_3 = obj_0.__str__()
            var_5 = obj_0.is_out_of_play()
            obj_0.burn()
            var_4 = obj_0.__str__()
        
    def test_692(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_5 = obj_1.overlaps_any_stone(Stone(False, (-0.38415411617872053, -6.334714543456473), 6, False, True))
            var_2 = obj_1.drawn()
            var_4 = obj_1.done()
            var_3 = obj_1.done()
            var_1 = obj_1.__str__()
            var_0 = obj_1.overlaps_any_stone(Stone(False, (-7.10640090086004, -3.625601078229172), 12, False, True))
        
    def test_693(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_1 = obj_1.__str__()
            var_2 = obj_1.score()
            var_0 = obj_1.done()
            obj_1.add_stone(Stone(True, (3.7717580046183077, 0.8115168933588048), 7, True, False))
        
    def test_694(self):
        obj_2 = Game()
        
        var_1 = obj_2.__str__()
        var_0 = obj_2.__str__()
        var_2 = obj_2.__str__()
        var_3 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, 'Game with 0 ends')
        
    def test_695(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_2 = obj_1.done()
            obj_1.add_stone(Stone(False, (-3.9900912334405856, -6.7611031742867524), 5, True, False))
            var_1 = obj_1.drawn()
        
    def test_696(self):
        obj_2 = Game()
        
        var_2 = obj_2.display_scoreboard()
        var_1 = obj_2.red_winner()
        var_4 = obj_2.score()
        var_3 = obj_2.red_winner()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_3, None)
        self.assertEqual(var_4, (0, 0))
        
    def test_697(self):
        obj_1 = End(True)
        
        var_2 = obj_1.red_won()
        var_0 = obj_1.score()
        var_1 = obj_1.red_won()
        
        self.assertEqual(var_0, 0)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, None)
        
    def test_698(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        obj_2.add_end(End(False))
        
        self.assertEqual(var_0, None)
        
    def test_699(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        var_2 = obj_2.__str__()
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_2, 'Game with 1 ends')
        
    def test_700(self):
        obj_1 = End(True)
        
        var_0 = obj_1.done()
        var_1 = obj_1.red_won()
        var_2 = obj_1.drawn()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, True)
        
    def test_701(self):
        obj_2 = Game()
        
        obj_2.add_end(End(True))
        var_2 = obj_2.display_scoreboard()
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |    1 | Total\n----|------|------\nRed | h  0 |     0\nYel |    0 |     0\n')
        self.assertEqual(var_2, 'End |    1 | Total\n----|------|------\nRed | h  0 |     0\nYel |    0 |     0\n')
        
    def test_702(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (4.1485785959964225, -7.492022007890501), 9, True, True)
            
            obj_0.move_out_of_play()
            obj_0.burn()
            obj_0.move_out_of_play()
            var_5 = obj_0.move((0.5259893637684385, 1.375673574946168), 9, False)
            var_0 = obj_0.__str__()
            var_2 = obj_0.move((1.938229314269206, -2.4158617499318122), 7, True)
            obj_0.burn()
            var_4 = obj_0.is_passed_hogline()
            obj_0.move_out_of_play()
            var_9 = obj_0.move((-7.1217568048498965, 1.399798173887861), 6, False)
        
    def test_703(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        var_3 = obj_2.red_winner()
        var_1 = obj_2.score()
        var_2 = obj_2.red_winner()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, None)
        
    def test_704(self):
        with self.assertRaisesRegex(ValueError, "Cannot calculate distance to center for a burned stone."):
            obj_0 = Stone(True, (-2.7329689085354616, 3.9436617360442003), 8, False, True)
            
            var_1 = obj_0.distance_to_center()
            var_2 = obj_0.distance_to_center()
            var_3 = obj_0.distance_to_center()
            var_0 = obj_0.is_out_of_bounds()
        
    def test_705(self):
        obj_1 = End(False)
        
        var_0 = obj_1.drawn()
        
        self.assertEqual(var_0, True)
        
    def test_706(self):
        obj_1 = End(True)
        
        var_0 = obj_1.score()
        var_1 = obj_1.red_won()
        var_2 = obj_1.score()
        
        self.assertEqual(var_0, 0)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 0)
        
    def test_707(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_3 = obj_1.score()
            var_0 = obj_1.drawn()
            var_2 = obj_1.score()
            obj_1.add_stone(Stone(True, (-4.738990573766591, 6.941894390778886), 9, True, False))
            var_1 = obj_1.score()
            var_5 = obj_1.done()
            var_4 = obj_1.done()
        
    def test_708(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (6.0114485475880475, -0.4870915052743001), 5, True, False)
            
            var_2 = obj_0.__str__()
            var_0 = obj_0.is_passed_hogline()
            var_1 = obj_0.move((-1.2062634083533101, -0.18337303627946078), 5, True)
        
    def test_709(self):
        obj_2 = Game()
        
        var_3 = obj_2.__str__()
        obj_2.add_end(End(False))
        var_2 = obj_2.red_winner()
        var_1 = obj_2.red_winner()
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, 'Game with 0 ends')
        
    def test_710(self):
        obj_2 = Game()
        
        var_1 = obj_2.display_scoreboard()
        obj_2.add_end(End(False))
        
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_711(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (5.311661728669943, 5.209577795061708), 3, False, False)
            
            var_0 = obj_0.move((-3.525501267939081, 6.140137321265252), 7, False)
            var_1 = obj_0.is_guard()
            var_3 = obj_0.move((3.50434657473952, -5.983127747937857), 10, True)
            var_2 = obj_0.is_in_house()
            obj_0.burn()
            var_5 = obj_0.is_out_of_bounds()
        
    def test_712(self):
        obj_1 = End(True)
        
        var_0 = obj_1.drawn()
        
        self.assertEqual(var_0, True)
        
    def test_713(self):
        obj_2 = Game()
        
        var_1 = obj_2.red_winner()
        obj_2.add_end(End(False))
        
        self.assertEqual(var_1, None)
        
    def test_714(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_4 = obj_1.__str__()
            var_5 = obj_1.score()
            var_3 = obj_1.__str__()
            var_6 = obj_1.__str__()
            var_0 = obj_1.drawn()
            var_1 = obj_1.score()
            obj_1.add_stone(Stone(False, (3.019357063383403, -7.231329402555614), 11, True, False))
        
    def test_715(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        var_1 = obj_2.red_winner()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, None)
        
    def test_716(self):
        with self.assertRaisesRegex(ValueError, "Stone's round does not match the expected round based on the number of stones already placed."):
            obj_1 = End(True)
            
            var_2 = obj_1.drawn()
            var_1 = obj_1.done()
            var_0 = obj_1.score()
            var_4 = obj_1.red_won()
            var_5 = obj_1.drawn()
            obj_1.add_stone(Stone(False, (-3.9046310676282285, 3.36474688528787), 10, True, True))
        
    def test_717(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (2.9883374362224604, -2.1993125629702632), 3, True, True)
            
            obj_0.burn()
            var_1 = obj_0.move((-0.5972014629993332, 2.3003641114122413), 4, False)
            obj_0.burn()
        
    def test_718(self):
        obj_2 = Game()
        
        var_2 = obj_2.red_winner()
        var_1 = obj_2.score()
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, None)
        
    def test_719(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (-4.50610975119816, 7.970928238533029), 3, False, False)
            
            var_0 = obj_0.__str__()
            obj_0.move_out_of_play()
            var_1 = obj_0.is_out_of_bounds()
        
    def test_720(self):
        obj_1 = End(True)
        
        var_1 = obj_1.score()
        var_0 = obj_1.overlaps_any_stone(Stone(False, (4.160598973025836, -6.556842359905843), 1, False, True))
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, 0)
        
    def test_721(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-4.332702544886363, 0.5390652814148336), 8, True, False)
            
            var_2 = obj_0.is_out_of_play()
            obj_0.burn()
            var_0 = obj_0.is_out_of_play()
            var_1 = obj_0.is_out_of_bounds()
        
    def test_722(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_723(self):
        with self.assertRaisesRegex(ValueError, "The first stone must be thrown by the team without the hammer."):
            obj_1 = End(True)
            
            var_0 = obj_1.__str__()
            var_4 = obj_1.score()
            obj_1.add_stone(Stone(True, (0.94180028899153, -5.957917305594449), 1, True, False))
            var_5 = obj_1.__str__()
            var_3 = obj_1.red_won()
            obj_1.add_stone(Stone(False, (0.23576600105539924, -7.8572637684406885), 8, True, False))
            var_6 = obj_1.score()
        
    def test_724(self):
        obj_2 = Game()
        
        var_2 = obj_2.__str__()
        var_1 = obj_2.red_winner()
        var_3 = obj_2.red_winner()
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, None)
        
    def test_725(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_3 = obj_1.red_won()
            obj_1.add_stone(Stone(False, (-5.163865342162961, 1.5105626119275826), 1, True, True))
            var_0 = obj_1.overlaps_any_stone(Stone(True, (-7.79625118618452, 0.514731988872521), 3, True, False))
            var_1 = obj_1.red_won()
        
    def test_726(self):
        obj_1 = End(False)
        
        var_2 = obj_1.score()
        var_0 = obj_1.__str__()
        var_3 = obj_1.red_won()
        var_1 = obj_1.overlaps_any_stone(Stone(False, (-1.8645131330933218, 2.0473106232488387), 4, False, False))
        
        self.assertEqual(var_0, 'End with Yellow hammer and 0 stones')
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, 0)
        self.assertEqual(var_3, None)
        
    def test_727(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (6.883454171891492, -4.327553457371195), 10, False, False)
            
            var_2 = obj_0.is_in_house()
            var_4 = obj_0.move((1.3878662305802134, 6.728573197941795), 2, True)
            var_5 = obj_0.is_passed_hogline()
            var_3 = obj_0.__str__()
            obj_0.move_out_of_play()
            var_0 = obj_0.is_in_house()
        
    def test_728(self):
        obj_2 = Game()
        
        var_1 = obj_2.score()
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, (0, 0))
        
    def test_729(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (-6.161008276898039, 4.707630499952206), 1, True, False)
            
            var_0 = obj_0.move((-5.946951578178044, 3.2566385128537583), 7, False)
            var_3 = obj_0.is_out_of_bounds()
            var_1 = obj_0.is_guard()
            var_7 = obj_0.move((-5.146481094202537, -5.46842400825331), 12, False)
            var_4 = obj_0.is_out_of_play()
            var_2 = obj_0.__str__()
            var_6 = obj_0.is_guard()
            var_5 = obj_0.is_guard()
        
    def test_730(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            obj_1.add_stone(Stone(True, (5.038670168811235, 5.768885830961546), 1, False, True))
            var_0 = obj_1.score()
            var_2 = obj_1.overlaps_any_stone(Stone(True, (6.988358028533549, 6.344783776509944), 3, True, False))
        
    def test_731(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            obj_1.add_stone(Stone(True, (-1.9154437953427124, 7.453257894085171), -1, False, True))
            var_1 = obj_1.red_won()
            var_2 = obj_1.done()
            obj_1.add_stone(Stone(True, (-4.032696855916308, -7.670142108266495), 12, True, False))
            var_3 = obj_1.drawn()
            var_4 = obj_1.red_won()
        
    def test_732(self):
        obj_2 = Game()
        
        var_1 = obj_2.score()
        var_2 = obj_2.display_scoreboard()
        var_0 = obj_2.red_winner()
        var_3 = obj_2.__str__()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_3, 'Game with 0 ends')
        
    def test_733(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (2.1142666942844777, -7.032715412263258), 11, False, True)
            
            var_1 = obj_0.is_guard()
            var_0 = obj_0.is_out_of_play()
        
    def test_734(self):
        with self.assertRaisesRegex(ValueError, "Stone's round does not match the expected round based on the number of stones already placed."):
            obj_1 = End(False)
            
            obj_1.add_stone(Stone(True, (0.21179853327710418, -7.585099865607246), 4, False, True))
            obj_1.add_stone(Stone(False, (0.1810057916612653, -5.930064012712357), -2, True, True))
            obj_1.add_stone(Stone(True, (-0.15359629524490437, -5.744280013747302), 3, True, False))
            var_3 = obj_1.red_won()
        
    def test_735(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-4.213931542397466, -6.327633415655853), -1, True, True)
            
            var_1 = obj_0.is_in_house()
            var_0 = obj_0.is_guard()
            var_2 = obj_0.is_out_of_bounds()
        
    def test_736(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |    1 | Total\n----|------|------\nRed |    0 |     0\nYel | h  0 |     0\n')
        
    def test_737(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            obj_1.add_stone(Stone(False, (7.431012728023319, -7.301923139154834), 8, False, False))
            var_0 = obj_1.red_won()
        
    def test_738(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-2.2581597319351747, -7.008422454407361), -2, False, True)
            
            var_0 = obj_0.is_passed_hogline()
        
    def test_739(self):
        obj_1 = End(True)
        
        var_0 = obj_1.done()
        
        self.assertEqual(var_0, False)
        
    def test_740(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-7.889698705911048, 3.104847920765394), 7, True, False)
            
            obj_0.burn()
            var_0 = obj_0.is_out_of_play()
            obj_0.move_out_of_play()
            var_4 = obj_0.is_out_of_play()
            var_3 = obj_0.__str__()
        
    def test_741(self):
        obj_2 = Game()
        
        var_3 = obj_2.score()
        var_2 = obj_2.__str__()
        var_0 = obj_2.display_scoreboard()
        var_1 = obj_2.red_winner()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, (0, 0))
        
    def test_742(self):
        obj_1 = End(True)
        
        var_0 = obj_1.score()
        var_1 = obj_1.done()
        var_2 = obj_1.done()
        
        self.assertEqual(var_0, 0)
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, False)
        
    def test_743(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (4.972267050211695, 0.38834197403988924), 0, False, False)
            
            obj_0.move_out_of_play()
        
    def test_744(self):
        obj_2 = Game()
        
        var_3 = obj_2.score()
        var_0 = obj_2.__str__()
        var_1 = obj_2.score()
        var_2 = obj_2.red_winner()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, (0, 0))
        
    def test_745(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        var_1 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, None)
        
    def test_746(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_1 = obj_1.score()
            var_2 = obj_1.score()
            obj_1.add_stone(Stone(False, (6.727916481692599, 4.457928829064032), 12, False, True))
        
    def test_747(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_2 = obj_1.done()
            var_4 = obj_1.score()
            var_0 = obj_1.score()
            var_3 = obj_1.drawn()
            obj_1.add_stone(Stone(False, (4.928353469947671, -1.984005013089929), -2, False, False))
        
    def test_748(self):
        obj_1 = End(False)
        
        var_5 = obj_1.__str__()
        var_0 = obj_1.score()
        var_4 = obj_1.red_won()
        var_2 = obj_1.done()
        var_1 = obj_1.red_won()
        var_3 = obj_1.drawn()
        
        self.assertEqual(var_0, 0)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, False)
        self.assertEqual(var_3, True)
        self.assertEqual(var_4, None)
        self.assertEqual(var_5, 'End with Yellow hammer and 0 stones')
        
    def test_749(self):
        obj_1 = End(False)
        
        var_5 = obj_1.__str__()
        var_3 = obj_1.drawn()
        var_2 = obj_1.drawn()
        var_4 = obj_1.overlaps_any_stone(Stone(True, (-7.39882477465866, 4.886935091603288), 10, False, True))
        var_0 = obj_1.done()
        var_1 = obj_1.red_won()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, True)
        self.assertEqual(var_3, True)
        self.assertEqual(var_4, False)
        self.assertEqual(var_5, 'End with Yellow hammer and 0 stones')
        
    def test_750(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (1.6879792948465013, 3.7809222538570904), 1, False, True)
            
            obj_0.burn()
            var_0 = obj_0.is_in_house()
            var_1 = obj_0.is_guard()
            var_4 = obj_0.is_out_of_play()
            var_2 = obj_0.is_out_of_play()
        
    def test_751(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (0.40597917513687065, -4.003541797407117), 11, False, True)
            
            var_0 = obj_0.__str__()
        
    def test_752(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        var_1 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_753(self):
        obj_1 = End(False)
        
        var_0 = obj_1.drawn()
        var_1 = obj_1.drawn()
        var_3 = obj_1.red_won()
        var_2 = obj_1.drawn()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, True)
        self.assertEqual(var_2, True)
        self.assertEqual(var_3, None)
        
    def test_754(self):
        obj_2 = Game()
        
        var_3 = obj_2.red_winner()
        obj_2.add_end(End(False))
        var_1 = obj_2.__str__()
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, 'Game with 1 ends')
        self.assertEqual(var_3, None)
        
    def test_755(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_3 = obj_1.overlaps_any_stone(Stone(False, (-5.937565211711529, 4.5857516865955095), 12, True, False))
            var_2 = obj_1.score()
            var_1 = obj_1.__str__()
            var_0 = obj_1.done()
            var_4 = obj_1.drawn()
        
    def test_756(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        
        
    def test_757(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            obj_1.add_stone(Stone(True, (-6.280950831825114, 1.9536941394968004), 12, False, True))
        
    def test_758(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (-2.348652835658596, 0.5053317633450725), 8, False, False)
            
            var_2 = obj_0.move((-6.351537887327339, -6.7130803855168), -1, False)
            var_1 = obj_0.is_in_house()
            obj_0.move_out_of_play()
            var_3 = obj_0.is_guard()
        
    def test_759(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (-6.665370075170641, -3.9457143482405357), 9, True, False)
            
            var_2 = obj_0.distance_to_center()
            var_1 = obj_0.is_out_of_play()
            var_0 = obj_0.is_passed_hogline()
        
    def test_760(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_761(self):
        obj_2 = Game()
        
        var_1 = obj_2.red_winner()
        var_3 = obj_2.score()
        var_4 = obj_2.score()
        obj_2.add_end(End(True))
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, None)
        self.assertEqual(var_3, (0, 0))
        self.assertEqual(var_4, (0, 0))
        
    def test_762(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_0 = obj_1.drawn()
            var_1 = obj_1.done()
            var_2 = obj_1.overlaps_any_stone(Stone(True, (4.4976313237886405, -6.097526419886385), 1, True, False))
            var_4 = obj_1.red_won()
            var_5 = obj_1.drawn()
            var_6 = obj_1.__str__()
            var_3 = obj_1.drawn()
        
    def test_763(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_0 = obj_1.done()
            var_6 = obj_1.score()
            var_4 = obj_1.score()
            var_3 = obj_1.done()
            obj_1.add_stone(Stone(False, (-0.7321107194850587, 6.902520663280152), -1, False, True))
            var_5 = obj_1.score()
            var_2 = obj_1.overlaps_any_stone(Stone(False, (5.227025497586665, 5.146710017906532), 3, False, True))
        
    def test_764(self):
        obj_1 = End(True)
        
        var_0 = obj_1.overlaps_any_stone(Stone(False, (-1.9803588917640251, -5.207645777289031), 7, True, False))
        
        self.assertEqual(var_0, False)
        
    def test_765(self):
        obj_1 = End(True)
        
        var_2 = obj_1.score()
        var_0 = obj_1.red_won()
        var_1 = obj_1.score()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 0)
        self.assertEqual(var_2, 0)
        
    def test_766(self):
        obj_1 = End(True)
        
        var_0 = obj_1.done()
        var_1 = obj_1.red_won()
        var_2 = obj_1.done()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, False)
        
    def test_767(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (1.7473788850005558, 2.265744731452319), 6, True, True)
            
            obj_0.burn()
            var_1 = obj_0.is_guard()
            var_2 = obj_0.__str__()
        
    def test_768(self):
        obj_1 = End(False)
        
        var_4 = obj_1.__str__()
        var_0 = obj_1.drawn()
        var_1 = obj_1.drawn()
        var_3 = obj_1.red_won()
        var_2 = obj_1.score()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, True)
        self.assertEqual(var_2, 0)
        self.assertEqual(var_3, None)
        self.assertEqual(var_4, 'End with Yellow hammer and 0 stones')
        
    def test_769(self):
        obj_0 = Stone(False, (-1.5039580925060143, -1.6714120230554936), 5, False, True)
        
        var_0 = obj_0.__str__()
        
        self.assertEqual(var_0, 'Yellow stone at (2.50, 5.49), round 5, burned')
        
    def test_770(self):
        obj_1 = End(False)
        
        var_0 = obj_1.drawn()
        
        self.assertEqual(var_0, True)
        
    def test_771(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        
    def test_772(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        
    def test_773(self):
        obj_2 = Game()
        
        var_1 = obj_2.score()
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, (0, 0))
        
    def test_774(self):
        obj_0 = Stone(False, (0.42414948517716944, -5.223935397219465), 9, False, False)
        
        var_0 = obj_0.is_out_of_bounds()
        var_1 = obj_0.is_passed_hogline()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, True)
        
    def test_775(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_2 = obj_1.score()
            var_1 = obj_1.overlaps_any_stone(Stone(True, (6.15402557170167, 4.771642256821806), -1, True, False))
            obj_1.add_stone(Stone(False, (-0.8786423153742007, 7.815029772149037), -2, True, True))
        
    def test_776(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            obj_1.add_stone(Stone(True, (-3.5052998924870007, -2.9765589315389054), 9, True, False))
            var_1 = obj_1.drawn()
            var_0 = obj_1.overlaps_any_stone(Stone(True, (0.993013501105052, -5.194272025448711), 8, True, False))
            var_3 = obj_1.score()
            var_2 = obj_1.red_won()
        
    def test_777(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-4.710617240491283, -2.9481136042362497), -1, True, True)
            
            var_0 = obj_0.distance_to_center()
            var_3 = obj_0.distance_to_center()
            var_2 = obj_0.is_in_house()
            var_1 = obj_0.is_in_house()
        
    def test_778(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (6.527683371593406, 5.877685796789029), 11, True, False)
            
            obj_0.move_out_of_play()
            var_3 = obj_0.is_out_of_bounds()
            var_5 = obj_0.is_guard()
            obj_0.burn()
            var_1 = obj_0.is_out_of_play()
            obj_0.move_out_of_play()
            var_9 = obj_0.is_in_house()
            var_7 = obj_0.move((3.8000711731752954, -7.7480921602641875), 7, True)
            var_0 = obj_0.is_passed_hogline()
            var_4 = obj_0.distance_to_center()
        
    def test_779(self):
        obj_2 = Game()
        
        var_4 = obj_2.__str__()
        var_0 = obj_2.display_scoreboard()
        obj_2.add_end(End(True))
        var_3 = obj_2.red_winner()
        var_1 = obj_2.red_winner()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, None)
        self.assertEqual(var_3, None)
        self.assertEqual(var_4, 'Game with 0 ends')
        
    def test_780(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (3.621369585142828, -4.810080918317796), 1, False, False)
            
            var_1 = obj_0.is_in_house()
            obj_0.burn()
            var_0 = obj_0.distance_to_center()
            var_2 = obj_0.move((5.476869427833588, 5.935494062863318), 8, False)
        
    def test_781(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (1.3666700947261337, -0.33567987758229734), -1, False, False)
            
            var_3 = obj_0.is_in_house()
            obj_0.move_out_of_play()
            var_0 = obj_0.is_passed_hogline()
            var_4 = obj_0.distance_to_center()
            obj_0.move_out_of_play()
            var_2 = obj_0.is_passed_hogline()
        
    def test_782(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        
    def test_783(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (2.7865198985965236, 0.3416366749256934), 10, False, True)
            
            var_5 = obj_0.__str__()
            var_4 = obj_0.__str__()
            obj_0.burn()
            var_1 = obj_0.is_out_of_bounds()
            var_8 = obj_0.is_out_of_play()
            var_0 = obj_0.is_out_of_bounds()
            obj_0.burn()
            var_3 = obj_0.move((7.267944309913641, 5.422852573172127), -1, False)
            var_6 = obj_0.is_out_of_play()
        
    def test_784(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (2.938914831461391, -2.9163368849359763), 10, False, False)
            
            var_6 = obj_0.move((-5.013328875626387, -0.17617352190697666), 4, False)
            var_4 = obj_0.is_out_of_play()
            var_5 = obj_0.move((-6.753703368544784, 1.1628932961113954), 0, True)
            var_2 = obj_0.__str__()
            var_3 = obj_0.__str__()
            var_1 = obj_0.__str__()
            var_0 = obj_0.is_in_house()
        
    def test_785(self):
        with self.assertRaisesRegex(ValueError, "The first stone must be thrown by the team without the hammer."):
            obj_1 = End(False)
            
            var_3 = obj_1.__str__()
            var_0 = obj_1.score()
            var_2 = obj_1.__str__()
            var_1 = obj_1.red_won()
            var_4 = obj_1.__str__()
            obj_1.add_stone(Stone(False, (3.0324907758339066, -0.32426115004290423), 5, False, True))
        
    def test_786(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-1.9820897207814827, 2.6329655800474807), 6, True, True)
            
            var_4 = obj_0.move((1.9837754551734665, -2.1647538073943533), -2, False)
            var_3 = obj_0.move((-7.9390305110740655, 3.552407059804999), 6, True)
            obj_0.move_out_of_play()
            var_2 = obj_0.is_out_of_bounds()
            var_5 = obj_0.is_out_of_bounds()
            var_1 = obj_0.is_in_house()
            var_7 = obj_0.is_in_house()
            var_6 = obj_0.is_out_of_bounds()
        
    def test_787(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        var_2 = obj_2.__str__()
        var_1 = obj_2.display_scoreboard()
        var_3 = obj_2.score()
        var_4 = obj_2.red_winner()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, (0, 0))
        self.assertEqual(var_4, None)
        
    def test_788(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_1 = obj_1.overlaps_any_stone(Stone(False, (7.092037541433964, -2.7766458958551397), 7, True, True))
            var_0 = obj_1.overlaps_any_stone(Stone(False, (4.219135744740591, -0.04264889513523329), -2, True, False))
        
    def test_789(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_790(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_3 = obj_1.overlaps_any_stone(Stone(True, (-5.603066011409769, 3.0270943351765016), 2, False, False))
            var_1 = obj_1.overlaps_any_stone(Stone(True, (4.83596928868001, -7.5350620839274605), -1, True, True))
            var_4 = obj_1.done()
            var_6 = obj_1.done()
            var_2 = obj_1.done()
            var_5 = obj_1.red_won()
            var_0 = obj_1.red_won()
        
    def test_791(self):
        obj_2 = Game()
        
        var_1 = obj_2.__str__()
        var_0 = obj_2.red_winner()
        var_2 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, None)
        
    def test_792(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (-6.538743078929727, -7.386084342953291), 1, False, True)
            
            obj_0.move_out_of_play()
            obj_0.move_out_of_play()
        
    def test_793(self):
        obj_1 = End(True)
        
        var_4 = obj_1.red_won()
        var_3 = obj_1.red_won()
        var_0 = obj_1.drawn()
        var_2 = obj_1.red_won()
        var_1 = obj_1.red_won()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, None)
        self.assertEqual(var_4, None)
        
    def test_794(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_0 = obj_1.overlaps_any_stone(Stone(False, (5.817201690525639, 7.581436477247179), 0, True, False))
            var_3 = obj_1.drawn()
            var_2 = obj_1.overlaps_any_stone(Stone(True, (6.128469866369313, 6.460625167097666), 12, False, False))
            var_1 = obj_1.drawn()
        
    def test_795(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        
    def test_796(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        
    def test_797(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        var_1 = obj_2.score()
        var_2 = obj_2.__str__()
        var_4 = obj_2.score()
        obj_2.add_end(End(False))
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_4, (0, 0))
        
    def test_798(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        var_2 = obj_2.score()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_2, (0, 0))
        
    def test_799(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
            obj_2 = Game()
            
            var_2 = obj_2.red_winner()
            obj_2.add_end(End(False))
            var_4 = obj_2.display_scoreboard()
            var_3 = obj_2.__str__()
            obj_2.add_end(End(True))
        
    def test_800(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (3.0872510663793733, 3.1265130662884175), 9, True, True)
            
            var_5 = obj_0.is_out_of_play()
            var_8 = obj_0.is_passed_hogline()
            var_9 = obj_0.is_out_of_play()
            var_6 = obj_0.is_passed_hogline()
            var_2 = obj_0.is_passed_hogline()
            var_7 = obj_0.is_out_of_play()
            obj_0.burn()
            var_0 = obj_0.is_out_of_bounds()
            obj_0.move_out_of_play()
            var_1 = obj_0.is_out_of_play()
        
    def test_801(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            obj_1.add_stone(Stone(False, (2.963809769807506, -3.9024012874514895), 3, False, False))
            obj_1.add_stone(Stone(False, (2.729409010458788, 5.7754727307080955), 12, False, True))
            var_0 = obj_1.drawn()
            var_1 = obj_1.__str__()
        
    def test_802(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (-4.832226493429642, 4.788169953348513), 3, True, False)
            
            var_3 = obj_0.move((-5.6879446645689935, -6.345876919790896), 12, True)
            var_1 = obj_0.__str__()
            var_2 = obj_0.move((-0.7192643273119614, -0.412569353510138), 0, True)
            var_0 = obj_0.__str__()
            obj_0.burn()
        
    def test_803(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
            obj_2 = Game()
            
            var_3 = obj_2.score()
            var_1 = obj_2.__str__()
            obj_2.add_end(End(False))
            obj_2.add_end(End(True))
        
    def test_804(self):
        obj_2 = Game()
        
        var_4 = obj_2.score()
        obj_2.add_end(End(False))
        var_1 = obj_2.display_scoreboard()
        var_2 = obj_2.display_scoreboard()
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 1 ends')
        self.assertEqual(var_1, 'End |    1 | Total\n----|------|------\nRed |    0 |     0\nYel | h  0 |     0\n')
        self.assertEqual(var_2, 'End |    1 | Total\n----|------|------\nRed |    0 |     0\nYel | h  0 |     0\n')
        self.assertEqual(var_4, (0, 0))
        
    def test_805(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_0 = obj_1.overlaps_any_stone(Stone(True, (-1.3520789987174133, 2.0119526661663496), 10, True, False))
            obj_1.add_stone(Stone(True, (-0.6138756070538793, 0.8147967358084962), 11, False, True))
        
    def test_806(self):
        obj_2 = Game()
        
        var_2 = obj_2.__str__()
        obj_2.add_end(End(True))
        var_1 = obj_2.score()
        
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'Game with 0 ends')
        
    def test_807(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-5.355055760893206, -4.334196744669244), 11, True, True)
            
            var_0 = obj_0.__str__()
            var_1 = obj_0.is_out_of_play()
            var_2 = obj_0.is_in_house()
        
    def test_808(self):
        obj_2 = Game()
        
        obj_2.add_end(End(True))
        var_1 = obj_2.display_scoreboard()
        
        self.assertEqual(var_1, 'End |    1 | Total\n----|------|------\nRed | h  0 |     0\nYel |    0 |     0\n')
        
    def test_809(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (-7.077443072462579, 1.8563814415589412), 7, True, False)
            
            var_5 = obj_0.is_guard()
            var_3 = obj_0.is_passed_hogline()
            var_7 = obj_0.__str__()
            var_4 = obj_0.is_guard()
            var_8 = obj_0.is_in_house()
            var_0 = obj_0.is_in_house()
            var_1 = obj_0.move((-4.2913439855999975, 2.942206513377929), 8, False)
            obj_0.burn()
            var_2 = obj_0.is_out_of_bounds()
        
    def test_810(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (4.076696070714306, -1.9504731944002973), 12, True, True)
            
            var_1 = obj_0.is_out_of_play()
            obj_0.move_out_of_play()
            var_2 = obj_0.is_out_of_play()
            obj_0.move_out_of_play()
            var_5 = obj_0.__str__()
            var_6 = obj_0.__str__()
            var_3 = obj_0.__str__()
        
    def test_811(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (4.105507331637909, 7.087706688465136), 11, True, False)
            
            var_6 = obj_0.is_guard()
            var_3 = obj_0.is_in_house()
            obj_0.burn()
            var_7 = obj_0.move((6.7151869277577525, -7.643917028832773), 2, True)
            var_8 = obj_0.is_out_of_play()
            obj_0.move_out_of_play()
            var_1 = obj_0.is_guard()
            var_2 = obj_0.__str__()
            var_5 = obj_0.move((-3.5598361641821334, -1.9619666926636246), 5, True)
        
    def test_812(self):
        obj_2 = Game()
        
        var_1 = obj_2.red_winner()
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, None)
        
    def test_813(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        var_0 = obj_2.display_scoreboard()
        var_2 = obj_2.display_scoreboard()
        var_3 = obj_2.score()
        
        self.assertEqual(var_0, 'End |    1 | Total\n----|------|------\nRed |    0 |     0\nYel | h  0 |     0\n')
        self.assertEqual(var_2, 'End |    1 | Total\n----|------|------\nRed |    0 |     0\nYel | h  0 |     0\n')
        self.assertEqual(var_3, (0, 0))
        
    def test_814(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (1.8841140763806976, 6.953770167364331), 4, False, False)
            
            var_0 = obj_0.move((-4.224248119884667, 2.0070620343603256), -2, True)
            var_1 = obj_0.is_passed_hogline()
            var_5 = obj_0.is_out_of_bounds()
            var_3 = obj_0.is_out_of_bounds()
            var_2 = obj_0.is_in_house()
            var_4 = obj_0.is_guard()
        
    def test_815(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        
    def test_816(self):
        obj_2 = Game()
        
        var_4 = obj_2.display_scoreboard()
        var_3 = obj_2.score()
        var_2 = obj_2.__str__()
        var_1 = obj_2.score()
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, (0, 0))
        self.assertEqual(var_4, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_817(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        var_1 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_818(self):
        obj_2 = Game()
        
        var_2 = obj_2.score()
        var_1 = obj_2.score()
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, (0, 0))
        
    def test_819(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        var_3 = obj_2.score()
        var_2 = obj_2.__str__()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, (0, 0))
        
    def test_820(self):
        obj_0 = Stone(False, (4.992271809723938, 0.36351112541688657), 1, True, True)
        
        var_0 = obj_0.is_passed_hogline()
        var_1 = obj_0.is_out_of_bounds()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, False)
        
    def test_821(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-1.5728733294337491, 5.134379817857781), 12, True, True)
            
            var_0 = obj_0.is_passed_hogline()
            var_2 = obj_0.is_passed_hogline()
            var_1 = obj_0.is_guard()
            var_5 = obj_0.is_out_of_bounds()
            var_4 = obj_0.is_guard()
            var_8 = obj_0.distance_to_center()
            obj_0.burn()
            var_3 = obj_0.is_out_of_play()
            var_6 = obj_0.is_out_of_bounds()
        
    def test_822(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
            obj_2 = Game()
            
            obj_2.add_end(End(True))
            obj_2.add_end(End(False))
            var_4 = obj_2.display_scoreboard()
            obj_2.add_end(End(False))
            var_1 = obj_2.score()
        
    def test_823(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-2.214146024123359, -1.4192516054945603), 12, True, True)
            
            var_1 = obj_0.is_passed_hogline()
            var_0 = obj_0.is_out_of_play()
            var_2 = obj_0.distance_to_center()
        
    def test_824(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (-3.369635824831988, -6.695996827912838), 7, False, True)
            
            obj_0.move_out_of_play()
            var_3 = obj_0.is_guard()
            obj_0.burn()
            var_0 = obj_0.__str__()
            var_1 = obj_0.is_out_of_bounds()
            var_5 = obj_0.is_guard()
            var_6 = obj_0.is_in_house()
            var_4 = obj_0.distance_to_center()
        
    def test_825(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (-5.697718176955011, 7.186657759436901), 3, True, False)
            
            obj_0.burn()
            obj_0.move_out_of_play()
            var_3 = obj_0.move((-2.684023681642641, 5.48775632215901), 8, True)
            var_5 = obj_0.is_guard()
            var_4 = obj_0.distance_to_center()
            var_9 = obj_0.is_out_of_bounds()
            var_6 = obj_0.move((-2.4669674129075982, 1.5802788822422364), 2, True)
            var_2 = obj_0.is_out_of_play()
            obj_0.burn()
            var_8 = obj_0.is_in_house()
        
    def test_826(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_3 = obj_1.done()
            var_2 = obj_1.drawn()
            var_4 = obj_1.overlaps_any_stone(Stone(True, (3.6088370035268866, -7.616296842702516), 0, False, True))
            var_0 = obj_1.score()
            var_1 = obj_1.done()
        
    def test_827(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (0.8658415601806819, -3.608627546015475), -2, False, True)
            
            obj_0.move_out_of_play()
        
    def test_828(self):
        with self.assertRaisesRegex(ValueError, "The first stone must be thrown by the team without the hammer."):
            obj_1 = End(True)
            
            var_0 = obj_1.overlaps_any_stone(Stone(True, (5.664450681235344, 4.106646472979895), 8, False, True))
            var_4 = obj_1.red_won()
            var_6 = obj_1.red_won()
            obj_1.add_stone(Stone(True, (5.397729023494643, 7.295074999307076), 8, False, True))
            var_1 = obj_1.red_won()
            var_2 = obj_1.drawn()
            var_3 = obj_1.overlaps_any_stone(Stone(False, (-6.042560357925749, 2.788090700541673), 10, True, True))
        
    def test_829(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (7.913804804126059, 2.2928207817930435), 2, False, False)
            
            var_1 = obj_0.is_guard()
            var_2 = obj_0.distance_to_center()
            var_4 = obj_0.distance_to_center()
            var_0 = obj_0.is_passed_hogline()
            var_3 = obj_0.is_in_house()
        
    def test_830(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (6.618062298595985, 4.813013140074405), 2, False, False)
            
            var_2 = obj_0.move((3.3194018348078025, 2.9701565196986586), 4, True)
            var_0 = obj_0.is_out_of_bounds()
            var_1 = obj_0.__str__()
        
    def test_831(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        
    def test_832(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_0 = obj_1.red_won()
            obj_1.add_stone(Stone(False, (-3.3790990541093784, -1.6024596789149594), 3, False, False))
            var_3 = obj_1.done()
            obj_1.add_stone(Stone(True, (6.419446864512311, -5.259935811114472), -1, True, False))
            var_2 = obj_1.score()
        
    def test_833(self):
        obj_2 = Game()
        
        var_1 = obj_2.red_winner()
        var_2 = obj_2.score()
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, (0, 0))
        
    def test_834(self):
        obj_1 = End(False)
        
        var_2 = obj_1.drawn()
        var_1 = obj_1.__str__()
        var_0 = obj_1.red_won()
        var_3 = obj_1.score()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'End with Yellow hammer and 0 stones')
        self.assertEqual(var_2, True)
        self.assertEqual(var_3, 0)
        
    def test_835(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_836(self):
        obj_2 = Game()
        
        var_1 = obj_2.score()
        var_0 = obj_2.__str__()
        var_2 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'Game with 0 ends')
        
    def test_837(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (5.421990316273716, -2.460828617802724), 6, False, False)
            
            var_2 = obj_0.is_out_of_bounds()
            var_1 = obj_0.distance_to_center()
            var_0 = obj_0.distance_to_center()
        
    def test_838(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (1.0705110352155298, 3.152949984372597), 12, False, True)
            
            var_0 = obj_0.is_passed_hogline()
        
    def test_839(self):
        obj_1 = End(True)
        
        var_2 = obj_1.red_won()
        var_1 = obj_1.score()
        var_4 = obj_1.__str__()
        var_0 = obj_1.done()
        var_3 = obj_1.drawn()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, 0)
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, True)
        self.assertEqual(var_4, 'End with Red hammer and 0 stones')
        
    def test_840(self):
        obj_1 = End(True)
        
        var_0 = obj_1.overlaps_any_stone(Stone(True, (-4.158688848044235, -6.018211757207512), 10, False, True))
        
        self.assertEqual(var_0, False)
        
    def test_841(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        
    def test_842(self):
        obj_1 = End(False)
        
        var_0 = obj_1.__str__()
        var_1 = obj_1.red_won()
        
        self.assertEqual(var_0, 'End with Yellow hammer and 0 stones')
        self.assertEqual(var_1, None)
        
    def test_843(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (6.829060594782209, -5.92885678419645), 0, False, False)
            
            obj_0.burn()
        
    def test_844(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (4.059602406057456, 1.2706170960809544), 9, True, False)
            
            obj_0.burn()
            var_1 = obj_0.is_out_of_play()
            var_2 = obj_0.move((2.254343061500821, -6.074922797166684), 6, True)
            var_6 = obj_0.is_guard()
            var_5 = obj_0.is_out_of_play()
            var_3 = obj_0.is_passed_hogline()
            var_7 = obj_0.is_out_of_play()
            var_4 = obj_0.move((-4.188430740506945, 1.8126780478045497), 4, False)
            obj_0.move_out_of_play()
        
    def test_845(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (3.211241665638564, 4.033831429784978), 5, False, True)
            
            var_0 = obj_0.move((-7.275086875012308, -7.587750142978905), 3, True)
        
    def test_846(self):
        obj_2 = Game()
        
        var_1 = obj_2.score()
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, (0, 0))
        
    def test_847(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (-4.259913076107027, 1.3425499870816768), 8, False, True)
            
            var_3 = obj_0.is_out_of_play()
            var_4 = obj_0.is_out_of_bounds()
            var_0 = obj_0.is_guard()
            obj_0.move_out_of_play()
            var_1 = obj_0.distance_to_center()
            var_7 = obj_0.is_passed_hogline()
            var_2 = obj_0.move((-3.3204779613108, -2.9189335212429466), -1, False)
            var_5 = obj_0.is_in_house()
            obj_0.burn()
        
    def test_848(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        var_1 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_849(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        var_1 = obj_2.score()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, (0, 0))
        
    def test_850(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            obj_1.add_stone(Stone(True, (-3.094059833307247, 1.7538782920657656), 2, False, False))
            var_0 = obj_1.overlaps_any_stone(Stone(False, (-5.909869232586805, -0.644341882441422), 10, False, False))
            var_3 = obj_1.__str__()
            var_4 = obj_1.red_won()
            var_1 = obj_1.__str__()
        
    def test_851(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_1 = obj_1.drawn()
            var_2 = obj_1.overlaps_any_stone(Stone(True, (3.6456461777149887, -2.699306251651617), 1, False, False))
            var_3 = obj_1.__str__()
            obj_1.add_stone(Stone(True, (1.1526689572876094, -6.385692500095672), 4, False, False))
            var_0 = obj_1.__str__()
        
    def test_852(self):
        obj_1 = End(True)
        
        var_1 = obj_1.score()
        var_3 = obj_1.overlaps_any_stone(Stone(False, (-3.1242000970519044, -1.4984450586879294), 6, False, True))
        var_2 = obj_1.overlaps_any_stone(Stone(True, (-1.8445174260188502, 0.7778191322791734), 5, True, True))
        var_0 = obj_1.__str__()
        
        self.assertEqual(var_0, 'End with Red hammer and 0 stones')
        self.assertEqual(var_1, 0)
        self.assertEqual(var_2, False)
        self.assertEqual(var_3, False)
        
    def test_853(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        var_0 = obj_2.red_winner()
        obj_2.add_end(End(False))
        var_2 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_2, None)
        
    def test_854(self):
        obj_1 = End(True)
        
        var_0 = obj_1.red_won()
        
        self.assertEqual(var_0, None)
        
    def test_855(self):
        obj_1 = End(False)
        
        var_2 = obj_1.overlaps_any_stone(Stone(False, (-7.300276281320954, -1.1465794113531107), 1, True, True))
        var_1 = obj_1.done()
        var_3 = obj_1.drawn()
        var_0 = obj_1.score()
        
        self.assertEqual(var_0, 0)
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, False)
        self.assertEqual(var_3, True)
        
    def test_856(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        obj_2.add_end(End(False))
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_857(self):
        obj_2 = Game()
        
        obj_2.add_end(End(True))
        
        
    def test_858(self):
        obj_2 = Game()
        
        var_1 = obj_2.score()
        obj_2.add_end(End(False))
        var_0 = obj_2.score()
        var_2 = obj_2.score()
        var_3 = obj_2.__str__()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, (0, 0))
        self.assertEqual(var_3, 'Game with 1 ends')
        
    def test_859(self):
        obj_2 = Game()
        
        var_3 = obj_2.display_scoreboard()
        var_2 = obj_2.__str__()
        obj_2.add_end(End(False))
        var_1 = obj_2.display_scoreboard()
        
        self.assertEqual(var_1, 'End |    1 | Total\n----|------|------\nRed |    0 |     0\nYel | h  0 |     0\n')
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_860(self):
        obj_1 = End(True)
        
        var_0 = obj_1.__str__()
        
        self.assertEqual(var_0, 'End with Red hammer and 0 stones')
        
    def test_861(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        
    def test_862(self):
        obj_2 = Game()
        
        var_1 = obj_2.red_winner()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_1, None)
        
    def test_863(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-6.836081761807998, -7.888883537934566), 3, True, True)
            
            var_1 = obj_0.__str__()
            var_6 = obj_0.move((-0.5048702890396246, -4.44321372107475), 10, False)
            var_0 = obj_0.is_in_house()
            var_4 = obj_0.is_out_of_play()
            var_3 = obj_0.is_guard()
            var_5 = obj_0.is_out_of_play()
            obj_0.move_out_of_play()
        
    def test_864(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (1.5848095372873399, 5.1157738799028944), 12, True, True)
            
            var_1 = obj_0.is_in_house()
            var_0 = obj_0.is_in_house()
        
    def test_865(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-5.422587478716629, -7.476223858246211), 9, False, False)
            
            var_1 = obj_0.is_out_of_play()
            obj_0.move_out_of_play()
            var_2 = obj_0.is_passed_hogline()
        
    def test_866(self):
        with self.assertRaisesRegex(ValueError, "Stone's hammer status does not match the end's hammer status."):
            obj_1 = End(True)
            
            obj_1.add_stone(Stone(False, (1.2294424656078018, -5.7656254140150995), 3, False, True))
            var_1 = obj_1.overlaps_any_stone(Stone(False, (4.408343120380094, 6.094456783409628), -2, False, False))
        
    def test_867(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (7.915469555332566, 0.8325229652071666), 1, False, False)
            
            var_7 = obj_0.is_in_house()
            var_3 = obj_0.is_out_of_bounds()
            var_5 = obj_0.is_out_of_play()
            var_0 = obj_0.is_out_of_play()
            var_4 = obj_0.is_passed_hogline()
            var_2 = obj_0.__str__()
            var_6 = obj_0.is_out_of_bounds()
            var_1 = obj_0.is_passed_hogline()
            var_8 = obj_0.is_out_of_play()
        
    def test_868(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (4.759563103915879, -2.679565636303826), 3, False, True)
            
            obj_0.move_out_of_play()
            var_0 = obj_0.is_out_of_play()
            obj_0.move_out_of_play()
            var_1 = obj_0.move((-6.140399096860566, -5.73603627594097), 3, True)
        
    def test_869(self):
        obj_2 = Game()
        
        var_1 = obj_2.display_scoreboard()
        obj_2.add_end(End(False))
        
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_870(self):
        obj_2 = Game()
        
        var_2 = obj_2.__str__()
        obj_2.add_end(End(True))
        var_1 = obj_2.red_winner()
        
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 'Game with 0 ends')
        
    def test_871(self):
        obj_1 = End(True)
        
        var_0 = obj_1.__str__()
        var_1 = obj_1.__str__()
        
        self.assertEqual(var_0, 'End with Red hammer and 0 stones')
        self.assertEqual(var_1, 'End with Red hammer and 0 stones')
        
    def test_872(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        var_2 = obj_2.red_winner()
        var_3 = obj_2.red_winner()
        var_1 = obj_2.red_winner()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, None)
        
    def test_873(self):
        obj_2 = Game()
        
        var_2 = obj_2.__str__()
        var_1 = obj_2.__str__()
        var_0 = obj_2.__str__()
        var_3 = obj_2.red_winner()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, 'Game with 0 ends')
        self.assertEqual(var_3, None)
        
    def test_874(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        var_4 = obj_2.red_winner()
        obj_2.add_end(End(True))
        var_3 = obj_2.__str__()
        var_1 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, 'End |    1 | Total\n----|------|------\nRed | h  0 |     0\nYel |    0 |     0\n')
        self.assertEqual(var_3, 'Game with 1 ends')
        self.assertEqual(var_4, None)
        
    def test_875(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_3 = obj_1.done()
            var_1 = obj_1.drawn()
            var_0 = obj_1.drawn()
            var_4 = obj_1.red_won()
            obj_1.add_stone(Stone(True, (3.5277874367730355, 4.2655621974937805), 3, False, False))
        
    def test_876(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        var_1 = obj_2.red_winner()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, None)
        
    def test_877(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        var_2 = obj_2.red_winner()
        var_1 = obj_2.red_winner()
        var_3 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, 'Game with 0 ends')
        
    def test_878(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_879(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        var_2 = obj_2.__str__()
        var_1 = obj_2.red_winner()
        var_0 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |    1 | Total\n----|------|------\nRed |    0 |     0\nYel | h  0 |     0\n')
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 'Game with 1 ends')
        
    def test_880(self):
        obj_2 = Game()
        
        var_3 = obj_2.score()
        obj_2.add_end(End(True))
        var_1 = obj_2.red_winner()
        var_2 = obj_2.red_winner()
        var_4 = obj_2.red_winner()
        
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, (0, 0))
        self.assertEqual(var_4, None)
        
    def test_881(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (1.5105753408525562, 5.820222452901641), 5, False, False)
            
            var_2 = obj_0.distance_to_center()
            obj_0.move_out_of_play()
            var_5 = obj_0.move((0.9018671656328969, -1.1631902129939604), 12, True)
            var_3 = obj_0.is_out_of_bounds()
            obj_0.burn()
            obj_0.move_out_of_play()
            var_6 = obj_0.distance_to_center()
        
    def test_882(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            obj_1.add_stone(Stone(True, (0.052377672593809876, -3.497770239183481), -2, True, False))
            var_0 = obj_1.drawn()
        
    def test_883(self):
        with self.assertRaisesRegex(ValueError, "Cannot calculate distance to center for a burned stone."):
            obj_0 = Stone(False, (-5.893997544199932, -7.294594261710705), 2, True, True)
            
            var_0 = obj_0.distance_to_center()
            var_1 = obj_0.move((-5.740773422940903, 4.435217272096597), 11, True)
        
    def test_884(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        var_1 = obj_2.__str__()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, 'Game with 0 ends')
        
    def test_885(self):
        obj_2 = Game()
        
        var_1 = obj_2.score()
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, (0, 0))
        
    def test_886(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (-5.586155041313948, 7.366240419176924), 9, False, True)
            
            obj_0.burn()
            var_2 = obj_0.distance_to_center()
            obj_0.move_out_of_play()
            obj_0.burn()
            obj_0.burn()
            var_6 = obj_0.is_passed_hogline()
            obj_0.burn()
        
    def test_887(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_6 = obj_1.red_won()
            var_2 = obj_1.score()
            obj_1.add_stone(Stone(False, (3.1218796353785994, -4.072693913441782), 11, False, False))
            var_0 = obj_1.drawn()
            var_4 = obj_1.drawn()
            obj_1.add_stone(Stone(False, (-3.2643510595644845, 5.490922825777565), 0, True, True))
            obj_1.add_stone(Stone(False, (-3.8514089397275146, -2.86872178214046), 1, False, False))
        
    def test_888(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (5.380714830842276, 2.133059133195715), 3, False, False)
            
            obj_0.burn()
            var_5 = obj_0.is_in_house()
            obj_0.move_out_of_play()
            var_1 = obj_0.is_passed_hogline()
            var_9 = obj_0.is_guard()
            var_3 = obj_0.is_in_house()
            var_2 = obj_0.move((7.908622613141127, 7.023376003833651), 5, False)
            var_6 = obj_0.distance_to_center()
            var_7 = obj_0.is_in_house()
            var_0 = obj_0.move((-6.3364076502732445, -1.371448516823916), 7, False)
        
    def test_889(self):
        obj_2 = Game()
        
        var_1 = obj_2.score()
        var_0 = obj_2.red_winner()
        obj_2.add_end(End(False))
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, (0, 0))
        
    def test_890(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-6.921064554512686, 6.3265743056074655), 0, True, True)
            
            obj_0.move_out_of_play()
            obj_0.move_out_of_play()
            obj_0.burn()
            var_1 = obj_0.is_out_of_play()
        
    def test_891(self):
        obj_2 = Game()
        
        var_4 = obj_2.red_winner()
        var_1 = obj_2.__str__()
        obj_2.add_end(End(False))
        var_0 = obj_2.score()
        var_3 = obj_2.red_winner()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_3, None)
        self.assertEqual(var_4, None)
        
    def test_892(self):
        obj_2 = Game()
        
        var_3 = obj_2.score()
        var_2 = obj_2.red_winner()
        var_4 = obj_2.__str__()
        var_0 = obj_2.red_winner()
        var_1 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, (0, 0))
        self.assertEqual(var_4, 'Game with 0 ends')
        
    def test_893(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        var_1 = obj_2.score()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, (0, 0))
        
    def test_894(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_4 = obj_1.overlaps_any_stone(Stone(True, (-5.574292439998056, -1.1604849243182027), 0, False, False))
            var_1 = obj_1.score()
            obj_1.add_stone(Stone(True, (-7.758857442383258, 2.8125768756984844), 1, True, False))
            var_2 = obj_1.drawn()
            obj_1.add_stone(Stone(False, (2.3908782746214055, 7.056231099827745), -1, True, True))
        
    def test_895(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-3.2217141560201856, -6.517348749774069), -2, True, False)
            
            var_6 = obj_0.distance_to_center()
            var_2 = obj_0.distance_to_center()
            var_4 = obj_0.distance_to_center()
            var_5 = obj_0.is_guard()
            var_1 = obj_0.is_guard()
            var_0 = obj_0.is_out_of_bounds()
            var_3 = obj_0.distance_to_center()
        
    def test_896(self):
        obj_1 = End(True)
        
        var_0 = obj_1.drawn()
        var_1 = obj_1.drawn()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, True)
        
    def test_897(self):
        obj_1 = End(True)
        
        var_1 = obj_1.red_won()
        var_3 = obj_1.overlaps_any_stone(Stone(True, (0.1437063626558608, -7.775085170163081), 9, True, True))
        var_0 = obj_1.__str__()
        var_2 = obj_1.__str__()
        
        self.assertEqual(var_0, 'End with Red hammer and 0 stones')
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 'End with Red hammer and 0 stones')
        self.assertEqual(var_3, False)
        
    def test_898(self):
        obj_1 = End(False)
        
        var_1 = obj_1.drawn()
        var_4 = obj_1.drawn()
        var_6 = obj_1.__str__()
        var_5 = obj_1.red_won()
        var_0 = obj_1.score()
        var_2 = obj_1.red_won()
        var_3 = obj_1.red_won()
        
        self.assertEqual(var_0, 0)
        self.assertEqual(var_1, True)
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, None)
        self.assertEqual(var_4, True)
        self.assertEqual(var_5, None)
        self.assertEqual(var_6, 'End with Yellow hammer and 0 stones')
        
    def test_899(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(False, (-4.721748216246885, 5.6230539787600335), 8, True, True)
            
            var_3 = obj_0.is_guard()
            var_2 = obj_0.is_in_house()
            var_1 = obj_0.is_passed_hogline()
            var_4 = obj_0.move((-6.142680976161225, 7.988661522546968), 7, True)
            var_0 = obj_0.distance_to_center()
        
    def test_900(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_1 = obj_1.__str__()
            var_0 = obj_1.done()
            obj_1.add_stone(Stone(True, (2.3927041763591443, 1.3121974255152278), 0, True, False))
        
    def test_901(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-7.14231841272133, -1.0691386658507795), 0, True, True)
            
            var_0 = obj_0.distance_to_center()
        
    def test_902(self):
        obj_2 = Game()
        
        var_1 = obj_2.red_winner()
        obj_2.add_end(End(False))
        
        self.assertEqual(var_1, None)
        
    def test_903(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (4.209625406993947, 2.4502863215394015), -2, False, False)
            
            var_0 = obj_0.__str__()
        
    def test_904(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (-0.23868555367147515, 4.625708429518436), 10, True, True)
            
            obj_0.move_out_of_play()
            var_8 = obj_0.is_in_house()
            var_6 = obj_0.distance_to_center()
            var_1 = obj_0.distance_to_center()
            var_7 = obj_0.is_in_house()
            var_3 = obj_0.is_out_of_play()
            var_5 = obj_0.move((-6.208983658201978, 7.390296690251521), -2, False)
            obj_0.burn()
            var_2 = obj_0.is_in_house()
        
    def test_905(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (2.943609396687, 1.2915381648197535), -1, True, True)
            
            obj_0.burn()
            var_0 = obj_0.is_passed_hogline()
            var_2 = obj_0.is_in_house()
            var_4 = obj_0.is_out_of_bounds()
            obj_0.burn()
        
    def test_906(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(False)
            
            var_4 = obj_1.score()
            var_2 = obj_1.__str__()
            obj_1.add_stone(Stone(True, (2.6632469037939757, -7.522068930887839), 4, False, False))
            var_0 = obj_1.done()
            var_5 = obj_1.drawn()
            var_3 = obj_1.done()
        
    def test_907(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        
    def test_908(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        var_2 = obj_2.score()
        var_3 = obj_2.score()
        var_1 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_2, (0, 0))
        self.assertEqual(var_3, (0, 0))
        
    def test_909(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (4.062229755390156, 0.9553013818468195), 8, False, False)
            
            var_2 = obj_0.distance_to_center()
            var_3 = obj_0.is_out_of_bounds()
            var_4 = obj_0.is_passed_hogline()
            var_6 = obj_0.__str__()
            var_0 = obj_0.is_guard()
            var_1 = obj_0.is_passed_hogline()
            var_5 = obj_0.is_out_of_bounds()
        
    def test_910(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (6.3298382330189416, 3.628100246143248), -1, True, False)
            
            var_0 = obj_0.is_out_of_play()
            var_1 = obj_0.is_passed_hogline()
        
    def test_911(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        
    def test_912(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        
    def test_913(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (2.8196899267877793, -1.554054940775984), -2, True, False)
            
            var_4 = obj_0.is_in_house()
            obj_0.burn()
            var_5 = obj_0.is_out_of_play()
            var_0 = obj_0.is_guard()
            var_1 = obj_0.is_out_of_bounds()
            obj_0.burn()
        
    def test_914(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_0 = obj_1.red_won()
            obj_1.add_stone(Stone(True, (2.0577366601386107, 4.09945230837762), 0, True, True))
            var_4 = obj_1.done()
            var_3 = obj_1.done()
            var_1 = obj_1.done()
        
    def test_915(self):
        obj_0 = Stone(False, (-0.4599282809477039, 3.445581585867844), 1, False, False)
        
        var_1 = obj_0.__str__()
        var_3 = obj_0.is_guard()
        var_0 = obj_0.__str__()
        var_4 = obj_0.__str__()
        var_2 = obj_0.is_out_of_bounds()
        
        self.assertEqual(var_0, 'Yellow stone at (-0.46, 3.45), round 1, active')
        self.assertEqual(var_1, 'Yellow stone at (-0.46, 3.45), round 1, active')
        self.assertEqual(var_2, False)
        self.assertEqual(var_3, True)
        self.assertEqual(var_4, 'Yellow stone at (-0.46, 3.45), round 1, active')
        
    def test_916(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (5.875704016688269, 3.3809651681164965), -1, False, False)
            
            var_0 = obj_0.is_passed_hogline()
            var_1 = obj_0.is_passed_hogline()
        
    def test_917(self):
        obj_2 = Game()
        
        var_0 = obj_2.red_winner()
        var_1 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, None)
        
    def test_918(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (-3.980080726801452, -7.425984640016136), 7, False, False)
            
            var_3 = obj_0.distance_to_center()
            var_2 = obj_0.is_guard()
            var_5 = obj_0.distance_to_center()
            var_0 = obj_0.is_in_house()
            var_1 = obj_0.distance_to_center()
            var_4 = obj_0.is_passed_hogline()
        
    def test_919(self):
        with self.assertRaisesRegex(ValueError, "Stone's hammer status does not match the end's hammer status."):
            obj_1 = End(False)
            
            var_1 = obj_1.done()
            var_3 = obj_1.drawn()
            obj_1.add_stone(Stone(True, (-2.133186100795177, -5.7468596646996435), 7, True, True))
            var_0 = obj_1.done()
        
    def test_920(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(False, (-4.919353551201592, 0.6651818258909561), 10, False, False)
            
            var_8 = obj_0.is_in_house()
            var_2 = obj_0.distance_to_center()
            var_6 = obj_0.__str__()
            var_1 = obj_0.distance_to_center()
            var_9 = obj_0.is_in_house()
            obj_0.move_out_of_play()
            var_3 = obj_0.move((0.14230367174772773, -5.488937616649226), -1, True)
            var_4 = obj_0.is_out_of_play()
            var_0 = obj_0.__str__()
            var_5 = obj_0.is_out_of_play()
        
    def test_921(self):
        obj_1 = End(True)
        
        var_1 = obj_1.overlaps_any_stone(Stone(False, (6.573093829923751, -7.516628184530914), 5, False, True))
        var_0 = obj_1.overlaps_any_stone(Stone(False, (-2.1456659583705626, 0.2799320454894385), 10, True, False))
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, False)
        
    def test_922(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (-0.4998596678207221, 0.6926229906406736), 6, False, True)
            
            var_0 = obj_0.is_passed_hogline()
            obj_0.move_out_of_play()
            var_3 = obj_0.move((7.155576278596616, 6.725100200767708), 8, False)
            var_2 = obj_0.move((-2.0136270518054697, 2.726784034691663), 11, True)
            var_5 = obj_0.distance_to_center()
            var_6 = obj_0.is_passed_hogline()
            var_1 = obj_0.is_out_of_bounds()
            var_4 = obj_0.is_out_of_play()
        
    def test_923(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_0, 'Game with 0 ends')
        
    def test_924(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_4 = obj_1.score()
            var_3 = obj_1.drawn()
            var_1 = obj_1.overlaps_any_stone(Stone(True, (7.856703581137619, 2.9801962248835903), -2, False, True))
            obj_1.add_stone(Stone(False, (6.945273102192129, 0.963502293781966), 12, True, True))
            var_2 = obj_1.done()
        
    def test_925(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (-2.514670297526436, -3.727416905182224), 8, True, True)
            
            var_2 = obj_0.is_out_of_play()
            obj_0.move_out_of_play()
            obj_0.burn()
        
    def test_926(self):
        obj_0 = Stone(False, (-0.7115143266939814, -5.408426855384105), 8, False, False)
        
        obj_0.move_out_of_play()
        var_4 = obj_0.is_out_of_bounds()
        var_0 = obj_0.is_in_house()
        var_2 = obj_0.is_out_of_play()
        var_6 = obj_0.is_in_house()
        var_3 = obj_0.is_out_of_bounds()
        var_5 = obj_0.is_out_of_bounds()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_2, True)
        self.assertEqual(var_3, False)
        self.assertEqual(var_4, False)
        self.assertEqual(var_5, False)
        self.assertEqual(var_6, False)
        
    def test_927(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-1.1415179542663552, -0.18331033137083175), 11, False, True)
            
            var_3 = obj_0.is_out_of_play()
            obj_0.move_out_of_play()
            obj_0.burn()
            var_1 = obj_0.is_passed_hogline()
            var_2 = obj_0.__str__()
            var_7 = obj_0.move((-0.8051502504395796, -5.941454890565229), 10, False)
            var_5 = obj_0.is_in_house()
            var_8 = obj_0.is_out_of_bounds()
            var_6 = obj_0.is_out_of_bounds()
        
    def test_928(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (7.189420197660738, -7.017598232422667), 3, False, True)
            
            var_4 = obj_0.is_passed_hogline()
            var_2 = obj_0.is_in_house()
            obj_0.move_out_of_play()
            var_5 = obj_0.distance_to_center()
            var_7 = obj_0.distance_to_center()
            var_3 = obj_0.__str__()
            var_1 = obj_0.is_out_of_bounds()
            var_0 = obj_0.move((7.662510400243466, -0.27702186935508166), 2, True)
        
    def test_929(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (5.219728294832997, 5.89461325247559), 11, True, True)
            
            var_0 = obj_0.is_out_of_bounds()
            obj_0.move_out_of_play()
            var_5 = obj_0.distance_to_center()
            obj_0.move_out_of_play()
            var_8 = obj_0.distance_to_center()
            obj_0.move_out_of_play()
            var_6 = obj_0.is_out_of_play()
            var_7 = obj_0.is_in_house()
            obj_0.burn()
        
    def test_930(self):
        obj_2 = Game()
        
        obj_2.add_end(End(True))
        var_1 = obj_2.__str__()
        var_2 = obj_2.__str__()
        var_4 = obj_2.score()
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'Game with 1 ends')
        self.assertEqual(var_2, 'Game with 1 ends')
        self.assertEqual(var_4, (0, 0))
        
    def test_931(self):
        obj_0 = Stone(False, (0.42438644707929996, -3.101637190920826), 2, False, False)
        
        var_1 = obj_0.is_in_house()
        var_3 = obj_0.move((-2.6054743255543897, -2.4172015171142576), 4, False)
        var_0 = obj_0.distance_to_center()
        var_7 = obj_0.is_out_of_play()
        var_2 = obj_0.is_out_of_play()
        var_5 = obj_0.distance_to_center()
        var_8 = obj_0.is_passed_hogline()
        var_4 = obj_0.is_passed_hogline()
        var_6 = obj_0.move((-1.3865709400857682, -4.823871830520201), 4, False)
        
        self.assertEqual(var_0, 5.934199610641465)
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, False)
        self.assertEqual(var_3, True)
        self.assertEqual(var_4, True)
        self.assertEqual(var_5, 5.934199610641465)
        self.assertEqual(var_6, True)
        self.assertEqual(var_7, False)
        self.assertEqual(var_8, True)
        
    def test_932(self):
        obj_2 = Game()
        
        var_1 = obj_2.score()
        var_2 = obj_2.__str__()
        obj_2.add_end(End(True))
        var_0 = obj_2.red_winner()
        obj_2.add_end(End(True))
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'Game with 0 ends')
        
    def test_933(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-7.470077071879727, -6.702558583214747), -1, False, True)
            
            var_2 = obj_0.is_passed_hogline()
            var_7 = obj_0.is_guard()
            var_1 = obj_0.is_in_house()
            var_5 = obj_0.is_out_of_play()
            var_3 = obj_0.is_in_house()
            var_0 = obj_0.is_guard()
            var_8 = obj_0.is_passed_hogline()
            obj_0.move_out_of_play()
            var_6 = obj_0.move((-0.04597418050370017, -4.409438701295468), 5, True)
        
    def test_934(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (-0.9866884342529563, -1.0110550263814684), 1, True, True)
            
            var_1 = obj_0.is_out_of_play()
            var_3 = obj_0.is_passed_hogline()
            obj_0.burn()
            var_0 = obj_0.__str__()
            var_2 = obj_0.move((-6.51606687819085, 7.254929694790183), 1, False)
        
    def test_935(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(True, (-1.9558800408690917, -0.3907439322265489), 5, True, False)
            
            var_4 = obj_0.move((0.3019978871291453, -1.4681870636782524), 8, True)
            var_2 = obj_0.distance_to_center()
            obj_0.move_out_of_play()
            var_5 = obj_0.move((1.4636358903557927, -4.329133864906455), 0, True)
            var_7 = obj_0.is_passed_hogline()
            var_0 = obj_0.is_guard()
            var_1 = obj_0.move((-7.330191139181387, -6.637095185867569), 2, True)
            var_8 = obj_0.__str__()
            var_6 = obj_0.is_out_of_play()
        
    def test_936(self):
        with self.assertRaisesRegex(ValueError, "Cannot calculate distance to center for a burned stone."):
            obj_0 = Stone(True, (-0.9134811122482382, -3.3904783356238646), 1, False, True)
            
            var_0 = obj_0.is_in_house()
            var_1 = obj_0.distance_to_center()
            var_2 = obj_0.is_in_house()
        
    def test_937(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
            obj_2 = Game()
            
            var_0 = obj_2.__str__()
            obj_2.add_end(End(True))
            obj_2.add_end(End(False))
        
    def test_938(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_5 = obj_1.__str__()
            var_0 = obj_1.__str__()
            obj_1.add_stone(Stone(True, (1.7680720296336485, -7.620223964646252), 9, True, False))
            var_6 = obj_1.red_won()
            var_2 = obj_1.done()
            var_1 = obj_1.done()
            var_4 = obj_1.done()
        
    def test_939(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (-7.539256274881563, -5.949290208946605), 5, False, True)
            
            obj_0.move_out_of_play()
            var_2 = obj_0.is_out_of_bounds()
            obj_0.move_out_of_play()
            var_3 = obj_0.is_out_of_play()
        
    def test_940(self):
        obj_1 = End(True)
        
        var_1 = obj_1.__str__()
        var_0 = obj_1.red_won()
        var_2 = obj_1.red_won()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'End with Red hammer and 0 stones')
        self.assertEqual(var_2, None)
        
    def test_941(self):
        with self.assertRaisesRegex(ValueError, "Cannot calculate distance to center for a burned stone."):
            obj_0 = Stone(False, (-7.399306710106218, 5.9095308422597395), 6, False, True)
            
            var_1 = obj_0.distance_to_center()
            obj_0.burn()
            var_5 = obj_0.__str__()
            var_3 = obj_0.__str__()
            var_8 = obj_0.is_in_house()
            var_7 = obj_0.is_out_of_play()
            obj_0.burn()
            var_0 = obj_0.is_guard()
            var_4 = obj_0.__str__()
        
    def test_942(self):
        obj_2 = Game()
        
        var_1 = obj_2.score()
        var_3 = obj_2.__str__()
        var_0 = obj_2.score()
        var_4 = obj_2.score()
        var_2 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_3, 'Game with 0 ends')
        self.assertEqual(var_4, (0, 0))
        
    def test_943(self):
        obj_2 = Game()
        
        var_1 = obj_2.display_scoreboard()
        obj_2.add_end(End(False))
        var_0 = obj_2.red_winner()
        var_3 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_3, 'End |    1 | Total\n----|------|------\nRed |    0 |     0\nYel | h  0 |     0\n')
        
    def test_944(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (-7.359041412735095, -2.6177927556777956), 2, True, True)
            
            obj_0.move_out_of_play()
            var_4 = obj_0.is_out_of_play()
            var_1 = obj_0.is_out_of_play()
            var_0 = obj_0.is_out_of_play()
            var_2 = obj_0.is_passed_hogline()
        
    def test_945(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (3.387749478466487, -6.1352535168177695), 12, True, True)
            
            obj_0.move_out_of_play()
            var_1 = obj_0.is_out_of_play()
            obj_0.burn()
            var_2 = obj_0.is_passed_hogline()
        
    def test_946(self):
        obj_2 = Game()
        
        var_1 = obj_2.red_winner()
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, None)
        
    def test_947(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        var_2 = obj_2.red_winner()
        var_1 = obj_2.red_winner()
        var_3 = obj_2.score()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, (0, 0))
        
    def test_948(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (-7.874010604145905, 0.2237176150851088), 7, False, True)
            
            obj_0.move_out_of_play()
            var_0 = obj_0.is_guard()
            var_2 = obj_0.move((-7.26755271778875, 7.682413362906825), 5, False)
        
    def test_949(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-0.5325544299755993, 0.023081545765732514), 0, False, False)
            
            var_2 = obj_0.is_out_of_bounds()
            var_3 = obj_0.distance_to_center()
            obj_0.move_out_of_play()
            var_5 = obj_0.is_in_house()
            var_0 = obj_0.is_in_house()
            var_7 = obj_0.is_in_house()
            var_6 = obj_0.move((0.6682550294297513, -4.15202970879897), 3, True)
            var_4 = obj_0.is_guard()
            var_1 = obj_0.__str__()
            var_9 = obj_0.move((-2.1933633991327515, 1.0155922387517702), 12, True)
        
    def test_950(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            obj_1.add_stone(Stone(False, (-4.247974330801775, -4.399791523407677), 3, True, False))
            var_0 = obj_1.overlaps_any_stone(Stone(False, (2.244040959863977, 0.4455550404830504), 11, True, False))
            var_3 = obj_1.red_won()
            obj_1.add_stone(Stone(False, (2.9036160252946033, 6.087415800428667), 0, False, False))
            var_4 = obj_1.drawn()
            var_5 = obj_1.score()
        
    def test_951(self):
        obj_2 = Game()
        
        var_1 = obj_2.__str__()
        var_3 = obj_2.__str__()
        obj_2.add_end(End(False))
        var_4 = obj_2.__str__()
        var_2 = obj_2.__str__()
        
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, 'Game with 1 ends')
        self.assertEqual(var_3, 'Game with 0 ends')
        self.assertEqual(var_4, 'Game with 1 ends')
        
    def test_952(self):
        with self.assertRaisesRegex(ValueError, "The first stone must be thrown by the team without the hammer."):
            obj_1 = End(True)
            
            var_3 = obj_1.score()
            obj_1.add_stone(Stone(True, (-5.219104698037324, 6.922904517354132), 1, True, True))
            var_0 = obj_1.drawn()
            var_1 = obj_1.score()
        
    def test_953(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        
    def test_954(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (-0.5856769838895595, 7.642243095823796), 8, False, False)
            
            var_1 = obj_0.distance_to_center()
            obj_0.move_out_of_play()
        
    def test_955(self):
        obj_1 = End(False)
        
        var_1 = obj_1.__str__()
        var_0 = obj_1.done()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, 'End with Yellow hammer and 0 stones')
        
    def test_956(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-4.663372444343464, 7.6446510385063515), 11, False, False)
            
            var_3 = obj_0.is_out_of_play()
            var_2 = obj_0.distance_to_center()
            obj_0.burn()
            obj_0.burn()
            var_0 = obj_0.is_passed_hogline()
            var_6 = obj_0.__str__()
            var_4 = obj_0.is_passed_hogline()
            obj_0.burn()
        
    def test_957(self):
        obj_0 = Stone(False, (0.07449730482512074, 0.31166247678064174), 6, False, False)
        
        var_0 = obj_0.is_in_house()
        var_4 = obj_0.distance_to_center()
        var_3 = obj_0.is_passed_hogline()
        var_2 = obj_0.is_guard()
        var_1 = obj_0.is_in_house()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, True)
        self.assertEqual(var_2, False)
        self.assertEqual(var_3, True)
        self.assertEqual(var_4, 0.3204424251862587)
        
    def test_958(self):
        obj_0 = Stone(True, (-2.4671953175541788, -5.77151116311734), 8, False, False)
        
        var_2 = obj_0.move((1.7601698654761702, 6.429293357753627), 5, False)
        var_3 = obj_0.is_guard()
        var_4 = obj_0.is_in_house()
        var_0 = obj_0.is_out_of_play()
        var_1 = obj_0.distance_to_center()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, 0.9656927075766091)
        self.assertEqual(var_2, True)
        self.assertEqual(var_3, False)
        self.assertEqual(var_4, True)
        
    def test_959(self):
        obj_1 = End(True)
        
        var_3 = obj_1.done()
        var_6 = obj_1.__str__()
        var_0 = obj_1.red_won()
        var_4 = obj_1.__str__()
        var_1 = obj_1.__str__()
        var_2 = obj_1.__str__()
        var_5 = obj_1.__str__()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, 'End with Red hammer and 0 stones')
        self.assertEqual(var_2, 'End with Red hammer and 0 stones')
        self.assertEqual(var_3, False)
        self.assertEqual(var_4, 'End with Red hammer and 0 stones')
        self.assertEqual(var_5, 'End with Red hammer and 0 stones')
        self.assertEqual(var_6, 'End with Red hammer and 0 stones')
        
    def test_960(self):
        obj_2 = Game()
        
        var_3 = obj_2.score()
        obj_2.add_end(End(True))
        var_0 = obj_2.score()
        var_2 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_2, (0, 0))
        self.assertEqual(var_3, (0, 0))
        
    def test_961(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_2 = obj_1.score()
            var_4 = obj_1.__str__()
            var_1 = obj_1.overlaps_any_stone(Stone(False, (0.9451873594606592, -7.732831454967489), 3, False, False))
            var_3 = obj_1.score()
            var_6 = obj_1.overlaps_any_stone(Stone(True, (-3.753149277480807, 6.200852299099747), 12, True, False))
            var_5 = obj_1.overlaps_any_stone(Stone(False, (3.377207605899681, -1.5430857464134355), 8, False, True))
            var_0 = obj_1.red_won()
        
    def test_962(self):
        obj_2 = Game()
        
        var_0 = obj_2.__str__()
        var_1 = obj_2.red_winner()
        var_2 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_963(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_6 = obj_1.drawn()
            var_5 = obj_1.drawn()
            obj_1.add_stone(Stone(False, (5.167388574665269, 3.902047272076352), -1, True, True))
            obj_1.add_stone(Stone(False, (1.306665293224805, 0.5509327670434523), 12, False, False))
            var_4 = obj_1.overlaps_any_stone(Stone(False, (0.5665860246127341, -5.655833565810861), 7, True, True))
            var_2 = obj_1.red_won()
            var_1 = obj_1.__str__()
        
    def test_964(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
            obj_2 = Game()
            
            obj_2.add_end(End(True))
            obj_2.add_end(End(False))
        
    def test_965(self):
        with self.assertRaisesRegex(ValueError, "Cannot move an out-of-play stone."):
            obj_0 = Stone(False, (0.7610626330179979, 2.622024195308766), 9, False, False)
            
            obj_0.burn()
            var_2 = obj_0.is_out_of_bounds()
            var_3 = obj_0.move((5.538474449254897, -4.504776532164193), 0, False)
            var_0 = obj_0.is_out_of_bounds()
        
    def test_966(self):
        obj_2 = Game()
        
        var_1 = obj_2.score()
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, (0, 0))
        
    def test_967(self):
        obj_0 = Stone(False, (-5.181450203069865, 3.4808723563983825), 8, True, True)
        
        var_2 = obj_0.is_passed_hogline()
        var_0 = obj_0.is_in_house()
        var_1 = obj_0.is_passed_hogline()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, False)
        self.assertEqual(var_2, False)
        
    def test_968(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(True)
            
            var_1 = obj_1.overlaps_any_stone(Stone(True, (2.4058561785841235, 6.595183313364817), 0, False, False))
            obj_1.add_stone(Stone(True, (-2.739595331997007, -5.9873933165481485), -1, False, False))
            var_5 = obj_1.__str__()
            var_4 = obj_1.red_won()
            var_3 = obj_1.drawn()
            obj_1.add_stone(Stone(True, (-7.166971954619516, -6.156694815802975), 6, True, True))
        
    def test_969(self):
        obj_2 = Game()
        
        obj_2.add_end(End(False))
        var_1 = obj_2.red_winner()
        
        self.assertEqual(var_1, None)
        
    def test_970(self):
        obj_2 = Game()
        
        var_1 = obj_2.score()
        var_0 = obj_2.__str__()
        var_2 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, (0, 0))
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_971(self):
        obj_2 = Game()
        
        var_1 = obj_2.red_winner()
        var_2 = obj_2.display_scoreboard()
        var_0 = obj_2.__str__()
        
        self.assertEqual(var_0, 'Game with 0 ends')
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_972(self):
        obj_0 = Stone(False, (-1.2866033043669898, -1.9668072131117516), 1, True, False)
        
        var_3 = obj_0.is_out_of_bounds()
        var_1 = obj_0.is_out_of_bounds()
        var_0 = obj_0.is_out_of_bounds()
        obj_0.move_out_of_play()
        var_4 = obj_0.is_passed_hogline()
        
        self.assertEqual(var_0, False)
        self.assertEqual(var_1, False)
        self.assertEqual(var_3, False)
        self.assertEqual(var_4, False)
        
    def test_973(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            obj_1.add_stone(Stone(True, (1.7959329943554057, 5.030063361645057), 12, False, True))
            var_2 = obj_1.__str__()
            obj_1.add_stone(Stone(True, (0.4543949150400799, -2.9669399382943773), -1, False, True))
            obj_1.add_stone(Stone(True, (6.833053168971411, 6.883608695112374), -1, False, False))
            var_1 = obj_1.score()
        
    def test_974(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(False, (-7.658562312380692, -7.998805165077746), 11, False, False)
            
            obj_0.burn()
            obj_0.move_out_of_play()
            var_1 = obj_0.move((6.9370301291213785, 3.7312062889967006), 12, False)
        
    def test_975(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_1 = End(False)
            
            var_1 = obj_1.overlaps_any_stone(Stone(False, (0.5497134012003908, -1.4662616229516203), 6, False, True))
            var_6 = obj_1.__str__()
            var_5 = obj_1.__str__()
            var_0 = obj_1.drawn()
            var_2 = obj_1.score()
            var_4 = obj_1.score()
            var_3 = obj_1.overlaps_any_stone(Stone(False, (-5.3922124283603505, 5.347942683739417), 11, True, True))
        
    def test_976(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (-1.8299037496852915, -1.3861017694073094), 9, True, True)
            
            var_5 = obj_0.is_out_of_bounds()
            var_2 = obj_0.is_out_of_play()
            var_0 = obj_0.is_guard()
            var_3 = obj_0.is_out_of_play()
            obj_0.move_out_of_play()
            var_1 = obj_0.is_out_of_play()
        
    def test_977(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        var_1 = obj_2.__str__()
        var_2 = obj_2.__str__()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, 'Game with 0 ends')
        self.assertEqual(var_2, 'Game with 0 ends')
        
    def test_978(self):
        obj_1 = End(True)
        
        var_0 = obj_1.red_won()
        var_1 = obj_1.red_won()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, None)
        
    def test_979(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-1.6736970775104005, 0.3413941613686369), -1, False, False)
            
            var_5 = obj_0.is_in_house()
            var_2 = obj_0.is_out_of_play()
            var_3 = obj_0.is_guard()
            obj_0.burn()
            var_1 = obj_0.is_out_of_bounds()
            obj_0.burn()
        
    def test_980(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_1 = End(True)
            
            var_0 = obj_1.done()
            obj_1.add_stone(Stone(True, (3.5771733862332376, 0.8091833753756035), 5, True, False))
        
    def test_981(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (4.113068944419901, -3.5876073267889588), 2, True, True)
            
            var_0 = obj_0.is_out_of_bounds()
            obj_0.burn()
            var_3 = obj_0.is_passed_hogline()
            var_1 = obj_0.move((-2.2781095699714573, -2.9103490235759253), 10, True)
        
    def test_982(self):
        obj_2 = Game()
        
        var_1 = obj_2.display_scoreboard()
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_983(self):
        obj_2 = Game()
        
        var_0 = obj_2.display_scoreboard()
        var_1 = obj_2.red_winner()
        var_2 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 'End |  | Total\n----|------\nRed |  |     0\nYel |  |     0\n')
        
    def test_984(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
            obj_2 = Game()
            
            obj_2.add_end(End(True))
            var_0 = obj_2.display_scoreboard()
            obj_2.add_end(End(True))
            var_1 = obj_2.red_winner()
            obj_2.add_end(End(False))
        
    def test_985(self):
        obj_1 = End(False)
        
        var_1 = obj_1.red_won()
        var_0 = obj_1.drawn()
        var_3 = obj_1.drawn()
        var_2 = obj_1.drawn()
        
        self.assertEqual(var_0, True)
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, True)
        self.assertEqual(var_3, True)
        
    def test_986(self):
        with self.assertRaisesRegex(ValueError, "The first stone must be thrown by the team without the hammer."):
            obj_1 = End(False)
            
            var_6 = obj_1.red_won()
            var_1 = obj_1.red_won()
            obj_1.add_stone(Stone(False, (7.237432435196768, 5.8017227837735525), 9, False, True))
            obj_1.add_stone(Stone(True, (-6.738467203139145, 2.3289713861489787), 4, True, True))
            var_2 = obj_1.drawn()
            var_5 = obj_1.done()
            var_0 = obj_1.red_won()
        
    def test_987(self):
        obj_2 = Game()
        
        var_0 = obj_2.score()
        var_2 = obj_2.__str__()
        var_1 = obj_2.red_winner()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, None)
        self.assertEqual(var_2, 'Game with 0 ends')
        
    def test_988(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(False, (-2.061208162850651, 2.4463112674464558), 8, False, False)
            
            var_1 = obj_0.distance_to_center()
            var_2 = obj_0.is_in_house()
            var_4 = obj_0.is_out_of_bounds()
            var_3 = obj_0.move((-6.243362862583242, 2.925185561897548), 9, False)
            var_8 = obj_0.is_passed_hogline()
            var_6 = obj_0.is_out_of_play()
            obj_0.move_out_of_play()
            var_0 = obj_0.is_out_of_play()
            obj_0.move_out_of_play()
        
    def test_989(self):
        obj_2 = Game()
        
        var_1 = obj_2.__str__()
        var_0 = obj_2.score()
        
        self.assertEqual(var_0, (0, 0))
        self.assertEqual(var_1, 'Game with 0 ends')
        
    def test_990(self):
        obj_1 = End(True)
        
        var_0 = obj_1.score()
        
        self.assertEqual(var_0, 0)
        
    def test_991(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
            obj_2 = Game()
            
            var_2 = obj_2.display_scoreboard()
            obj_2.add_end(End(True))
            obj_2.add_end(End(False))
        
    def test_992(self):
        obj_2 = Game()
        
        obj_2.add_end(End(True))
        var_0 = obj_2.display_scoreboard()
        var_2 = obj_2.display_scoreboard()
        
        self.assertEqual(var_0, 'End |    1 | Total\n----|------|------\nRed | h  0 |     0\nYel |    0 |     0\n')
        self.assertEqual(var_2, 'End |    1 | Total\n----|------|------\nRed | h  0 |     0\nYel |    0 |     0\n')
        
    def test_993(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
            obj_0 = Stone(True, (4.08661245131321, -2.692353417753308), 6, False, False)
            
            var_4 = obj_0.is_in_house()
            var_3 = obj_0.move((-5.115894367703456, 1.2235736697268411), 0, False)
            obj_0.burn()
            var_2 = obj_0.is_out_of_play()
            var_5 = obj_0.is_in_house()
            var_0 = obj_0.__str__()
            var_1 = obj_0.move((-7.2653647714617655, 7.0324727836277106), 1, False)
        
    def test_994(self):
        with self.assertRaisesRegex(ValueError, "Stone's round does not match the expected round based on the number of stones already placed."):
            obj_1 = End(True)
            
            var_3 = obj_1.red_won()
            obj_1.add_stone(Stone(False, (4.22953269429633, -6.645663184483869), 2, True, True))
            var_1 = obj_1.__str__()
            var_0 = obj_1.__str__()
        
    def test_995(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
            obj_0 = Stone(True, (-3.3223198328447108, 7.491465000604961), -2, True, True)
            
            var_0 = obj_0.distance_to_center()
            var_3 = obj_0.distance_to_center()
            var_5 = obj_0.distance_to_center()
            var_4 = obj_0.__str__()
            var_1 = obj_0.move((6.8499509513847165, 4.674935281105025), 8, True)
            var_6 = obj_0.__str__()
            var_2 = obj_0.is_out_of_play()
        
    def test_996(self):
        obj_1 = End(False)
        
        var_0 = obj_1.done()
        
        self.assertEqual(var_0, False)
        
    def test_997(self):
        obj_2 = Game()
        
        var_1 = obj_2.score()
        var_0 = obj_2.red_winner()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, (0, 0))
        
    def test_998(self):
        with self.assertRaisesRegex(ValueError, "Stone is already out of play."):
            obj_0 = Stone(True, (-3.2773016039464373, 5.840443447463107), 2, True, True)
            
            var_2 = obj_0.is_passed_hogline()
            obj_0.burn()
            obj_0.move_out_of_play()
            var_5 = obj_0.is_passed_hogline()
            var_4 = obj_0.is_passed_hogline()
            var_1 = obj_0.is_passed_hogline()
        
    def test_999(self):
        obj_1 = End(True)
        
        var_3 = obj_1.drawn()
        var_0 = obj_1.red_won()
        var_1 = obj_1.drawn()
        var_4 = obj_1.__str__()
        var_2 = obj_1.red_won()
        
        self.assertEqual(var_0, None)
        self.assertEqual(var_1, True)
        self.assertEqual(var_2, None)
        self.assertEqual(var_3, True)
        self.assertEqual(var_4, 'End with Red hammer and 0 stones')
        