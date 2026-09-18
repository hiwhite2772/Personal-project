import textwrap
def wrap_1(string, max_width):
    result = ""
    for i in range((len(string) // max_width)+1):
        result += f"{string[(i*max_width):((i+1)*max_width)]}\n"
    return result.rstrip("\n")

def wrap_2(string, max_width):
    result = textwrap.wrap(string, max_width)
    return "\n".join(result)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    # result_1 = wrap_1(string, max_width)
    result_2 = wrap_2(string, max_width)
    # print(result_1) 
    print(result_2)

