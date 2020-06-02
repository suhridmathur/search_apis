from rest_framework.throttling import UserRateThrottle

class PerMinuteThrottle(UserRateThrottle):
    scope = 'per_minute'


class PerDayThrottle(UserRateThrottle):
    scope = 'per_day'