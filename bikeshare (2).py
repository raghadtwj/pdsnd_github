import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
                        'new york city': 'new_york_city.csv',
                        'washington': 'washington.csv' }

def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    
    
    city = input('Please enter the city. (chicago, new york city or washington) ').lower()

    while city not in ['chicago', 'new york city', 'washington']:
        city = input('sorry, the city you requested is unavailable! Please enter another city ').lower()
        
        
        
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input('Please enter the month. enter month from january to june or enter "all" for all months ').lower()
    
    while month not in months:
        month = input('sorry, the month you requested is unavailable! Please enter another month ')
        
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input('please enter the day. enter day from Monday to Sunday or enter "all" for all days ').lower()
   
    while day not in days:
        day = input('sorry, the day you requested is unavailable! Please enter another day ')
        
        
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
  
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
 

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

   
    common_month = df['month'].mode()[0]
    print(' The most common month; ', common_month)

   
    common_day = df['day_of_week'].mode()[0]
    print(' The most common day; ', common_day)

  
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(' The most common hour; ', common_hour)

   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

   

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    most_common_start_st = df['Start Station'].mode()[0]
    print('The most commonly used start station:', most_common_start_st)
    
    most_common_end_st = df['End Station'].mode()[0]
    print('The most commonly used end station:', most_common_end_st)

    most_common_start_end= (df['Start Station'] + 'to' + df['End Station']).mode()[0]
    print('The most frequent combination of start station and end station trip:', most_common_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel = df['Trip Duration'].sum()
    print('The total travel time is:', total_travel)

    mean_travel = df['Trip Duration'].mean()
    print('The mean travel time is:', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    
    user_types = df['User Type'].value_counts()
    print(user_types,'\n')
    
    
    
    if 'Gender' in df.columns:    
        gender_counts = df['Gender'].value_counts()
        print(gender_counts,'\n')
        
        
        
    if 'Birth Year' in df.columns:
        print('earliest year of Birth :', df['Birth Year'].min())
        print('most Recent year of Birth :', df['Birth Year'].max())
        print('most Common year of Birth :', df['Birth Year'].mode()[0])
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def GPA():
    print("5 out of 5")

def printinfo():
    print("raghad altuwayjiri")


def raw_display(df):
    raw_display= input("Would you like to view 5 rows of data?")
    start_loc= 0 
    while raw_display.lower() == 'yes':
        print(df.iloc[start_loc: start_loc+5])
        start_loc +=5
        raw_display= input("Would you like to view 5 rows of data?")
        
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
            
if __name__ == "__main__":
	main()