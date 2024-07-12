# UML-diagram

Project Name: Course Management System
Overview
This project implements a Course Management System where users can enroll in courses, request instructor roles, and have courses assigned to them. It includes classes for users, courses, topics, enrollments, instructor requests, and instructor courses.

Classes and Relationships
User
Represents a user of the system.
Attributes:
user_id: Unique identifier for the user.
password: Password for user authentication.
user_type: Type of user (e.g., "Student", "Instructor").
enrollments: List of courses the user is enrolled in.
instructor_courses: List of courses assigned to the user as an instructor.
requests: List of requests made by the user (e.g., to become an instructor).
Course
Represents a course offered in the system.
Attributes:
course_id: Unique identifier for the course.
course_name: Name of the course.
about: Description of the course.
topics: List of topics covered in the course.
enrollments: List of enrollments (users enrolled in the course).
instructor_courses: List of instructors assigned to teach the course.
Topic
Represents a topic within a course.
Attributes:
topic_id: Unique identifier for the topic.
lecture: Description of the lecture for the topic.
quizzes: Details about quizzes related to the topic.
programming_quiz: Details about programming quizzes related to the topic.
CourseEnrollment
Represents the enrollment of a user in a course.
Attributes:
course_enrollment_id: Unique identifier for the enrollment.
user_id: Identifier of the user enrolled.
course_id: Identifier of the course enrolled.
InstructorRequest
Represents a request from a user to become an instructor for a course.
Attributes:
request_id: Unique identifier for the request.
user_id: Identifier of the user making the request.
course_id: Identifier of the course for which the request is made.
status: Current status of the request (e.g., "Pending", "Approved", "Rejected").
InstructorCourse
Represents the assignment of an instructor to teach a course.
Attributes:
user_id: Identifier of the user assigned as instructor.
course_id: Identifier of the course assigned.
Class Diagram
The class diagram below illustrates the relationships between these classes:

## plantuml

[Insert your PlantUML code here]

Usage
Clone the repository and set up the necessary environment (Python, dependencies).
Modify the classes and methods as per your project requirements.
Use the provided example usage or integrate these classes into your application.
Example Usage
Here's a brief example of how to use these classes:

python
Copy code
# Example usage (Python code)
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
License
This project is licensed under the MIT License - see the LICENSE file for details.
