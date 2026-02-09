print("=== simple score tracker ===")
 
scores = []

for i in range(5):
    score = int(input("fill in score: "))
    scores.append(score)

print("scores:")
print(f" {scores}")

print(f"there are {len(scores)} scores in the list")