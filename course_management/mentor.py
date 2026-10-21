from .user import User
from .logger_config import logger


class Mentor(User):

    def __init__(
        self,
        user_id,
        name,
        email,
        expertise
    ):
        super().__init__(user_id, name, email)

        self.expertise = expertise
        self.assigned_courses = []

        logger.info(
            "Mentor created: %s",
            self.name
        )

    def assign_course(self, course):
        if course not in self.assigned_courses:
            self.assigned_courses.append(course)

            logger.info(
                "Mentor %s assigned to %s",
                self.name,
                course.course_name
            )

    def display_info(self):
        courses = [
            course.course_name
            for course in self.assigned_courses
        ]

        return (
            f"Mentor ID: {self.user_id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Expertise: {self.expertise}\n"
            f"Assigned Courses: {courses}"
        )