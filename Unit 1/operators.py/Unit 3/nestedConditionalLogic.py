# What is a conditinal statement
'A conditional statement is a type of construct'
'That checks for a specific condition and will output'
'A specific result'
'If the condition is not met, It will return a different'
'result'

'We use the IF/ Else keywords to create conditions.'


def schoolHours(hour, meridiem):
        print('conected')
        if (hour > 7 and hour < 12):
            print('school is IN session')
    if meridiem == 'pm':
        print('its the pm')
        if(hour >= 1 and hour <= 3):
            print('school is IN school')
  
    else:
        print('school is NOT in session.')

schoolHours(7,'am')