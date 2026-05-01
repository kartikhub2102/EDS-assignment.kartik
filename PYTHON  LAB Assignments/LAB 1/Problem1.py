
n = int(input())
marks = list(map(int,input().split()))
for m in marks:
	if m<40:
		print("Fail")
		break
else:
	percentage=sum(marks)/n
	print(f"Aggregate Percentage: {percentage:.2f}")
	if percentage>=75:
		print("Grade: Distinction")
	elif percentage>=60:
		print("Grade: First Division")
	elif percentage>=50:
		print("Grade: Second Division")
	else:
		print("Grade: Third Division")