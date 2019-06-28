import os
import sys
import argparse

parser = argparse.ArgumentParser(description='End-to-end canvas autograding script')


if __name__ == "__main__":
    print("Here", sys.argv)

    deb = CourseWrapper()
    # deb.get_account_assignments()
    # deb.set_assignment(82461, 298510)
    # deb.get_student_list()