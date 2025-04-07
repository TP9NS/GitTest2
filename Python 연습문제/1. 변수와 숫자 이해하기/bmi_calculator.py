weight,height = map(int,input().split())

print(f"bmi: {weight / (height / 100) ** 2:.1f}")