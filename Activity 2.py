amount=int(input("Enter amount: "))
n100=amount//100
n50=( amount % 100)//50
n10=( ( amount % 100)%50)//10
print("Notes of 100 $: ", n100)
print("Notes of 50 $: ", n50)
print("Notes of 10 $: ", n10)