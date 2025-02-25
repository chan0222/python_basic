# 단일 조건 조건문
# value = 30

# 이 값이 20을 초과하늘 경우, big 이라는 메세지를 출력

# if value > 20:
#     print("big!")


# 복합 조건문
# value = 50
# 20보다 큰 경우 big, 그렇지 않은 경우 small

# if value > 20:
#     print("big")
# else :
#     print("small")

# 50보다 큰 경우 great, 50보다 작거나 같고 20보다 큰 경우 big, 그렇지 않은 경우 small
# value = 10
# if value >50:
#     print("great")
# elif 50 >= value > 20:
#     print("big")
# else:
#     print("small")                                             

# 날씨가 흐리고, 강수확률이 70% 이상이면 -> 비가 온다.
# 날씨와 강수확률 파악 해야됨

condition = "맑음"
rain_rate = 0.7

if condition is "흐림" and rain_rate >= 0.70:
    print("비가 올 확률이 높습니다.")
elif condition is "흐림":
    print("날씨가 많이 흐립니다.")
elif condition is "맑음" and rain_rate >= 0.70:
    print("마지막 비가 올 확률이 높습니다.")
else:
    print("날씨가 좋습니다. ")