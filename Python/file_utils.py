import re
import os
import sys
import mock
import shutil
import fnmatch
from string_utils import parse_properties_from_multiline_string

from time import gmtime, strftime
START_TIME = strftime("%Y-%m-%d_%H.%M.%S", gmtime())

#import log_utils
import xml.etree.ElementTree as ET

#file_utils_logger = log_utils.get_logger("file_utils") if 'PYTHON_DEBUG' in os.environ else mock.Mock()

def create_dir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

def write_file(output_file_path, file_content):
    #file_utils_logger.debug("Writing file. output_file_path = %s, file_content:\n%s" % (output_file_path, file_content[0:100] if len(file_content) > 100 else file_content))
    create_dir(dirname=os.path.dirname(output_file_path))

    with open(output_file_path, 'wb') as out:
        if file_content is not None:
            out.write(file_content)

def find_files_rec(src, pattern):
    matches = []
    for root, dirnames, filenames in os.walk(src):
      for filename in fnmatch.filter(filenames, pattern):
          matches.append(os.path.abspath(os.path.join(root, filename)))

    return matches

def read_file(file_path):
    if not os.path.exists(file_path):
        #file_utils_logger.error("FILE DOES NOT EXIST. file_path=%s", (file_path))
        return None
    with open(file_path) as a_file:
        return a_file.read()

def get_all_direct_subdirs(path):
    return os.walk(path).next()[1]

def get_stripped_lines_from_file_as_list(a_file):
    res = []
    with open(a_file) as f:
        for line in f: 
            res.append(line.strip())
    return res

def get_root_xml(path_to_xml):
    if not os.path.exists(path_to_xml):
        file_utils_logger.error("Cannot find job: %s!" % (path_to_xml,))
        sys.exit(1)

    try:
        tree = ET.parse(path_to_xml)
        return tree.getroot()
    except:
        file_utils_logger.error("Error while parsing file: %s" % (path_to_xml,))        
        file_utils_logger.error(sys.exc_info()[0])
        raise

def return_valid_filename(filename):
    return ''.join(c for c in filename if c in '-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

def create_backup(src, dest=None, postfix=None):
    ''' Works for both files and folders.
        By default creates src.bak in the same place as src'''

    if postfix is None:
        postfix = 'bak'
    if dest is None:
        dest = os.path.join('%s.%s' % (src, postfix))

    if os.path.isfile(src):
        shutil.copyfile(src, dest)
    elif os.path.isdir(src):
        if os.path.exists(dest):
            shutil.rmtree(dest)        
        shutil.copytree(src, dest)

def read_properties(src):
    return parse_properties_from_multiline_string(read_file(src))

def find_replace_in_file(file_path, pattern, repl, count=0, backup=True):
    content = read_file(file_path)
    content = re.sub(pattern, repl, content, count=count)
    if backup:
        create_backup(file_path)
    write_file(file_path, content)

def remove_non_printalbe_characters(file):
    import string
    write_file(file, filter(lambda x: x in string.printable, read_file(file)))
    
# until time_utils
def now_strf(format="%Y-%m-%d_%H.%M.%S"):
    from time import gmtime, strftime   
    return strftime(format, gmtime())