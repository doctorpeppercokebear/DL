import numpy as np

# 넘파이 출력 소수점 자릿수 설정
np.set_printoptions(precision=2)

# 행동에 대한 상수 정의
LEFT, DOWN, RIGHT, UP = 0, 1, 2, 3

class Environment:
    """
    4x4 격자 환경을 나타내는 클래스입니다.

    Attributes:
        row (int): 에이전트의 현재 행 번호.
        col (int): 에이전트의 현재 열 번호.
        size (int): 환경의 크기 (4).

    Methods:
        reset(): 에피소드 시작 시 에이전트의 위치를 초기화하고 초기 위치를 반환합니다.
        step(action): 주어진 행동에 따라 에이전트의 위치를 업데이트하고 다음 상태, 보상, 종료 여부를 반환합니다.
        is_done(): 게임 종료 여부를 확인합니다.
    """

    def __init__(self):
        # 에이전트의 초기 위치 설정
        self.row = 0
        self.col = 0
        # 환경의 크기 설정 (4x4 격자)
        self.size = 4

    def reset(self):
        # 에피소드 시작 시 에이전트의 위치를 초기화하고 초기 위치 반환
        self.row = 0
        self.col = 0
        return self.row, self.col

    def step(self, action):
        """
        주어진 행동에 따라 에이전트의 위치를 업데이트하고 다음 상태, 보상, 종료 여부를 반환합니다.

        Args:
            action (int): 에이전트의 선택한 행동 (LEFT, DOWN, RIGHT, UP).

        Returns:
            tuple: 다음 상태 (행, 열), 보상 (int), 종료 여부 (bool).
        """

        # 주어진 행동에 따라 에이전트의 위치 업데이트
        
        if action == LEFT and self.col > 0:  # 왼쪽으로 이동
            self.col -= 1
        elif action == RIGHT and self.col < self.size - 1:  # 오른쪽으로 이동
            self.col += 1
        elif action == UP and self.row > 0:  # 위쪽으로 이동
            self.row -= 1
        elif action == DOWN and self.row < self.size - 1:  # 아래쪽으로 이동
            self.row += 1

        # 다음 상태, 보상, 종료 여부 반환

        next_state = (self.row, self.col)  # 다음 상태
        reward = -1  # 모든 이동에 대해 -1 보상
        done = self.is_done()  # 게임 종료 여부 확인

        return next_state, reward, done

    def is_done(self):
        """
        게임 종료 여부를 확인합니다.

        Returns:
            bool: 게임 종료 여부.
        """

        return self.row == self.size - 1 and self.col == self.size - 1  # 목적지 도달 여부 확인

def select_action():
    """
    확률적으로 행동을 선택합니다.

    Returns:
        int: 선택된 행동 (LEFT, DOWN, RIGHT, UP).
    """

    # 확률적으로 행동 선택
    coin = np.random.rand()
    return int(coin / 0.25)

def mc_method(n_iteration, alpha):
    """
    몬테 카를로 방식을 사용하여 가치 함수를 학습합니다.

    Args:
        n_iteration (int): 반복 횟수.
        alpha (float): 학습률.
    """

    env = Environment()  # 환경 객체 생성
    grid = np.zeros([4, 4])  # 4x4 크기의 가치 그리드 초기화

    print("초기 가치 그리드:")
    print(grid)

    for k in range(n_iteration):
        state = env.reset()  # 에피소드 시작 시 에이전트 초기화

        episode = []  # 에피소드 저장
        done = False
        while not done:
            action = select_action()  # 행동 선택
