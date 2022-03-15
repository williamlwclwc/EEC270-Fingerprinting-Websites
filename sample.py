import os
import argparse
import json

def get_parser():
    parser = argparse.ArgumentParser(description="automatically sample website hardware events")
    parser.add_argument(
        "--websites",
        help="filepath of all websites you want to sample(json)",
        default="./websites.json"
    )
    parser.add_argument(
        "--outputdir",
        help="dir of the output results",
        default="./sample_output/"
    )
    parser.add_argument(
        "--rate",
        help="perf sample rate, default 1000, i.e. 1HZ",
        default=1000
    )
    parser.add_argument(
        "--duration",
        help="how long you want to profile a webpage, default 5s",
        default=5
    )
    parser.add_argument(
        "--traces",
        help="how many traces you want per website",
        default=70
    )
    return parser

def perf_web(website_name, sample_rate, outputfiles, duration):
    os.system("timeout " + str(duration+1) + \
    " perf stat -e cache-misses,node-loads,branch-misses,branch-load-misses -I " + \
    str(sample_rate) + " -o " + outputfiles + " google-chrome-stable " + website_name)


if __name__ == "__main__":
    args = get_parser().parse_args()
    print("Arguments: " + str(args))
    # read website lists from json file
    website_filepath = args.websites
    with open(website_filepath, 'r') as f:
        websites = json.load(f)
    # perf websites
    num_traces = args.traces
    sample_rate = args.rate
    outputdir = args.outputdir
    duration = args.duration
    for i in range(len(websites)):
        for j in range(num_traces):
            outputfile = outputdir + str(i+1) + "_" + str(j+1) + ".txt"
            perf_web(websites[str(i+1)], sample_rate, outputfile, duration)
    print("Done")