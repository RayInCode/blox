import sys
import time
from blox_enumerator import bloxEnumerate
import argparse


def main(args):
    run_times = 2
    print("Job ID {}".format(args.jid))
    print("Iterator initilized")
    print("Initialized enumerator")
    enumerator = bloxEnumerate(range(100), args.jid)
    for ictr, key in enumerator:
        print(ictr, key)
        enumerator.push_metrics({"attained_service": 10})
        enumerator.push_metrics({"per_iteration_time": 1})
        if ictr is False:
            print("Time to exit")
        time.sleep(1)


def parse_args(parser):
    """
    parser : argparse.ArgumentParser
    return a parser with arguments
    """
    parser.add_argument(
        "--jid", required=True, type=int, help="Name of the scheduling strategy"
    )
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    print("In Main")
    args = parse_args(
        argparse.ArgumentParser(description="Arguments for Starting the scheduler")
    )
    main(args)
