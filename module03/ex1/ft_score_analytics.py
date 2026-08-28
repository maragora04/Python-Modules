import sys


def score_calculator() -> None:
    arg_len = len(sys.argv) - 1
    if (arg_len == 0):
        print("No scores provided. Usage: python3 script.py \
    <score1> <score2> ...")
        return
    score = []
    for arg in sys.argv[1:]:
        try:
            score.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: {arg}")
    if (len(score) == 0):
        print("No scores provided. Usage: python3 script.py \
<score1> <score2> ...")
        return
    total_score = sum(score)
    highest = max(score)
    lowest = min(score)
    print(f"Scores processed: {score}")
    print(f"Total players : {arg_len}")
    print(f"Total score: {total_score}")
    print(f"Average score: {(total_score / arg_len):.2f}")
    print(f"High score: {highest}")
    print(f"Low score: {lowest}")
    print(f"Score range: {highest - lowest}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score_calculator()
