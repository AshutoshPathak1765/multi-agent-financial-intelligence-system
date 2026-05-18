from langchain_unstructured import UnstructuredLoader
import glob
import os
from app.core.vector_db import insert_into_vector_db
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
    db = insert_into_vector_db(docs=docs)
    print("Inserted into vector db: ",db)
    # print("------docs-----")
    # print(len(docs))
    # print(docs[1].page_content)
