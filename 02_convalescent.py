import matplotlib.pyplot as plt

time_limit = 12

state = {
    'time': 0,
    'healthy': 0.99,
    'infected': 0.01,
    'convalescent': 0
}

h = 1

data = [state]


def healthy_dt(state):
    return -(state['healthy'] * state['infected'])


def infected_dt(state):
    return state['healthy'] * state['infected']


def convalescent_dt(state):
    return 0


while state['time'] < time_limit:
    diff1 = {
        'healthy': h * healthy_dt(state),
        'infected': h * infected_dt(state),
        'convalescent': h * convalescent_dt(state)
    }
    arg = {
        'time': state['time'] + h / 2,
        'healthy': state['healthy'] + diff1['healthy'] / 2,
        'infected': state['infected'] + diff1['infected'] / 2,
        'convalescent': state['convalescent'] + diff1['convalescent'] / 2,
    }
    diff2 = {
        'healthy': h * healthy_dt(arg),
        'infected': h * infected_dt(arg),
        'convalescent': h * convalescent_dt(arg),
    }
    arg = {
        'time': state['time'] + h / 2,
        'healthy': state['healthy'] + diff2['healthy'] / 2,
        'infected': state['infected'] + diff2['infected'] / 2,
        'convalescent': state['convalescent'] + diff2['convalescent'] / 2,
    }
    diff3 = {
        'healthy': h * healthy_dt(arg),
        'infected': h * infected_dt(arg),
        'convalescent': h * convalescent_dt(arg)
    }
    arg = {
        'time': state['time'] + h,
        'healthy': state['healthy'] + diff3['healthy'],
        'infected': state['infected'] + diff3['infected'],
        'convalescent': state['convalescent'] + diff3['convalescent'],
    }
    diff4 = {
        'healthy': h * healthy_dt(arg),
        'infected': h * infected_dt(arg),
        'convalescent': h * convalescent_dt(arg)
    }

    new_state = {
        'time': state['time'] + h,
        'healthy': state['healthy'] + (
                    diff1['healthy'] + 2 * diff2['healthy'] + 2 * diff3['healthy'] + diff4['healthy']) / 6,
        'infected': state['infected'] + (
                diff1['infected'] + 2 * diff2['infected'] + 2 * diff3['infected'] + diff4['infected']) / 6,
        'convalescent': state['convalescent'] + (
                diff1['convalescent'] + 2 * diff2['convalescent'] + 2 * diff3['convalescent'] + diff4['convalescent']) / 6,
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
ax.plot(list(map(lambda state: state['time'], data)), list(map(lambda state: state['convalescent'], data)),
        color='tab:green')

# set the limits
ax.set_xlim([0, time_limit])
ax.set_ylim([0, 1])

ax.set_title('Healthy + infected + convalescent, Runge-Kutta 4th order method')

# display the plot
plt.show()

