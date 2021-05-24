result = None

try:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    result = a/b
except Exception as e:
    print("Severo error :V ", e)
    print(type(e))

print("All full", result)
