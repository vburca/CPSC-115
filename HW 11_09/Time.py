class Time(object):
  '''Represents the time of day in the 24-hour notation.
     Attributes: hour, minute, second.'''

  def __init__(self, hour=0, minute=0, second=0):
    '''Instantiates a Time object.  Unless specified otherwise, it is
       initialized to 00:00:00.'''
    self.hour = hour
    self.minute = minute
    self.second = second

  def __str__(self):
    '''Returns a string representation of a Time object.'''
    return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

  def to_hours(self):
    '''Returns the number of hours that the current time represents.'''
    return self.hour

  def to_minutes(self):
    '''Returns the number of minutes that the current time represents.'''
    return self.hour * 60 + self.minute

  def from_hours(self, hours):
    '''Sets the hours of the current time to a specified value of hours.'''
    self.hour = hours % 24

  def from_minutes(self, minutes):
    '''Sets the minutes and, if necessary, the hours, of the current time
       to a specified value of minutes.'''
    self.hour = (minutes / 60) % 24
    self.minute = minutes % 60

  def h_increment(self, hours):
    '''Increments the current time with a specified amount of hours.'''
    self.from_hours(self.to_hours() + hours)

  def m_increment(self, minutes):
    '''Increments the current time with a specified amount of minutes.'''
    self.from_minutes(self.to_minutes() + minutes)

  def to_seconds(self):
    '''Returns the number of seconds that the current time represents.'''
    return self.hour * 60 * 60 + self.minute * 60 + self.second

  def from_seconds(self, seconds):
    '''Sets the seconds and, if necessary, the minutes and the seconds, of the
     current time to a specified value of seconds.'''
    self.hour = (seconds / 3600) % 24
    self.minute = (seconds / 60) % 60
    self.second = seconds % 60

  def s_increment(self, seconds):
    '''Increments the current time with a specified amount of seconds.'''
    self.from_seconds(self.to_seconds() + seconds)
  
  def difference(self, another_time):
    '''Returns the difference between two specified times.'''
    diff_time = Time()
    diff_time.from_seconds(abs(self.to_seconds() - another_time.to_seconds()))
    return diff_time

    
