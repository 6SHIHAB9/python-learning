def minimumBribes(q):
    bribes = 0
    for i in range(len(q)):
        # 1. The Chaos Check
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return # This stops the extra print!

        # 2. The Bribe Count
        # Look from where they COULD have started (at most 2 spots ahead) 
        # to where they are now.
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
    
    print(bribes)


q = [1, 2, 5, 3, 7, 8, 6, 4]
minimumBribes(q)