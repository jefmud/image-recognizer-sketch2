# image url downloader
# expects a text file of URLs (one per line)
import argparse
import os
from urllib.request import urlopen

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--destdir", required=True,
                help="path to training dataset (i.e., directory of images top level named for label)")
ap.add_argument("-u", "--urlfile", required=True,
                help="path to url file listing")
ap.add_argument('-p','--prefix',required=False,
                help='optional filename prefix')

args = vars(ap.parse_args())

def download_picture(url, dest_filename, dest_folder='./', overwrite=False, verbose=False):
    """download_picture(url, dest_filename, dest_folder, overwrite=False)"""
    response = urlopen(url)
    document = response.read()

    outfile = os.path.join(dest_folder, dest_filename)
    if not os.path.isdir(dest_folder):
                # make directory if required
        os.mkdir(dest_folder)

    if os.path.isfile(outfile) and overwrite == False:
        if verbose: print("skipping overwrite of {}".format(outfile))
        return False # don't overwrite existing file
    else:
        if verbose: print("saving file {}".format(outfile))
        with open(outfile,'wb') as fp:
            fp.write(document)
        return True
    
def main():
    # get the destination directory
    dest_folder = args['destdir']
    
    # optional file prefix
    prefix = args.get('prefix','')
    
    # read the data in the urlfile
    with open(args['urlfile'],'r') as input_file:
        data = input_file.read()
        
    lines = data.split('\n')
    for line in lines:
        url = line.strip()
        if '.jpg' in url.lower():
            # in this case we're only going to process jpg files
            parts = url.split('/')
            if prefix:
                dest_filename = "{}#{}#{}".format(prefix, parts[-2], parts[-1])
            else:
                dest_filename = "{}#{}".format(parts[-2],parts[-1])
            download_picture(url, dest_filename, dest_folder=dest_folder)
    print('==done==')
    
    
    
if __name__ == '__main__':
    main()