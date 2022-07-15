import matplotlib.pyplot as plt

time_limit = 12

# current state (on each step)
state = {
    'time': 0,
    'healthy': 0.99,
    'infected': 0.01,
}

# step value
h = 0.1

# all integrated data
data = [state]


# dH/dt
def healthy_dt(state):
    return -(state['healthy'] * state['infected'])


# dI/dt
def infected_dt(state):
    return state['healthy'] * state['infected']


while state['time'] < time_limit:
    diff1 = {
        'healthy': h * healthy_dt(state),
        'infected': h * infected_dt(state)
    }
    arg = {
        'time': state['time'] + h / 2,
        'healthy': state['healthy'] + diff1['healthy'] / 2,
        'infected': state['infected'] + diff1['infected'] / 2
    }
    diff2 = {
        'healthy': h * healthy_dt(arg),
        'infected': h * infected_dt(arg)
    }
    arg = {
        'time': state['time'] + h / 2,
        'healthy': state['healthy'] + diff2['healthy'] / 2,
        'infected': state['infected'] + diff2['infected'] / 2
    }
    diff3 = {
        'healthy': h * healthy_dt(arg),
        'infected': h * infected_dt(arg)
    }
    arg = {
        'time': state['time'] + h,
        'healthy': state['healthy'] + diff3['healthy'],
        'infected': state['infected'] + diff3['infected']
    }
    diff4 = {
        'healthy': h * healthy_dt(arg),
        'infected': h * infected_dt(arg)
    }

    new_state = {
        'time': state['time'] + h,
        'healthy': state['healthy'] + (
                    diff1['healthy'] + 2 * diff2['healthy'] + 2 * diff3['healthy'] + diff4['healthy']) / 6,
        'infected': state['infected'] + (
                diff1['infected'] + 2 * diff2['infected'] + 2 * diff3['infected'] + diff4['infected']) / 6
    }

    data.append(new_state)
    state = new_state

# plot the data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(list(map(lambda state: state['time'], data)), list(map(lambda state: state['healthy'], data)),
        color='tab:blue')
ax.plot(list(map(lambda state: state['time'], data)), list(map(lambda state: state['infected'], data)),
        color='tab:orange')

# set the limits
ax.set_xlim([0, time_limit])
ax.set_ylim([0, 1])

ax.set_title('Healthy + infected, Runge-Kutta 4th order method')
ax.legend(['Healthy', 'Infected'])

# display the plot
plt.show()
