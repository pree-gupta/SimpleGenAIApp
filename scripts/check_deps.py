# Quick import smoke-test for dependencies
import importlib

pkgs = {
    "langchain": "langchain",
    "langchain_community": "langchain_community",
    "langchain_huggingface": "langchain_huggingface",
    "transformers": "transformers",
    "sentence_transformers": "sentence_transformers",
    "faiss": "faiss",
    "pypdf": "pypdf",
    "fastapi": "fastapi",
    "uvicorn": "uvicorn",
}

failed = []
for pretty, mod in pkgs.items():
    try:
        m = importlib.import_module(mod)
        ver = getattr(m, "__version__", "<no __version__>")
        print(f"OK  - {pretty:24s}  version: {ver}")
    except Exception as e:
        failed.append((pretty, e))
        print(f"ERR - {pretty:24s}  {e}")

if failed:
    raise SystemExit(1)
