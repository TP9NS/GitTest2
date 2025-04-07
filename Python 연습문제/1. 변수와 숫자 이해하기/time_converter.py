seconds = 12345
h = seconds // 3600
m = (seconds % 3600) // 60
s = seconds % 60
print(f"{h}시간 {m}분 {s}초입니다.")
