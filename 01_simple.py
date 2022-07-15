import matplotlib.pyplot as plt

time0 = 0.0
time_limit = 12
healthy0 = 0.99
infected0 = 0.01
h = 1

time_data = [time0]
healthy_data = [healthy0]
infected_data = [infected0]


def healthy_dt(time, healthy, infected):
    return -(healthy * infected)


def infected_dt(time, healthy, infected):
    return healthy * infected


while time0 < time_limit:
    healthy1 = h * healthy_dt(time0, healthy0, infected0)
    infected1 = h * infected_dt(time0, healthy0, infected0)

    healthy2 = h * healthy_dt(
        time0 + h / 2,
        healthy0 + healthy1 / 2,
        infected0 + infected1 / 2
    )
    infected2 = h * infected_dt(
        time0 + h / 2,
        healthy0 + healthy1 / 2,
        infected0 + infected1 / 2
    )

    healthy3 = h * healthy_dt(
        time0 + h / 2,
        healthy0 + healthy2 / 2,
        infected0 + infected2 / 2
    )
    infected3 = h * infected_dt(
        time0 + h / 2,
        healthy0 + healthy2 / 2,
        infected0 + infected2 / 2
    )

    healthy4 = h * healthy_dt(
        time0 + h,
        healthy0 + healthy3,
        infected0 + infected3
    )
    infected4 = h * infected_dt(
        time0 + h,
        healthy0 + healthy3,
        infected0 + infected3
    )

    healthy = (healthy1 + 2 * healthy2 + 2 * healthy3 + healthy4) / 6
    infected = (infected1 + 2 * infected2 + 2 * infected3 + infected4) / 6

    healthy_n = healthy0 + healthy
    infected_n = infected0 + infected

    time_n = time0 + h
    time_data.append(time_n)
    healthy_data.append(healthy_n)
    infected_data.append(infected_n)
    (time0, healthy0, infected0) = (time_n, healthy_n, infected_n)

# plot the data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(time_data, healthy_data, color='tab:blue')
ax.plot(time_data, infected_data, color='tab:orange')

# set the limits
ax.set_xlim([0, time_limit])
ax.set_ylim([0, 1])

ax.set_title('Healthy + infected, Runge-Kutta 4th order method')

# display the plot
plt.show()

