from langchain_unstructured import UnstructuredLoader
import glob
import os
from pathlib import Path


def ingest_pdf(file_path: str):
    BASE_DIR = Path(__file__).resolve().parent
    documents_path = BASE_DIR / file_path

    file_paths = glob.glob(str(documents_path / "*.pdf"))
    print("file_paths: ", file_paths)
    loader = UnstructuredLoader(
        file_path=file_paths, chunking_strategy="by_title", include_orig_elements=True
    )
    docs = loader.load()
    print("------docs-----")
    print(len(docs))
    print(docs[0].page_content)
