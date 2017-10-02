from math import atan

class YawController(object):
    def __init__(self, wheel_base, steer_ratio, min_speed, max_lat_accel, max_steer_angle):
        self.wheel_base = wheel_base
        self.steer_ratio = steer_ratio
        self.min_speed = min_speed
        self.max_lat_accel = max_lat_accel

        self.min_angle = -max_steer_angle
        self.max_angle = max_steer_angle


    def get_angle(self, radius):
        angle = atan(self.wheel_base / radius) * self.steer_ratio
        return max(self.min_angle, min(self.max_angle, angle))

    def get_steering(self, linear_velocity, angular_velocity, current_velocity):
        cur_ang_velocity = 0
        if abs(linear_velocity) > 0:
            cur_ang_velocity = current_velocity * angular_velocity / linear_velocity

        if abs(current_velocity) > 0.1:
            max_yaw_rate = abs(self.max_lat_accel / current_velocity);
            cur_ang_velocity = max(-max_yaw_rate, min(max_yaw_rate, cur_ang_velocity))

        if abs(angular_velocity) > 0 and abs(cur_ang_velocity) > 0:
          return self.get_angle(max(current_velocity, self.min_speed) / cur_ang_velocity)
        else:
          return 0.0
