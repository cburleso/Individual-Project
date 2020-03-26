import unittest
import member
import equipment
import reservation
import gym


# member1 = member.Member('Connor B.') 
# member1info = member1.get_info()

# equip1 = equipment.Equipment('Leg Press', 'Strength Training')
# print(equip1.is_reserved())
# res1 = reservation.Reservation(member1, equip1, '12:00-1:00')
# print(equip1.is_reserved())
# print(res1)
# print('-------------------------------------------')
# member1.add_reservation(res1)
# member1res = member1.get_reservations()
# print(member1res)
# print(res1.get_equipment())

gym = gym.Gym()

equip1 = equipment.Equipment('Leg Press', 'Strength Training')
equip2 = equipment.Equipment('Smith Machine', 'Strength Training')
equip3 = equipment.Equipment('Sitting Bike', 'Cardio')

gym.add_equipment(equip1)
gym.add_equipment(equip2)
gym.add_equipment(equip3)

equipment = gym.get_equipment()
print(equipment)

member1 = member.Member('Connor B.')
member2 = member.Member('Jack L.')
member3 = member.Member('Vanessa M.')
member4 = member.Member('Ryan R.')
member5 = member.Member('Josh P.')

gym.add_member(member1)
gym.add_member(member2)
gym.add_member(member3)
gym.add_member(member4)
gym.add_member(member5)

members = gym.get_members()
print(members)

res1 = gym.make_reservation(member1, equip1, '11:00-12:00')
print(res1)

res2 = gym.make_reservation(member2, equip2, '11:00-12:00')
print(res2)

info = member1.get_info()
print(info)
#unrestest = gym.unreserve(member3, equip2)
#print(unrestest)
#unres1 = gym.unreserve(member1, equip1)
#print('unreserve', unres1)

print(gym.get_reservations())

print(len(member1.get_reservations()))

search = gym.find_member(3)
print(search)