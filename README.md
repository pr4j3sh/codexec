# codexec

codexec is a Python package that allows you to execute code written in various programming languages (C, C++, Java, Python, and JavaScript) by making API calls to a server. The package takes code files and optional input files, executes the code, and returns the output.

## features

-   Execute code in multiple languages: C, C++, Java, Python, and JavaScript.
-   Simple command-line interface (CLI) for executing code files.
-   Supports optional input files for code that requires input.
-   Easy integration with environment variables for configuration.

<!-- ## Installation -->
<!---->
<!-- 1. Clone the repository: -->
<!---->
<!--     ```bash -->
<!--     git clone https://github.com/yourusername/codexec.git -->
<!--     cd codexec -->
<!--     ``` -->
<!---->
<!-- 2. Install the required dependencies: -->
<!---->
<!--     ```bash -->
<!--     pip install -r requirements.txt -->
<!--     ``` -->
<!---->
<!-- 3. (Optional) Install the package locally: -->
<!---->
<!--     ```bash -->
<!--     pip install . -->
<!--     ``` -->

<!-- ## Usage -->
<!---->
<!-- ### Command-Line Interface -->
<!---->
<!-- You can use the command-line interface to execute your code files: -->
<!---->
<!-- ```bash -->
<!-- python cli.py path/to/code_file.py [path/to/input_file.txt] -->
<!-- ``` -->
<!---->
<!-- -   `path/to/code_file.py`: The path to the code file you want to execute. -->
<!-- -   `path/to/input_file.txt`: (Optional) The path to an input file containing input data for the code. -->
<!---->
<!-- ### Example -->
<!---->
<!-- 1. Create a Python file `hello.py`: -->
<!---->
<!--     ```python -->
<!--     print("Hello, World!") -->
<!--     ``` -->
<!---->
<!-- 2. Execute the code using codexec: -->
<!---->
<!--     ```bash -->
<!--     python cli.py hello.py -->
<!--     ``` -->
<!---->
<!--     Output: -->
<!---->
<!--     ``` -->
<!--     Hello, World! -->
<!--     ``` -->
<!---->
<!-- 3. Create an input file `input.txt`: -->
<!---->
<!--     ```plaintext -->
<!--     Input data for the code -->
<!--     ``` -->
<!---->
<!-- 4. Modify the code to read from input: -->
<!---->
<!--     ```python -->
<!--     input_data = input() -->
<!--     print(f"You entered: {input_data}") -->
<!--     ``` -->
<!---->
<!-- 5. Execute the code with input: -->
<!---->
<!--     ```bash -->
<!--     python cli.py hello.py input.txt -->
<!--     ``` -->
<!---->
<!-- ## Contributing -->
<!---->
<!-- Contributions are welcome! Please fork the repository and submit a pull request with your improvements. -->
<!---->
<!-- ## License -->
<!---->
<!-- This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. -->
