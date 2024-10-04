import spacy
import PyPDF2
import docx

def retrieve_text(file_path):
    extracted_text = ""
    
    if file_path.endswith(".pdf"):
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            extracted_text = " ".join([pg.extract_text() for pg in reader.pages])
    
    elif file_path.endswith(".docx"):
        document = docx.Document(file_path)
        extracted_text = " ".join([p.text for p in document.paragraphs])
    
    return extracted_text.strip()

def identify_keywords(input_text):
    processor = spacy.load("en_core_web_sm")
    doc = processor(input_text.lower())
    key_terms = {"python", "sql", "flask", "django", "machine learning", "nlp", "deep learning"}
    return {token.text for token in doc if token.text in key_terms}

def execute_analysis():
    file_source = input("Provide document path (PDF/DOCX): ")
    reference_text = input("Insert reference description: ")
    
    processed_text = retrieve_text(file_source)
    acquired_terms = identify_keywords(processed_text)
    expected_terms = identify_keywords(reference_text)
    gaps = expected_terms - acquired_terms
    
    print(f"\n✅ Recognized Terms in Document: {acquired_terms}")
    print(f"✅ Expected Terms from Reference: {expected_terms}")
    print(f"⚠️ Missing Terms: {gaps}" if gaps else "🎉 All criteria met!")

if __name__ == "__main__":
    execute_analysis()
