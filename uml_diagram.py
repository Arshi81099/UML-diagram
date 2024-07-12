class User:
    user_id: int
    password: str
    user_type: str
    enrollments: list
    instructor_courses: list
    requests: list

    def __init__(self, user_id, password, user_type):
        self.user_id = user_id
        self.password = password
        self.user_type = user_type

    def enroll_course(self, course):
        if not hasattr(self, 'enrollments'):
            self.enrollments = []
        if not hasattr(course, 'enrollments'):
            course.enrollments = []
            
        enrollment = CourseEnrollment(len(self.enrollments) + 1, self.user_id, course.course_id)
        self.enrollments.append(enrollment)
        course.enrollments.append(enrollment)

    def request_instructor(self, course):
        if not hasattr(self, 'requests'):
            self.requests = []
            
        request = InstructorRequest(len(self.requests) + 1, self.user_id, course.course_id, "Pending")
        self.requests.append(request)

    def assign_course(self, course):
        if self.user_type == "Instructor":
            if not hasattr(self, 'instructor_courses'):
                self.instructor_courses = []
            if not hasattr(course, 'instructor_courses'):
                course.instructor_courses = []
                
            instructor_course = InstructorCourse(self.user_id, course.course_id)
            self.instructor_courses.append(instructor_course)
            course.instructor_courses.append(instructor_course)
        else:
            print("Only users with 'Instructor' type can be assigned courses.")


class Course:
    course_id: int
    course_name: str
    about: str
    topics: list
    enrollments: list
    instructor_courses: list

    def __init__(self, course_id, course_name, about):
        self.course_id = course_id
        self.course_name = course_name
        self.about = about

    def add_topic(self, topic):
        if not hasattr(self, 'topics'):
            self.topics = []
        self.topics.append(topic)


class Topic:
    topic_id: int
    lecture: str
    quizzes: str
    programming_quiz: str

    def __init__(self, topic_id, lecture, quizzes, programming_quiz):
        self.topic_id = topic_id
        self.lecture = lecture
        self.quizzes = quizzes
        self.programming_quiz = programming_quiz


class CourseEnrollment:
    course_enrollment_id: int
    user_id: int
    course_id: int

    def __init__(self, course_enrollment_id, user_id, course_id):
        self.course_enrollment_id = course_enrollment_id
        self.user_id = user_id
        self.course_id = course_id


class InstructorRequest:
    request_id: int
    user_id: int
    course_id: int
    status: str

    def __init__(self, request_id, user_id, course_id, status):
        self.request_id = request_id
        self.user_id = user_id
        self.course_id = course_id
        self.status = status


class InstructorCourse:
    user_id: int
    course_id: int

    def __init__(self, user_id, course_id):
        self.user_id = user_id
        self.course_id = course_id


# Example usage:
if __name__ == "__main__":
    # Creating Users
    student = User(1, "student_pass", "Student")
    instructor = User(2, "instructor_pass", "Instructor")

    # Creating a Course
    python_course = Course(1, "Python Programming", "Learn Python from basics to advanced.")

    # Creating Topics
    topic1 = Topic(1, "Introduction to Python", "Quiz 1", "Programming Quiz 1")
    topic2 = Topic(2, "Advanced Python", "Quiz 2", "Programming Quiz 2")

    # Adding Topics to Course
    python_course.add_topic(topic1)
    python_course.add_topic(topic2)

    # Enrolling Student in Course
    student.enroll_course(python_course)

    # Student Requests to be an Instructor
    student.request_instructor(python_course)

    # Instructor Assigns Course
    instructor.assign_course(python_course)

    # Print details to verify
    print(f"Course: {python_course.course_name}, Enrolled Students: {[e.user_id for e in python_course.enrollments]}")
    print(f"Instructor Courses: {[ic.course_id for ic in instructor.instructor_courses]}")
    print(f"Student Requests: {[r.course_id for r in student.requests]}")
