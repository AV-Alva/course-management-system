from .user import User
from .logger_config import logger


class Student(User):

    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)

        self.enrolled_courses = []
        self.completed_assignments = 0

        logger.info(
            "Student created: %s",
            self.name
        )

    def enroll_course(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)

            logger.info(
                "Student %s enrolled in %s",
                self.name,
                course.course_name
            )

    def submit_assignment(self):
        self.completed_assignments += 1

        logger.info(
            "%s submitted an assignment",
            self.name
        )

    def display_info(self):
        courses = [
            course.course_name
            for course in self.enrolled_courses
        ]

        return (
            f"Student ID: {self.user_id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Courses: {courses}\n"
            f"Completed Assignments: "
            f"{self.completed_assignments}"
        )