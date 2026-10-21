from .exceptions import (
    InvalidCapacityError,
    CourseFullError
)

from .logger_config import logger


class Course:
    total_courses = 0

    def __init__(
        self,
        course_id,
        course_name,
        duration,
        capacity
    ):
        if not self.validate_capacity(capacity):
            raise InvalidCapacityError(
                "Course capacity must be greater than zero."
            )

        self.course_id = course_id
        self.course_name = course_name
        self.duration = duration

        # Encapsulation
        self.__capacity = capacity

        self.mentor = None
        self.students = []

        Course.total_courses += 1

        logger.info(
            "Course created: %s",
            self.course_name
        )

    @property
    def capacity(self):
        return self.__capacity

    @staticmethod
    def validate_capacity(capacity):
        return (
            isinstance(capacity, int)
            and capacity > 0
        )

    @classmethod
    def get_total_courses(cls):
        return cls.total_courses

    def assign_mentor(self, mentor):
        self.mentor = mentor
        mentor.assign_course(self)

        logger.info(
            "Mentor %s assigned to course %s",
            mentor.name,
            self.course_name
        )

    def add_student(self, student):
        if student in self.students:
            return

        if len(self.students) >= self.__capacity:
            logger.error(
                "Course full: %s",
                self.course_name
            )

            raise CourseFullError(
                f"{self.course_name} is full."
            )

        self.students.append(student)
        student.enroll_course(self)

        logger.info(
            "%s added to course %s",
            student.name,
            self.course_name
        )

    def available_seats(self):
        return self.__capacity - len(self.students)

    def display_course(self):
        mentor_name = (
            self.mentor.name
            if self.mentor
            else "Not Assigned"
        )

        return (
            f"Course ID: {self.course_id}\n"
            f"Course: {self.course_name}\n"
            f"Duration: {self.duration}\n"
            f"Mentor: {mentor_name}\n"
            f"Capacity: {self.__capacity}\n"
            f"Available Seats: {self.available_seats()}"
        )