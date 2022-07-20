import matplotlib.pyplot as plt

time_limit = 30

state = {
    'time': 0,
    'romeo': 0.8,
    'juliet': 0.6,
}

h = 0.2

data = [state]


def romeo_dt(state):
    return state['juliet']


def juliet_dt(state):
    return -state['romeo']


while state['time'] < time_limit:
    diff1 = {
        'romeo': h * romeo_dt(state),
        'juliet': h * juliet_dt(state),
    }
    arg = {
        'time': state['time'] + h / 2,
        'romeo': state['romeo'] + diff1['romeo'] / 2,
        'juliet': state['juliet'] + diff1['juliet'] / 2,
    }
    diff2 = {
        'romeo': h * romeo_dt(arg),
        'juliet': h * juliet_dt(arg),
    }
    arg = {
        'time': state['time'] + h / 2,
        'romeo': state['romeo'] + diff2['romeo'] / 2,
        'juliet': state['juliet'] + diff2['juliet'] / 2,
    }
    diff3 = {
        'romeo': h * romeo_dt(arg),
        'juliet': h * juliet_dt(arg),
    }
    arg = {
        'time': state['time'] + h,
        'romeo': state['romeo'] + diff3['romeo'],
        'juliet': state['juliet'] + diff3['juliet'],
    }
    diff4 = {
        'romeo': h * romeo_dt(arg),
        'juliet': h * juliet_dt(arg),
    }

    new_state = {
        'time': state['time'] + h,
        'romeo': state['romeo'] + (
                    diff1['romeo'] + 2 * diff2['romeo'] + 2 * diff3['romeo'] + diff4['romeo']) / 6,
        'juliet': state['juliet'] + (
                diff1['juliet'] + 2 * diff2['juliet'] + 2 * diff3['juliet'] + diff4['juliet']) / 6,
    }

    data.append(new_state)
    state = new_state

# plot the data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(list(map(lambda state: state['time'], data)), list(map(lambda state: state['romeo'], data)),
        color='tab:blue')
ax.plot(list(map(lambda state: state['time'], data)), list(map(lambda state: state['juliet'], data)),
        color='tab:orange')

# set the limits
ax.set_xlim([0, time_limit])
ax.set_ylim([-5, 5])

ax.set_title('Romeo + Juliet, Runge-Kutta 4th order method')
ax.legend(['Romeo', 'Juliet'])

# display the plot
plt.show()

