import sys
from pathlib import Path

from palindromy.palindromes_analyser import palindromes_in_json_keys, count_palindromes

"""Simple commandline client, call it by passing the full path to the file, containing 
   the lines with Strings / JSONs to be analysed, that's the only parameters to be passed

   Run it by calling in your terminal:
    {project_root_path}$ python command_line_app.py $full_Path_to_file
"""

if __name__ == '__main__':
    try:
        path = sys.argv[1]
        file = Path(path)
        jsons = file.read_text().splitlines()
        palindromes_in_file = palindromes_in_json_keys(jsons)
        count = count_palindromes(jsons)
        print('Palindromes are ' + str(palindromes_in_file))
        print('count of palindromes is ' + str(count))
    except Exception as e:  # kept simple due to time constraints
        print('Error while processing file to find palindromes: ', e)
        sys.exit(-1)
