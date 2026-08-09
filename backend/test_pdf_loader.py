from app.loaders.pdf_loader import PDFLoader

pdf_path = "knowledge_base/nutrition/healthy_diet.pdf"

loader = PDFLoader()
documents = loader.load(pdf_path)

print(f"Pages loaded: {len(documents)}")
print("\nFirst page:\n")
print(documents[0].page_content)
print("\nMetadata:\n")
print(documents[0].metadata)