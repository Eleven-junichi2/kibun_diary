import unittest
import calendar

from app import FeelingDiary, FeelingColor


class TestFeelingDiary(unittest.TestCase):
    def setUp(self):
        self.feelingdiary = FeelingDiary()

    def test_calendar(self):
        self.feelingdiary.reset_calendar(0, 1, calendar.monthcalendar(0, 1),
                                         FeelingColor.NONE)
        self.assertEqual(self.feelingdiary.calendar,
                         {0:
                          {1:
                           {1: FeelingColor.NONE,
                            2: FeelingColor.NONE,
                            3: FeelingColor.NONE,
                            4: FeelingColor.NONE,
                            5: FeelingColor.NONE,
                            6: FeelingColor.NONE,
                            7: FeelingColor.NONE,
                            8: FeelingColor.NONE,
                            9: FeelingColor.NONE,
                            10: FeelingColor.NONE,
                            11: FeelingColor.NONE,
                            12: FeelingColor.NONE,
                            13: FeelingColor.NONE,
                            14: FeelingColor.NONE,
                            15: FeelingColor.NONE,
                            16: FeelingColor.NONE,
                            17: FeelingColor.NONE,
                            18: FeelingColor.NONE,
                            19: FeelingColor.NONE,
                            20: FeelingColor.NONE,
                            21: FeelingColor.NONE,
                            22: FeelingColor.NONE,
                            23: FeelingColor.NONE,
                            24: FeelingColor.NONE,
                            25: FeelingColor.NONE,
                            26: FeelingColor.NONE,
                            27: FeelingColor.NONE,
                            28: FeelingColor.NONE,
                            29: FeelingColor.NONE,
                            30: FeelingColor.NONE,
                            31: FeelingColor.NONE
                            }
                           }
                          },
                         "生成されるFeelingDiary.calendarの値が正しいか確認")
