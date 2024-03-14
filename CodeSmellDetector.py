from typing import List
from typing import Tuple

# source: https://www.geeksforgeeks.org/how-to-calculate-jaccard-similarity-in-python/

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
        line_index = self.get_index_of_lines_starting_with_def(sanitized_lines)
        method_lengths = self.count_lines_between_methods(sanitized_lines, line_index)

        for line_index, length in zip(line_index, method_lengths):
            method_line = sanitized_lines[line_index]
            method_name = method_line.split('def ')[-1].split('(')[0]
            if length > threshold: long_methods.append(f"Long method detected: {method_name} contains {length} lines.")
        if not long_methods: long_methods.append("No long methods detected.")
        return long_methods     

    def get_lines_starting_with_def(self, nonblank_lines) -> List[str]:
        line_starting_with_def = []   
        for line in nonblank_lines:
            if line.startswith("def"): line_starting_with_def.append(line)
        return line_starting_with_def

    def get_parameter_count(self, lines_starting_with_def) ->List[int]:
        parameter_counts = []
        for line in lines_starting_with_def:
            parameter_str = line.split('(')[1].split(')')[0]
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
        parameter_counts = self.get_parameter_count(lines_starting_with_def)

        for line_index, count in enumerate(parameter_counts):
            method_line = lines_starting_with_def[line_index] 
            method_name = method_line.split('def ')[-1].split('(')[0]
            if count > threshold: long_parameter_list.append(f"\nLong parameter list detected: {method_name} contains {count} parameters.")
        if not long_parameter_list: long_parameter_list.append("No long parameter list detected.")
        return long_parameter_list  

    def get_list_of_functions(self, lines, def_line_index) -> List[str]:
        current_function, functions_list = [], []
        for index in range(len(def_line_index) - 1):
            start_index = def_line_index[index]
            end_index = def_line_index[index + 1] - 1
            current_function = [line.strip("\n") for line in lines[start_index : end_index + 1]]
            functions_list.append((current_function, start_index, end_index))
        return functions_list

    def calculate_jaccard_similarity(self, func1, func2) -> int:
        intersection = len(func1.intersection(func2))
        union = len(func1.union(func2))
        similarity = intersection / union if union != 0 else 0 
        return similarity 
        
    def find_duplicated_code(self) -> Tuple[List[str], List[str]]:
        duplicated_code, remove_list = [], []
        threshold = 0.75
        lines = self.get_sanitized_lines()
        def_index_lines = self.get_index_of_lines_starting_with_def(lines)
        functions_list = self.get_list_of_functions(lines, def_index_lines)

        for i in range(len(functions_list)):
            for j in range(i + 1, len(functions_list)):
                func1, func2 = [], []
                for line in functions_list[i][0]:
                    func1 += line.split(" ")
                for line in functions_list[j][0]:
                    func2 += line.split(" ")
                similarity = self.calculate_jaccard_similarity(set(func1), set(func2))

                if similarity >= threshold:
                   duplicated_code.append(f"'\nSimilar code found between {functions_list[i]} and {functions_list[j]}") 
                   remove_list.append(functions_list[i]) 
        if not duplicated_code: duplicated_code.append("No duplciated code detected")
        code_with_removed_duplicates = self.remove_duplicated_code(remove_list)
        return duplicated_code, code_with_removed_duplicates
    
    def remove_duplicated_code(self, remove_list) -> List[str]:
        indexes_to_remove = [list(range(start_index, stop_index + 1)) for _, start_index, stop_index in remove_list]
        indexes_to_remove = set([index for group in indexes_to_remove for index in group])
        source_code = [line for line in self.source_code.split("\n") if line.strip(" ") != ""]
        filtered_source_code = [line for i, line in enumerate(source_code) if i not in indexes_to_remove]
        source_code_str = ""
        for line in filtered_source_code:
            source_code_str += line + "\n"
        return source_code_str

 










        