import pyautogui as pyg
import webbrowser as wb
import datetime
import time


# functions to format date, time
def format_date(x):
    date_list = x.split(sep="-")
    return list(map(int, date_list))


def format_time(x):
    time_list = x.split(sep="-")
    return list(map(int, time_list))


def given_datetime(given_date, given_time):
    # YY, MM, DD, HH, MM
    return datetime.datetime(given_date[2], given_date[1], given_date[0], given_time[0], given_time[1], given_time[2])


# join the meeting
def join_meeting(zoom_link, meeting_date, meeting_time):
    meeting_date_x = format_date(meeting_date)
    meeting_time_x = format_time(meeting_time)
    required_datetime = given_datetime(meeting_date_x, meeting_time_x)

    # time difference between current and meeting time
    wait_time_sec = (required_datetime - datetime.datetime.now().replace(microsecond=0)).total_seconds()
    print("Your ZOOM meeting starts in " + str(wait_time_sec / 60) + " min")
    while wait_time_sec > 0:
        wait_time_sec = (required_datetime - datetime.datetime.now().replace(microsecond=0)).total_seconds()
        if wait_time_sec > 60:
            time.sleep(60)
            pyg.click(x=0, y=20, clicks=1, interval=0, button='left')
    # time.sleep(wait_time_sec)

    # zoom app related
    wb.open(zoom_link, new=2)  # open zoom link in a new window
    time.sleep(5)  # given time for the link to show app top-up window
    pyg.click(x=935, y=220, clicks=1, interval=0, button='left')  # click on open zoom.app option
    time.sleep(10)  # wait for 10 sec
    pyg.click(x=834, y=676, clicks=1, interval=0, button='left')  # click on "Join Without Video"
    time.sleep(60)  # wait for 60 sec
    pyg.click(x=601, y=418, clicks=1, interval=0, button='left')  # click on "Connect Audio"
    time.sleep(1)  # wait for 1 secs
    pyg.click(x=41, y=804, clicks=1, interval=0, button='left')  # click on "mute button"


def join_meeting_ID(meetingid, password, meeting_date, meeting_time):
    meeting_date_x = format_date(meeting_date)
    meeting_time_x = format_time(meeting_time)
    required_datetime = given_datetime(meeting_date_x, meeting_time_x)

    # time difference between current and meeting time
    wait_time_sec = (required_datetime - datetime.datetime.now().replace(microsecond=0)).total_seconds()
    print("Your ZOOM meeting starts in " + str(wait_time_sec / 60) + " min")
    while wait_time_sec > 0:
        wait_time_sec = (required_datetime - datetime.datetime.now().replace(microsecond=0)).total_seconds()
        if wait_time_sec > 60:
            time.sleep(60)
            pyg.click(x=0, y=20, clicks=1, interval=0, button='left')

    # open spotlight
    pyg.press('win')  # pressing windows key.
    # open zoom.us
    pyg.write('zoom')
    time.sleep(3)
    pyg.press('enter')
    time.sleep(5)   # wait for 5 seconds
    # inside zoom client
    pyg.click(x=575, y=312, clicks=1, interval=0, button='left')  # click on join meeting
    time.sleep(3)
    pyg.write(meetingid)  # type meeting ID
    time.sleep(1)
    # pyg.click(x=858, y=532, clicks=1, interval=0, button='left')  # click on join button or press enter
    pyg.press("enter")
    time.sleep(4)  # wait for 4 seconds
    pyg.write(password)
    time.sleep(1)
    pyg.press('enter')
    time.sleep(10)  # wait for 10 seconds
    pyg.click(x=834, y=676, clicks=1, interval=0, button='left')  # click on "Join Without Video"
    time.sleep(60)  # wait for 60 sec
    pyg.click(x=601, y=418, clicks=1, interval=0, button='left')  # click on "Connect Audio"
    time.sleep(1)  # wait for 1 secs
    pyg.click(x=41, y=804, clicks=1, interval=0, button='left')  # click on "mute button"


no_of_classes = int(input("aapko kitni virtual kakshayein join karni hain??"))
class_link = []
class_date = []
class_time = []
meeting_ID = []
meeting_PW = []
choice = []
for i in range(no_of_classes):
    print("-" * 40)
    choice.append(input("How do you want to enter the zoom meeting(By 'meeting ID' or by 'link'): "))
    if 'LINK' in choice[i].upper():
        class_link.append(input("Please Copy Paste the link for your zoom meet: "))
        class_date.append(input("Please enter the date of your zoom meeting(28 June 2021 will be 28-06-2021): "))
        class_time.append(input("Please enter time of your zoom meeting(5:04PM will be 17-04-00, yes, u have to mention seconds too!!)"))
        meeting_PW.append("")
        meeting_ID.append("")
    elif 'ID' in choice[i].upper():
        meeting_ID.append(input("Please enter meeting ID : "))
        meeting_PW.append(input("Please enter meeting PW : "))
        class_date.append(input("Please enter the date of your zoom meeting(28 June 2021 will be 28-06-2021): "))
        class_time.append(input("Please enter time of your zoom meeting(5:04PM will be 17-04-00, yes, u have to mention seconds too!!))"))
        class_link.append('')

for i in range(no_of_classes):
    if 'LINK' in choice[i].upper():
        join_meeting(class_link[i], class_date[i], class_time[i])
        if i < no_of_classes - 1:
            wait_time = given_datetime(format_date(class_date[i + 1]),
                                       format_time(class_time[i + 1])) - datetime.datetime.now().replace(microsecond=0)
            time.sleep(wait_time.total_seconds())
    elif 'ID' in choice[i].upper():
        join_meeting_ID(meeting_ID[i], meeting_PW[i], class_date[i], class_time[i])
        if i < no_of_classes - 1:
            wait_time = given_datetime(format_date(class_date[i + 1]),
                                       format_time(class_time[i + 1])) - datetime.datetime.now().replace(microsecond=0)
            time.sleep(wait_time.total_seconds())
