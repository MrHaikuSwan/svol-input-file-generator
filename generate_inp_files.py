# Make sure this directory exists when you run the script
# Make sure the variable you put in here ends with a slash
OUTPUT_DIR = 'generated_input_files/'

INP_VARS = [
  'svol1',
  'svol2',
  'svol3',
  'svol4',
  'svol5',
  'svol6',
  'svol7',
  'svol8',
  'svol9',
  'svol10',
  'svol11',
  'svol12',
  'svol13',
  'svol14',
  'svol15',
  'svol16',
]

def create_input_file(var_name, template):
  fname = f"{OUTPUT_DIR}ADI_{var_name}.inp"
  input_file_contents = template.format(f"ADI_{var_name}", var_name, var_name)
  with open(fname, 'w') as outfile:
    outfile.write(input_file_contents)

def main():
  with open('svol_inp_template.txt') as infile:
    template = infile.read()
  for var_name in INP_VARS:
    create_input_file(var_name, template)

if __name__ == '__main__':
  main()