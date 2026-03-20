from parser import extract_from_docx

text = extract_from_docx("entry level resume.docx")
print(text[:500])
print("Total words:", len(text.split()))