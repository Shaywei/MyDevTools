import re
import os
import sys
import shutil
import fnmatch

from time import gmtime, strftime
START_TIME = strftime("%Y-%m-%d_%H.%M.%S", gmtime())

import log_utils
import xml.etree.ElementTree as ET

file_utils_logger = log_utils.get_logger("file_utils")

def write_file(output_file_path, file_content):
    file_utils_logger.debug("Writing file. output_file_path = %s, file_content:\n%s" % (output_file_path, file_content[0:100] if len(file_content) > 100 else file_content))
    
    dirname = os.path.dirname(output_file_path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

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
        file_utils_logger.error("FILE DOES NOT EXIST. file_path=%s", (file_path))
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

# until string_utils
def prefix_replace_pattern_postfix(s, prefix=None, pattern=None, replacement=None, postfix=None):
        if isinstance(pattern, str) and isinstance(replacement, str):
            s = re.sub(pattern, replacement, s)
        s = s if prefix is None else (prefix + s)
        s = s if postfix is None else (s + postfix)
        return s

def parse_properties_from_multiline_string(s):
    propeties = dict()
    for line in s.splitlines():
        key, val = line.strip().split('=', 2)
        propeties[key] = val
    return propeties

def find_replace_in_file(file_path, pattern, repl, count=0, backup=True):
    content = read_file(file_path)
    content = re.sub(pattern, repl, content, count=count)
    if backup:
        create_backup(file_path)
    write_file(file_path, content)

# until xml_utils:

def get_parent_gav(pom):
    q = etree.parse(pom)
    parent = q.find('.//{http://maven.apache.org/POM/4.0.0}parent')
    if parent is not None:
        gav = dict()
        for child in list(parent):
            gav[child.tag[35:]] = child.text    
        return gav
        
# until time_utils
def now_strf(format="%Y-%m-%d_%H.%M.%S"):
    from time import gmtime, strftime   
    return strftime(format, gmtime())