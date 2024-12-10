'''def count_unique_palindromic_substrings(s: str) -> int:
    # Your code goes here
    unique_s_set = set()
    i = 1
    a = 0

    #Letters are already palindrome so we just add them to the set.
    for letter in s:
        if letter not in unique_s_set: 
            unique_s_set.add(letter)
    
    while a <= len(s):
      while i <= len(s):
        rev_s = s[a:i][::-1]
        if (s[a:i] not in unique_s_set) and (s[a:i] == rev_s):
            unique_s_set.add(s[a:i]) 
        i+=1

      a+=1
      i = 1
    
    unique_s_set.remove('')'''

#count_unique_palindromic_substrings("aaabaaab")

def count_unique_palindromic_substrings(s: str) -> int:
    # Preprocess the string
    transformed = '#' + '#'.join(s) + '#'
    n = len(transformed)
    P = [0] * n
    center = right = 0

    # Manacher's Algorithm
    for i in range(n):
      mirror = 2 * center - i
      if i < right:
        P[i] = min(right - i, P[mirror])
      while i + P[i] + 1 < n and i - P[i] - 1 >= 0 and transformed[i + P[i] + 1] == transformed[i - P[i] - 1]:
        P[i] += 1
        if i + P[i] > right:
          center, right = i, i + P[i]
    
    palidrome_set = set()
    for i in range(n):
      length = P[i]
      for l in range(1, length + 1):
        start = (i - l) // 2
        end = start + l
        if start >= 0 and end <= len(s):
          substring = s[start:end]
          if substring == substring[::-1]:  # Double-check palindrome
            palidrome_set.add(substring)
            
    return palidrome_set
       
print(count_unique_palindromic_substrings("aabaa"))