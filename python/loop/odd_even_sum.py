start=10
end=20
odd_sum=0
even_sum=0
while(start<=end):
    if start%2==0:
        even_sum=even_sum+start
    else:
        odd_sum=odd_sum+start
    start=start+1
print("odd sum =",odd_sum)
print("even sum = ",even_sum)