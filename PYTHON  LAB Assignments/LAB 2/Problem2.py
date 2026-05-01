h=list(map(int,input().split()))
sml=h[0]
for i in range(len(h)):
	if(sml<h[i]):
		sml=h[i]
print(sml)