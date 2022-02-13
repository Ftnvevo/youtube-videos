import time

print()
print(' *** INTERVAL TIMER ***')
print()

cycles = int(input('Number of cycles --> '))
seconds_exercise = int(input('Seconds of exercise --> '))
seconds_rest = int(input('Seconds of rest --> '))
print()

spaces = ' ' * 30
print('\rGet ready, the timer will start in: 5  ', end='')
for n in reversed(range(0, 5)):
    time.sleep(1)
    if n > 0:
        print('\rGet ready, the timer will start in: {}  '.format(n), end='')
    else:
        print('\rGOOOOO!!' + spaces, end='')

for cycle in range(cycles):
    print('\rExercise: 0' + spaces, end='')
    for n in range(seconds_exercise):
        time.sleep(1)
        print('\rExercise: {}   '.format(n + 1), end='')

    if cycle + 1 == cycles:
        print('\rWELL DONE!!' + spaces, end='')
        break
    else:
        print('\rRest: 0' + spaces, end='')
        for n in range(seconds_rest):
            time.sleep(1)
            print('\rRest: {}  '.format(n + 1), end='')
