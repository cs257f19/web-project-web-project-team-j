import json

def ReddDataSampleElection(data):
    for line in data:





def main(filename):
    with open(filename, "r") as data_file:
        data = json.loads(data_file)
    #print(ReddDataSampleElection(data))
    print(json.dumps(data, indent=4, sort_keys=True))
main():
