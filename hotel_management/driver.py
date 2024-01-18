import sys
sys.path.append('/Users/akash/Desktop/learnings/LLD')

from hotel_management.controllers.guest_controller import GuestController
from hotel_management.controllers.room_controller import RoomController
from hotel_management.controllers.reservation_controller import ReservationController


from hotel_management.services.guest_service import GuestService
from hotel_management.services.room_service import RoomService
from hotel_management.services.reservation_service import ReservationService



guest_controller = GuestController(GuestService())
room_controller = RoomController(RoomService())
reservation_controller = ReservationController(ReservationService())


g1 = guest_controller.addGuest(1,"akash")
g2 = guest_controller.addGuest(2,"chethan")
g3 = guest_controller.addGuest(3,"ashwini")

r1 = room_controller.addRoom(101, 2, 200, False)
r2 = room_controller.addRoom(102, 1, 150, False)
r3 = room_controller.addRoom(103, 2, 200, False)


reservation_controller.makeReservation(g1, r1)

avail = room_controller.checkAvailability(r1.getId())
print(avail.getIsOccupied())
avail = room_controller.checkAvailability(r2.getId())
print(avail.getIsOccupied())


