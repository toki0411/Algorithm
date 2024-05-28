def prime_numbers(n):
	arr = [i for i in range(n+1)]
	end = int(n ** (1/2))
	for i in range(2, end + 1):
		if arr[i] == 0:
			continue
		for j in range(i*i, n+1, i):
			arr[j] = 0

	return [i for i in arr[2:] if arr[i]]

def isPrime(n):
	end = int(n ** (1 / 2))
	for i in range(2, end + 1):
		if n % i == 0:
			return False
	return True

n = int(input())
if n == 1:
	print(0)
	exit()
ans = 0
prime = prime_numbers(n)
start = 0
end = 1
if n != 2:
	if isPrime(n):
		ans += 1
# print(prime)
while start < end:
	# if end + 1 <= len(prime):
	value = sum(prime[start:end+1])
	if value == n:
		# print(start, end)
		ans += 1
		start += 1
	elif value > n :
		start += 1
	elif value < n:
		end += 1

print(ans)