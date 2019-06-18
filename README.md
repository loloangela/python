# Convert Case
---
A python program that converts words to camel case, snake case, pascal case and several other formats.
It uses the pip stringcase library created by @okunishinishi.

For this program to run you will need to install stringcase.
`pip install stringcase`

This program takes command line arguments to convert text directly from the command line.
## Flags:
|Flags          | Description                           | Valid Inputs             			| Caveats. |
|---------------|:-------------------------------------:|:---------------------------------:|:--------:|
| -c, --camel   | Converts given word(s) to camel case. |snake_case or PascalCase 			|
| -s, --snake   | Converts given word(s) to snake case. |camelCase, PascalCase, spinal-case | No numbers
| -a, --caps    | Converts given word(s) to all caps.   |All 							    |
| -l, --lower   | Converts given word(s) to lower case. |All 								|
| -p, --pascal  | Converts given word(s) to pascal case.|snake_case, camelCase |
| -d, --path    | Converts given word(s) to path case.  |snake_case, camelCase, PascalCase, spinal-case | No all caps, will make it lowercase
| -m, --minus   | Converts given word(s) to spinal case.|snake_case, camelCase, PascalCase | No ALL CAPS
| -f, --filename| Converts given word(s) to camel case. | Name of text file, followed by an option | Defaults to camel case, Options follow the same as the single letter flags (without the dash). The output will go to given file (or file path) ending in "_out.txt"


## Examples:

### Convert to Camel Case
```python ./convertCase.py -c snake_case PascalCase```
#### Output
```
Camel: snakeCase
Camel: pascalCase
```

### Convert to Path Case
```python ./convertCase.py -d camelCase snake_case PascalCase```
#### Output
```
Path: camel/case
Path: snake/case
Path: pascal/case
```

### Convert to Different Types
```python ./convertCase.py -d camelCase snake_case PascalCase -c snake_case PascalCase```
#### Output
```
Path: camel/case
Path: snake/case
Path: pascal/case
Camel: snakeCase
Camel: pascalCase
```

### Convert a File to Camel Case
```python ./convertCase.py -f parseFile2.txt```
**NOTE: Not providing an option after filename or providing an invalid value will cause it to default to camel case.
#### Output
```
Output File: parseFile2_out.txt
```
### Convert a File to All Caps
```python ./convertCase.py -f parseFile2.txt a```
#### Output
```
Output File: parseFile2_out.txt
```
