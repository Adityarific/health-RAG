from app.loaders.pdf_loader import PDFLoader
from app.preprocessing.splitter import TextSplitter


pdf_path = "knowledge_base/nutrition/healthy_diet.pdf"

loader = PDFLoader()
documents = loader.load(pdf_path)

splitter = TextSplitter()
chunks = splitter.split(documents)

print(f"Original pages: {len(documents)}")
print(f"Total chunks: {len(chunks)}")

print("\nFirst chunk:")
print(chunks[0].page_content)


print("\nFirst chunk:")
print(chunks[1].page_content)

print("\nFirst chunk metadata:")
print(chunks[0].metadata)