from typing import List
# Assumptions: comments are counted as lines of code and 2) last function goes til end of file 
class CodeSmellDetector:
    def __init__(self, source_code) -> str:
        self.source_code = source_code

    def get_sanitized_lines(self) -> List[str]:        
        nonblank_lines = []
        for line in self.source_code.split("\n"):
            stripped_line = line.strip(" ")
            not_empty_line = stripped_line != ""
            if not_empty_line: nonblank_lines.append(stripped_line)
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
        length_of_last_method = len(nonblank_lines) - lines_starting_with_def[-1] # Assuming last function goes till end of file 
        method_lengths.append(length_of_last_method)    
        return method_lengths    
        
    def find_long_method(self) -> str:
        threshold = 15
        sanitized_lines = self.get_sanitized_lines()
        line_index = self.get_index_of_lines_starting_with_def(sanitized_lines)
        method_lengths = self.count_lines_between_methods(sanitized_lines, line_index)

        for line_index, length in zip(line_index, method_lengths):
            method_line = sanitized_lines[line_index]
            method_name = method_line.split('def ')[-1].split('(')[0]

            if length > threshold: return f"Long method detected: {method_name} is longer than {threshold} lines."
        return "No long methods detected."

    def get_lines_starting_with_def(self, nonblank_lines) -> str:
        line_starting_with_def = []   
        for line in nonblank_lines:
            if line.startswith("def"): line_starting_with_def.append(line)
        return line_starting_with_def

    def get_parameter_count(self, lines_starting_with_def) ->List[int]:
        parameter_count = []
        for line in lines_starting_with_def:
            parameter_str = line.split('(')[1].split(')')[0]
            print(parameter_str)
            if parameter_str:
                parameters = parameter_str.split(',')
                parameter_count.append(len(parameters))
            parameter_count.append(0)
        return parameter_count
        
    def find_long_parameter_list(self) -> str:
        threshold = 3
        sanitized_lines = self.get_sanitized_lines()
        lines_starting_with_def = self.get_lines_starting_with_def(sanitized_lines)
        print('lines_starting_with_def:', lines_starting_with_def)
        parameter_count = self.get_parameter_count(lines_starting_with_def)
        print('parameter_count:', parameter_count)

        for line_index, count in enumerate(parameter_count):
            method_line = lines_starting_with_def[line_index]
            print(method_line)
            method_name = method_line.split('def ')[-1].split('(')[0]
            if count > threshold:
                return f'Long parameter list detected: {method_name} has greater than {threshold} parameters.'
        return f'No long parameter list detected.'
    