#include <iostream>
#include <cstdlib>

using namespace std;


const int FIXED_YEAR = 0;
const short LEAP_YEAR_DAYS = 366;
const short NON_LEAP_YEAR_DAYS = 365;


int days_in_month(int month, int year);


bool is_leap_year(int year)
{
    if (year % 400 == 0) return true;
    if (year % 100 == 0) return true;
    if (year % 4 == 0) return true;
    return false;
}


size_t count_days(int year, int month, int day)
{
    size_t days_count = 0;
    for (int cur_year = FIXED_YEAR; cur_year < year; ++cur_year)
    {
        days_count += ((is_leap_year(cur_year)) ? LEAP_YEAR_DAYS : NON_LEAP_YEAR_DAYS);
    }

    for (int cur_month = 1; cur_month < month; ++cur_month)
    {
        days_count += days_in_month(cur_month, year);
    }

    return days_count + day;
}


int days_between(int year1, int month1, int day1, int year2, int month2, int day2)
{
    int days_diff = count_days(year2, month2, day2) - count_days(year1, month1, day1);
    return (days_diff < 0) ? -days_diff : days_diff;
}


int main()
{
    cout << days_between(2010, 2, 20, 2013, 12, 1) << endl;
    return 0;
}


int days_in_month(int month, int year)
{
    if (month == 1) return 31;
    if (month == 2) return ((is_leap_year(year)) ? 29 : 28);
    if (month == 3) return 31;
    if (month == 4) return 30;
    if (month == 5) return 31;
    if (month == 6) return 30;
    if (month == 7) return 31;
    if (month == 8) return 31;
    if (month == 9) return 30;
    if (month == 10) return 31;
    if (month == 11) return 30;
    if (month == 12) return 31;
}
