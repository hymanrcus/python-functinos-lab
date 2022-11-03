# EX 1

def sum_to(n):
  i = 0
  sum = 0
  while i <= n:
    sum += i
    i+= 1
  return sum

# print(sum_to(10))

# EX 2


def largest(nums):
  sorted_nums =sorted(nums)
  return sorted_nums[-1]


# print(largest([10, 4, 2, 231, 91, 54])) 


# EX 3

def occurences(Str1, Str2):
  return Str1.count(Str2)

print(occurences('HAHAHHHHAAAHHHAHAHAAA', 'AAA'))
