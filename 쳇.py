def ant(load):
    # 개미의 초기 위치 설정
    x, y = 1, 1  # 2, 2에서 출발하지만 0-index로 변환하면 1, 1

    # 개미가 움직이는 경로
    while True:
        if load[x][y] == 2:  # 먹이를 찾으면 멈춤
            load[x][y] = 9
            break
        load[x][y] = 9  # 이동한 자리를 9로 표시

        # 오른쪽으로 이동
        if y + 1 < len(load[0]) and load[x][y + 1] != 1:
            y += 1
        # 밑으로 이동
        elif x + 1 < len(load[0]) and load[x + 1][y] != 1:
            x += 1
        else:
            break

    return load


# 미로 입력 받기
load = []
for _ in range(10):
    row = list(map(int, input().split()))
    load.append(row)

load = ant(load)

# 결과 출력
for row in load:
    print(" ".join(map(str, row)))
