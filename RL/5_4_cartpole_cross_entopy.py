import gym
import numpy as np
import matplotlib.pyplot as plt

def run_episode(env, w, b, render=False):
    state = env.reset()
    step_count, done = 0, False
    while not done:
        if render:
            env.render()

        action = np.dot(state, w) + b
        best = np.argmax(action)
        state, reward, done, info = env.step(best)
        step_count += 1

    return step_count

def make_thetea(theta_mean, theta_sd):
    return np.random.multivariate_normal(mean=theta_mean, cov=np.diag(theta_sd))


env = gym.make('CartPole-v0')


input_size, output_size = 4, 2

n_sample = 32
w_size = input_size * output_size
b_size = output_size

theta_mean = np.zeros(w_size + b_size)
theta_sd = np.ones(w_size + b_size)

for episode in range(100):
    population = [make_thetea(theta_mean, theta_sd) for _ in range(n_sample)]

    # p = population[0]
    # run_episode(env)
    rewards = [run_episode(env, p[:w_size].reshape(4, 2), p[w_size:]) for p in population]

    print(sorted(rewards, reverse=True))

    sorted_idx = np.argsort(rewards)[-int(n_sample * 0.2):]
    elite = [population[idx] for idx in sorted_idx]

    theta_mean = np.mean(elite, axis=0)
    theta_sd = np.std(elite, axis=0)

    elite_reward = [rewards[idx] for idx in sorted_idx]
    avg_reward = np.mean(elite_reward)
    print(episode, avg_reward, elite_reward)

    if avg_reward >= 195:
        break


'''
퀴즈
앞에서 만든 분포 중에서 가장 좋은 것을 골라서 시뮬레이션 해보세요
'''
# p = elite[-1]
# p = np.array([1.2134538, 1.4656119, 0.31089044, 0.9477146, -1.77367499,
#               -0.33214496, -3.32289745, 2.17838657, -0.54949139, -0.5702288])
#
# run_episode(env, p[:w_size].reshape(4, 2), p[w_size:], render=True)

'''
퀴즈
elit 분포를 그래프에 표시하세요
'''
plt.subplot(1, 2, 1)
plt.ylim(-5, 5)
for i in range(len(elite)):
    # plt.plot(elite[i][:8], 'o')
    plt.plot([i] * 8, elite[i][:8], 'o')

plt.subplot(1, 2, 2)
for i in range(len(elite)):
    plt.plot([i]* 2, elite[i][8:], 'o')

plt.show()