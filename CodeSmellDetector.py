from typing import List

class CodeSmellDetector:
    def __init__(self, source_code) -> str:
        self.source_code = source_code

    def get_sanitized_lines(self) -> List[str]:        
        nonblank_lines = []
        for line in self.source_code.split("\n"):
            stripped_line = line.strip(" ")
            empty_line = stripped_line == ""
            if not empty_line: nonblank_lines.append(stripped_line)
        return nonblank_lines
    
    def get_index_of_lines_starting_with_def(self, lines) -> List[int]:
        index_of_lines_starting_with_def = []       
        for index, line in enumerate(lines):
            if line.startswith("def"): index_of_lines_starting_with_def.append(index)
        return index_of_lines_starting_with_def 

    def count_lines_between_methods(self, nonblank_lines, lines_starting_with_def) -> List[int]:
        method_lengths = []
        for index in range(len(lines_starting_with_def) - 1):
            length_of_method = lines_starting_with_def[index + 1] - lines_starting_with_def[index]
            method_lengths.append(length_of_method)
        length_of_last_method = len(nonblank_lines) - lines_starting_with_def[-1] 
        method_lengths.append(length_of_last_method)    
        return method_lengths    
        
    def find_long_method(self) -> List[str]:
        long_methods = []
        threshold = 15
        sanitized_lines = self.get_sanitized_lines()
        print('sanitized lines:', sanitized_lines)
        line_index = self.get_index_of_lines_starting_with_def(sanitized_lines)
        print('line index:', line_index)
        method_lengths = self.count_lines_between_methods(sanitized_lines, line_index)
        print('method lengths:', method_lengths)

        for line_index, length in zip(line_index, method_lengths):
            method_line = sanitized_lines[line_index]
            method_name = method_line.split('def ')[-1].split('(')[0]
            if length > threshold: long_methods.append(f"Long method detected: {method_name} contains {length} lines.")
        if not long_methods: long_methods.append("No long methods detected.")
        return long_methods     

    def get_lines_starting_with_def(self, nonblank_lines) -> str:
        line_starting_with_def = []   
        for line in nonblank_lines:
            if line.startswith("def"): line_starting_with_def.append(line)
        return line_starting_with_def

    def get_parameter_count(self, lines_starting_with_def) ->List[int]:
        parameter_counts = []
        for line in lines_starting_with_def:
            parameter_str = line.split('(')[1].split(')')[0]
            print('parameter str:', parameter_str)
            parameter = parameter_str.count(',')
            if parameter_str and ',' in parameter_str: parameter_counts.append(parameter + 1)
            if parameter_str and ',' not in parameter_str: parameter_counts.append(1)
            if not parameter_str: parameter_counts.append(0)
        return parameter_counts
        
    def find_long_parameter_list(self) -> List[str]:
        long_parameter_list = []
        threshold = 3
        sanitized_lines = self.get_sanitized_lines()
        lines_starting_with_def = self.get_lines_starting_with_def(sanitized_lines)
        print('\nlines_starting_with_def:', lines_starting_with_def)
        parameter_counts = self.get_parameter_count(lines_starting_with_def)
        print('parameter_count:', parameter_counts)

        for line_index, count in enumerate(parameter_counts):
            method_line = lines_starting_with_def[line_index] 
            method_name = method_line.split('def ')[-1].split('(')[0]
            if count > threshold: long_parameter_list.append(f"\nLong parameter list detected: {method_name} contains {count} parameters.")
        if not long_parameter_list: long_parameter_list.append("No long parameter list detected.")
        return long_parameter_list  
    
    def get_dictionary_of_functions(self, lines, def_line_index):
        functions_dictionary = {}
        for index in range(len(def_line_index) - 1):
            start_index = def_line_index[index]
            end_index = def_line_index[index + 1] - 1
            print('start and end index:', start_index, end_index)

            function_body, function_name = self.get_function_body(start_index, end_index, lines)
            print('function name and function body:', function_name, function_body)
            functions_dictionary[function_name] = function_body
            print('functions_body', functions_dictionary[function_name])
        
        function_body, function_name = self.get_function_body(def_line_index[-1], len(lines), lines)
        print('function name and function body:', function_name, function_body)
        functions_dictionary[function_name] = function_body
        print('functions_body', functions_dictionary[function_name])
        print('functions dictionary:', functions_dictionary)
        return functions_dictionary

    def get_function_body(self, start_index, end_index, lines):
        function_name = lines[start_index].split("def ")[1].split("(")[0]
        function_body = [line.strip("\n") for line in lines[start_index : end_index + 1]]
        return function_body, function_name

    def find_duplicated_code(self) -> List[str]:
        # duplicated_code = []
        threshold = 0.75
        lines = self.get_sanitized_lines()
        def_index_lines = self.get_index_of_lines_starting_with_def(lines)
        print('def_index_lines:', def_index_lines)
        functions_dictionary = self.get_dictionary_of_functions(lines, def_index_lines)
        return 0








        