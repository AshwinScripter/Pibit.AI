import fitz  # PyMuPDF
import json
import re
import sys
import os

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text, document

def extract_links_from_pdf(document):
    links = []
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        page_links = page.get_links()
        for link in page_links:
            links.append({
                "url": link.get("uri"),
                "page": page_num + 1
            })
    return links

def parse_resume(resume_text):
    resume_dict = {
        "Contact Information": {},
        "Education": [],
        "Experience": [],
        "Skills": [],
        "Projects": [],
        "Publication and Research": [],
        "Links": []
    }
    
    # Splitting the resume into lines for easier processing
    lines = resume_text.split('\n')
    
    # Regular expressions for different sections
    contact_info_pattern = re.compile(r"\(\+91\)-[0-9]+|@[a-zA-Z0-9._-]+|LinkedIn|GitHub")
    education_pattern = re.compile(r"EDUCATION")
    experience_pattern = re.compile(r"EXPERIENCE")
    skills_pattern = re.compile(r"SKILLS")
    projects_pattern = re.compile(r"PROJECTS")
    publications_pattern = re.compile(r"PUBLICATION AND RESEARCH")
    
    section = None
    for line in lines:
        line = line.strip()
        
        # Identify and switch sections
        if education_pattern.search(line):
            section = "Education"
            continue
        elif experience_pattern.search(line):
            section = "Experience"
            continue
        elif skills_pattern.search(line):
            section = "Skills"
            continue
        elif projects_pattern.search(line):
            section = "Projects"
            continue
        elif publications_pattern.search(line):
            section = "Publication and Research"
            continue
        elif contact_info_pattern.search(line):
            section = "Contact Information"
        
        # Parse content based on the current section
        if section == "Contact Information":
            if "LinkedIn" in line:
                resume_dict["Contact Information"]["LinkedIn"] = line
            elif "GitHub" in line:
                resume_dict["Contact Information"]["GitHub"] = line
            elif "@" in line:
                resume_dict["Contact Information"]["Email"] = line
            elif re.match(r"\(\+91\)-[0-9]+", line):
                resume_dict["Contact Information"]["Phone"] = line
        elif section == "Education":
            if line:
                resume_dict["Education"].append(line)
        elif section == "Experience":
            if line:
                resume_dict["Experience"].append(line)
        elif section == "Skills":
            if line:
                resume_dict["Skills"].append(line)
        elif section == "Projects":
            if line:
                resume_dict["Projects"].append(line)
        elif section == "Publication and Research":
            if line:
                resume_dict["Publication and Research"].append(line)
    
    return resume_dict

if __name__ == "__main__":
    # Get the PDF file path from user input
    pdf_path = input("Please enter the path to your PDF resume: ")
    
    # Extract text from the PDF resume and get the document object
    resume_text, document = extract_text_from_pdf(pdf_path)
    
    # Extract links from the PDF
    pdf_links = extract_links_from_pdf(document)
    
    # Parse the resume
    parsed_resume = parse_resume(resume_text)
    
    # Include extracted links in the parsed resume
    parsed_resume["Links"] = pdf_links
    
    # Get the directory path to save the JSON file
    output_directory = input("Please enter the directory path to save the JSON file: ")
    
    # Ensure the directory exists, create it if necessary
    os.makedirs(output_directory, exist_ok=True)
    
    # Construct the output JSON file path
    json_file_path = os.path.join(output_directory, "resume.json")
    
    # Convert parsed resume to JSON and save it
    with open(json_file_path, 'w') as json_file:
        json.dump(parsed_resume, json_file, indent=4)
    
    print(f"JSON file saved successfully at: {json_file_path}")
