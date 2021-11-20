from datetime import datetime
from typing import List

class Base_charge:
    user_id: int
    base_pricing: int

class User:
    user_id : int
    use_deer_name: str
    use_end_lat: float
    use_end_lng: float

    use_start_at: datetime
    use_end_at: datetime


class Deer:
    deer_name: str
    deer_area_id: int


class Area:
    area_id: int
    area_bounday: List[tuple]
    # 실제는 폴리곤타입이라고 함.
    area_center: tuple
    area_coords: List[tuple]


class ParkingZone:
    parkingzone_id: int
    parkingzone_center_lat: float
    parkingzone_center_lng: float
    parkingzone_radius: float


class ForbiddenArea:
    forbidden_area_id: int
    forbidden_area_boundary: List[tuple]
    forbidden_area_coords: List[tuple]
