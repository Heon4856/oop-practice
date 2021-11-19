from dto import Deer, Area, ParkingZone, ForbiddenArea
from datetime import datetime, timedelta

def find_deer_info(use_deer_name):
    deer = Deer()
    deer.deer_area_id = 1
    deer.deer_name = "test"
    return deer


def find_area_info(area_id):
    area = Area()
    area.id = 1
    area.area_boundary = [(5, 5)]
    area.area_center = [(2.5, 2.5)]
    area.area_coords = [(5, 5)]
    return area


def find_parking_zone():
    parkingzone = ParkingZone()
    parkingzone.parkingzone_radius = 5
    parkingzone.parkingzone_center_lng = 2
    parkingzone.parkingzone_center_lat = 2
    parkingzone.parkingzone_id = 1
    return parkingzone


def find_user_last_use():
    return datetime.now() - timedelta(minutes=10)


def find_forbidden_area():
    forbidden = ForbiddenArea()
    forbidden.forbidden_area_id = 1
    forbidden.forbidden_area_boundary = [(5, 5)]
    forbidden.forbidden_area_coords = [(5, 5)]
    return forbidden