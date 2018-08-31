from enum import IntEnum
import datetime
import calendar
import pathlib
import pickle




class FeelingColor(IntEnum):
    NONE = 0
    GREEN = 1
    YELLOW = 2
    RED = 3
    BLUE = 4


def make_calendarday_to_key(year, month,
                            monthcalendar,
                            default_item) -> dict:
    """
    example return: {year: int {month: int} {day: item}}
    """
    new_calendar = {year: {month: {}}}
    for week_number, week in enumerate(monthcalendar):
        new_calendar[year][month]
        for day in week:
            if not day == 0:
                new_calendar[year][month][day]\
                    = default_item
    return new_calendar


class FeelingDiary:
    def __init__(self):
        today = datetime.datetime.today()
        monthcalendar = calendar.monthcalendar(today.year, today.month)
        self.calendar = make_calendarday_to_key(
            today.year, today.month, monthcalendar, FeelingColor.NONE)

    def reset_calendar(self, year, month, monthcalendar,
                       default_color: FeelingColor):
        self.calendar = make_calendarday_to_key(
            year, month, monthcalendar, default_color)


def data_dir() -> pathlib.Path:
    path = pathlib.Path(__file__).parent
    path = path / "data"
    return path


def open_feelingdiary() -> FeelingDiary:
    path = data_dir()
    if not path.is_dir():
        path.mkdir()
    path = path / "calendar.pickle"
    if not path.is_file():
        with path.open(mode="wb+") as calendar_fileobj:
            feelingdiary = FeelingDiary()
            pickle.dump(feelingdiary, calendar_fileobj)
    else:
        with path.open(mode="rb") as calendar_fileobj:
            feelingdiary = pickle.load(calendar_fileobj)
    return feelingdiary


def save_feelingdiary(feelingdiary: FeelingDiary):
    path = data_dir()
    path = path / "calendar.pickle"
    with path.open(mode="wb") as calendar_fileobj:
        pickle.dump(feelingdiary, calendar_fileobj)


def main():
    feelingdiary = open_feelingdiary()
    while True:
        today = datetime.datetime.today()
        print("気分ダイアリー")
        print(f"- {today.year}年 {today.month}月")
        for i in range(7):
            if not today.day - i <= 0:
                print(f"{today.month}月{today.day-i}日")
                print(feelingdiary.calendar[today.year]
                      [today.month][today.day-i])
        print("-")
        print("今日の気分はどんな色ですか?")
        print("1:Green 2:Yellow 3:Red 4:Blue")
        print("上記以外を入力: アプリケーションを終了")
        option = input("入力してください: ")
        if option == "1":
            feelingdiary.calendar[today.year][today.month][today.day]\
                = FeelingColor.GREEN
        elif option == "2":
            feelingdiary.calendar[today.year][today.month][today.day]\
                = FeelingColor.YELLOW
        elif option == "3":
            feelingdiary.calendar[today.year][today.month][today.day]\
                = FeelingColor.RED
        elif option == "4":
            feelingdiary.calendar[today.year][today.month][today.day]\
                = FeelingColor.BLUE
        else:
            break
        save_feelingdiary(feelingdiary)


def guimain():
    import sys
    from PySide2.QWidget import QApplication, QLabel

    app = QApplication(sys.argv)
    label = QLabel("<font color=#6495ed size=22px>Hello World!</font>")
    label.show()
    app.exec()


if __name__ == '__main__':
    guimain()
