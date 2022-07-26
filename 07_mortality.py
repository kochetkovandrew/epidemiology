import matplotlib.pyplot as plt
from rk4 import Rk4


time_limit = 100

beta = 2.1
gamma = 1
zeta = 0.04
eta = 0.04
tau1 = 2.6
tau2 = 1


def tau_idx(tau):
    idx = int(len(rk4.data) - tau/rk4.h)
    if idx < 0:
        idx = 0
    return idx


def healthy_dt(state):
    return -(beta * state['healthy'] * rk4.data[tau_idx(tau2)]['infected']) + zeta * \
           rk4.data[tau_idx(tau1)]['convalescent']


def infected_dt(state):
    return beta * state['healthy'] * rk4.data[tau_idx(tau2)]['infected'] - gamma * state['infected'] - \
           eta * state['infected']


def convalescent_dt(state):
    return gamma * state['infected'] - zeta * rk4.data[tau_idx(tau1)]['convalescent']


def dead_dt(state):
    return eta * state['infected']


rk4 = Rk4({
    'h': 0.2,
    'x': {
        'time': 0
    },
    'y': {
        'healthy': {'value': 0.99, 'func': healthy_dt},
        'infected': {'value': 0.01, 'func': infected_dt},
        'convalescent': {'value': 0, 'func': convalescent_dt},
        'dead': {'value': 0, 'func': dead_dt}
    }
})


while rk4.state['time'] < time_limit:
    rk4.step()


# plot the data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

colors = {'healthy': 'tab:blue', 'infected': 'tab:orange', 'convalescent': 'tab:green', 'dead': 'tab:red'}

for key in colors.keys():
    ax.plot(list(map(lambda state: state['time'], rk4.data)), list(map(lambda state: state[key], rk4.data)),
            color=colors[key])

# set the limits
ax.set_xlim([0, time_limit])
ax.set_ylim([0, 1])

ax.set_title('Not immune + infected + convalescent + dead, RK4')
ax.legend(['Not immune', 'Infected', 'Convalescent', 'Dead'])

# display the plot
plt.show()

