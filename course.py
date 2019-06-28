import os
import sys
import json
import shutil

from canvasapi import Canvas

class CourseWrapper:
    def __init__(self):
        self.canvas  = Canvas(os.environ["API_URL"], os.environ["API_KEY"])
        self.account = self.canvas.get_current_user()
        self.BASE_DIR = os.getcwd()

    def get_courses(self, mode='ta'):
        for course in self.account.get_courses(enrollment_type=mode):
            print(course)
    
    def get_assignments(self, course_id):
        course = self.canvas.get_course(course_id)
        for assignment in course.get_assignments():
            print(assignment)

    def set_assignment(self, courseID, assignmentID):
        self.course     = self.canvas.get_course(courseID)
        self.assignment = self.course.get_assignment(assignmentID)

    def get_student_list(self, mode=('StudentEnrollment',)):
        """
        :param course canvasapi.course.Course
        :param mode tuple of StudentEnrollment | StudentViewEnrollment | TaEnrollment | TeacherEnrollment
        """
        student_data = {}
        
        for enrollment in self.course.get_enrollments():
            if enrollment.type in mode:
                student = enrollment.user

                lms = student['id']
                uni = student['sis_user_id']
                name = student['sortable_name']
                
                student_data[uni] = {'canvas_id': lms, 'name':name}
        
        with open("students.json", "w") as json_file:
            json.dump(student_data, json_file)

        return student_data