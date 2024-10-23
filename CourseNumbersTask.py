###
# Project:      CourseNumbersTask.py
# Author:       Michael Keeton
# Created:      10/23/2024
# Description:  User enters a course number and displays the course's
#               room number, instructor, and meeting time.
###

# Global variable of course numbers.
course_num_list = [
    'CSC101',
    'CSC102',
    'CSC103',
    'NET110',
    'COM241'
]

#
def course_lookup(course_number):
    """
    Prints a course's room number, instructor, and meeting time.
    
    Args:
        course_number (string): The course number.
    """
    
    room_num_dict = {
        course_num_list[0]: 3004,
        course_num_list[1]: 4501,
        course_num_list[2]: 6755,
        course_num_list[3]: 1244,
        course_num_list[4]: 1411
    }
    
    instructor_dict = {
        course_num_list[0]: 'Haynes',
        course_num_list[1]: 'Alvarado',
        course_num_list[2]: 'Rich',
        course_num_list[3]: 'Burke',
        course_num_list[4]: 'Lee'
    }
    
    meet_time_dict = {
        course_num_list[0]: '8:00 a.m.',
        course_num_list[1]: '9:00 a.m.',
        course_num_list[2]: '10:00 a.m.',
        course_num_list[3]: '11:00 a.m.',
        course_num_list[4]: '1:00 p.m.'
    }
    
    # Uses course_number as a key to access the values in the dictionaries.
    if course_number in course_num_list:
        print('Room Number:', room_num_dict[course_number])
        print('Instructor:', instructor_dict[course_number])
        print('Meeting Time:', meet_time_dict[course_number])
    else:
        print('Invalid Course Number')

def main():    
    print('The following course numbers are available:', course_num_list)
    course_num = input('Enter a course number: ')
    course_lookup(course_num)

main()
    