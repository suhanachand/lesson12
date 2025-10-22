# U - UNDERSTAND: GENERATE A LIST BASED ON FIZZBUZZ RULES
# C - CLUES: 3 → "FIZZ", 5 → "BUZZ", BOTH → "FIZZBUZZ"
# A - ASSEMBLE: LOOP 1→n, APPLY RULES, STORE IN LIST
def fizz_buzz(n):
    answer = []
    # S - SOLVE: CHECK EACH NUMBER AND ADD CORRECT STRING
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
    # E - EXAMINE: RETURN FINAL LIST
    return answer


# TAKE USER INPUT AND PRINT IN REQUIRED FORMAT
if __name__ == "__main__":
    n = int(input("Enter n: "))  # Example: 5
    print(f"Input: n = {n}")
    print("Output:", fizz_buzz(n))

