import unittest
import member
import equipment
import reservation
import gym

class TestGym(unittest.TestCase):

    
    @classmethod
    def setUpClass(cls):
        # called once at beginning 
        print('setUpClass()')

        # create gym instance 
        cls.gym = gym.Gym()

        # initialize gym member instances (member ID's 0-7)
        cls.connor = member.Member('Connor')
        cls.vanessa = member.Member('Vanessa')
        cls.tina = member.Member('Tina')
        cls.joe = member.Member('Joe')
        cls.seth = member.Member('Seth')
        cls.scott = member.Member('Scott')
        cls.mary = member.Member('Mary')
        cls.max = member.Member('Max')

        # initialize gym equipment instances 
        cls.benchPress = equipment.Equipment('Bench Press', 'Weight Training')
        cls.inclineBench = equipment.Equipment('Incline Bench', 'Weight Training')
        cls.declineBench = equipment.Equipment('Decline Bench', 'Weight Training')
        cls.kettleBells = equipment.Equipment('Kettle Bells', 'Weight Training')
        cls.treadmill1 = equipment.Equipment('Treadmill', 'Cardio')
        cls.treadmill2 = equipment.Equipment('Treadmill', 'Cardio')
        cls.rowMachine = equipment.Equipment('Row Machine', 'Cardio')
        cls.resistanceBands = equipment.Equipment('Resistance Bands', 'Stretching')
        cls.wobbleBoard = equipment.Equipment('Wobble Board', 'Balance')

        # add member instances to gym member set 
        cls.gym.add_member(cls.connor)
        cls.gym.add_member(cls.vanessa)
        cls.gym.add_member(cls.tina)
        cls.gym.add_member(cls.joe)
        cls.gym.add_member(cls.seth)
        cls.gym.add_member(cls.scott)
        cls.gym.add_member(cls.mary)
        cls.gym.add_member(cls.max)

        # add equipment instances to gym equipment set 
        cls.gym.add_equipment(cls.benchPress)
        cls.gym.add_equipment(cls.inclineBench)
        cls.gym.add_equipment(cls.declineBench)
        cls.gym.add_equipment(cls.kettleBells)
        cls.gym.add_equipment(cls.treadmill1)
        cls.gym.add_equipment(cls.treadmill2)
        cls.gym.add_equipment(cls.rowMachine)
        cls.gym.add_equipment(cls.resistanceBands)
        cls.gym.add_equipment(cls.wobbleBoard)

    @classmethod
    def tearDownClass(cls):
        # called once at the end 
        print('tearDownClass()')
    
    def setUp(self):
        # called before each test
        print('setUp()')

    def tearDown(self):
        # called after each test
        print('tearDown()')

    #------------------------------------------------------------------------------------------------------------

    def test_reservation_one(self):
        # ensure the gym has no current reservations 
        reservations = self.gym.all_reservations()
        self.assertEqual(len(reservations), 0)

        # reserve bench press for Joe 
        jr = self.gym.make_reservation(self.joe, self.benchPress, '11:00am-12:00pm')

        # ensure the gym and Joe have the same number of reservations
        totalReservations = self.gym.all_reservations()
        joeReservations = self.joe.get_reservations() # test of member instance method 
        self.assertEqual(len(totalReservations), len(joeReservations))

        # reserve another (different) piece of equipment for Joe
        jr_2 = self.gym.make_reservation(self.joe, self.treadmill1, '12:00pm-12:30pm')

        # ensure Joe has two current reservations (using gym instance method)
        joeReservations = self.gym.get_reservations(self.joe)
        self.assertEqual(len(joeReservations), 2)

        # reserve wobble board for Vanessa 
        vr = self.gym.make_reservation(self.vanessa, self.wobbleBoard, '2:30pm-3:00pm')

        # ensure Vanessa only has one current reservation
        vanessaReservations = self.gym.get_reservations(self.vanessa)
        self.assertEqual(len(vanessaReservations), 1)

        # ensure Vanessa and the entire gym have a different number of reservations 
        totalReservations = self.gym.all_reservations()
        self.assertNotEqual(len(totalReservations), len(vanessaReservations))

    def test_reservation_two(self):
        # reserve the incline bench for Max
        mr = self.gym.make_reservation(self.max, self.inclineBench, '3:15pm-4:00pm')

        # ensure Max only has one current reservation
        maxReservations = self.gym.get_reservations(self.max)
        self.assertEqual(len(maxReservations), 1)

        # attempt to reserve the same bench for Scott (should return False, bench is 
        # already reserved by Max)
        sr = self.gym.make_reservation(self.scott, self.inclineBench, '3:30pm-4:15pm')
        self.assertFalse(sr)

        # ensure Scott can reserve the decline bench (not currently reserved, should return True)
        sr = self.gym.make_reservation(self.scott, self.declineBench, '3:30pm-4:15pm')
        self.assertTrue(sr)

        # after reserving only one piece of available equipment, ensure Scott has just one
        # reservation
        scottReservations = self.gym.get_reservations(self.scott)
        self.assertEqual(len(scottReservations), 1)

    def test_unreserve(self):
        # ensure a member can't unreserve equipment they don't already have reserved 
        # (should return False)
        us = self.gym.unreserve(self.seth, self.inclineBench)
        self.assertFalse(us)

        # ensure Joe can unreserve the bench press he currently has reserved (should return True)
        uj = self.gym.unreserve(self.joe, self.benchPress)
        self.assertTrue(uj)

        # ensure Joe only has one piece of equipment currently reserved (should now be 1, was 
        # previously 2)
        joeReservations = self.gym.get_reservations(self.joe)
        self.assertEqual(len(joeReservations), 1)

        # after unreserving the bench press from Joe, ensure the gym has a total of only 
        # 4 reservations 
        totalReservations = self.gym.all_reservations()
        self.assertEqual(len(totalReservations), 4)

        # ensure there is 5 pieces of equipment available for the gym (from the 9 instances)
        available = self.gym.get_available_equipment()
        self.assertEqual(len(available), 5)


if __name__ == "__main__":
  unittest.main()