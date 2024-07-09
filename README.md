Certainly! Here's a README.md template that provides clear instructions and formatting for your project:

---

# Resume PDF to JSON Converter

This Python script extracts text and hyperlinks from a PDF resume, parses it into structured data, and saves the result as a JSON file. It utilizes PyMuPDF (fitz) for PDF handling and regular expressions for parsing.

## Features

- **PDF Text Extraction:** Extracts text content from each page of the PDF resume.
- **Hyperlink Extraction:** Retrieves hyperlinks embedded in the PDF and associates them with the relevant resume sections.
- **Resume Parsing:** Parses the extracted text into structured data for Contact Information, Education, Experience, Skills, Projects, and Publications.
- **JSON Output:** Saves the parsed resume data along with associated hyperlinks as a JSON file.

## Installation

Before running the script, ensure you have Python 3.x installed. Clone the repository and install dependencies using pip:

```bash
git clone <repository-url>
cd <repository-directory>
pip install PyMuPDF
```

## Usage

1. **Run the Script:**

   ```bash
   python pdf_to_json.py
   ```

2. **Follow the prompts:**
   - Enter the path to the PDF resume when prompted.
   - Enter the directory path where you want to save the JSON output.

3. **Output:**
   - The parsed resume data, including extracted hyperlinks, will be saved as `resume.json` in the specified directory.

## Example

Suppose you have a PDF resume located at `/path/to/resume.pdf` and you want to save the JSON output to `/output/directory/`. Here’s how you would run the script:

```bash
python pdf_to_json.py
```

- **Input:**
  ```
  Please enter the path to your PDF resume: /path/to/resume.pdf
  Please enter the directory path to save the JSON file: /output/directory/
  ```

- **Output:**
  ```
  JSON file saved successfully at: /output/directory/resume.json
  ```

Adjust the paths and instructions based on your specific use case and file locations.

## Dependencies

- **PyMuPDF:** Python bindings for the MuPDF library. Install using:
  ```
  pip install PyMuPDF
  ```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README.md provides a structured guide on how to install, use, and contribute to your project. It also includes information about dependencies and licensing, ensuring clarity and accessibility for users and potential contributors. Adjust the content as needed to fit your specific project details and preferences.
