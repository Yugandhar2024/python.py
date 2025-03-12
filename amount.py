amount=int(input())
five=amount//500
remain=amount%500
hundr=remain//100
remain=remain%100
fifty=remain//50
remain=remain%50
ten=remain//10
remain=remain%10
print("five hundred notes:",five)
print("Hundred notes:",hundr)
print("Fifty notes:",fifty)
print("Ten notes:",ten)
