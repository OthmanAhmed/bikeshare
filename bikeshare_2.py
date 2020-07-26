#!/home/othman/Software/anaconda/envs/udacity-itida/bin/ipython

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputsity
    check_city = True
    while (check_city):
        global city
        print()
        city = input("Which city you want to explore its data, (chicago, new york city, washington)? \n").lower()
        print()
        check_city = not(city in CITY_DATA.keys())


    # TO DO: get user input for month (all, january, february, ... , june)
    check_month = True
    while(check_month):
        month = input('Which month you want to filter the data with, (all, january, february, ... , june)? \n').lower()
        print()
        check_month = not(month in months)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    check_week_day = True
    while(check_week_day):
        day = input('Which day of week you want to filter the data with, (all, monday, tuesday, ... sunday)? \n').lower()
        print()
        check_week_day = not(day in week_days)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Loading Data
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['Day of Week'] = df['Start Time'].dt.dayofweek
    df['Month'] = df['Start Time'].dt.month
    df['Hour'] = df['Start Time'].dt.hour
    df['Station Combination'] = df['Start Station'] + '--->' + df['End Station']


    # Filtering by month
    if month != 'all':
        month = months.index(month.lower()) + 1
        df = df[df['Month'] == month]

    if day != 'all':
        day = week_days.index(day.lower())
        df = df[df['Day of Week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Month'].mode()[0]
    print(common_month)
    print('The most common month was ', months[common_month-1], '\n')

    # TO DO: display the most common day of week
    common_dayofweek = df['Day of Week'].mode()[0]
    print('The most common day of week was ', week_days[common_dayofweek], '\n')


    # TO DO: display the most common start hour
    common_hour = df['Hour'].mode()[0]
    print('The most common start hour was ', common_hour, '\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station was ', common_start_station, '\n')


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station was ', common_end_station, '\n')


    # TO DO: display most frequent combination of start station and end station trip
    common_combination = df['Station Combination'].mode()
    print('The most common start & end stations combination was ', common_combination, '\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time was ', total_time, '\n')

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean travel time was ', mean_time, '\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print('The user type counts is as follows:\n', user_counts)

    # TO DO: Display counts of gender
    if (city.lower()!='washington'):
        gender_counts = df['Gender'].value_counts()
        print('The user gender counts is as follows:\n', gender_counts)
    else: print('Gender data is not available for Washington DC')

    # TO DO: Display earliest, most recent, and most common year of birth
    if (city.lower()!='washington'):
        earliest_year = df['Birth Year'].min()
        print('The earliest year of birth: ', earliest_year, '\n')

        recent_year = df['Birth Year'].max()
        print('The most recent year of birth: ', recent_year, '\n')

        common_year = df['Birth Year'].mode()[0]
        print('The most common year of birth: ', common_year, '\n')

    else: print('Year of birth data is not available for Washington DC')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
