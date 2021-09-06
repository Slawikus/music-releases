def to_snake_case(class_line):
	class_name = class_line.split(" ")[1].split("(")[0]
	# PascalCase to snake_case
	snake_case = "".join([f"_{i.lower()}" if i.isupper() else i for i in class_name])
	return snake_case[1:]

def refactor_files():
	"""
	Creates .py file and writes into it every class in file refactoring file
	name to snake_case, separates every class by double whitespace
	WARNING!:
		temporary delete all import and there is must not be any whitespace
		on the top of file and double whitespace
	"""
	with open("tests/tests.py", "r") as views:
		for cls in views.read().split("\n\n"):
			lines = [i for i in cls.split("\n") if i != ""]
			class_line = lines[0]
			snake_name = to_snake_case(class_line)
			with open(f"{snake_name}.py", "w") as file:
				file.write(cls)


if __name__ == "__main__":
	refactor_files()