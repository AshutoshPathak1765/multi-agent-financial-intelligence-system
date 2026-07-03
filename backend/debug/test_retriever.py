from app.core.vector_db import get_vector_db

db = get_vector_db()

query = "Analyze Apple's latest quarterly earnings"

results = db.similarity_search_with_score(
    query,
    k=5,
)

print("=" * 80)
print("QUERY:", query)
print("=" * 80)


for i, (doc, score) in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("-" * 60)
    print("Score:", score)
    print("Source:", doc.metadata.get("source"))
    print("Metadata:", doc.metadata)
    print()
    print(doc.page_content[:500])