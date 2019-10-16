import json

def listparse(filename):
    
    print("listparse")
    print(filename)

    commlines = []

    for line in open(filename, 'r'):
        commlines.append(json.loads(line))
    
    commentlist = []
    for line in commlines:
        commentlist.append(line.get("body"))
    print(commentlist)


def main():
    filename = "RC_2016-11_r_pol_only.json"

    return listparse(filename)
    
if __name__ == "__main__":
    main()
