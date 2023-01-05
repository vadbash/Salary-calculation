import unittest
import datetime
import main as mn


class TestCases(unittest.TestCase):
    def test_string_parse_date(self):
        self.assertEqual(mn.split_time_string("11:00-20:00"),
                         (datetime.datetime.strptime("11:00", '%H:%M').time(),
                          datetime.datetime.strptime("20:00", '%H:%M').time()))

    #test for salary for morning
    def test_salary_morning(self):
        self.assertEqual(mn.calculate_price_for_hour("1:00-03:00",
        work_time=["00:01-09:00", "09:01-18:00", "18:01-23:59"],
        salary_dict={"00:01-09:00": 25, "09:01-18:00": 15, "18:01-23:59": 20})[0], 25)

    #test for salary for afternoon
    def test_salary_afternoon(self):
        self.assertEqual(mn.calculate_price_for_hour("10:00-12:00",
        work_time=["00:01-09:00", "09:01-18:00", "18:01-23:59"],
        salary_dict={"00:01-09:00": 25, "09:01-18:00": 15, "18:01-23:59": 20})[0], 15)

    #test for salary for evening
    def test_salary_evening(self):
        self.assertEqual(mn.calculate_price_for_hour("20:00-21:00",
        work_time=["00:01-09:00", "09:01-18:00", "18:01-23:59"],
        salary_dict={"00:01-09:00": 25, "09:01-18:00": 15, "18:01-23:59": 20})[0], 20)

    #test for worked hours
    def test_worked_hours(self):
        self.assertEqual(mn.calculate_price_for_hour("10:00-12:00",
        work_time=["00:01-09:00", "09:01-18:00", "18:01-23:59"],
        salary_dict={"00:01-09:00": 25, "09:01-18:00": 15, "18:01-23:59": 20})[1], 2)


if __name__ == '__main__':
    unittest.main()
