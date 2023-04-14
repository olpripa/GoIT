import sys

def parse_args():
    list = sys.argv
    list.pop(0)
    result = " ".join(map(str, list))

    return result

# def main():
#     list = sys.argv
#     list.pop(0)
#     result = " ".join(map(str, list))
#     print(result)

    

# if __name__ == '__main__':
#     main()